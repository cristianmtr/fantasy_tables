#! /usr/bin/env python
import random
import os
import sys
from collections import OrderedDict
from glob import glob

TABLE_DIR = os.path.abspath(".")

SUB_TABLE_PREFIX = "-->"

DEFAULT = "table"

if os.path.exists("tables"):
    TABLE_DIR = os.path.join(TABLE_DIR, "tables")


def d(sides):
    return random.randint(1, sides)


def d_roll(n, sides):
    return sum(tuple(d(sides) for _ in range(n)))


def table_exists(table_name):
    table_path = os.path.join(TABLE_DIR, table_name + ".table")
    if os.path.exists(table_path):
        return [l.strip() for l in open(table_path, "r").readlines()]
    else:
        return None


def handle_table3(lines):
    results = []
    for subtable_name in lines:
        table_lines = table_exists(subtable_name)
        if table_lines:
            results.append("%s : %s" % (subtable_name, handle_table(table_lines)))
    return "\n".join(results)


def handle_table2(lines):
    d = OrderedDict({
        int(l.split(":")[0].split("-")[-1]): l.split(":")[1].strip()
        for l in lines
    })
    roll = random.randint(1, max(d.keys()))
    chosen_entity = None
    lower_bound = 1
    upper_bounds = sorted(list(d.keys()))
    for i in range(len(upper_bounds)):
        upper_bound = upper_bounds[i]
        if roll >= lower_bound and roll <= upper_bound:
            chosen_entity = d[upper_bound]
            break
        lower_bound = upper_bound
    return chosen_entity


def handle_table_folder_choice(lines):
    choices = glob(os.path.join(lines[0], "*"))
    if len(choices) == 0:
        return "Folder not found"
    return handle_table1(choices)


def handle_table1(lines):
    return random.choice(lines)


def handle_table_proc(lines):
    chances = []
    entitites = []
    for l in lines:
        l_split = l.split("%")
        chance = int(l_split[0]) / 100
        entity = l_split[1]
        chances.append(chance)
        entitites.append(entity)
    return random.choices(entitites, chances)[0]


def handle_tableroll(lines):
    roll = lines[0].split(":")[1]  # ex. d8, 2d4
    sides = int(roll.split("d")[-1])
    nr_die = roll.split("d")[0] if roll.split("d")[0] != 'd' else '1'
    nr_die = int(nr_die)
    result = d_roll(nr_die, sides) - nr_die
    choices = lines[1:]
    return choices[result]


SCHEMAS = {
    "table": lambda lines: handle_table1(lines),  # random choice of lines
    "table2": lambda lines: handle_table2(lines),  # chances
    "table3": lambda lines: handle_table3(lines),  # subtables
    "tableroll": lambda lines: handle_tableroll(lines),  # subtables
    "table_proc": lambda lines: handle_table_proc(lines),
    "folder_choice": lambda lines: handle_table_folder_choice(lines)  # random file from glob of contents of directory
}


def handle_table(lines):
    schema_line = lines[0]
    choice = None
    if schema_line in list(SCHEMAS.keys()):
        choice = SCHEMAS[schema_line](lines[1:])
    elif ":" in schema_line and "d" in schema_line:
        choice = SCHEMAS["tableroll"](lines)
    else:
        choice = SCHEMAS[DEFAULT](lines)
    # perhaps subttable?
    if SUB_TABLE_PREFIX in choice and "\n" not in choice:
        subtable_lines = table_exists(choice.split(SUB_TABLE_PREFIX)[1])
        choice = choice.split(SUB_TABLE_PREFIX)[0]
        subroll = handle_table(subtable_lines)
        choice = "%s -- %s" % (choice, subroll)
    return choice


def main(tables, amount, out=True):
    results = []
    for table_name in tables:
        if ".table" not in table_name:
            full_table_file = os.path.join(TABLE_DIR, table_name) + ".table"
        else:
            full_table_file = os.path.join(TABLE_DIR, table_name)
        if os.path.exists(full_table_file):
            lines = [l.strip() for l in open(full_table_file, "r").readlines() if len(l.strip()) > 0]
            if out:
                print('=' * 10, table_name, '=' * 10)
            for nr in range(1, amount + 1):
                chosen = handle_table(lines)
                if out:
                    print('%s. %s' % (nr, chosen))
                results.append([chosen])
            if out:
                print()
    return results


def process_args():
    args = sys.argv[1:]
    amount = 1
    # print('args = %s' %args)
    to_remove = []
    for i, arg in enumerate(args):
        if arg == "-n":
            amount = int(args[i + 1])
            to_remove = [i, i + 1]

    tables = [t for i, t in enumerate(args) if i not in to_remove]
    return tables, amount


if __name__ == "__main__":
    tables, amount = process_args()
    main(tables, amount)
