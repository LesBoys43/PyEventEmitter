from EventEmitter import EventEmitter
from liblbtest import test

def do_test():
    emitter = EventEmitter()
    
    loggedIn = False
    
    def login(args):
        nonlocal loggedIn  # 先声明nonlocal
        loggedIn = not loggedIn  # 再赋值
    
    emitter.once("login", login)
    
    # 测试用例1 - 第一次触发
    emit_result1 = emitter.emit("login", [])
    print(f"[调试] 首次触发结果: {emit_result1} (预期: True)")
    test("仅限一次 - 第一次", emit_result1, True)
    listsners = dir(emitter)
    print(f"[调试] 首次存在性检查结果: {listeners} (预期: ['login'])")
    test("仅限一次 - 第一次存在性检查", listeners, ["login"])
    
    print(f"[调试] 首次触发后状态: {loggedIn} (预期: True)")
    test("仅限一次 - 第一次正确调用", loggedIn, True)
    
    # 测试用例2 - 第二次触发
    emit_result2 = emitter.emit("login", [])
    print(f"[调试] 二次触发结果: {emit_result2} (预期: False)")
    test("仅限一次 - 第二次", emit_result2, False)
    
    listsners2 = dir(emitter)
    print(f"[调试] 首次存在性检查结果: {listeners2} (预期: [])")
    test("仅限一次 - 第二次存在性检查", listeners2, [])
    
    print(f"[调试] 二次触发后状态: {loggedIn} (预期: True)")
    test("仅限一次 - 第一次正确未调用", loggedIn, True)

if __name__ == "__main__":
    do_test()