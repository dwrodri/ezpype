from datetime import datetime
from typing import Callable, Sequence, Any, Optional
import logging


class Pipeline:
    def __init__(
        self,
        name: Optional[str] = None,
        transforms: Sequence[Callable[[Any], Any]] = [],
    ) -> None:
        pass
