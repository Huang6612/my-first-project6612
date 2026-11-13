# 工程小项与 CLI 说明（v1.0）

**日期：** 2026-11-09  
**范围：** 仅补充“真正有用的小项”——元数据字段、CLI / 默认说明、关键错误提示。  
**不做：** PyPI、CI、万节点并行、模块大拆分。

> 本文记录用户提供的工程说明。文中提到的 `exp_meta.py` 与 `mother_field_model.py` 尚未出现在当前仓库文件列表中；代码文件补齐前，相关命令与实现细节不能仅凭本文在仓库中独立验证。

## 1. 已补内容（按提供资料）

| 项 | 交付 |
|---|---|
| 实验元数据 | `exp_meta.py`：`make_meta` / `write_result` / `defaults_option_b` |
| CLI 说明 | `python3 mother_field_model.py defaults` |
| 元数据示例 | `python3 mother_field_model.py meta-example` |
| 错误提示 | 转化失败、消散失败的 `RuntimeError` 文案补充可操作建议 |

## 2. 结果 JSON 元数据约定

Schema 名称：`mother_field_exp_meta_v1`。

```json
{
  "meta": {
    "schema": "mother_field_exp_meta_v1",
    "experiment": "deff_n60_main",
    "timestamp_utc": "2026-11-09T12:00:00Z",
    "python": "3.x.x",
    "platform": "...",
    "params": {
      "n": 60,
      "p_link": 0.0,
      "seeds": 12
    },
    "code": {
      "model_sha256_16": "前16位",
      "model_path": "mother_field_model.py"
    }
  },
  "result": {}
}
```

### 用法示例

```python
from exp_meta import make_meta, write_result

meta = make_meta("my_exp", {"n": 40, "p_link": 0.0})
write_result("out.json", {"d_eff_mean": 1.83}, meta)
```

元数据建议保留实验参数、运行环境、代码路径及代码哈希，以便追溯结果来源。

## 3. 选项 B 默认

以下默认口径与理论 / 口径一页纸一致（按提供资料）：

| 参数 | 默认 |
|---|---|
| `inherit` | `True` |
| `p_link` | `0.0` |
| `use_synergy` / `use_density` | `True` |
| `star_m` / `dens_theta` | `5` / `0.35` |
| `use_balance` | `False` |
| `policy` | 重组优先 |
| `max_resplit_depth` | `1` |
| `alpha` | `1.0` |

查看默认值：

```bash
python3 mother_field_model.py defaults
```

## 4. CLI 子命令一览

| 命令 | 用途 | 口径提示 |
|---|---|---|
| （无子命令） | 自检 A–D | 固定回归 |
| `scale` | 规模扫描 | 可加 `--whole` |
| `whole` | 三形式对照 | 对应主说明第 20 节 |
| `hysteresis` | `R(3)` / `A_stub` | T2 结构记忆指标线 |
| `tau` | 多循环 `Δτ` | T2 结构记忆指标线 |
| `stability` | 延续与扰动 | 验收 D |
| `locality` | 有效维 / 局域性 | `d_eff` 指标线；默认 `p_link=0`、开启三形式 |
| `defaults` | 显示默认值与命令一览 | 本说明所列口径 |
| `meta-example` | 输出元数据 JSON 示例 | 结果溯源 |

其它命令：`budget` / `burst` / `construct` / `select` / `x1`，用于历史或对照实验。

## 5. 用户可见错误提示

| 异常 | 含义 | 建议 |
|---|---|---|
| `ValueError: alpha 过小` | `k=2` 时 `alpha<1/2`，即使空图配额也不可行 | 提高 `alpha` |
| `ValueError: select ...` | 选择原则参数非法 | 使用 `random` / `min` / `max` |
| `RuntimeError: 转化失败` | `k` 连增 50 次仍不自洽 | 检查配额与约束；不要无限转化 |
| `RuntimeError: 消散无法恢复` | 边拆尽后仍不满足配额 | 增大 `k` 或 `alpha`；避免该 policy |

按提供资料，未引入独立异常类层级，以避免大规模改动；错误文案已补充可操作建议。

## 6. 与理论口径的关系

- 默认设置和指标分线见[理论 / 口径一页纸（v1.0）](theory_scope_one_page_v1.md)。
- T2 结构记忆使用 `hysteresis` / `tau` 与 `R(3)` / `Δτ`。
- 有效维使用 `locality` 与 `locality_probe`，不用于替代 T2 指标。
- 这些工程小项不改变公设或验收阈值。

## 7. 一句话

**能复现、能溯源、能查默认；不把玩具模型做成发行版框架。**
