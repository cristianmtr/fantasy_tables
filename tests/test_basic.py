from collections import Counter
import random

from ..roll import main
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


def test_subtable():
    table = "npc_rural"
    random.seed(1)
    amount = 1
    res = [main([table], amount, out=False)][0]
    assert res == [["jobs_rural : Military  -- 3) Bodyguard\nideals : Freedom. Everyone should be free to pursue his or her livelihood. (Chaotic)\ngoals : I will become the greatest thief that ever lived.\nflaws : Once I start drinking, it's hard for me to stop.\npersonality : I ask a lot of questions.\nnames : Karma\tKelvin\tMinax\nraces_prime :  Human"]]

def test_table2():
    table_name = "swn_atmosphere"
    random.seed(1)
    amount = 100
    res = [main([table_name], amount, out=False)][0]
    hist = Counter(list(chain(*res)))
    assert 9 == hist['Corrosive']
    assert 8 == hist['Inert gas']
    assert 13 == hist['Airless or thin atmosphere']
    assert 23 == hist['Breatheable mix']
    assert 22 == hist['Thick atmosphere, breathable with a pressure mask']
    assert 15 == hist['Invasive, toxic atmosphere']
    assert 10 == hist['Corrosive and invasive atmosphere'] 
