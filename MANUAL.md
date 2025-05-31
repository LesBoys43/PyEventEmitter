# EventEmitter 使用手册

`EventEmitter` 是一个轻量级事件管理类，用于注册、触发和移除事件监听器。适用于事件驱动编程场景，例如 GUI 交互、异步任务通知等。

---

## 目录

1. [安装](#安装)
2. [配置选项](#配置选项)
3. [钩子功能](#钩子功能)
4. [基本用法](#基本用法)
   - [初始化](#初始化)
   - [注册事件监听器](#注册事件监听器)
   - [移除事件监听器](#移除事件监听器)
   - [触发事件](#触发事件)
   - [获取监听器列表](#获取监听器列表)
5. [操作符重载](#操作符重载)
6. [完整示例](#完整示例)
7. [注意事项](#注意事项)

---

## 安装

将 `EventEmitter.py`、`Event.py` 和 `EventListener.py` 文件放入项目目录，通过以下方式导入：

```python
from EventEmitter import EventEmitter
```

---

## 配置选项

`EventEmitter` 支持通过构造函数传入配置字典，用于定制事件触发行为。目前支持的配置项如下：

### `backwardTransfer` (bool)
- **功能**：控制 `emit` 方法的返回值类型。
- **默认值**：`False`
- **行为**：
  - `False`（默认）：`emit` 返回布尔值，表示是否存在对应的监听器。
  - `True`：`emit` 返回最后一个注册的监听器的返回值。若没有监听器，返回 `None`。

示例：

```python
# 默认配置（返回布尔值）
emitter_default = EventEmitter()

# 启用返回值传递
emitter_custom = EventEmitter({"backwardTransfer": True})
```

---

## 钩子功能（新增）

钩子（Hooks）允许在事件触发前后执行自定义逻辑，适用于日志记录、参数验证等场景。

### 可用钩子类型
- `sth-emitted`：任何事件被触发时调用
- `sth-emitted-exist-listener`：有监听器的事件被触发时调用（在监听器执行前）

### 注册钩子
#### 方法 `hook(act: str, cb: Callable)`
- **功能**：为特定动作注册钩子
- **参数**：
  - `act`：钩子类型（必须是支持的钩子类型）
  - `cb`：回调函数，接受以下参数：
    - `args`：原始事件参数列表
    - `kwargs`：包含事件信息的字典（键 `emitted` 为事件名）
- **异常**：如果钩子类型不支持，抛出 `ValueError`

示例：
```python
# 注册全局事件日志钩子
def log_hook(args, kwargs):
    print(f"事件触发: {kwargs['emitted']}, 参数: {args}")

emitter.hook("sth-emitted", log_hook)

# 注册带监听器的事件钩子
def listener_hook(args, kwargs):
    print(f"事件 {kwargs['emitted']} 有监听器将被执行")

emitter.hook("sth-emitted-exist-listener", listener_hook)
```

---

## 基本用法

### 初始化

创建 `EventEmitter` 实例时可传入配置字典：

```python
# 默认配置（backwardTransfer=False）
emitter = EventEmitter()

# 自定义配置（启用返回值传递）
emitter = EventEmitter({"backwardTransfer": True})
```

---

### 触发事件

#### 方法 `emit(action: str, args: List[Any]) -> any`
- **功能**：触发指定事件（`action`），并传递参数 `args` 给监听器。
- **参数**：
  - `action`：事件名称（字符串）。
  - `args`：传递给回调函数的参数列表。
- **返回值**：
  - 若 `backwardTransfer=False`（默认）：
    - `True`：存在至少一个监听器。
    - `False`：无监听器。
  - 若 `backwardTransfer=True`：
    - 返回最后一个注册的监听器的返回值。若没有监听器，返回 `None`。

示例：

```python
# 默认行为（返回布尔值）
emitter = EventEmitter()
emitter.on("log", lambda args: print("日志记录"))
print(emitter.emit("log", []))  # 输出：True

# 启用返回值传递
emitter_bw = EventEmitter({"backwardTransfer": True})
emitter_bw.on("calc", lambda args: args[0] + args[1])
result = emitter_bw.emit("calc", [3, 5])
print(result)  # 输出：8
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

#### 仅限一次（once）
- **功能**：为指定事件（`action`）绑定回调函数（`cb`）但是只会被调用一次。
- **参数**：
  - `action`：事件名称（字符串）。
  - `cb`：回调函数，需接受一个 `List[Any]` 类型的参数。

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

### 获取监听器列表
* 函数: `emitter.__dir__` (`dir(emitter)`)
- **返回**: `List[Any]`: 至少被一个监听器监听的事件列表

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

# 初始化带配置的发射器
emitter = EventEmitter({"backwardTransfer": True})

# 注册钩子：记录所有触发的事件
def global_hook(args, kwargs):
    print(f"[全局钩子] 事件 {kwargs['emitted']} 被触发，参数: {args}")

emitter.hook("sth-emitted", global_hook)

# 注册钩子：记录有监听器的事件
def listener_hook(args, kwargs):
    print(f"[监听器钩子] 事件 {kwargs['emitted']} 有监听器")

emitter.hook("sth-emitted-exist-listener", listener_hook)

# 注册监听器
emitter.on("process", lambda args: f"处理结果：{args[0] * 2}")

# 触发事件并获取返回值
result = emitter.emit("process", [10])
# 输出:
# [全局钩子] 事件 process 被触发，参数: [10]
# [监听器钩子] 事件 process 有监听器
print(result)  # 输出：处理结果：20

# 触发无监听器的事件
emitter.emit("unknown", [1, 2, 3])
# 输出:
# [全局钩子] 事件 unknown 被触发，参数: [1, 2, 3]
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

7. **返回值传递**：
   - 若启用 `backwardTransfer`，确保回调函数有明确返回值。未显式返回时，默认返回 `None`。
   - 返回值传递模式下，即使存在多个监听器，仅最后一个监听器的返回值会被传递。

8. **钩子使用**：
   - 钩子名称必须完全匹配可用钩子列表（`sth-emitted`, `sth-emitted-exist-listener`）
   - 钩子回调中修改参数不会影响实际的事件参数传递
   - 钩子应避免执行长时间阻塞操作
--- 

通过本手册，您可以快速掌握 `EventEmitter` 的核心功能。如有进一步问题，可参考源码或提交 Issue。