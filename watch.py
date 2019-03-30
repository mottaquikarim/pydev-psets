import ast
import sys
import time


import glob
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyFileSystemEventHandler(FileSystemEventHandler):
    def on_any_event(self, evt):
        str_ = [
            '# README',
            '',
            '## Problems',
            '',
            '| Problem        | Desc           |',
            '| -------------  |:-------------: |',
        ]
        for filename in glob.iglob('pset*/**/[!test]*.py', recursive=True):
            currRow = f"| [{filename}]({filename}) | "
            file = open(filename, "r")
            code = ast.parse(file.read())
            for node in ast.walk(code):
                if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
                    docstring = ast.get_docstring(node)
                    if docstring:
                        currRow += f"{docstring} |"
                        str_.append(currRow)
                        break

        f = open("README.md", "w")
        f.write("\n".join(str_ + ['', open('running.md', 'r').read()]))
        f.close()

        

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
