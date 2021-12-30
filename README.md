# Aqueduct Fluidics Template Project #

This is a project that contains Aqueduct Device
Object creation methods to enable easier scripting
of Recipes in external IDEs like Pycharm and VS Code
with full fledged type-hinting and error checking.

### Setup Project ###

* Install & Activate Virtual Environment

On Linux/MacOS:

```
python3 -m venv env
source env/bin/activate
```

On Windows:

```
python -m venv env
env/Scripts/activate
```

* Install Requirements

On Linux/MacOS:

```
pip install -r requirements.txt
```

On Windows:

```
pip install -r requirements.txt
```

### Usage ###

The

```
local/lib/
```

path is intended to contain custom Python modules for the project.
The files in this path will be copied to the

```
~/aqueduct_app/local/lib/
```

path on the Hub to enable easy usage in complex recipes.

The

```
local/recipes/
```

path is intended to contain Recipe code scripts that can be copied
into the Aqueduct Recipe editor and run in simulation or lab mode.

The only files that should be modified are in the

```
local/
```
path.

### Testing ###

Requires module pytest (not part of requirements.txt)

```
pip install pytest-cov
```

to run tests:

```
python -m pytest
```