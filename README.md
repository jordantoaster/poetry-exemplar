# poetry-exemplar

## Setup

1. Install Poetry as per the official documentation as a one off installation.

https://python-poetry.org/docs/

2. Clone the repository.

3. 


## Use

- Running ``poetry add <DEPENDENCY>`` has to default behaviour to find the dependency on PyPi and to insert it into the relavent section in the ``pyproject.toml`` file.

- ``peotry install`` takes all the depedencies outlined in the ``pyproject.toml`` file and writes them to a ``peotry.lock`` file with precise versions, this is then committed to the repository to ensure environment consistency. If the ``.lock`` file already exists, Poetry installs the depedencies in this file and any new ones added to the ``.toml`` file (which then get added to the ``.lock`` file as well), with version preference given to the former to avoid version conflicts among a team.

- To use the latest versions of dependencies you can run ``poetry update`` which will update the ``.lock`` file accordingly.

- If you run ``poetry build`` the tool will package your application as a library for distribution to either PyPi or another repository. You can publish the library using the ``Poetry publish`` command (PyPi by default) if you have registered an account (it will ask you to login).

- If you want to have a 'src' folder you can run ``poetry new --src my-package``

- The ```remove`` command removes a package from the current list of installed packages.

- The ``shell`` command spawns a shell, according to the ``$SHELL`` environment variable, within the virtual environment. If one doesn't exist yet, it will be created. Inside a shell if you run ``exit`` you will leave the shell. Running ``poetry shell`` is also the easiest way to activate the venv for use.

- Getting a Venv up and running is easier with Poetry versus a MAKE process, running the ``shell`` command is more intuitive.




## Dev Notes

- The core value of Poetry is dependency management in a collaborative setting, to ensure consistent development and deployment against a consistent set of dependencies.

- Poetry also helps easing project setup, through following the Poetry project scaffolding.

- Poetry has the potential to play nice with DVC, with the data folder at project root. This also extends to tools like MLFlow.

- Poetry uses your system default Python. If you need to change this. Poetry has a process to do so.


## Questions

- Is Poetry equally suitable for production and EDA / iteration?
    - ANSWER: It will run notebooks etc. fine.

- How to run Tests? (Do I need a MAKEFILE that can be ran inside the venv?)

- Does Poetry play nice with CI?

- How to develop in a Poetry venv?


## Ideas

- Can I extend This Poetry projects?
    - Github Actions? Travis CI? DVC? ...

- Poetry needs a 'test' command, which spins up the venv and runs the unit tests via your given test framework.
