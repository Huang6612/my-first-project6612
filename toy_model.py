from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Tuple


@dataclass(frozen=True)
class State:
    a: int
    b: int
    c: int
    e: int = 0

    def valid(self) -> bool:
        """合法状态：A/B/C/E 都非负，且总量固定为 10。"""
        return (
            self.a >= 0
            and self.b >= 0
            and self.c >= 0
            and self.e >= 0
            and self.a + self.b + self.c + self.e == 10
        )

    def __str__(self) -> str:
        return f"(A={self.a}, B={self.b}, C={self.c}, E={self.e})"


def neighbors(state: State) -> Iterable[State]:
    """一步合法动作集合。"""

    # 1) 核心内部重组：从一个核心变量转 1 到另一个核心变量
    for src_name, dst_name in (
        ("a", "b"), ("a", "c"),
        ("b", "a"), ("b", "c"),
        ("c", "a"), ("c", "b"),
    ):
        if getattr(state, src_name) <= 0:
            continue
        vals = {"a": state.a, "b": state.b, "c": state.c, "e": state.e}
        vals[src_name] -= 1
        vals[dst_name] += 1
        next_state = State(**vals)
        if next_state.valid():
            yield next_state

    # 2) 消散：核心变量 -> 环境 E
    for name in ("a", "b", "c"):
        if getattr(state, name) <= 0:
            continue
        vals = {"a": state.a, "b": state.b, "c": state.c, "e": state.e}
        vals[name] -= 1
        vals["e"] += 1
        next_state = State(**vals)
        if next_state.valid():
            yield next_state

    # 3) 转化：环境 E -> 核心变量
    if state.e <= 0:
        return
    for name in ("a", "b", "c"):
        vals = {"a": state.a, "b": state.b, "c": state.c, "e": state.e}
        vals[name] += 1
        vals["e"] -= 1
        next_state = State(**vals)
        if next_state.valid():
            yield next_state


def manhattan_distance(s1: State, s2: State) -> int:
    return (
        abs(s1.a - s2.a)
        + abs(s1.b - s2.b)
        + abs(s1.c - s2.c)
        + abs(s1.e - s2.e)
    )


def min_change_path(start: State, target: State) -> List[State]:
    """最小改变规则：每一步都从合法下一状态里选离目标最近的那个。"""
    current = start
    path = [current]

    while current != target:
        candidates = list(neighbors(current))
        if not candidates:
            raise ValueError(f"从 {start} 无法到达 {target}")

        current = min(
            candidates,
            key=lambda s: (
                manhattan_distance(s, target),
                s.a,
                s.b,
                s.c,
                s.e,
            ),
        )
        path.append(current)

    return path


def demo() -> None:
    start = State(3, 3, 4, 0)

    # 这些案例分别对应：扩展、重组、转化、消散
    # 不是唯一写法，但它们都能在该系统中自然出现
    examples = {
        "扩展": State(4, 3, 3, 0),
        "重组": State(2, 5, 3, 0),
        "转化": State(4, 2, 3, 1),
        "消散": State(3, 3, 3, 1),
    }

    print("最小玩具模型：A + B + C + E = 10")
    print("一步动作：")
    print("  - A/B/C 之间互相转移 1 个单位")
    print("  - 核心变量 -> 环境 E (消散)")
    print("  - 环境 E -> 核心变量 (转化)")
    print("最小改变规则：每一步挑最近目标的合法状态")
    print(f"起始状态：{start}")
    print()

    for label, target in examples.items():
        path = min_change_path(start, target)
        print(f"{label}：目标 = {target}")
        print("  路径：" + " -> ".join(str(s) for s in path))
        print()


if __name__ == "__main__":
    demo()
