# 介绍
![GitHub License](https://img.shields.io/github/license/LesBoys43/PyEventEmitter?style=plastic) ![GitHub branch status](https://img.shields.io/github/checks-status/LesBoys43/PyEventEmitter/master?style=plastic) PyEventEmitter 是一个 Python 中类似 JavaScript 中事件发射器的工具 能够优秀的异步 跨文件处理消息传输
# 需求
* Python: 最低 3.6.0
# 功能
## 发射事件
通过 `emitter.emit` 来向所有监听了这个事件的人发射
## 监听／取消监听事件
通过 `emitter.on` `emitter.deon` 或者 += -= 来轻松处理
### 仅限一次（once）
通过 `emitter.once` 限制只被触发一次
### 运算符重载！
我们重载了 += 和 -= 让你十分简单的创建／取消监听器！
# 安装和使用
## 安装
直接复制 *.py 到项目目录中就能开始
## 使用
参考 MANUAL.md
# 贡献
如果你想贡献代码 请 fork 本项目 进行更改 然后发布拉取请求！