from itertools import chain
from collections import Counter
import random
import roll
import unittest


class MyTestCase(unittest.TestCase):
    def test_tableroll(self):
        table_name = "wandering_activities"
        random.seed(1)
        amount = 100
        res = [roll.main([table_name], amount, out=False)][0]
        hist = Counter(list(chain(*res)))
        self.assertEqual(
            9,
            hist.get("Resting/wounded")
        )
        self.assertEqual(
            19,
            hist.get("Exploring")
        )
        self.assertEqual(
            6,
            hist.get("Fleeing")
        )
        self.assertEqual(
            24,
            hist.get("Hunting")
        )
        self.assertEqual(
            7,
            hist.get("Lost")
        )
        self.assertEqual(
            23,
            hist.get("Eating")
        )
        self.assertEqual(
            12,
            hist.get("Sleeping")
        )


if __name__ == '__main__':
    unittest.main()
