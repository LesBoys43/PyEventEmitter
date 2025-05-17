All test passed in 2025-05-17T20:26:21Z, triggered by commit 3a9cf4c, log:
[调试] 触发 'great' 事件结果: True (预期: True)
Execute: 基础调用 - 找到监听器; Summary: Nothing
Result: Pass
[调试] 回调后 'hey' 的值: 'Hello, Peppa' (预期: 'Hello, Peppa')
Execute: 基础调用 - 回调被正确调用; Summary: Nothing
Result: Pass
[调试] 触发 'bye' 事件结果: False (预期: False)
Execute: 基础调用 - 找不到监听器; Summary: Nothing
Result: Pass
[调试] 触发 'great' 事件结果: False (预期: False)
Execute: 基础调用 - 撤销的监听器; Summary: Nothing
Result: Pass
[调试] 运算符重载 - 添加监听器后触发结果: True (预期: True)
Execute: 运算符重载 - 创建; Summary: Nothing
Result: Pass
[调试] 回调执行状态: True (预期: True)
[调试] 运算符重载 - 移除监听器后触发结果: False (预期: False)
Execute: 运算符重载 - 删除; Summary: Nothing
Result: Pass
