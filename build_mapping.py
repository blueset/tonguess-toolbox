from itertools import product
from guess import guess
from typing import Dict, Set, Tuple, List
from multiprocessing import Pool
import pickle
from tqdm import tqdm
import sys


def calculate(i):
    idx = i[0]
    query = "".join(i[1])
    outcomes: Dict[Tuple[int, int], Set[str]] = {}
    for iidx, word in enumerate(words):
        outcome: Tuple[int, int] = guess(query, word)
        if outcome not in outcomes:
            outcomes[outcome] = 0
        outcomes[outcome] |= 1 << iidx
    # mapping[query] = outcomes

    # print(query, *[len(j) for j in outcomes.values()])
    return (idx, outcomes)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"""
    Build guess-outcome mappings.

    Usage:
        {sys.argv[0]} 3
        {sys.argv[0]} 4
        """)
        exit()

    word_len = int(sys.argv[1])

    if word_len not in (3, 4):
        print("word length must be 3 or 4.")
        exit(1)

    words: List[str] = [i.strip() for i in open(f"dict{word_len}")]

    mapping = {}

    with Pool(8) as pool:
        prod = enumerate(product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=word_len))
        m = pool.imap_unordered(calculate, prod)

        for k, v in tqdm(m, total=26**word_len):
            mapping[k] = v

    for k, v in enumerate(product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=word_len)):
        if len(set(v)) != len(v):
            del mapping[k]

    with open(f"mapping{word_len}", "wb") as f:
        pickle.dump(mapping, f)
