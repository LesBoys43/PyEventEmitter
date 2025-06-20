# Stub
from typing import List, Any, Callable, Union, Dict
from Event import Event
from EventListener import EventListener

class EventEmitter:
    """
    事件发射器类，用于管理事件监听器并触发相应事件。

    属性:
        listeners (List[EventListener]): 存储所有事件监听器的列表。
        hooks: (Dict[str, List[Hook]]): 勾子列表。
    """
    listeners: List[EventListener]
    
    def __init__(self, cfg: Dict[Any, Any] = {}):
        """初始化事件发射器，创建空监听器列表
        
        Args:
            cfg: 配置选项
        """
        ...
    
    def on(self, action: str, cb: Callable) -> None:
        """
        注册事件监听器
        
        Args:
            action: 要监听的事件名称
            cb: 事件触发时的回调函数，需接受一个List[Any]参数
        """
        ...
    
    def deon(self, action: str) -> None:
        """
        移除指定事件的所有监听器
        
        Args:
            action: 要移除监听器的事件名称
        """
        ...
    
    def once(self, action: str, cb: Callable) -> None:
        """
        注册事件监听器 但只会被触发一次
        
        Args:
            action: 要监听的事件名称
            cb: 事件触发时的回调函数，需接受一个List[Any]参数
        """
        ...
        
    def emit(self, action: str, args: List[Any]) -> any:
        """
        触发指定事件
        
        Args:
            action: 要触发的事件名称
            args: 传递给事件监听器的参数列表

        Returns:
            bool: 是否存在对应的监听器
            或
            any: Listener的返回值
        """
        ...
    
    def __dir__(self) -> List[str]:
      """
      获取当前已经注册的事件
      
      Returns:
          List[Any]: 有至少一个监听器监听的事件
      """
      ...
    
    def __iadd__(self, other: Dict[str, Union[str, Callable]]) -> "EventEmitter":
        """
        操作符重载 +=，用于快速注册事件监听器

        Args:
            other: 包含'act'（事件名）和'cb'（回调函数）的字典

        Returns:
            EventEmitter: 返回实例本身以支持链式调用
        """
        ...
    
    def __isub__(self, other: str) -> "EventEmitter":
        """
        操作符重载 -=，用于快速移除事件监听器

        Args:
            other: 要移除监听器的事件名称

        Returns:
            EventEmitter: 返回实例本身以支持链式调用
        """
        ...
    
    def hook(act: str, cb: Callable[[List[Any], Dict[str, Any]], None]) -> None:
        """
        注册一个钩子以在特定动作发生时执行回调函数

        Args:
            act (str): 钩子的名称，必须是available_hooks中定义的可用钩子之一
            cb (Callable[[List[Any], Dict[str, Any]], None]): 回调函数，接受参数列表和参数字典

        Raises:
            ValueError: 如果钩子名称不在支持的可用钩子列表中
        """
        ...