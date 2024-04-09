from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("poetry shell", pty=True)
    ctx.run("pytest src/tests", pty=True)
    ctx.run("exit", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)
    ctx.run("coverage html", pty=True)