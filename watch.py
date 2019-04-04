import ast
import sys
import time


import glob
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def get_psets(pattern):
    psets = {}

    for filename in glob.iglob(pattern, recursive=True):
        if "__pycache__" in filename or "solution" in filename:
            continue

        print(filename)
        parts = filename.split('/')

        pset_name = parts[0]
        problem_name = ".".join(parts[1:-1])
        as_module = filename.replace(
            '/', '.').replace('.py', '').replace('.__init__', '')

        print(pset_name, problem_name, as_module)
        if not psets.get(pset_name):
            psets[pset_name] = {}

        ptr = psets[pset_name]
        print('PTR', pset_name, as_module, problem_name)
        if problem_name and not ptr.get(problem_name):
            ptr[problem_name] = {}
            ptr[problem_name][as_module] = {
                "filename": filename,
            }
            ptr = ptr[problem_name]
        else:
            ptr[problem_name][as_module] = {
                "filename": filename,
            }
            ptr = ptr[problem_name]

        with open(filename, "r") as file:
            code = ast.parse(file.read())
            valid_types = (ast.FunctionDef, ast.ClassDef, ast.Module)
            for node in ast.walk(code):
                if isinstance(node, valid_types):
                    docstring = ast.get_docstring(node) or "No Desc Provided"
                    if docstring:
                        ptr[as_module]["docstring"] = docstring

    return psets


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
