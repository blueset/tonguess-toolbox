import json
t3 = json.load(open("entropy_tree3.json"))
t4 = json.load(open("entropy_tree4.json"))


print("""digraph tree{
    node [fontname="FiraGo-Light"];
    edge [fontname="FiraGo-Light"];
    start [label="start", shape=box];""")

def traverse(node, path):
    if not isinstance(node, dict):
        raise ValueError(node)
    for k, v in node["outcomes"].items():
        branch = f"{k[0]} – {k[1]}"
        if isinstance(v, str):
            print(f'A_{v} [label="{v}", shape=box];')
            print(f'{path} -> A_{v} [label="{branch}"];')
        elif isinstance(v, dict):
            guess = v["guess"]
            n_path = f'{path}_{guess}'
            print(f'{n_path} [label="{guess}"];')
            print(f'{path} -> {n_path} [label="{branch}"];')
            traverse(v, n_path)

print(f"""

    {t3["guess"]};
    start -> {t3["guess"]} [label="3"];
""")


traverse(t3, t3["guess"])


print(f"""

    {t4["guess"]};
    start -> {t4["guess"]} [label="4"];
""")

traverse(t4, t4["guess"])

print("}")
