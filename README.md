# Fantasy Tables

This is a Python script to generate random stuff for inspiration in fantasy pen&paper gaming.

Uses Python 3.6. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/)

## Usage

Open a terminal and run

```
python roll.py [-n (how many)] name_of_table
```

If `-n` is not provided, it generates one entity.


Examples:

```
$ python roll.py -n 3 jobs

========== jobs ==========
1. Bowyer
2. Madhouse caretakers
3. Cultist

```

There are also more complex tables, with sub-tables:

```
$ python roll.py npc_rural
========== npc_rural ==========
1. jobs_rural : Agriculture  -- 2) Farmer- a worker of the fields
ideals : Greed. I will do whatever it takes to become wealthy. (Evil)
goals : A powerful person killed someone I love. Some day soon, I'll have my revenge.
flaws : Gold seems like a lot of money to me, and I'll do just about anything for more of it.
personality : I'm willing to listen to every side of an argument before I make my own judgment.
portrait : /home/cristian/Downloads/Portraits-Portraits-Everywhere/PPE/Portraits/BDVALIS.bmp
```

## Adding your own tables

There are three types of supported schemas for the tables:

1. `table`. Picks at random from the list provided Ex.: `ideals.table`
2. `table2`. Picks at random, given distribution of probabilities. Ex.: `jobs_urban.table`
3. `table3`. Rolls on the given table names, and provides one final result. Ex.: `npc_rural.table`
4. `folder_choice`. Gets list of files in folder and picks at random between them. Ex.: `portrait.table`



