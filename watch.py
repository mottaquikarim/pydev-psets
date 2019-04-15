import ast
import sys
import time


import glob
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from get_psets import get_psets


class MyFileSystemEventHandler(FileSystemEventHandler):
    def on_any_event(self, evt):
        str_ = [
            '# README',
            '',
            '## Problems',
            '',
            # '| Problem        | Desc           |',
            # '| -------------  |:-------------: |',
        ]
        psets = get_psets('pset*/**/[!test]*.py')
        print('----------------------------')
        print(psets)
        print('----------------------------')
        for pset in psets:
            print('----------------------------')
            print(pset)
            print('----------------------------')
            str_ += ['', f'### {pset.replace("_", " ").replace("pset ", "").title()}']
            for subitem in psets[pset]:
                str_ += ['', f'#### {subitem.replace("_", " ").title()} ({len(psets[pset][subitem].items())} problems)']
                print('----------------------------')
                print(subitem)
                print(psets[pset][subitem])
                print('----------------------------')
                str_ += [
                    '',
                    # '| Desc        | ModuleName           |',
                    # '| -------------  |:-------------: |',
                ]
                for module in psets[pset][subitem]:
                    print('----------------------------')
                    print(subitem, module)
                    print(psets[pset][subitem][module])
                    print('----------------------------')
                    item = psets[pset][subitem][module]
                    filename = "tests/test_"+item['filename'].split('/').pop()
                    testfilename = item['filename'].split(
                        '/')[0:-1] + [(filename)]
                    # print('HERE', item, module, pset, subitem, psets)
                    # str_.append(f"| {item['docstring']} | [{module}]({item['filename']}) | ")
                    str_.append(f"* **[{item['docstring']}]({item['filename']})** | **[Tests]({'/'.join(testfilename)})**")
        print('here')
        f = open("README.md", "w")
        f.write("\n".join(str_ + ['', open('running.md', 'r').read()]))
        f.close()

        #     currRow = f"| [{filename}]({filename}) | "
        #     file = open(filename, "r")
        #     code = ast.parse(file.read())
        #     for node in ast.walk(code):
        #         if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
        #             docstring = ast.get_docstring(node)
        #             if docstring:
        #                 currRow = f"{docstring} |"
        #                 str_.append(currRow)
        #                 break

        # f = open("README.md", "w")
        # f.write("\n".join(str_ + ['', open('running.md', 'r').read()]))
        # f.close()


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = MyFileSystemEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
