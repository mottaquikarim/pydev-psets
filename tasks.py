from invoke import task

@task
def test(c, module=None):
    c.run(f"python -m pytest") 

@task
def watch(c):
    c.run("python watch.py")
