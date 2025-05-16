from EventEmitter import EventEmitter
from typing import List, Any

# 创建事件发射器
emitter = EventEmitter()

def on_die(args: List[Any]):
  print(f"玩家{args[0]}被{args[1]}杀了")
  
# 使用once而不是on
emitter.once("die", on_die)

# 第一次：True
print(emitter.emit("die", ["张三", "李四"]))

# 第二次：False
print(emitter.emit("die", ["张三", "王五"]))