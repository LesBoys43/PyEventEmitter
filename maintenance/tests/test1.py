from EventEmitter import EventEmitter
from liblbtest import test

# 将 hey 提升为模块级全局变量
hey = None

def do_test():
  global hey  # 声明操作的是全局变量
  emitter = EventEmitter()
  
  hey = None  # 重置状态
  
  def hello(args):
    global hey  # 明确操作全局变量
    hey = f"Hello, {args[0]}"
    
  emitter.on("great", hello)
  
  # 测试用例1 - 找到监听器
  emit_result = emitter.emit("great", ["Peppa"])
  print(f"[调试] 触发 'great' 事件结果: {emit_result} (预期: True)")
  test("基础调用 - 找到监听器", emit_result, True)
  listeners = dir(emitter)
  print(f"[调试] 监听器列表: {listeners} (预期: ['great'])")
  test("基础调用 - 列出监听器", listeners, ["great"])
  
  print(f"[调试] 回调后 'hey' 的值: {repr(hey)} (预期: 'Hello, Peppa')")
  test("基础调用 - 回调被正确调用", hey, "Hello, Peppa")
  
  # 测试用例2 - 找不到监听器
  emit_result = emitter.emit("bye", [])
  print(f"[调试] 触发 'bye' 事件结果: {emit_result} (预期: False)")
  test("基础调用 - 找不到监听器", emit_result, False)
  
  emitter.deon("great")
  
  # 测试用例3 - 撤销的监听器
  emit_result = emitter.emit("great", [])
  print(f"[调试] 触发 'great' 事件结果: {emit_result} (预期: False)")
  test("基础调用 - 撤销的监听器", emit_result, False)

if __name__ == "__main__":
  do_test()