
---

## Overview

The `python-basic/` directory provides a Cookiecutter template for generating structured Python projects.

---

## Components

### **`cookiecutter.json`**
Defines the variables Cookiecutter requests when generating a project.

### **`hooks/post_gen_project.py`**
Executed after project creation. Initializes a Git repository and creates the initial commit.

### **`{{ cookiecutter.project_slug }}/`**
Represents the structure of the generated project.

- **`.gitignore`**  
  Defines ignored files and directories.

- **`pyproject.toml`**  
  Defines project metadata, dependencies, and tool configurations.

- **`README.md`**  
  Contains basic setup and usage instructions.

- **`src/`**
  Holds the project’s source code:

  - **`libs/`**  
    Internal modules or utilities.

  - **`main.py`**  
    Project entry point.

---

Si necesitas incluir esto para varias plantillas o generar un README general para todo el repositorio, te lo preparo también.

