# My First Python App

An example Python application for students to run to test their local development environment setups.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/prof-rossetti/my-first-python-app) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd my-first-python-app
```

Use Anaconda to create and activate a new virtual environment, perhaps called "my-first-env":

```sh
conda create -n my-first-env python=3.8
conda activate my-first-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

## Setup

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username:

    USER_NAME="John Snow"

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [.gitignore](/.gitignore) file)

## Usage

Run the game script:

```py
python app/my_script.py

# alternative module-style invocation (only required if importing from one file to another):
python -m app.my_script
```

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment

## Further Exploration

If you would optionally like to learn the tricks for importing code from one local Python file to another, also attempt the steps below:

1. Un-comment the commented lines (13, 48, and 49) in "my_script.py". This code will attempt to import and use a function defined in the my_mod.py" file. After un-commenting these lines, save the file and try to re-run it. Notice the file will only run if you use the alternative module-style command (`python -m app.my_script`).

2. Read the contents of "my_mod.py". Try to run that file directly. Notice nothing happens. Un-comment the code in the global scope, save the file, and try to run the file directly. Notice it works, but if you try to run the "my_script.py" file again, the script is now broken. Finally, re-comment the code in the global scope, and un-comment the main conditional at the bottom, then save the file and re-run both the my_mod.py" and "my_script.py" files to see they now both work.
