# Python Boilerplate

This is a boilerplate for Python (3.9+) projects that contain both documentation generation (utilizing `pdoc`), and unit test generation (utilizing `pytest` and `pytest-cov` for code coverage). The project includes pre-made scripts and template code. Example docstrings are created using the Google-style Python docstring convention.

This project also includes `Makefile`, thus the Unix built-in command `make` can be used to automatically achieve all tasks.

## Usage

After you have cloned the repository, just run the command ``make`` or ``make help`` in the terminal to see all available commands:

```bash
$ make
Commands available:
 * clean          Remove all automatically generated files and folders
 * doc            Output pdoc HTML code documentation into folder docs/
 * help           Prints these help pages
 * install-deps   Install all required pip packages (dependencies)
 * run            Run code
 * test           Run tests in the tests/ folder. Outputs HTML results in folder htmlcov/
```

For example, to run the project:
```bash
make run
```

## Requirements

The following packages should be installed. They can be installed using the ``make install-deps`` commands.

- pytest (`pip3 install pytest`)
- pytest-cov (`pip3 install pytest-cov`)
- pdoc  (`pip3 install pdoc`)

## Usage

Just download this repository and add your own code in the `src` folder. Then you can run any of the scripts to run tests, create documentation or run your application.

## Project Structure

The project contains the following structure:
- `src/`: Contains all source code of the project.
- `resources/`: Contains all external resources of the project.
- `tests/`: There are generally two ways to load the test files; Alongside the source code, or in a separate folder. The second approach, where one tests folder is used, is used in this boilerplate. All test files are being mirrored in the same folder structure as the source code. The unit tests can be found under `tests/unit` and integration tests under `tests/integration`.

## Configuration Files

- `.coveragerc`: Contains the configurations for the code coverage package (`pytest-cov`).
- `conftest.py`: Contains the configurations for the `pytest` package.
