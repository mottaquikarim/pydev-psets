import ast
import sys
import time


import glob
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from get_psets import _get_psets


def get_doc_str(file):
    docstring = "No Desc Provided"
    with open(file, "r") as fh:
        code = ast.parse(fh.read())
        valid_types = (ast.FunctionDef, ast.ClassDef, ast.Module)
        for node in ast.walk(code):
            if isinstance(node, valid_types):
                docstring = ast.get_docstring(
                    node)

    return docstring


def get_file_blocks(files):
    fileblocks = [
        '| PSET Desc  | Jupyter Notebook |',
        '| ------------- | ------------- |',
    ]
    for i, file in enumerate(files):
        docstring = get_doc_str(file)

        # build the `**/nb/**.ipynb` path
        dir_ = "/".join(file.split('/')[:-1] + ['nb'])
        filename = file.split('/').pop().split('.')[0]
        ipynb = "https://colab.research.google.com/github/mottaquikarim/pydev-psets/blob/master/" + dir_ + '/' + filename + '.ipynb'

        fileblocks.append(f"""| [{docstring}]({file})  | [Notebook]({ipynb}) |""")
    fileblocks.append("")
    return "\n".join(fileblocks)


def get_sub_blocks(subk, files, fileblocks):
    return f"""
### {" ".join(subk.split("_")).capitalize()} ({len(files)})
<details>
<summary>View Problems</summary>
<br/><br/>

{fileblocks}

<br/><br/>
</details>

    """


def get_block(label, total_problems, subblocks):
    return f"""
## {label} ({total_problems})
<details>
<summary>View Problems</summary>

{subblocks}

</details>

    """


def assemble_readme():
    psets, as_dict = _get_psets('pset*/**/*.py')
    num_problems = sum(
        [1 for pset in psets if not "solution" in pset[0] and not "test" in pset[0]])

    str_ = []
    header_ = [
        '# README',
        '',
        f'## Problems ({num_problems})',
        '',
    ]
    table_ = [
        '| PSET Name  | Num Problems | External? |',
        '| ------------- | ------------- | ------------- |',
    ]

    for key, val in as_dict.items():
        total_problems = 0
        subblocks = ""
        is_external = False
        if "_ext" in key:
            is_external = True

        for subk, subv in val.items():
            print(subv)
            files = subv["files"]
            total_problems += len(files)
            subblocks += get_sub_blocks(subk, files, get_file_blocks(files))

        label = " ".join(key.split('_')[1:]).upper()
        url = "-".join(key.split('_')[1:]) + '-' + str(total_problems)

        if is_external:
            is_external = f"[Yes](exports/{key})"
        else:
            is_external = "No"
        table_.append(f'| **[{label}](PROBLEMS.md/#{url})**  | {total_problems}  | {is_external}  |')
        str_.append(get_block(label, total_problems, subblocks))

    f = open("README.md", "w")
    f.write("\n".join(header_ + [""] + table_ +
                      ['', open('running.md', 'r').read()]))
    f.close()

    str_ = [
        "# Problems",
        "",
        "Listing of all problems defined"] + str_
    f = open("PROBLEMS.md", "w")
    f.write("\n".join(str_))
    f.close()


class MyFileSystemEventHandler(FileSystemEventHandler):
    def on_any_event(self, evt):
        assemble_readme()


if __name__ == "__main__":
    assemble_readme()

    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    # event_handler = MyFileSystemEventHandler()
    # observer = Observer()
    # observer.schedule(event_handler, path, recursive=True)
    # observer.start()
    # try:
    #     while True:
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     observer.stop()
    # observer.join()
