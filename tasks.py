from invoke import task

@task
def test(c, module=None):
    c.run(f"python -m pytest") 

@task
def watch(c):
    c.run("python watch.py")

@task
def flask(c):
    c.run('FLASK_ENV=development FLASK_APP=api.py flask run')
    #c.run('FLASK_APP=api.py flask run')
