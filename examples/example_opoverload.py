from EventEmitter import EventEmitter

# 创建事件发射器
emitter = EventEmitter()

# 使用 += 快速注册
emitter += {
    "act": "file_upload",
    "cb": lambda args: print(f"Uploaded {args[0]} ({args[1]} MB)")
}

# 触发带参数的匿名函数
emitter.emit("file_upload", ["report.pdf", 5.2])
# 输出: Uploaded report.pdf (5.2 MB)

# 使用 -= 快速移除
emitter -= "file_upload"
emitter.emit("file_upload", [])  # 返回 False