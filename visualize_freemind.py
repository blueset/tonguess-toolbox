import json
t3 = json.load(open("entropy_tree3.json"))
t4 = json.load(open("entropy_tree4.json"))

def traverse(node, path):
    if not isinstance(node, dict):
        raise ValueError(node)
    guess = node["guess"]
    print(f'<node TEXT="{guess}">')
    for k, v in sorted(node["outcomes"].items()):
        branch = f"{k[0]} – {k[1]}"
        if v is None:
            continue
        print(f'<node TEXT="{branch}">')
        if isinstance(v, str):
            print(f'<node TEXT="💡{v}"></node>')
        elif isinstance(v, dict):
            n_path = f'{path}_{guess}'
            traverse(v, n_path)
        print('</node>')
    print('</node>')


print("""
<map version="1.0.1">
<node TEXT="Start">
        <font NAME="SansSerif" SIZE="12" />
        <node POSITION="right" TEXT="4 letters">""")
traverse(t4, t4["guess"])
print("""
        </node>
        <node POSITION="left" TEXT="3 letters">""")
traverse(t3, t3["guess"])
print("""
        </node>
    </node>
</map>""")

# 