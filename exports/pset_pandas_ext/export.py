import json
import pathlib

pathlib.Path(
    "../../pset_pandas_ext/101problems").mkdir(parents=True, exist_ok=True)
pathlib.Path(
    "../../pset_pandas_ext/101problems/solutions").mkdir(parents=True, exist_ok=True)

fh = open('data.json', 'r')
contents = json.loads(fh.read())
for idx, problem in enumerate(contents):
    fh2 = open(f'../../pset_pandas_ext/101problems/p{idx+1}.py', 'w')
    fh2.write(problem['p'])
    fh2.close()

    fh2 = open(f'../../pset_pandas_ext/101problems/solutions/p{idx+1}.py', 'w')
    fh2.write(problem['s'])
    fh2.close()

fh.close()
