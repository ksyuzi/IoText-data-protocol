from dataclasses import dataclass
from decimal import Decimal
from typing import TypeVar, Union
from .metric_data import MetricDataTypes

MetricValueType = TypeVar("MetricValueType", bound=Union[str, int, Decimal, bool])


@dataclass(frozen=True)
class MetricDataItem:
    data_type: MetricDataTypes
    value: MetricValueType
