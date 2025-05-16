from EventEmitter import EventEmitter
from typing import Any, List
# 创建事件发射器并激活backwardTransfer选项
emitter = EventEmitter({'backwardTransfer': True})

# 创建处理器
full = False

def on_eat(args: List[Any]) -> bool:
  global full
  
  if not full:
    print(f"他吃下了 {args[0]}")
  else:
    print("他饱了！")
  
  _full = full # 临时储存
  
  full = True
  
  # 提交返回值
  return _full

# 激活监听器
emitter.on("eat", on_eat)

# 调用并保存返回值
first = emitter.emit("eat", ["猪肉"]) # False

second = emitter.emit("eat", ["牛肉"]) # True

print(first)
print(second)

# 未开启backwardTransfer时，emit返回是否有监听器（布尔值）
emitter_no_bt = EventEmitter({'backwardTransfer': False})

emitter_no_bt.on("eat", on_eat)

result = emitter_no_bt.emit("eat", ["猪肉"])  # True（表示有监听器）