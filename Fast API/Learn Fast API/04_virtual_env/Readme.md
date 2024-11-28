# Virtual Environment
We use virtual environment to isolate the packages we install for each project locally.

# steps
- Create a directory for the project
- Create a virtual environment
go to the dir and then `python -m venv .venv` to create a new virtual environment.
- Activate the environment
activate the environment so that python command we run uses it for our project.
```bash
.venv\Scripts\Activate.ps1
```
Everytime a new package is installed we need to activate the environment again.
- Check if the environment is active
check with command `Get-Command python` if it shows python binary at .venv\Scripts
python then it is working.

**Upgrade the pip to the latest version**
`python -m pip install --upgrade pip`
- Add .gitignore file
add **.venv/** in the gitignore to ignore it.
- After activating the environment install packages in it
basically it is a good idea to install from `requirements.txt` ot `pyproject.toml` file.

**Installing fastapi**
`pip install "fastapi[standard]"`

- Run the program
- Deactivate the environment
After we are done working on our project we can deactivate the virtual environment
```bash
deactivate
```

- Try **uv** as alternative.