from collections import Counter
import random
from roll import main
from itertools import chain

def test_tableroll():
    table_name = "wandering_activities"
    random.seed(1)
    amount = 100
    res = [main([table_name], amount, out=False)][0]
    hist = Counter(list(chain(*res)))
    assert 9 == hist.get("Resting/wounded")
    assert 19 == hist.get("Exploring")
    assert 6 == hist.get("Fleeing")
    assert 24 == hist.get("Hunting")
    assert 7 == hist.get("Lost")
    assert 23 == hist.get("Eating")
    assert 12 == hist.get("Sleeping")