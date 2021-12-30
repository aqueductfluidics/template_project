# Aqueduct Fluidics Template Project #

Use this repository as a template for developing Libraries and Recipes
for the Aqueduct Fluidics laboratory automation platform. 

### Aqueduct Module ###

The <b>aqueduct</b> module contains the API for the Aqueduct class. 

When a Recipe is executed in the Hub environment, an instance of the 
Aqueduct class named "aqueduct" is accessible globally. This class 
provides APIs for generating user prompts and inputs, creating setpoints, and 
recording and logging data.

### Devices Module ###

The <b>devices</b> module contains the APIs for each type of Device available 
in the Aqueduct Device Library. 

When a Recipe is executed in the Hub environment, instances of each Device Object
class are created for every Device in the active Setup with the same name as the Device. 
For example, a Peristaltic Pump of type <b>PP</b> and name <b>PPSIM</b> would be accessible 
as the global variable PPSIM. The <b>obj.py</b> files for each Device contain the 
hardware-specific API for a specific type of device.

### Setup Project ###

The Hub environment runs Python version 3.7. 

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

### Getting Started ###

The

```
local/lib/
```

path is intended to contain custom Python modules for your project.
When you're ready to upload a library to the Hub, compress your library 
in .zip format and upload using the user interface. For example, if you have
a libraru named "example", zip the "example" directory and upload. 

The files in this path will be copied to the

```
~/aqueduct_app/local/lib/
```

path on the Hub and can be used in your Recipes.

The

```
local/recipes/
```

path is intended to contain Recipe code scripts that can be copied
into the Aqueduct Recipe editor and run in simulation or lab mode.

Typically, you only want to modify files in the

```
local/
```
path.

