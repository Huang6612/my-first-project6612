# 母场玩具模型：研究资料与代码

> 这是一个面向“整体性 / 局域性 / 结构重组”问题的玩具模型仓库。这里的内容分层明确：
> - 母场 / 公设 / 推论 / 玩具实现 / 探测指标 是不同层次，不能相互混用；
> - 任何实验结论都必须与其对应层次一致；
> - 代码与数据是研究中的基本材料，不等于对现实宇宙或母场终极理论的证明。

## 仓库定位

本仓库包含：
- 玩具模型说明与三稿对齐笔记
- 统一理论口径文档
- 上位概念稿（候选与已定标签分开）
- 公设与 T1–T3 半形式推论的旁证对照
- 选项 B 的主通道变更纪要
- 局域性探测基线与有效维说明
- 工程/CLI / 元数据说明

所有文档都遵循同一口径：
- 公设负责推论边界
- 选项 B 负责默认实现
- `R(3)` / `Δτ` 负责结构记忆 / 时间箭头厚度
- `d_eff` 负责声明窗中的局域性探测
- 不允许把不同指标线串成同一结论

## 推荐阅读顺序

1. [理论 / 口径一页纸（v1.0）](docs/theory_scope_one_page_v1.md)
   - 最关键的统一口径文档
   - 规定分层、默认参数、写作检查清单

2. [母场玩具模型三稿对齐笔记](mother_field_toy_v2_note.md)
   - 模型定义、动力学、响应、验收和默认条件

3. [状态流宇宙模型 v2.5](docs/state-flow-cosmos-v2.5.md)
   - 上位概念稿
   - 这是概念层 / 候选层，不等价于代码或实验结论

4. [T1–T3 ↔ 玩具验收 A–D 对照表](docs/t1_t3_acceptance_mapping.md)
   - 旁证对齐：模型观测与公设推论如何对应

5. [选项 B：B2 主通道变更纪要](docs/option_b_b2_change_log.md)
   - 三形式主通道如何取代历史 `p_link` 主通道

6. [局域性探测基线实验纪要（v0.1）](docs/locality_baseline_v0.1.md)
   - 记录声明窗内的局域性基线
   - 不宣称空间 / 物理局域性已涌现

7. [工程小项与 CLI 说明（v1.0）](docs/engineering_cli_v1.md)
   - 元数据字段、默认参数、错误处理、命令说明

8. [文档与代码索引（收束 v1.0）](docs/documentation_code_index_v1.md)
   - 文件入口、归档状态和待补充项

## 当前仓库状态

### 已归档文档

- README.md
- mother_field_toy_v2_note.md
- toy_model.py
- docs/theory_scope_one_page_v1.md
- docs/state-flow-cosmos-v2.5.md
- docs/t1_t3_acceptance_mapping.md
- docs/option_b_b2_change_log.md
- docs/locality_baseline_v0.1.md
- docs/engineering_cli_v1.md
- docs/documentation_code_index_v1.md

### 待补充的重要材料

下列资料在文档中被提到，但当前仓库中尚未出现：

- `mother_field_model.py`
- `locality_probe.py`
- `exp_meta.py`
- 选项 B 原始扫描数据：
  - `b2_gen_scan_phase1.json`
  - `b2_gen_scan_phase2.json`
- 有效维原始数据：
  - `deff_n40_seeds12.json`
  - `deff_n60_seeds12.json`
  - `deff_window_robust_n40.json`
  - `deff_T2_hysteresis_main.json`
- 进一步归档的公设草案 / 规格文档：
  - 《母场到最小动力学公设草案》v0.5.1
  - 《有效维诠释边界与 d_eff 检验方案》v0.1
  - 《有效距离与局域性探测规格》v0.1

这些文件没有补齐之前，仓库仍属于“说明型 / 汇总型”而不是“完全可复现型”研究仓库。

## 研究边界

本仓库的定位是：
- 可运行的模型原型
- 可复现的实验记录与说明
- 清晰的口径划分
- 不是现实宇宙 / 物理机制的直接证明

因此，仓库中所有结论都应在项目限定的语义内理解：
- 公设只负责“在模型内部的有效性”
- 模型实验只负责“在选定规则下的行为表现”
- 不得直接推导成现实宇宙的物理规律

## 使用建议

- 撰写论文或对外说明时，先看 [理论 / 口径一页纸](docs/theory_scope_one_page_v1.md)
- 若需要解释“为什么这不是物理空间维度涌现”，看局域性基线与口径说明
- 若需要解释“为什么不是从母场推出的直接定理”，看 T1–T3 对照表与公设说明
- 若需要复现或核验实验参数，优先补齐代码和原始 JSON 数据

## 一句话

本仓库的主线是：公设管推论，选项 B 管默认实现，`R(3)` / `Δτ` 管结构记忆，`d_eff` 管声明窗内局域性探测；四者并列，禁止串档。
