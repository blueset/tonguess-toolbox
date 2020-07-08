import pickle
import gmpy2
import json
import sys

trans = str.maketrans(
    "0123456789abcdefghijklmnop",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
)

if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(f"""
Translate a tree from pickle format to JSON.

Usage:
    {sys.argv[0]}
    {sys.argv[0]} stdev_tree
    {sys.argv[0]} entropy_tree
    """)
    exit()

tree_name = "entropy_tree"

if len(sys.argv) > 1:
    tree_name = sys.argv[1]

d = {
    3: [i.strip() for i in open(f"dict3")],
    4: [i.strip() for i in open(f"dict4")]
}

def trans_guess(guess: int, size: int) -> str:
    s: str = gmpy2.digits(guess, 26)
    s = s.rjust(size, "0")
    s = s.translate(trans)
    return s


def trans_outcome(index: int, size: int) -> str:
    try:
        return d[size][index]
    except KeyError:
        print("id", index, "is not found in size", size)
        return None

def translate(node, size):
    if isinstance(node, tuple):
        guess = trans_guess(node[0], size)
        branches = {f"{k[0]}{k[1]}": translate(v, size) for k, v in node[1].items()}
        return {
            "guess": guess,
            "outcomes": branches
        }
    elif node is None:
        return None
    else:
        return trans_outcome(node, size)


for l in (3,4):
    base = pickle.load(open(f"{tree_name}{l}", "rb"))
    result = translate(base, l)
    with open(f"{tree_name}{l}.json", "w") as f:
        json.dump(result, f)

