
  

## Clone the repository
```
git clone https://github.com/vxvishal/python-rest-api.git
```

## Download Python
[Download](https://www.python.org/downloads/) and install Python version **3.13.5**.

## Create a virtual environment
Create a Python virtual environment with the version above.

    python -m venv .venv

## Activate the environment
Windows:

    .venv/Scripts/activate
    
macOS and Linux:

    source .venv/bin/activate
    
## Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
Install uv inside the virtual environment with:

    pip install uv
    
## Install the dependencies
    uv sync
    
## Install pre-commit hooks
    pre-commit install
