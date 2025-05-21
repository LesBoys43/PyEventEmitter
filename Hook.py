from typing import Callable, Any, List, Dict
class Hook:
    def __init__(cb: Callable[[List[Any], Dict[str, Any]], Any]) -> None:
        self.cb = cb
    def __call__(self, *args, **kwargs) -> Any:
        return self.cb(args, kwargs)