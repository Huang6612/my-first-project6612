# 母场玩具模型 · 文档与代码索引（收束 v1.0）

**日期：** 2026-11-10  
**用途：** 防止多文件口径漂移；对外表述以[理论 / 口径一页纸](theory_scope_one_page_v1.md)为准，本页负责导航和标明归档状态。  
**当前仓库程序文件：** `toy_model.py`。其他资料中提到的 `mother_field_model.py` 尚未出现在当前仓库文件列表中。

> 本索引按当前仓库实际文件整理。原资料中提及但尚未归档的代码、数据和文档会明确标为“待补充”，不代表它们已存在于仓库。

---

## 1. 推荐阅读顺序

1. [理论 / 口径一页纸（v1.0）](theory_scope_one_page_v1.md)：统一口径、分层、公设状态、选项 B 和指标分线。
2. [母场玩具模型三稿对齐笔记](../mother_field_toy_v2_note.md)：模型规则、动力学、验收及探测说明。
3. [状态流宇宙模型 v2.5](state-flow-cosmos-v2.5.md)：概念稿；遵守稿内“已定 / 候选”标签，不把候选内容当成已验证结论。
4. [T1–T3 ↔ 玩具验收 A–D 对照表](t1_t3_acceptance_mapping.md)：半形式推论与固定回归的旁证对应。
5. [选项 B：B2 主通道变更纪要](option_b_b2_change_log.md)：主通道变更及阶段扫描汇总。
6. [局域性探测基线实验纪要（v0.1）](locality_baseline_v0.1.md)：局域性探测协议和汇总结果。
7. 本索引：查看文件清单、待补充项和代码 / 数据状态。

## 2. 当前已归档文档

| 顺序 | 主题 | 仓库路径 | 用途 / 状态 |
|---:|---|---|---|
| 1 | 单一口径源 | `docs/theory_scope_one_page_v1.md` | 写作检查清单；区分理论、公设、推论、实现和指标 |
| 2 | 玩具模型说明 | `mother_field_toy_v2_note.md` | 模型定义、动力学、选项 B 与探测规格汇总 |
| 3 | 概念稿 | `docs/state-flow-cosmos-v2.5.md` | 上位概念与候选问题；不是代码验收报告 |
| 4 | T1–T3 ↔ A–D | `docs/t1_t3_acceptance_mapping.md` | 旁证对齐；不含有效维 |
| 5 | 选项 B 纪要 | `docs/option_b_b2_change_log.md` | 主通道变更与阶段 1/2 汇总 |
| 6 | 局域性基线 | `docs/locality_baseline_v0.1.md` | 候选探测基线；不宣称物理局域性或空间维度已涌现 |
| 7 | 本索引 | `docs/documentation_code_index_v1.md` | 导航和归档状态 |
| — | 代码 | `toy_model.py` | 当前仓库唯一可见的 Python 源文件；需核对是否与文档中的统一程序版本一致 |

## 3. 代码与数据状态

### 当前仓库已存在

- `toy_model.py`
- Markdown 文档及其中的实验汇总表

### 原资料提到、但当前仓库尚未归档

| 类型 | 文件名 / 资料 | 状态 |
|---|---|---|
| 统一程序 | `mother_field_model.py` | 待补充；README 中的详细复现命令暂不能由当前仓库验证 |
| 局域性探测程序 | `locality_probe.py` | 待补充 |
| 实验 meta | `exp_meta.py` | 待补充 |
| 选项 B 扫描原始数据 | `b2_gen_scan_phase1.json`, `b2_gen_scan_phase2.json` | 待补充；当前仅有 Markdown 汇总 |
| 有效维 n=40/60 | `deff_n40_seeds12.json`, `deff_n60_seeds12.json` | 待补充 |
| 窗稳健性 | `deff_window_robust_n40.json` | 待补充 |
| 主通道消散路径 | `deff_T2_hysteresis_main.json` | 待补充 |
| 公设草案 | `母场到最小动力学公设草案.md` v0.5.1 | 当前仓库未见；待归档 |
| 有效维方案 | `有效维诠释边界与deff检验方案_v0.1.md` | 当前仓库未见；待归档 |
| 局域性规格 | `有效距离与局域性探测规格_v0.1.md` | 当前仓库未见；待归档 |
| 工程 / CLI 说明 | `工程小项与CLI说明_v1.0.md` / `.docx` | 当前仓库未见；待归档 |

原始 JSON/CSV 上传后，建议按 `data/raw/`、`data/processed/` 分类，并在每份数据旁补充来源、字段说明、种子、参数、程序版本和生成命令。

## 4. 常用命令与可复现性

原资料列出的命令包括：

```bash
python3 mother_field_model.py              # 自检 A–D
python3 mother_field_model.py defaults     # 选项 B 默认
python3 mother_field_model.py meta-example
python3 mother_field_model.py locality --seeds 6 --steps 14
python3 mother_field_model.py hysteresis
python3 mother_field_model.py tau
```

**注意：** `mother_field_model.py` 尚未出现在当前仓库文件树中，因此以上命令是资料所述的预期入口，不应标注为已在当前仓库复现。当前存在的 `toy_model.py` 也不应未经核对就当作它的等价替代。

## 5. 分线速查

| 问题 | 查看 | 不要据此声称 |
|---|---|---|
| 结构记忆 / 时间箭头厚度 | `hysteresis` / `tau`，`R(3)`、`Δτ` | 用 `d_eff` 消散回线证明 T2 |
| 有效维 / 局域性 | locality 资料与预声明拟合窗 | 物理空间维度已涌现，或证明 T2 |
| 条件性质变 | 验收 A、选项 B 纪要 | 母场已推出转化 |
| 默认参数 | 理论 / 口径一页纸 §3 与选项 B 纪要 | 旧“高 `p_link` 主通道”是当前默认 |

## 6. 降级 / 勿作权威

| 文件或做法 | 说明 |
|---|---|
| 旧 v2.1 / v2.2 散页、未标选项 B 的笔记片段 | 以统一玩具笔记与理论 / 口径一页纸为准 |
| NetworkX 平均路径“`d_eff`”草稿 | 按提供资料已放弃，不接入基线 |
| 高 `p_link`、n=60 的结果“凑满 12 个种子” | 按提供资料已放弃；报告为 7 个种子的结果 |
| “有效维验证 T2”主线 | 不推进；资料称主通道实验不支持同型有效维回线 |

## 7. 一句话

**口径看一页纸，模型看三稿对齐笔记，概念背景看状态流稿，旁证看 T1–T3 对照与实验纪要；`R(3)` / `Δτ` 与 `d_eff` 分线不变。**
