@echo off
REM 创建或清空testing.log文件
type nul > testing.log

REM 依次执行test1.py到test4.py，并将输出追加到日志
for /l %%i in (1,1,2) do (
    python3.8 test%%i.py >> testing.log 2>&1
)

REM 运行check.py并捕获其标准输出作为退出码
for /f %%a in ('python3.8 check.py') do set "exit_code=%%a"
exit /b %exit_code%
