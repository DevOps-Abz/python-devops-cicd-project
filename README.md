# python-devops-cicd-project
This repo contains the code for the CI/CD section of my Python for DevOps project.

# venv setup

git clone https://github.com/DevOps-Abz/python-devops--cicd-project
in project directory run: 
python3 -m venv .venv
source .venv/bin/activate
which python

# command for .toml
pip install -e .

# 
src/ (This folder contains the application's Python code)
└── simple_http_checker/ (This folder groups related Python files together)
    ├── __init__.py (Makes the folder a Python package (it is often empty))
    ├── checker.py (This contains the code that performs the URL checking.)
    └── cli.py (CLI = Command Line Interface. This file handles user input from the terminal. talks to the user)