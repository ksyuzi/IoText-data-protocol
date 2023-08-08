from enum import Enum


class MetricDataTypes(str, Enum):
    INTEGER = "i"
    BOOL = "b"
    DECIMAL = "d"
    TEXT = "t"
