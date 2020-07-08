import pickle

trees = [
    ("stdev_tree3", 3),
    ("stdev_tree4", 4),
    ("entropy_tree3", 3),
    ("entropy_tree4", 4)
]

def recur(node, depth, data, size):
    node = node[1]
    for k, v in node.items():
        if k == (size, 0):
            data[depth] += 1
        elif isinstance(v, int):
            data[depth + 1] += 1
        elif v is None:
            pass
        else:
            recur(v, depth + 1, data, size)


def stats(filename, size):
    tree = pickle.load(open(filename, "rb"))
    data = [0] * 10
    recur(tree, 1, data, size)
    print(data)
    total = sum(data)
    accum = 0
    for idx, i in enumerate(data):
        accum += idx * i
    print("Avg:", accum / total)


for i, size in trees:
    print()
    print(f"Stats for {i}")
    print("==============================")
    stats(i, size)