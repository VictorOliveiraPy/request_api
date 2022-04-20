from abc import ABC
from typing import List, Dict


class AbstractStarships(ABC):
    def get(self, page: int) -> List[Dict]:
        ...
