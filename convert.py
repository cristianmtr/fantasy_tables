import glob
import json
import os


def ignore_l(l):
    if "table3" in l or "table2" in l:
        return True

    return False


files = glob.glob("*.table")
for f in files:
    table_lines = open(f, "r", encoding="utf8").readlines()
    lines = [l.strip().replace("\u2013", "--") for l in table_lines if not ignore_l(l)]
    f = f.split(".table")[0]
    table_json = {
        "id": f,
        "name": " ".join(f.split("_")).title(),
        "roll": lines
    }
    json.dump(table_json, open(os.path.join("json", f + ".json"), "w", encoding="utf8"))
