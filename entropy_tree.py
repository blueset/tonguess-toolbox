#! /usr/bin/env python3

import pickle
from std_dev import entropy, count
from tqdm import tqdm
from multiprocessing import Pool
import math
import sys

if len(sys.argv) < 2:
    print(f"""
Build a decision tree by entropy.

Usage:
    {sys.argv[0]} 3
    {sys.argv[0]} 4
    """)
    exit()

word_length = int(sys.argv[1])
outcome_size = sum(range(word_length + 2))

if word_length not in (3, 4):
    print("word length must be 3 or 4.")
    exit(1)


# disbale debug
# print = lambda *a, **b: pass

base_indent = "  "

base = pickle.load(open(f"mapping{word_length}", "rb"))

depths = []


def entropy_set(item):
    guess, outcomes = item
    return guess, outcomes, entropy(outcomes, size=outcome_size)


def build(branch, level=0):
    # get the entry with min entropy
    best_entropy = float("-inf")
    best_outcomes = None
    best_guess = None
    main_indent = base_indent * (level * 2)
    sub_indent = base_indent * (level * 2 + 1)
    print(main_indent + "Calculating best entropy...")
    with Pool(8) as pool:
        entropys = pool.map(entropy_set, branch.items())
        for guess, outcomes, entropy in tqdm(entropys, total=len(branch), desc = main_indent):
            if entropy > best_entropy or (math.isclose(entropy, best_entropy) and outcomes.get((word_length, 0), 0)):
                best_entropy = entropy
                best_guess = guess
                best_outcomes = outcomes
    print(main_indent + "Guess word", best_guess, "with entropy", best_entropy)
    # count_map = {k: count(v) for k, v in best_outcomes.items()}
    # input(main_indent+f"distribution becomes {count_map}")

    print(main_indent + "Build decision tree branch...")
    deci_tree = {}
    # traverse outcomes
    for k, words in best_outcomes.items():
        if words == 0:
            deci_tree[k] = None
            print(sub_indent + "outcome", k, "has no word")
        elif count(words) == 1:
            deci_tree[k] = words.bit_length() - 1
            print(sub_indent + "outcome", k, "has word at index", deci_tree[k])
            depths.append(level)
        else:
            # build new branch
            print(sub_indent+"outcome", k,
                  "need further exploration. building new mappings...")
            new_branch = {}
            for guess, outcomes in base.items():
                new_outcomes = {}
                for outcome, i_words in outcomes.items():
                    new_outcomes[outcome] = words & i_words
                new_branch[guess] = new_outcomes
            print(sub_indent+"mappings built for outcome", k)
            deci_tree[k] = build(new_branch, level=level + 1)
    print(main_indent + "Branch built for", best_guess)

    return best_guess, deci_tree


decisions = build(base)

print("max depth =", max(depths), "avg depth = ", sum(depths)/len(depths))

print("tree is built, dumping...")
with open(f"entropy_tree{word_length}", "wb") as f:
    pickle.dump(decisions, f)
print("tree dumped.")
