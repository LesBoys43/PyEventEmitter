All test passed in 2025-05-31T05:35:00Z, triggered by commit 791cf35, log:
[调试] 触发 'great' 事件结果: True (预期: True)
Execute: 基础调用 - 找到监听器; Summary: Nothing
Result: Pass
[调试] 监听器列表: ['great'] (预期: ['great'])
Execute: 基础调用 - 列出监听器; Summary: Nothing
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
[调试] 反向传递 - 传输结果: 10 (预期: 10)
Execute: 反向传递 - 传输; Summary: Nothing
Result: Pass
[调试] 反向传递 - 优先级结果: 25 (预期: 25)
Execute: 反向传递 - 优先级; Summary: Nothing
Result: Pass
[调试] 反向传递 - 默认值结果: None (预期: None)
Execute: 反向传递 - 默认值; Summary: Nothing
Result: Pass
[调试] 首次存在性检查结果: ['login'] (预期: ['login'])
Execute: 仅限一次 - 第一次存在性检查; Summary: Nothing
Result: Pass
[调试] 首次触发结果: True (预期: True)
Execute: 仅限一次 - 第一次; Summary: Nothing
Result: Pass
[调试] 首次触发后状态: True (预期: True)
Execute: 仅限一次 - 第一次正确调用; Summary: Nothing
Result: Pass
[调试] 二次触发结果: False (预期: False)
Execute: 仅限一次 - 第二次; Summary: Nothing
Result: Pass
[调试] 首次存在性检查结果: [] (预期: [])
Execute: 仅限一次 - 第二次存在性检查; Summary: Nothing
Result: Pass
[调试] 二次触发后状态: True (预期: True)
Execute: 仅限一次 - 第二次正确未调用; Summary: Nothing
Result: Pass
