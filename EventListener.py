from typing import List, Any, Callable
from Event import Event

class EventListener:
    """
    事件监听器类，封装事件处理逻辑

    属性:
        event (str): 要监听的事件名称
        listener (Callable): 事件触发时的回调函数
    """
    def __init__(self, event: str, listener: Callable) -> None:
        """
        初始化事件监听器

        Args:
            event: 要监听的事件名称标识
            listener: 事件匹配时执行的回调函数，接收参数列表
        """
        self.event = event
        self.listener = listener

    def __call__(self, event: Event) -> any:
        """
        执行事件监听逻辑（使实例可被直接调用）
        
        Args:
            event: 接收到的事件对象，包含事件名称和参数
        
        Returns:
            any: Listener的返回值（如果适用的话）
        """
        args: List[Any] = event.args
        action: str = event.action
        # 事件名称匹配时才执行回调
        if self.event == action:
            # 将事件参数列表传递给监听器
            return self.listener(args)
            
        return None