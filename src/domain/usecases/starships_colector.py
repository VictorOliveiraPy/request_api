from abc import ABC
from typing import List, Dict


class AbstractStarships(ABC):
    def gt(self, page: int) -> List[Dict]:
        ...
