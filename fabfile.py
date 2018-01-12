# pylint: missing-docstring
import os
import sys
import logging

from fabric.api import task, run, local


DOT_FILES = [
    ("dotfiles/gitconfig", "~/.gitconfig"),
    ("dotfiles/simple_vimrc", "~/.vimrc"),
    ("dotfiles/tmux.conf", "~/.tmux.conf"),
]

logging.basicConfig(stream=sys.stdout)


def ab_path(fp):
    """get absolute path for file under dotfiles dir"""
    dirname = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dirname, fp)



@task
def install(ctx):
    for dotfile, target in DOT_FILES:
        if os.path.exists(target):
            msg = "{} exists, {} will not installed".format(target, dotfile)
            logging.warning(msg)


        cmd = "ln -s {source} {target}".format(source=ab_path(dotfile),
                                               target=target)
        ctx.run()
