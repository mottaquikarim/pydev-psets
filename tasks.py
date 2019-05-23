from invoke import task

@task
def test(c, module=None):
    c.run(f"python -m pytest") 
