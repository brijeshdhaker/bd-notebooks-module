uv init 

#
uv sync 
uv sync --active
uv sync --active --dev

#
uv build --wheel

#
uv pip install dist/bd_notebooks_module-1.0.0-py3-none-any.whl

uv tool install dist/bd_notebooks_module-1.0.0-py3-none-any.whl

uv pip freeze > requirments.txt

uv run -m zipfile -c dist/bd_notebooks_module-1.0.0.zip src/main/py/*


# Install Using Pip
python -m pip install --upgrade build
python -m build
pip install --force-install dist/bd_notebooks_module-1.0.0-py3-none-any.whl

# Run Module
python -m module_name.main
python -m com.example.hello
python -m com.example.app

python -m com.example.ai.apps.crewai.main

#
## Run Python __main__.py get executed
```bash

python dist/bd_notebooks_module-1.0.0.zip --Host localhost --App hello_py
````