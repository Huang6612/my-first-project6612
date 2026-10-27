from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional, Set, Tuple
import random

TOTAL = 10


@dataclass(frozen=True)
class State:
    """A minimal toy state: four variables whose total is fixed.

    This is intentionally not a physical model. It is a constrained state-space
    toy model used only to explore how a system can exhibit staged changes under
    explicit rules.
    """

    a: int
    b: int
    c: int
    e: int = 0

    def valid(self) -> bool:
        """Legal state: all values are nonnegative and the sum is fixed."""
        return (
            self.a >= 0
            and self.b >= 0
            and self.c >= 0
            and self.e >= 0
            and self.a + self.b + self.c + self.e == TOTAL
        )

    def gap(self) -> int:
        return max(self.a, self.b, self.c, self.e) - min(self.a, self.b, self.c, self.e)

    def __str__(self) -> str:
        return f"(A={self.a}, B={self.b}, C={self.c}, E={self.e})"


@dataclass
class ResourceGraph:
    """A separate relation layer.

    This graph is intentionally not equated with the constraint system. A visible
    relationship does not automatically mean a hard constraint has been generated.
    """

    edges: Set[Tuple[str, str]] = field(default_factory=set)

    def add_edge(self, u: str, v: str) -> None:
        self.edges.add((min(u, v), max(u, v)))

    def has_edge(self, u: str, v: str) -> bool:
        return (min(u, v), max(u, v)) in self.edges


