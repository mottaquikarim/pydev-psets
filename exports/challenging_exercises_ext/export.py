import pathlib
import re

pathlib.Path(
    "../../pset_challenging_ext/exercises").mkdir(parents=True, exist_ok=True)
pathlib.Path(
    "../../pset_challenging_ext/exercises/solutions").mkdir(parents=True, exist_ok=True)

fh = open('data.md', 'r')
contents = fh.read()
lines = contents.split('\n')
problems = []
start = False
for line in lines:
    if line == '#----------------------------------------#' and not start:
        problems.append('')
        start = True
        continue
    elif line == '#----------------------------------------#' and start:
        start = False
        continue

    if start:
        problems[len(problems)-1] += line + '\n'


for idx, problem in enumerate(problems):
    problem = re.sub('\n+', '\n', problem)
    pr_lines = problem.split('\n')

    ans_ = ""
    str_ = "\"\"\"\n"
    first_line = False
    for jdx, prl in enumerate(pr_lines):
        if first_line:
            str_ += f"\"\"\"\n\n\"\"\""
            break

        if 'question' in prl.lower() or 'level' in prl.lower():
            continue

        str_ += prl + '\n'
        first_line = True

    for jdx, prl in enumerate(pr_lines):
        if "Solution" in prl:
            ans_ = "\n".join(pr_lines[jdx+1:])
            str_ += "\n\"\"\""
            break

        str_ += prl + "\n"

    fh2 = open(f'../../pset_challenging_ext/exercises/p{idx+1}.py', 'w')
    fh2.write(str_)
    fh2.close()

    fh2 = open(f'../../pset_challenging_ext/exercises/solutions/p{idx+1}.py', 'w')
    fh2.write(str_ + "\n" + ans_)
    fh2.close()

fh.close()
