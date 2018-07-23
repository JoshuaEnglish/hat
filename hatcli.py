"""hat
track the hat
"""

import os
import datetime
import click

DATA_PATH = click.get_app_dir('hat')
DATE_FMT = '%Y-%m-%d %H:%M:%S'

TEAMS = ['fed', 'smb', 'k12', 'pickering']
TASKS = ['quoting', 'bookings', 'shipping', 'opportunity']


@click.group()
@click.version_option()
@click.pass_context
def main(ctx):
    if not os.path.isdir(DATA_PATH):
        os.mkdir(DATA_PATH)
    pass


@main.command()
@click.argument('tags', nargs=-1)
@click.pass_context
def wear(ctx, tags):
    """Log switching to a new hat"""
    today = str(datetime.date.today())+'.txt'
    with open(os.path.join(DATA_PATH, today), 'a') as fp:
        timestamp = datetime.datetime.now().strftime(DATE_FMT)
        fp.write("%s: %s\n" % (timestamp, " ".join(tags)))
    click.echo(tags)


@main.command()
@click.pass_context
def showdata(ctx):
    """Opens the data folder"""
    os.startfile(DATA_PATH)


@main.command()
@click.pass_context
def showtoday(ctx):
    today = str(datetime.date.today())+'.txt'
    with open(os.path.join(DATA_PATH, today), 'r') as fp:
        for line in fp.readlines():
            print(line, end='')
