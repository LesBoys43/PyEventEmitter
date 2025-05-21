from typing import Callable, Any, List, Dict

class Hook:
    """
    钩子类，用于封装回调函数
    
    属性:
        cb (Callable[[List[Any], Dict[str, Any]], Any]): 回调函数参数处理器
    """
    def __init__(self, cb: Callable[[List[Any], Dict[str, Any]], Any]) -> None:
        """
        初始化钩子处理器

        Args:
            cb: 接受参数列表和关键字参数字典的回调函数
        """
        ...

    def __init__(self, cb: Callable[[List[Any], Dict[str, Any]], Any]) -> None:
        """
        初始化钩子实例

        Args:
            cb: 回调函数，接受位置参数列表和关键字参数字典
            
        Raises:
            TypeError: 参数无效时
        """
        ...