@dataclass
class ToySystem:
    """Toy system for staged state transitions under explicit rules.

    The purpose is not to prove physical emergence; it is to test whether a small,
    constrained state-space can exhibit a pattern resembling:
    expansion -> local instability -> structural reorganization -> dissipative release.
    """

    state: State
    relations: ResourceGraph = field(default_factory=ResourceGraph)
    rnd: random.Random = field(default_factory=lambda: random.Random(42))

    def __post_init__(self) -> None:
        if not self.state.valid():
            raise ValueError(f"Initial state is invalid: {self.state}")
        # Relationship layer is intentionally separate from the hard constraint.
        for pair in (("a", "b"), ("a", "c"), ("b", "c")):
            self.relations.add_edge(*pair)

    @staticmethod
    def _move_one(src: str, dst: str, state: State) -> Optional[State]:
        vals = {"a": state.a, "b": state.b, "c": state.c, "e": state.e}
        if vals[src] <= 0:
            return None
        vals[src] -= 1
        vals[dst] += 1
        nxt = State(**vals)
        return nxt if nxt.valid() else None

    def legal_neighbors(self) -> List[State]:
        """Legal moves under the current constraint system.

        This is intentionally a finite and clearly bounded neighborhood, not a
        universal proof of all possible state transitions.
        """
        moves: List[State] = []
        seen: Set[Tuple[int, int, int, int]] = set()

        # Core-to-core reallocation.
        for src, dst in (("a", "b"), ("a", "c"), ("b", "a"), ("b", "c"), ("c", "a"), ("c", "b")):
            nxt = self._move_one(src, dst, self.state)
            if nxt is not None:
                key = (nxt.a, nxt.b, nxt.c, nxt.e)
                if key not in seen:
                    moves.append(nxt)
                    seen.add(key)

        # Core -> environment dissipation.
        for src in ("a", "b", "c"):
            nxt = self._move_one(src, "e", self.state)
            if nxt is not None:
                key = (nxt.a, nxt.b, nxt.c, nxt.e)
                if key not in seen:
                    moves.append(nxt)
                    seen.add(key)

        # Environment -> core conversion.
        for dst in ("a", "b", "c"):
            if self.state.e <= 0:
                continue
            vals = {"a": self.state.a, "b": self.state.b, "c": self.state.c, "e": self.state.e}
            vals[dst] += 1
            vals["e"] -= 1
            nxt = State(**vals)
            if nxt.valid():
                key = (nxt.a, nxt.b, nxt.c, nxt.e)
                if key not in seen:
                    moves.append(nxt)
                    seen.add(key)

        return moves

    def expand(self) -> None:
        """A weak expansion step: accumulate local dominance but remain valid."""
        candidates = self.legal_neighbors()
        if not candidates:
            return
        # Favor the most unequal state while staying valid.
        self.state = max(candidates, key=lambda s: s.gap())

    def local_instability(self) -> None:
        """Autonomously create a stronger local imbalance.

        This is intentionally a constrained step, not a universal physical law.
        """
        vals = [self.state.a, self.state.b, self.state.c, self.state.e]
        max_idx = max(range(4), key=lambda i: vals[i])
        min_idx = min(range(4), key=lambda i: vals[i])
        names = ["a", "b", "c", "e"]

        # If the max and min are in the core, move one unit from the minimum to the maximum.
        if max_idx in (0, 1, 2) and min_idx in (0, 1, 2):
            src = names[min_idx]
            dst = names[max_idx]
            nxt = self._move_one(src, dst, self.state)
            if nxt is not None:
                self.state = nxt
                return

        # Fallback: convert one unit from environment to the maximum-core variable.
        if self.state.e > 0:
            dst = names[max_idx]
            vals = {"a": self.state.a, "b": self.state.b, "c": self.state.c, "e": self.state.e}
            vals[dst] += 1
            vals["e"] -= 1
            nxt = State(**vals)
            if nxt.valid():
                self.state = nxt
                return

    def reorganize(self) -> Optional[str]:
        """Limited local search for reorganization.

        The state is not forced to reconfigure; if the bounded search cannot find a
        valid reconfiguration candidate, the model reports that the search was
        unsuccessful rather than claiming a universal no-solution.
        """
        best: Optional[State] = None
        best_score: Optional[int] = None
        for _ in range(200):
            cand = self.rnd.choice(self.legal_neighbors()) if self.legal_neighbors() else None
            if cand is None:
                break
            score = cand.gap() + (cand.a + cand.b + cand.c)  # broad structural differentiation
            if best is None or score > (best_score or -1):
                best = cand
                best_score = score
        if best is None:
            return None
        self.state = best
        return "reorganized"

    def dissolve(self) -> Optional[str]:
        """Guaranteed termination by repeatedly removing local dominance to the environment.

        This is stronger than the earlier 'delete at most 3 edges' pattern and is
        intentionally written to find a valid stabilized state if one exists under
        the toy rule set.
        """
        attempts = 0
        while True:
            if self.state.valid() and self.state.gap() <= 1:
                return "dissipated"

            candidates = self.legal_neighbors()
            if not candidates:
                return None

            # Prefer the move that reduces disparity the most.
            nxt = min(candidates, key=lambda s: (s.gap(), s.a, s.b, s.c, s.e))
            self.state = nxt
            attempts += 1
            if attempts > 200:
                return None

    def step(self, phase: str) -> Optional[str]:
        """Run one explicit phase transition.

        Returns a message describing what happened under the current toy rules.
        """
        if phase == "expand":
            self.expand()
            return "expand"
        if phase == "local_instability":
            self.local_instability()
            return "local_instability"
        if phase == "reorganize":
            return self.reorganize() or "limited_search_failed"
        if phase == "dissolve":
            return self.dissolve() or "no_dissolution_path_found"
        raise ValueError(f"Unknown phase: {phase}")

    def run(self, phases: Iterable[str], max_steps: int = 30) -> List[Tuple[int, str, State, int]]:
        """Run a short staged simulation and return a compact trace.

        This is a demonstrative lifecycle trace, not a proof of physical emergence.
        """
        trace: List[Tuple[int, str, State, int]] = []
        for idx, phase in enumerate(phases):
            if idx >= max_steps:
                break
            msg = self.step(phase)
            trace.append((idx + 1, phase, self.state, self.state.gap()))
            if msg is None:
                # Explicitly record that no valid next response was found.
                trace.append((idx + 1, "no_valid_transition", self.state, self.state.gap()))
                break
        return trace


def demo() -> None:
    """Illustrative simulation output.

    The aim is to show that a constrained toy state-space can generate a staged
    trajectory that looks like:
      expansion -> local instability -> reorganization -> dissipative release.

    This is only a toy demonstration and should not be mistaken for a proven law
    of physical emergence.
    """
    system = ToySystem(State(3, 3, 2, 2))
    phases = ["expand", "local_instability", "reorganize", "dissolve"]
    print("Toy state-space experiment: total = 10")
    print("Rule layer: explicit constraints are separate from the relationship layer.")
    print("This model is only a minimal demonstration, not a physical theory.")
    print()

    for step, phase, state, gap in system.run(phases, max_steps=8):
        print(f"step={step:02d} phase={phase:<20} state={state} gap={gap}")


if __name__ == "__main__":
    demo()
