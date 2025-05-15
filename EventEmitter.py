from typing import List, Any, Callable, Union, Dict
from Event import Event
from EventListener import EventListener

class EventEmitter:
    """
    事件发射器类，用于管理事件监听器并触发相应事件。

    属性:
        listeners (List[EventListener]): 存储所有事件监听器的列表。
    """
    def __init__(self, cfg: Dict[Any] = {}):
        """初始化事件发射器，创建空监听器列表
        
        Args:
            cfg: 配置选项
        """
        self.cfg = cfg
        self.listeners: List[EventListener] = []
    
    def on(self, action: str, cb: Callable) -> None:
        """
        注册事件监听器
        
        Args:
            action: 要监听的事件名称
            cb: 事件触发时的回调函数，需接受一个Event参数
        """
        self.listeners.append(EventListener(action, cb))
    
    def deon(self, action: str) -> None:
        """
        移除指定事件的所有监听器
        
        Args:
            action: 要移除监听器的事件名称
        """
        for listener in self.listeners:
            if listener.event == action:
                self.listeners.remove(listener)
    
    def emit(self, action: str, args: List[Any]) -> bool:
        """
        触发指定事件
        
        Args:
            action: 要触发的事件名称
            args: 传递给事件监听器的参数列表

        Returns:
            bool: 是否存在对应的监听器
        """
        has = False
        for listener in self.listeners:
            if listener.event == action:
                has = True
                event = Event(action, args)
                listener(event)
        return has
    
    def __iadd__(self, other: Dict[str, Union[str, Callable]]) -> "EventEmitter":
        """
        操作符重载 +=，用于快速注册事件监听器

        Args:
            other: 包含'act'（事件名）和'cb'（回调函数）的字典

        Returns:
            EventEmitter: 返回实例本身以支持链式调用
        """
        if other is not None and isinstance(other["act"], str) and callable(other["cb"]):
            self.on(other["act"], other["cb"])
        return self
    
    def __isub__(self, other: str) -> "EventEmitter":
        """
        操作符重载 -=，用于快速移除事件监听器

        Args:
            other: 要移除监听器的事件名称

        Returns:
            EventEmitter: 返回实例本身以支持链式调用
        """
        self.deon(other)
        return self