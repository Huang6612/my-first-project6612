# 母场玩具模型 · 文档与代码索引（收束 v1.0）

**日期：** 2026-11-10  
**用途：** 防止多文件口径漂移；对外表述以“理论 / 口径一页纸”为准，本页只做导航。  
**程序入口（按提供资料）：** `mother_field_model.py`

> 本索引依据用户提供的 v1.0 资料整理。下列某些权威文件名和数据文件名尚未在当前仓库中确认或归档；它们保留为项目资料清单，不代表文件已存在。当前仓库内可点击的文档列在“本仓库已归档入口”中。

---

## 1. 推荐阅读顺序

1. [理论 / 口径一页纸（v1.0）](theory_scope_one_page_v1.md)：分层、公设、选项 B，以及 `R(3)` / `Δτ` 与 `d_eff` 分线。
2. 玩具整理笔记：`mother_field_toy_v2_notes.md`（含选项 B、验收；需确认仓库中的实际文件名）。
3. 母场到最小动力学公设草案（v0.5.1）：A2/B2/C2/D2 与 T1–T3 半形式论证（待归档或确认实际路径）。
4. 按需阅读：有效维方案、选项 B 纪要、工程 CLI 说明、T1–T3 对照表。

## 2. 权威文档表

| 主题 | 文件 / 入口（按提供资料） | 口径角色 / 状态 |
|---|---|---|
| 单一口径源 | `理论口径一页纸_v1.0.md` / `.docx`；本仓库入口：[theory_scope_one_page_v1.md](theory_scope_one_page_v1.md) | 写作检查清单；避免混淆不同层次 |
| 玩具笔记 | `mother_field_toy_v2_notes.md` | 动力学、默认参数、验收叙述；需确认仓库实际文件名 |
| 公设与推论 | `母场到最小动力学公设草案.md`（v0.5.1） | 公设采纳集、T1–T3；待归档或确认实际路径 |
| T ↔ 验收 | [t1_t3_acceptance_mapping.md](t1_t3_acceptance_mapping.md) | 旁证对齐；不含有效维 |
| 选项 B | [option_b_b2_change_log.md](option_b_b2_change_log.md)；原资料另列 `.docx` | 主通道数据与默认变更 |
| 有效维 | `有效维诠释边界与deff检验方案_v0.1.md` | 声明窗、归档 12 vs 7、§8 非 T2 回线；待归档或确认实际路径 |
| 局域性基线 | [locality_baseline_v0.1.md](locality_baseline_v0.1.md) | 当前仓库已归档 v0.1；提供资料中提到的 v0.2 尚未归档 |
| 局域性规格 | `有效距离与局域性探测规格_v0.1.md` | `D_eff` 定义；待归档或确认实际路径 |
| 工程 / CLI | `工程小项与CLI说明_v1.0.md` / `.docx` | meta、defaults、错误提示；待归档或确认实际路径 |
| 本索引 | `docs/documentation_code_index_v1.md` | 导航 |

## 3. 代码与数据清单

以下路径和文件名来自提供的索引；未提供的文件需后续上传后才能核验或复现。

| 类型 | 路径 / 文件 | 状态 |
|---|---|---|
| 统一程序 | `mother_field_model.py` | 索引列出的程序入口；需确认当前仓库实际存在情况 |
| 有效维探测 | `locality_probe.py` | 索引列出的程序；需确认当前仓库实际存在情况 |
| 实验 meta | `exp_meta.py` | 索引列出的程序；需确认当前仓库实际存在情况 |
| 选项 B 扫描 | `b2_gen_scan_phase1.json`, `b2_gen_scan_phase2.json` | 原始 JSON 待上传 |
| `d_eff`，n=40/60 | `deff_n40_seeds12.json`, `deff_n60_seeds12.json` | 原始 JSON 待上传 |
| 窗稳健性 | `deff_window_robust_n40.json` | 原始 JSON 待上传 |
| 主通道消散路径 | `deff_T2_hysteresis_main.json` | 原始 JSON 待上传；提供资料称结论为“不支持同型有效维回线” |

### 常用命令（按提供资料）

```bash
python3 mother_field_model.py              # 自检 A–D
python3 mother_field_model.py defaults     # 选项 B 默认
python3 mother_field_model.py meta-example
python3 mother_field_model.py locality --seeds 6 --steps 14
python3 mother_field_model.py hysteresis
python3 mother_field_model.py tau
```

## 4. 分线速查（与一页纸一致）

| 问题 | 看哪里 | 不看哪里 |
|---|---|---|
| 结构记忆 / 时间箭头厚度 | `hysteresis` / `tau`，`R(3)`、`Δτ` | `d_eff` 消散回线 |
| 有效维 / 局域性 | `locality` + 有效维方案 | 不用来冒充 T2 或物理空间维 |
| 条件性质变 | 验收 A、选项 B 纪要 | 不声称“母场已推出转化” |
| 默认参数 | `defaults`、一页纸 §3 | 旧“高 `p_link` 主通道”叙述 |

## 5. 明确降级 / 勿作权威

| 文件或做法 | 说明 |
|---|---|
| 旧 v2.1/v2.2 散页、未标选项 B 的笔记片段 | 以统一玩具笔记与理论 / 口径一页纸为准 |
| NetworkX 平均路径“`d_eff`”草稿 | 已放弃，不接入基线 |
| 高 `p_link`、n=60 的结果“凑满 12 个种子” | 已放弃；按提供资料，归档为 7 个种子的同口径结果 |
| “有效维验证 T2”主线 | 不推进；提供资料称主通道实验不支持同型回线 |

## 6. 本仓库已归档入口

- [理论 / 口径一页纸（v1.0）](theory_scope_one_page_v1.md)
- [选项 B：B2 主通道变更纪要](option_b_b2_change_log.md)
- [局域性探测基线实验纪要（v0.1）](locality_baseline_v0.1.md)
- [T1–T3 ↔ 玩具验收 A–D 对照表](t1_t3_acceptance_mapping.md)

## 7. 一句话

**口径看一页纸，细节看笔记与公设草案，导航看本索引；`R(3)` / `Δτ` 与 `d_eff` 分线不变。**
