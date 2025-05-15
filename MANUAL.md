# EventEmitter 使用手册

`EventEmitter` 是一个轻量级事件管理类，用于注册、触发和移除事件监听器。适用于事件驱动编程场景，例如 GUI 交互、异步任务通知等。

---

## 目录

1. [安装](#安装)
2. [基本用法](#基本用法)
   - [初始化](#初始化)
   - [注册事件监听器](#注册事件监听器)
   - [移除事件监听器](#移除事件监听器)
   - [触发事件](#触发事件)
3. [操作符重载](#操作符重载)
4. [完整示例](#完整示例)
5. [注意事项](#注意事项)

---

## 安装

将 `EventEmitter.py`、`Event.py` 和 `EventListener.py` 文件放入项目目录，通过以下方式导入：

```python
from EventEmitter import EventEmitter
```

---

## 基本用法

### 初始化

创建一个 `EventEmitter` 实例：

```python
emitter = EventEmitter()
```

---

### 注册事件监听器

#### 方法 `on(action: str, cb: Callable)`
- **功能**：为指定事件（`action`）绑定回调函数（`cb`）。
- **参数**：
  - `action`：事件名称（字符串）。
  - `cb`：回调函数，需接受一个 `List[Any]` 类型的参数。

示例：

```python
def on_data_received(args: List[Any]):
    print(f"收到数据：{args}")

emitter.on("data", on_data_received)
```

---

### 移除事件监听器

#### 方法 `deon(action: str)`
- **功能**：移除指定事件（`action`）的所有监听器。
- **参数**：
  - `action`：事件名称（字符串）。

示例：

```python
emitter.deon("data")  # 移除所有 "data" 事件的监听器
```

---

### 触发事件

#### 方法 `emit(action: str, args: List[Any]) -> bool`
- **功能**：触发指定事件（`action`），并传递参数 `args` 给监听器。
- **参数**：
  - `action`：事件名称（字符串）。
  - `args`：传递给回调函数的参数列表。
- **返回值**：
  - `True`：存在至少一个监听器。
  - `False`：无监听器。

示例：

```python
emitter.emit("data", [1, 2, 3])  # 输出：收到数据：[1, 2, 3]
```

---

## 操作符重载

### `+=` 快速注册监听器

通过字典 `{"act": action, "cb": callback}` 添加监听器：

```python
# 等效于 emitter.on("click", handle_click)
emitter += {"act": "click", "cb": lambda args: print(f"点击事件，参数：{args}")}
```

### `-=` 快速移除监听器

通过事件名称字符串移除所有相关监听器：

```python
# 等效于 emitter.deon("click")
emitter -= "click"
```

---

## 完整示例

```python
from EventEmitter import EventEmitter

# 初始化发射器
emitter = EventEmitter()

# 定义回调函数
def log_event(args: List[Any]):
    print(f"日志事件：{args}")

# 注册事件
emitter.on("log", log_event)
emitter += {"act": "error", "cb": lambda args: print(f"错误：{args[0]}")}

# 触发事件
emitter.emit("log", ["用户登录"])      # 输出：日志事件：['用户登录']
emitter.emit("error", ["权限不足"])    # 输出：错误：权限不足

# 移除事件
emitter.deon("log")
emitter -= "error"

# 再次触发（无监听器）
emitter.emit("log", [])               # 返回 False
```

---

## 注意事项

1. **回调函数参数**：
   - 回调函数需接受一个 `List[Any]` 参数。例如：
     ```python
     # 正确
     def callback(args: List[Any]):
         print(args[0])

     # 错误（缺少参数）
     def invalid_callback():
         pass
     ```

2. **事件触发顺序**：
   - 监听器按注册顺序依次执行。

3. **异常处理**：
   - 如果回调函数抛出异常，`EventEmitter` 不会自动捕获，需在回调内部处理。

4. **线程安全**：
   - 默认非线程安全。若在多线程环境中使用，需自行添加锁机制。

5. **重复注册**：
   - 允许为同一事件多次注册同一回调函数，它们会被视为独立的监听器。

6. **操作符限制**：
   - `+=` 必须使用键名 `act` 和 `cb`，否则操作无效。
   - `-=` 只能移除事件的全部监听器，无法移除单个回调。

--- 

通过本手册，您可以快速掌握 `EventEmitter` 的核心功能。如有进一步问题，可参考源码或提交 Issue。