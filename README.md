[![Build Status](https://travis-ci.com/joshuago78/labcat.svg?branch=master)](https://travis-ci.com/joshuago78/labcat) [![Coverage Status](https://coveralls.io/repos/github/joshuago78/labcat/badge.svg?branch=master)](https://coveralls.io/github/joshuago78/labcat?branch=master)

# labcat
A simple catalog for materials in the IS Lab.

This is a class project for students in IS289-4 - Web Development. It is intended for use by the student library/lab in the Information Studies Department at UCLA.

## Set Up for Developers

### Setting up Github accoutn with Git
At the command line:
- `git config --global user.name "<your name>"`
- `git config --global user.email <your email>`


### Installing the project
1. Go to the directory on your machine where you want to store your project repositories: `cd ~/projects` (or something similar)
2. Clone this repository: `git clone https://github.com/joshuago78/labcat.git`
3. Change directory: `cd labcat`
4. Create a virtual environment: `python3 -m venv ENV`
5. Activate the environment `source ENV/bin/activate`
6. Install the dependencies: `pip install -r requirements.txt`
7. Change directories to the django project: `cd labcat`

Now you are all set to run the Django management commands

## Some common Django management commands you will want to use

- `python manage.py shell` starts the Python interpreter that is Django aware.
- `python manage.py dbshell` starts the shell for SQLite3 (or whatever RDBMS you configure)
- `python manage.py runserver` runs your application on port 8000 (point your browser at http://127.0.0.1:8000)
- `python manage.py test catalog` runs the test suite in the `catalog/tests.py` file
- `python manage.py makemigrations` checks for changes to your models and makes a migration file
- `python manage.py migrate` converts migration files to SQL and implements the changes in the database

## Student / Developer Guide

Steps to take when working on this project

1. Pick an issue (or write a new one) to work on (remember the number)
2. Go to your project at the command line: `cd <some path>/labcat`
3. Activate virtual environment: `source ENV/bin/activate`
4. Checkout master branch: `git checkout master`
5. Create a new branch off of master: `git checkout -b <issue desc>/<issue #>`
6. Make your changes (inlcuding tests!)
7. Stage your changes for commit: `git add <some file>`
8. Commit your changes: `git commit -m "some message summarizing what you did"` (You can reference the issue number as well: "addresses #39" or "fixes #39")
9. Push changes to github: `git push origin <your branch>`
10. Create a Pull Request in Github, assign the instructor as a reviewer.
11. Reviewer will review the code, and if it is OK and the tests pass, then merge.