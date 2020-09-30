SUBLIME
    Preferences.sublime-settings
    {
        "color_scheme": "Packages/Agila Theme/Agila Cobalt.tmTheme",
        "ensure_newline_at_eof_on_save": true,
        "ignored_packages":
        [
            "Vintage"
        ],
        "theme": "Agila Cobalt.sublime-theme",
        "ensure_newline_at_eof_on_save": true,
    }

    Python.sublime-settings
    {
        "tab_size": 4,
        "translate_tabs_to_spaces": true,
        "trim_trailing_white_space_on_save": true,
        "ensure_newline_at_eof_on_save": true,
        "rulers": [
            72,
            79
        ],
        "word_wrap": true,
        "wrap_width": 80,
    }

$ sudo apt update
$ sudo apt upgrade -y

$ exec "$SHELL"

GIT
    $ sudo apt install git -y
    $ clear;tree -I ".git|venv" -a -L 3
    $ clear;tree -a -I "__pycache__|Trash"
    $ git status
    $ git add -A
    $ git commit -m ""
    $ git checkout -b authentication
    $ git branch -d api
    $ git branch
    $ git branch -r
    $ git merge api
    $ git checkout master
    $ git pull origin
    $ git log --pretty=oneline -10
    # https://git-scm.com/book/sv/v2/Git-Tools-Stashing-and-Cleaning
    $ git stash -u
    git reset --hard
    $ git remote rm origin
    $ git remote add origin https://github.com/user/repo.git
    $ git remote -v
    $ git push -u origin db-register-execution # create remote branch
    $ git push origin db-register-execution
    $ git log --all --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
    $ git log --pretty=format:"%h %s" --graph
    # Move or rename a file, directory or symlink.
    $ git mv [-v] [-f] [-n] [-k] <source> <destination>
    $ git rm -f conf.py <-- saca del tracking

    git remote update
    git status -uno
    git pull

    git stash
    git checkout -b new-branch-name
    git stash apply
    git commit -a -m "commit message here"
    git checkout current-branch-name

    cjgith79
    cjwom790

    githubcj79 <-- mine
    gitcj79

TREE
    $ sudo apt install tree -y
    $ tree -a -I ".git|__pycache__|.gitignore" -L 3 -D

PYENV
    https://realpython.com/intro-to-pyenv/

    $ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
    libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl

    $ curl https://pyenv.run | bash

    # Load pyenv automatically by adding
    # the following to ~/.bashrc:

    export PATH="/home/ghost/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

    $ exec "$SHELL"


    $ pyenv install --list | grep " 3\.[678]"
    $ pyenv install --list | grep "jython"
    $ pyenv install --list
    $ pyenv install -v 3.8.3
    $ pyenv update <-- If you don’t see the version you’re looking for
    $ ls ~/.pyenv/versions/
    $ rm -rf ~/.pyenv/versions/2.7.15 <-- removing a version
    $ pyenv uninstall 2.7.15
    $ pyenv versions
    $ pyenv global 3.8.3 <-- The global command sets the global Python version.
    $ python -V
    $ python -m test
    $ pyenv commands
    $ pyenv shims --help
    $ pyenv which pip
    $ pip install -U pip

    $ pyenv local 2.7.15 <-- The local command is often used to set an application-specific Python version.
    # This command creates a .python-version file in your current directory. If you have pyenv active in your environment, this file will automatically activate this version for you.

    $ pyenv shell 3.8-dev <-- The shell command is used to set a shell-specific Python version.
    # This command activates the version specified by setting the PYENV_VERSION environment variable. This command overwrites any applications or global settings you may have. If you want to deactivate the version, you can use the --unset flag.

OPENFORTIVPN
    https://blog.zenggyu.com/en/post/2019-03-27/openfortivpn-an-open-source-alternative-to-fortinet-s-sslvpn-client/
    $ sudo openfortivpn

POSTGRESQL
    https://tecadmin.net/install-postgresql-server-on-ubuntu/
    $ psql --version
        psql (PostgreSQL) 12.2 (Ubuntu 12.2-4)

    ~/Documents/fosis/innovafosis$ psql ideas_fosis
    psql (12.2 (Ubuntu 12.2-4))
    Type "help" for help.

    ideas_fosis=> \l
                                       List of databases
        Name     |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges
    -------------+----------+----------+-------------+-------------+-----------------------
     ideas_fosis | ghost    | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
     postgres    | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
     template0   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
                 |          |          |             |             | postgres=CTc/postgres
     template1   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
                 |          |          |             |             | postgres=CTc/postgres
    (4 rows)

    ideas_fosis=> \dt

DUPLICATE ENVIRONMENT
    https://itsfoss.com/python-setup-linux/
    $ pip install -U pip
    $ pip freeze > requirements.txt <-- project
    $ pip install -r requirements.txt <-- duplicate

NPM
    $ sudo apt install -y npm

LINUX MINT
    Creating Soft Link or Symbolic Link
        $ ln -s source.file softlink.file

FIND & GREP
    https://alvinalexander.com/linux-unix/recursive-grep-r-searching-egrep-find/
    find . -type f -exec grep -l 'alvin' {} \;
    grep -rl alvin .
    grep -ril alvin /home/cato /htdocs/zenf
    egrep -ril 'aja|alvin' .
    egrep -ri href . | less

OD
$ od -c data/output.rst | less

PYTHON

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    print('Hello world !!!')

if __name__ == '__main__':
    main()

DOCKER
$ docker-compose up
$ docker stop $(docker ps -aq)
$ docker images
$ docker ps -a
$ docker rm $(docker ps -a -q -f status=exited)
$ docker volume ls
$ docker volume prune

MYSQL
# Para entrar a la consola mysql con el usuario testuser
$ docker exec -it mysql-test mysql -u testuser -ptestpassword
mysql> show databases;
mysql> use mytestdb;
mysql> show tables;
mysql> describe file;
mysql> select * from file;
mysql> quit

IMPORTS
# https://www.pythonforthelab.com/blog/complete-guide-to-imports-in-python-absolute-relative-and-more/

To execute file_b.py, do:

~/Document/lab$ ./execute_file_b.sh


~/Document/lab$ tree -I "__pycache__" imports/
imports/
├── mod_a
│   └── file_a.py
└── mod_b
    └── file_b.py

2 directories, 2 files
~/Document/lab$ cat imports/mod_a/file_a.py
def f_a():
    print('f_a()')
~/Document/lab$ cat imports/mod_b/file_b.py
from ..mod_a.file_a import f_a

def f_b():
    print('f_b()')
    f_a()

f_b()
~/Document/lab$ python -m imports.mod_b.file_b
f_b()
f_a()
~/Document/lab$
