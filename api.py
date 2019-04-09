import json
import os
import pathlib
import sys


from ansi2html import Ansi2HTMLConverter
from flask import Flask, request
from subprocess import Popen, PIPE

from watch import get_psets

app = Flask(__name__, static_folder='public/build',static_url_path='',)
conv = Ansi2HTMLConverter()

def get_newpath(subpath):
    return subpath

    # get dir parts
    subpath_dir_parts = subpath.split('/')
    print(0, subpath_dir_parts)
    # get everything except last file
    subpath_dir = subpath_dir_parts[0:-1]
    print(1, subpath_dir)

    # read last part - that is filename
    filename = subpath_dir_parts.pop()
    print(2, filename)

    # try to create newpath directory
    newpath_dir = f"{'/'.join(subpath_dir)}/session"
    pathlib.Path(newpath_dir).mkdir(parents=True, exist_ok=True)
    print(3, newpath_dir)

    # assemble newpath
    return f"{newpath_dir}/{filename}"

@app.route("/list/problems", methods=['GET'])
def list_problems():
    psets = get_psets('pset*/**/[!test]*.py')
    return (json.dumps(psets), 200, {"Content-Type": "application/json",})

@app.route('/path/<path:subpath>', methods=["GET", "POST"])
def filepath(subpath):
    print(9)
    newpath = get_newpath(subpath)

    if request.method == "GET":

        if pathlib.Path(newpath).is_file():
            path_to_open = newpath
            with open(path_to_open, "r") as fh:
                content = fh.read()
        else:
            with open(subpath, "r") as fh:
                content = fh.read()
                with open(newpath, "w") as fh2:
                    fh2.write(content)

        return (json.dumps({
            "content": content,
        }), 200, {"Content-Type": "application/json"})

    payload = request.get_json()
    with open(f"{os.getcwd()}/{newpath}", "w") as fh:
        print('here')
        content = payload.get('content', None)
        if content:
            fh.write(content)
            return (json.dumps({
                "success": True,
            }), 200, {"Content-Type": "application/json"})

    return (json.dumps({
        "success": False,
    }), 200, {"Content-Type": "application/json"})

@app.route('/test/<path:subpath>', methods=["POST"])
def filepath_test(subpath):

    newpath = get_newpath(subpath)
    #abspath = os.path.abspath(newpath)
    app_dir = '/'.join(newpath.split('/')[0:-1])
    test_dir = '/'.join(newpath.split('/')[0:-1] + ['tests'])

    print('NEWPATH', newpath, app_dir, os.path.abspath(test_dir))
    print(f"{os.getcwd()}/{test_dir}")
    curr = os.getcwd()
    os.chdir(f"{os.getcwd()}/{app_dir}")
    output = ""
    with Popen(['python3',
                '-m',  # shorter traceback format
                'pytest',
                f"tests",], stdout=PIPE, bufsize=1, universal_newlines=True) as p:
        ansi = "".join(p.stdout)

    os.chdir(curr)

    return (json.dumps({
        "content": conv.convert(ansi),
    }), 200, {"Content-Type": "application/json"})

@app.route('/run/<path:subpath>', methods=["POST"])
def filepath_run(subpath):

    newpath = get_newpath(subpath)
    #abspath = os.path.abspath(newpath)
    app_dir = '/'.join(newpath.split('/')[0:-1])
    test_dir = '/'.join(newpath.split('/')[0:-1] + ['tests'])

    print('NEWPATH', newpath, app_dir, os.path.abspath(test_dir))
    print(f"{os.getcwd()}/{test_dir}")
    curr = os.getcwd()
    os.chdir(f"{os.getcwd()}/{app_dir}")
    output = ""
    p = Popen(['python3', newpath.split('/')[-1],], stdout=PIPE, stderr=PIPE, bufsize=1, universal_newlines=True)
    output, error = p.communicate()
    ansi = "".join(output)
    ansi += "".join(error)

    os.chdir(curr)

    return (json.dumps({
        "content": conv.convert(ansi),
    }), 200, {"Content-Type": "application/json"})

@app.route("/pyversion", methods=['GET'])
def py_version():
    return (json.dumps({
        "content": conv.convert(sys.version),
    }), 200, {"Content-Type": "application/json"})


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
