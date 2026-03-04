# Native Python Bit Array

Native python ```bitarray``` implementation supporting bitwise operations on instances as though the entire array was an integer.

This is similar to but not the same as the github package ```bitarray```.

## **UNDER DEVELOPMENT AND SUBJECT TO CHANGE**

```bitarray```s behave similar to ```bytearray```s, ```list```s and ```str```s.

- Instantiation:
  - ```bitarray(None)``` creates an empty bit array.
  - ```bitarray```s can be instantiated from ```bytearray```s, ```int```s, hex strings or an array of ```int```s.

- Conversions:
  - ```bitarray.to_bytearray()```
  - ```bitarray.to_int()```
  - ```bitarray.to_list()```

- List-like behavior:
  - ```bitarray``` objects support many standard sequence operations like slicing (including slice assignment and deletion), concatenation, iteration, the ```in``` operator, ```len()```.

- Bitwise Operations:
  - It supports bitwise operators such as ```&```, ```|```, ```^```, ```~```, ```<<```, and ```>>```.

## Usage Examples

## Python Project Software Build and Installation

For this project, [```uv```](https://github.com/astral-sh/uv) is used to

- Install Python
- Create and manage the virtual Python runtime environment
- Create a Python package and install it into the virtual environment
- Run specific Python modules installed in the virtual environment

Install ```git``` before cloning the software from this [github repository](https://github.com/thatlarrypearson/bitarray).  For a Windows or Mac ```git``` installation, go to [Microsoft Learn - Install and set up Git](https://learn.microsoft.com/en-us/devops/develop/git/install-and-set-up-git) and follow their instructions.

Use the ```apt``` package management system to install ```git``` on Debian Linux variants including Raspberry Pi, Ubuntu and Linux Mint.

```bash
apt install git
```

For Windows (and Mac) users, [GitHub Desktop](https://desktop.github.com/download/) is a GUI interface simplifying development workflows.

To install [```uv```](https://github.com/astral-sh/uv), follow these [```uv``` install instructions](https://docs.astral.sh/uv/getting-started/installation/)

After installing and testing [```uv```](https://github.com/astral-sh/uv), use [```git```](https://git-scm.com/downloads) to [clone this repository](https://github.com/thatlarrypearson/bitarray) onto your local target computer.

```bash
# Clone the git repository
git clone https://github.com/thatlarrypearson/bitarray.git
```

Next, use [```uv```](https://github.com/astral-sh/uv) to prepare the virtual Python environment, install the needed Python version (if needed), install the required external Python libraries, build [Vehicle Telemetry System software](https://github.com/thatlarrypearson/bitarray), install [```bitarray```](https://github.com/thatlarrypearson/bitarray) and run a simple test of the newly installed software.

```bash
# get into the cloned repository directory
cd bitarray

# create the virtual Python environment with the needed libraries
# by using the ```dependencies``` in the ```pyproject.toml``` file
uv sync

# Activate the Python Virtual Environment

# Windows PowerShell
.\.venv\Scripts\activate

# Linux/Mac bash Shell
source .venv/bin/activate

# When the Python Virtual Environment is activated, the prompt will change.

# Windows PowerShell
#     - (bitarray) PS C:\Users\username\bitarray >

# Linux/Mac bash Shell
#     - (bitarray) user@hostname:~/bitarray $

uv build .

# Developers and data analysts install the software such that changes are reflected
# in the virtual runtime environment automatically.
uv pip install -e .

# For production use, install the software as a Python package.
uv pip install dist/bitarray-0.0.0-py3-none-any.whl
```

## Simple Tests Validating Build and Installation

Before running any module, be sure to activate the Python virtual environment.

```bash
# get into the cloned repository directory
cd bitarray

# Activate the Python Virtual Environment

# Windows PowerShell
.\.venv\Scripts\activate

# Linux/Mac bash Shell
source .venv/Scripts/activate
```

Once the Python virtual environment is activated, run the tests as shown below.  Resolve any errors before continuing.

```bash
uv run -m bitarray.tester
```

Results should look something like the following:

```bash

```
