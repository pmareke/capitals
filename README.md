# Capitals API

## Endpoints

![Swagger docs](/images/swagger.png)

## Requirements
- You only need to have [Docker](https://www.docker.com/) installed.

## Folder structure

- The code is structured in four layers following the Hexagonal Architecture:
  - `Delivery`
  - `Use Cases`
  - `Infrastructure`
  - `Domain`

## Project commands

The project uses [Makefiles](https://www.gnu.org/software/make/manual/html_node/Introduction.html) to run the most common tasks:

- `help` : Shows this help.
- `local-setup`: Sets up the local environment (e.g. install git hooks).
- `build`: Builds the app.
- `update`: Updates the app packages.
- `install package=XXX`: Installs the package XXX in the app, ex: `make install package=requests`.
- `run`: Runs the app.
- `check-typing`: Runs a static analyzer over the code in order to find issues.
- `check-format`: Checks the code format.
- `check-style`: Checks the code style.
- `reformat`: Formats the code.
- `test`: Run all the tests.

**Important: Please run the `make local-setup` command before starting with the code.**

_In order to create a commit you have to pass the pre-commit phase which runs the check and test commands._

