import json
import random
import sys

if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(f"""
Run an interactive session based on a decision tree.

Usage:
    {sys.argv[0]}
    {sys.argv[0]} stdev_tree
    {sys.argv[0]} entropy_tree
    """)
    exit()

base = "entropy_tree"

if len(sys.argv) > 1:
    base = sys.argv[1]

trees = {
    3: json.load(open(f"{base}3.json")),
    4: json.load(open(f"{base}4.json")),
}
d = {
    3: [i.strip() for i in open(f"dict3")],
    4: [i.strip() for i in open(f"dict4")]
}

threshold = 15

def candidates(tree, words=None):
    if words is None:
        words = list()
    if isinstance(tree, str):
        words.append(tree)
        return words
    if isinstance(tree, dict):
        for i in tree["outcomes"].values():
            words = candidates(i, words)
            if len(words) == threshold:
                words.append("...")
            elif len(words) > threshold:
                break
    return words

size = int(input("size? "))
tree = trees[size]
print(f"{random.choice(d[size])}!")

while isinstance(tree, dict):
    print("candidates", *candidates(tree))
    outcome = input(f"{tree['guess']}? ")
    tree = tree["outcomes"].get(outcome, None)
print(f"{tree}.")


