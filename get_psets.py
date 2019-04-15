import ast
import glob

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
        print('PTR', pset_name, as_module, problem_name, parts)
        if problem_name and not ptr.get(problem_name):
            print("problem_name", problem_name, as_module)
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
