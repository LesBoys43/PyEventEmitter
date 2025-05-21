from typing import Callable, Any, List, Dict

class Hook:
    """
    钩子函数封装类

    属性:
        cb (Callable[[List[Any], Dict[str, Any]], Any): 注册的回调函数
    """
    def __init__(self, cb: Callable[[List[Any], Dict[str, Any]], Any]) -> None:
        """
        初始化钩子实例

        Args:
            cb: 回调函数，接受位置参数列表和关键字参数字典
        """
        self.cb = cb

    def __call__(self, *args, **kwargs) -> Any:
        """
        执行回调函数

        Args:
            *args: 位置参数列表
            **kwargs: 关键字参数字典

        Returns:
            Any: 回调函数的执行结果
        """
        return self.cb(list(args), kwargs)