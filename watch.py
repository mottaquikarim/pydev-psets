import ast
import sys
import time


import glob
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from get_psets import _get_psets


def assemble_readme():
    psets, as_dict = _get_psets('pset*/**/*.py')
    num_problems = sum(
        [1 for pset in psets if not "solution" in pset[0] and not "test" in pset[0]])
    print(num_problems)
    str_ = [
        '# README',
        '',
        f'## Problems ({num_problems})',
        '',
        # '| Problem        | Desc           |',
        # '| -------------  |:-------------: |',
    ]

    for key, val in as_dict.items():
        total_problems = 0
        subblocks = ""

        for subk, subv in val.items():
            files = subv["files"]
            total_problems += len(files)
            fileblocks = ["<p>"]
            for i, file in enumerate(files):
                fileblocks.append(f"""
{i+1}. {file}
                """)
            fileblocks.append("</p>")
            fileblocks = "\n".join(fileblocks)
            subblocks += f"""
<details>
<summary><strong>{subk} ({len(files)})</strong></summary>
{fileblocks}
</details>
            """

        label = " ".join(key.split('_')[1:]).capitalize()
        block = f"""
<details>
<summary><strong>{label} ({total_problems})</strong></summary>
Here are the problems, broken into subblocks.
{subblocks}
</details>
        """
        str_.append(block)

    f = open("README.md", "w")
    f.write("\n".join(str_ + ['', open('running.md', 'r').read()]))
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
