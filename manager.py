from unittest import TestLoader, runner
import click

@click.group()
def c():
    ...

@c.command()
def tests_codewars():
    loader = TestLoader()
    test = loader.discover('codewars/tests/')
    testrunner = runner.TextTestRunner()
    testrunner.run(test)

c()
