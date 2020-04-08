# poetry-exemplar

## Setup

1. Install Poetry as per the official documentation as a one off installation.

https://python-poetry.org/docs/

2. Clone the repository.

3. Run ``poetry install`` in the project root via terminal.

4. Run ``poetry shell`` to activate your virtual environment, you can now develop as required.


## Build & Publish

If you run ``poetry build`` inside your package, it will create a PyPi ready .tar.gz file (or a .whl) in your ``dist`` folder that can pip installed.

If you have this project in another projects folder, you can pip install as ``pip install local_pypi/poetry-exemplar-0.1.0.tar.gz ``.

This can then be used in any file as ``from poetry_exemplar.add_one import add_one`` and use the function as ``add_one(2)``

If you run ``poetry publish`` and you have configured a repository with suitable credentials, it will push the package to a remote store. This can be pip installed with a suitable index.

## Use

- Running ``poetry add <DEPENDENCY>`` has to default behaviour to find the dependency on PyPi and to insert it into the relavent section in the ``pyproject.toml`` file.

- ``peotry install`` takes all the depedencies outlined in the ``pyproject.toml`` file and writes them to a ``peotry.lock`` file with precise versions, this is then committed to the repository to ensure environment consistency. If the ``.lock`` file already exists, Poetry installs the depedencies in this file and any new ones added to the ``.toml`` file (which then get added to the ``.lock`` file as well), with version preference given to the former to avoid version conflicts among a team.

- To use the latest versions of dependencies you can run ``poetry update`` which will update the ``.lock`` file accordingly.

- If you run ``poetry build`` the tool will package your application as a library for distribution to either PyPi or another repository. You can publish the library using the ``Poetry publish`` command (PyPi by default) if you have registered an account (it will ask you to login).

- If you want to have a 'src' folder you can run ``poetry new --src my-package``

- The ``remove`` command removes a package from the current list of installed packages.

- The ``shell`` command spawns a shell, according to the ``$SHELL`` environment variable, within the virtual environment. If one doesn't exist yet, it will be created. Inside a shell if you run ``exit`` you will leave the shell. Running ``poetry shell`` is also the easiest way to activate the venv for use.

- Getting a Venv up and running is easier with Poetry versus a MAKE process, running the ``shell`` command is more intuitive.

- You can add dev only dependenccies like so, these will not be packaged during a build - ``poetry add --dev pytest pytest-cov pytest-django pytest-xdist``

- You can run tests using the command ``poetry run pytest``

- You can configure Poetry to run scripts according to a command outlined the the 'toml' file e.g. ``Poetry run entry`` which runs dummy entry point code.

- You can add versioning via ``poetry version patch`` or ``poetry version minor`` etc.

## Dev Notes

- The core value of Poetry is dependency management in a collaborative setting, to ensure consistent development and deployment against a consistent set of dependencies.

- Poetry also helps easing project setup, through following the Poetry project scaffolding.

- Poetry has the potential to play nice with DVC, with the data folder at project root. This also extends to tools like MLFlow.

- Poetry uses your system default Python. If you need to change this. Poetry has a process to do so.


## Questions

- Is Poetry equally suitable for production and EDA / iteration?
    - ANSWER: It will run notebooks etc. fine.

- Does Poetry play nice with CI?

## Ideas

- Can I extend This Poetry projects?
    - Github Actions? Travis CI? DVC? ...

- CI Github Actions with poetry:

https://medium.com/@vanflymen/blazing-fast-ci-with-github-actions-poetry-black-and-pytest-9e74299dd4a5
