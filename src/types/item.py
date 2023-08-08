from typing import Optional
from dataclasses import dataclass
from .metric_data_item import MetricDataItem
from .item_type import ItemTypes


@dataclass(frozen=True)
class Item:
    kind: ItemTypes
    name: str
    metric: Optional[MetricDataItem] = None
