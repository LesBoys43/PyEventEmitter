from EventEmitter import EventEmitter
from liblbtest import test

def do_test():
    emitter = EventEmitter({'backwardTransfer': True})
    
    # 测试用例1 - 传输
    def calc1(args):
        return args[0] + args[1]  # 修正原代码的 args1] 拼写错误
    
    emitter.on("calc", calc1)
    result = emitter.emit("calc", [5, 5])  # 先捕获结果
    print(f"[调试] 反向传递 - 传输结果: {result} (预期: 10)")  # 调试输出
    test("反向传递 - 传输", result, 10)
    
    # 测试用例2 - 优先级
    emitter.on("calc", lambda args: args[0] * args[1])  # 修正参数索引为[0]和[1]
    result = emitter.emit("calc", [5, 5])
    print(f"[调试] 反向传递 - 优先级结果: {result} (预期: 25)")
    test("反向传递 - 优先级", result, 25)
    
    # 测试用例3 - 默认值
    result = emitter.emit("eat", [])
    print(f"[调试] 反向传递 - 默认值结果: {repr(result)} (预期: None)")  # 使用repr显示None
    test("反向传递 - 默认值", result, None)

if __name__ == "__main__":
    do_test()