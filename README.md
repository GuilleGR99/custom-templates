custom-templates/
├── python-basic/
│   ├── cookiecutter.json
│   ├── hooks/
│   │   └── post_gen_project.py
│   └── {{ cookiecutter.project_slug }}/
│       ├── .gitignore
│       ├── pyproject.toml
│       ├── README.md
│       └── src/
│           ├── libs/
│           │   └── __init__.py
│           └── main.py


The python-basic/ directory provides a Cookiecutter template for generating structured Python projects.

cookiecutter.json

Defines the variables Cookiecutter requests when generating a project.

hooks/post_gen_project.py

Runs after project creation. Initializes a Git repository and creates the initial commit.

{{ cookiecutter.project_slug }}/

Represents the generated project structure:

.gitignore
Specifies files and directories excluded from version control.

pyproject.toml
Defines project metadata, dependencies, and tool configurations.

README.md
Provides basic usage and setup instructions.

src/
Contains the project’s source code:

libs/
Holds internal modules or utilities.

main.py
Entry point for executing the project.
