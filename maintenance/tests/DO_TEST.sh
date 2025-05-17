#!/bin/bash

cd maintenance/tests/

# 创建或清空testing.log文件
> testing.log

# 依次执行test1.py到test4.py，并将输出同时显示在终端和追加到日志
for i in {1..2}; do
    python3.8 "test$i.py" 2>&1 | tee -a testing.log
done

# 运行check.py并捕获其标准输出作为退出码，不显示任何输出
exit_code=$(python3.8 check.py 2>/dev/null)
exit $exit_code
