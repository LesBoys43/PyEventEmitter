from typing import List, Any, Callable
from Event import Event

class EventListener:
    """
    事件监听器类，封装事件处理逻辑

    属性:
        event (str): 要监听的事件名称
        listener (Callable): 事件触发时的回调函数
    """
    event: str
    listener: Callable
    once: bool
    trigged: bool

    def __init__(self, event: str, listener: Callable, once: bool = False) -> None:
        """
        初始化事件监听器

        Args:
            event: 要监听的事件名称标识
            listener: 事件匹配时执行的回调函数，接收参数列表
            once: 是否只允许触发一次
        """
        ...

    def __call__(self, event: Event) -> Any:
        """
        执行事件监听逻辑（使实例可被直接调用）
        
        Args:
            event: 接收到的事件对象，包含事件名称和参数
        
        Returns:
            any: Listener的返回值（如果适用的话）
        """
        ...