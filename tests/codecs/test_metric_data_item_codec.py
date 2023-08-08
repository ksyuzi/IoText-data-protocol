from unittest import TestCase, skip

from src.codecs.metric_data_item_codec import MetricDataItemCodec
from src.types.metric_data import MetricDataTypes
from src.types.metric_data_item import MetricDataItem


class MetricDataItemCodecTest(TestCase):

    def test_decode(self):
        expected = MetricDataItem(MetricDataTypes.INTEGER, 1234)
        msg = 'i:1234'

        result = MetricDataItemCodec.decode(msg)

        self.assertEqual(expected, result)

    def test_encode(self):
        expected = 'd:100.09'
        mdi = MetricDataItem(MetricDataTypes.DECIMAL, 100.09)

        result = MetricDataItemCodec.encode(mdi)

        self.assertEqual(expected, result)

    def test_from_value_type_int(self):
        expected = MetricDataItem(MetricDataTypes.INTEGER, 42)

        result = MetricDataItemCodec.from_value(42)

        self.assertEqual(expected, result)

    def test_from_value_type_decimal(self):
        expected = MetricDataItem(MetricDataTypes.DECIMAL, 123.01)

        result = MetricDataItemCodec.from_value(123.01)

        self.assertEqual(expected, result)

    def test_from_value_type_text(self):
        expected = MetricDataItem(MetricDataTypes.TEXT, "xyZ")

        result = MetricDataItemCodec.from_value("xyZ")

        self.assertEqual(expected, result)

    def test_from_value_type_bool_true(self):
        expected = MetricDataItem(MetricDataTypes.BOOL, '1')

        result = MetricDataItemCodec.from_value(True)

        self.assertEqual(expected, result)

    def test_from_value_type_bool_true(self):
        expected = MetricDataItem(MetricDataTypes.BOOL, '0')

        result = MetricDataItemCodec.from_value(False)

        self.assertEqual(expected, result)
