# My First Python App

An introductory Python application (an unfinished game of rock-paper-scissors) for instructional purposes.

## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

## Installation

Fork this [remote repository](https://github.com/prof-rossetti/my-first-python-app) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd my-first-python-app
```

Use Anaconda to create and activate a new virtual environment, perhaps called "game-env":

```sh
conda create -n game-env python=3.7 # (first time only)
conda activate game-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

## Setup

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username:

    USER_NAME="Your Name"

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (via the [.gitignore](/.gitignore) file)

## Usage

Run the game script:

```py
python app/my_game.py

# OR ...

python -m app.my_game
```
