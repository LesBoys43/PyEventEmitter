from typing import List, Any

class Event:
    """
    事件对象类，用于封装事件相关信息

    属性:
        action (str): 事件名称
        args (List[Any]): 事件携带的参数列表
    """
    def __init__(self, action: str, args: List[Any]) -> None:
        """
        初始化事件对象

        Args:
            action: 事件名称标识
            args: 事件携带的参数列表
        """
        self.action = action
        self.args = args