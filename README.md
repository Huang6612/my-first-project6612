# 母场玩具模型：研究资料与代码

> 本仓库包含母场概念稿、玩具模型说明、实验纪要与对照表。阅读时请区分概念立场、公设、推论、模型实现和实验探测；玩具实验是特定规则下的旁证，不是母场理论或物理现象的证明。

## 推荐阅读顺序

按“先统一口径，再理解模型，再看推论与实验”的顺序阅读：

1. **[理论 / 口径一页纸（v1.0）](docs/theory_scope_one_page_v1.md)** — 首要口径来源：分层、公设状态、选项 B 默认，以及 `R(3)` / `Δτ` 与 `d_eff` 两条指标线。
2. **[母场玩具模型三稿对齐笔记](mother_field_toy_v2_note.md)** — 模型定义、规则、响应、验收口径与探测说明。
3. **[状态流宇宙模型 v2.5](docs/state-flow-cosmos-v2.5.md)** — 上位概念稿和候选问题；阅读时注意文内“已定 / 候选”标签，不将概念稿中的候选表述当作玩具实验结论。
4. **[T1–T3 ↔ 玩具验收 A–D 对照表](docs/t1_t3_acceptance_mapping.md)** — 公设下半形式推论与固定回归的旁证对应；不含有效维探测。
5. **[选项 B：B2 主通道变更纪要](docs/option_b_b2_change_log.md)** — 三形式主通道的变更摘要和阶段扫描汇总。
6. **[局域性探测基线实验纪要（v0.1）](docs/locality_baseline_v0.1.md)** — 声明窗、分通道数据与有效维基线；不宣称物理空间维度涌现。
7. **[文档与代码索引（收束 v1.0）](docs/documentation_code_index_v1.md)** — 文件状态、代码/数据清单和分线速查。

## 代码与数据状态

- 当前仓库中可见的 Python 文件是 [`toy_model.py`](toy_model.py)。
- 部分资料提到统一程序 `mother_field_model.py`、探测程序 `locality_probe.py`、`exp_meta.py` 和多份 JSON 原始数据；这些文件**目前不在仓库文件列表中**。文档中的命令和结果因此尚不能仅凭当前仓库完整复现。
- 当前已归档的是 Markdown 说明和汇总表。若要让读者复核数值，请继续补充原始 JSON/CSV、运行配置、随机种子及对应代码版本；收到后再将其归入 `data/raw/` 等目录并更新索引。

## 建议的阅读边界

- “与 T1/T2/T3 一致”表示模型结果与相应推论方向相符，不表示证明了母场。
- 三形式、`p_link`、配额和有限重组容量是模型表示或实验设定，不是唯一物理实现。
- `R(3)` / `Δτ` 用于结构记忆相关讨论；`d_eff` 只按预先声明的拟合窗报告，不拿来替代 T2 或物理空间维数。

## 当前仓库文件

```text
README.md
 toy_model.py
 mother_field_toy_v2_note.md
 docs/
   documentation_code_index_v1.md
   locality_baseline_v0.1.md
   option_b_b2_change_log.md
   state-flow-cosmos-v2.5.md
   t1_t3_acceptance_mapping.md
   theory_scope_one_page_v1.md
```
