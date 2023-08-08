from typing import List

from src.codecs.item_codec import ItemCodec
from src.types.item import Item


class IoTextCodec:
    ITEMS_DIVIDER: str = ","

    @staticmethod
    def decode(payload: str, items_divider: str = ITEMS_DIVIDER) -> List[Item]:
        items: List[Item] = []
        items_lst = payload.split(items_divider)
        for item_str in items_lst:
            item_obj = ItemCodec.decode(item_str)
            items.append(item_obj)
        return items

    @staticmethod
    def encode(items: List[Item], items_divider: str = ITEMS_DIVIDER) -> str:
        return items_divider.join([ItemCodec.encode(i) for i in items])
