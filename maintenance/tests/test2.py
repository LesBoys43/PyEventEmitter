from EventEmitter import EventEmitter
from liblbtest import test

def do_test():
    emitter = EventEmitter()
    
    # 定义事件处理器
    triggered = False  # 用于验证回调是否执行
    def handler(args):
        nonlocal triggered
        triggered = True
    
    # 测试用例1 - 通过 += 添加监听器
    emitter += {'act': 'handle', 'cb': handler}
    emit_result = emitter.emit("handle", [])
    print(f"[调试] 运算符重载 - 添加监听器后触发结果: {emit_result} (预期: True)")
    test("运算符重载 - 创建", emit_result, True)
    print(f"[调试] 回调执行状态: {triggered} (预期: True)")
    
    # 测试用例2 - 通过 -= 移除监听器
    emitter -= 'handle'
    emit_result = emitter.emit("handle", [])
    print(f"[调试] 运算符重载 - 移除监听器后触发结果: {emit_result} (预期: False)")
    test("运算符重载 - 删除", emit_result, False)

if __name__ == "__main__":
    do_test()