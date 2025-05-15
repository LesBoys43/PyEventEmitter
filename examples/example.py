from EventEmitter import EventEmitter
from typing import List, Any

# 创建事件发射器
emitter = EventEmitter()

# 定义回调函数
def user_login_handler(args: List[Any]):
    username, ip_address = args
    print(f"[Login] User {username} logged in from {ip_address}")

# 注册事件监听器
emitter.on("user_login", user_login_handler)

# 触发事件
emitter.emit("user_login", ["Alice", "192.168.1.100"])
# 输出：[Login] User Alice logged in from 192.168.1.100

# 检查是否存在监听器
print(emitter.emit("unknown_event", []))  # 输出: False