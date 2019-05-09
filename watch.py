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
        '| PSET Desc  |',
        '| ------------- |',
    ]
    for i, file in enumerate(files):
        docstring = get_doc_str(file)
        fileblocks.append(f"""| [{docstring}]({file})  |""")
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

{subblocks}
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
        '| PSET Name  | Num Problems |',
        '| ------------- | ------------- |',
    ]

    for key, val in as_dict.items():
        total_problems = 0
        subblocks = ""

        for subk, subv in val.items():
            files = subv["files"]
            total_problems += len(files)
            subblocks += get_sub_blocks(subk, files, get_file_blocks(files))

        label = " ".join(key.split('_')[1:]).upper()
        url = "-".join(key.split('_')[1:]) + '-' + str(total_problems)
        table_.append(f'| **[{label}](PROBLEMS.md/#{url})**  | {total_problems}  |')
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


if __name__ == '__main__':
    assemble_readme()


# class MyFileSystemEventHandler(FileSystemEventHandler):
#     def on_any_event(self, evt):
#         # _get_psets('pset*/**/[!test]*.py')
#         assemble_readme()
#         return
#         print('----------------------------')
#         print(psets)
#         print('----------------------------')
#         for pset in psets:
#             print('----------------------------')
#             print(pset, psets[pset]['time'])
#             print('----------------------------')

#             str_ += ['', f'### {pset.replace("_", " ").replace("pset ", "").title()}']
#             for subitem in psets[pset]['data']:
#                 str_ += ['', f'#### {subitem.replace("_", " ").title()} ({len(psets[pset][subitem].items())} problems)']
#                 # print('----------------------------')
#                 # print(subitem)
#                 # print(psets[pset][subitem])
#                 # print('----------------------------')
#                 str_ += [
#                     '',
#                     # '| Desc        | ModuleName           |',
#                     # '| -------------  |:-------------: |',
#                 ]
#                 for module in psets[pset][subitem]:
#                     # print('----------------------------')
#                     #print(subitem, module)
#                     # print(psets[pset][subitem][module])
#                     # print('----------------------------')
#                     item = psets[pset][subitem][module]
#                     filename = "tests/test_"+item['filename'].split('/').pop()
#                     testfilename = item['filename'].split(
#                         '/')[0:-1] + [(filename)]
#                     # print('HERE', item, module, pset, subitem, psets)
#                     # str_.append(f"| {item['docstring']} | [{module}]({item['filename']}) | ")
#                     str_.append(f"* **[{item['docstring']}]({item['filename']})** | **[Tests]({'/'.join(testfilename)})**")
#         print('here')
#         f = open("README.md", "w")
#         f.write("\n".join(str_ + ['', open('running.md', 'r').read()]))
#         f.close()

#         #     currRow = f"| [{filename}]({filename}) | "
#         #     file = open(filename, "r")
#         #     code = ast.parse(file.read())
#         #     for node in ast.walk(code):
#         #         if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
#         #             docstring = ast.get_docstring(node)
#         #             if docstring:
#         #                 currRow = f"{docstring} |"
#         #                 str_.append(currRow)
#         #                 break

#         # f = open("README.md", "w")
#         # f.write("\n".join(str_ + ['', open('running.md', 'r').read()]))
#         # f.close()


# if __name__ == "__main__":
#     path = sys.argv[1] if len(sys.argv) > 1 else '.'
#     event_handler = MyFileSystemEventHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path, recursive=True)
#     observer.start()
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()
