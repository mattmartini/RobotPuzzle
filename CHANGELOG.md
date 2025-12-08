# Changelog for Robot Puzzle

All notable changes to this project will be documented in this file.

## [unreleased]

### 🚜 Refactor

- *(logging)* Move log statements to beginning of methods
- *(node)* Use set_outputs method

### 🧪 Testing

- *(node)* Differentiate tic from toc

### 📚 Documentation

- *(readme)* Clarification of legend
- *(notes)* How to run the puzzle app (also via watch & run)
- *(readme)* Fix typo

### 🎨 Styling

- *(readme)* Clean up documentation

### 🚧 Build

- *(cliff)* Fix error in default cliff.toml

### Other

- *(other)* Merge branch 'trial01'

* trial01:
  refactor(node): Use set_outputs method

## [1.4.2] - 2024-12-11

### ⚙️ Miscellaneous Tasks

- *(version)* Bump version 1.4.1 → 1.4.2

### 🚜 Refactor

- *(node)* Use match case to decide on actions

### 📚 Documentation

- *(api)* Rebuild API docs
- *(changelog)* Update Changelog
- Add doc for circles.py

### 🚧 Build

- *(bump)* Fix bump-my-version rc file git options

## [1.4.1] - 2024-12-11

### 🚀 Features

- *(circle)* Show status of robots in between tic and tock
- *(buffers)* Make buffers standout more

### ⚙️ Miscellaneous Tasks

- *(notes)* Update circle diagram
- *(ripgrep)* Don't search docs/ via .ignore
- *(version)* Bump patch version

### 🚜 Refactor

- *(circle)* Rename robots.py to circles.py. Fix references
- *(clock)* [**breaking**] Change take_action to advance_clock
- *(puzzle)* Refactor puzzle main

### 📚 Documentation

- *(changelog)* Update Changelog
- *(pytest)* Document run_pytest with help message
- *(readme)* Add to readme.md docs
- *(readme)* Add descriptions

### 🚧 Build

- *(bump)* Fix bump-my-version rc file date update

## [1.4.0] - 2024-12-06

### 🚀 Features

- *(console)* Add rich console for output
- *(console)* Update class outputs to use console with themes
- *(circle)* Increase the number of robots in the circle
- *(panels)* Introduce rich panels to buffer printing
- *(panels)* Use panels for robot printing
- *(circle)* Make robots print across via rich columns and panels
- *(console)* Improve output via console, panels, and columns

### ⚙️ Miscellaneous Tasks

- *(version)* Bump minor version

### 🧪 Testing

- *(console)* Update tests to use console with themes

### 📚 Documentation

- *(api)* Rebuild API docs
- *(changelog)* Update Changelog
- *(changelog)* Update Changelog
- *(api)* Rebuild API docs

### Other

- *(other)* Merge branch 'main' of gitvault.home.arpa:robotpuzz

* 'main' of gitvault.home.arpa:robotpuzz:
  docs(changelog): Update Changelog

## [1.3.1] - 2024-12-05

### 🚀 Features

- *(docs)* Update make_docs.sh to include changelog
- *(classes)* Log class instance deletion
- *(pytest)* Clear scrollback buffer before a series of tests
- *(puzzle)* Point puzzle at robotpuzzle:main in __init__.py
- *(puzzle)* Add commands for puzzle (uv run puzzle), bpython startup
- *(robots)* Add run_clock method

### 🐛 Bug Fixes

- *(node)* [**breaking**] Fix algorythm error caused by typo

### ⚙️ Miscellaneous Tasks

- *(notes)* Add note for PYTHONSTARTUP
- *(notes)* Add circle diagram
- Merge branch 'algorithm'

* algorithm:
  refactor(tock): Change algorithm for robots
  feat(robots): Add run_clock method
  feat(puzzle): Add commands for puzzle (uv run puzzle), bpython startup
  chore(notes): Add circle diagram
  chore(notes): Add note for PYTHONSTARTUP
  feat(puzzle): Point puzzle at robotpuzzle:main in __init__.py
  refactor(node): Move actions on tic and tock to new methods
- *(version)* Bump patch version

### 🚜 Refactor

- *(node)* Move actions on tic and tock to new methods
- *(tock)* Change algorithm for robots

### 📚 Documentation

- *(api)* Rebuild API docs
- *(changelog)* Update Changelog

### 🎨 Styling

- *(buffer)* Remove extra linefeed from repr

### 🚧 Build

- *(docs)* Script to create docs

### ◀️  Revert

- *(test)* Revert test values, changed due to error fixed in prev commit

## [1.3.0] - 2024-12-04

### 🚀 Features

- *(buffers)* Change Node buffers to a class

### ⚙️ Miscellaneous Tasks

- *(version)* Bump minor version

### 📚 Documentation

- *(changelog)* Update Changelog
- *(api)* Rebuild API docs

### 🎨 Styling

- *(typo)* Fix method name
- *(robots)* Update repr output

## [1.2.2] - 2024-12-04

### ⚙️ Miscellaneous Tasks

- *(version)* Bump patch version

### 🚜 Refactor

- *(logging)* Remove f-strings in logging

### 🧪 Testing

- *(coverage)* Report in html
- *(logging)* Add RichHandler, formats and handlers
- *(fixtures)* Add fixtures for CDLLs
- *(robots)* Add tests for CDLLs

## [1.2.1] - 2024-12-02

### 🚀 Features

- *(pytest)* Configure pytest options; watch files and re-run tests

### 🐛 Bug Fixes

- *(regex)* Fix escaping of double quotes
- *(node)* Remove default time value. Fix typo

### ⚙️ Miscellaneous Tasks

- *(uv)* Add pytest-html, ignore generated files
- *(uv)* Add pytest plugins, pytest-cov pytest-sugar pytest-random-order
- *(git)* Ignore .coverage
- *(version)* Bump patch version

### 🚜 Refactor

- *(node)* Split tests: initial and methods

### 🧪 Testing

- *(robots)* Temporarily disable robot tests
- *(node)* Add fixture returning a new node
- *(node)* Define test for a new node, method tests
- *(fixtures)* Move fixtures to conftest.py
- *(markers)* Add markers for node and initial
- *(node)* Add mode node tests. Fix activate call.
- *(marks)* Add multi mark
- *(fixtures)* Fixture for multiple nodes
- *(node)* Move class tests to pytest

### 📚 Documentation

- *(changelog)* Update Changelog

### 🚧 Build

- *(git)* Update files ignored
- *(metadata)* Add Author
- *(pytest)* Add more options to the runner

## [1.2.0] - 2024-11-27

### 🚀 Features

- *(path)* Use sys.path to show current path

### 🐛 Bug Fixes

- *(package)* Fix paths to include package
- *(paths)* Remove debugging for paths
- *(package)* Fix paths to include package

### ⚙️ Miscellaneous Tasks

- *(uv)* Install pytest module
- *(uv)* Add pylint
- *(uv)* Add bpython
- *(config)* Add configs for pylint, flake8, isort
- *(uv)* Remove textual module
- *(logs)* Create logs dir.  Git to ignore contents
- *(logs)* Send logfile to logs dir
- *(version)* Bump minor version

### 🚜 Refactor

- *(log)* Refactor per pylint
- *(logging)* Move to pkgutil from os path

### 🧪 Testing

- Create tests for node and robots

### 📚 Documentation

- *(changelog)* Update Changelog
- Add module docstring
- Clean up comments as per pylint

### 🎨 Styling

- *(quoting)* Use proper quoting

### 🚧 Build

- *(pytest)* Ignore scratch dir
- *(uv)* Add setuptools build system
- *(backend)* Try other backends hatch, flit
- *(pytest)* Add/remove pythonpath.  Seems not needed

### Other

- *(other)* Merge branch 'testing'

* testing: (21 commits)
  refactor(logging): Move to pkgutil from os path
  chore(logs): Send logfile to logs dir
  chore(logs): Create logs dir.  Git to ignore contents
  fix(package): Fix paths to include package
  build(pytest): Add/remove pythonpath.  Seems not needed
  fix(paths): Remove debugging for paths
  fix(package): Fix paths to include package
  chore(uv): Remove textual module
  style(quoting): Use proper quoting
  chore(config): Add configs for pylint, flake8, isort
  build(backend): Try other backends hatch, flit
  build(uv): Add setuptools build system
  feat(path): Use sys.path to show current path
  build(pytest): Ignore scratch dir
  test: Create tests for node and robots
  docs: Clean up comments as per pylint
  refactor(log): Refactor per pylint
  docs: Add module docstring
  chore(uv): Add bpython
  chore(uv): Add pylint
  ...

## [1.1.0] - 2024-11-25

### 🚀 Features

- *(logging)* Add simple logging to Node
- *(logging)* Move logging config to robots.py
- *(logging)* Convert to config file for logging
- *(logging)* Use in-line json for logging config
- *(logging)* Move logging config to jason file
- *(logging)* [**breaking**] Move logger definition to log.py
- *(logging)* Reconfigure logging config

### ⚙️ Miscellaneous Tasks

- *(logging)* Remove non-json config
- *(version)* Bump minor version

### 🚜 Refactor

- *(logging)* Remove extraneous code

### 📚 Documentation

- *(changelog)* Update Changelog

### Other

- *(other)* Merge branch 'logging'

Create a logging system

* logging:
  chore(logging): Remove non-json config
  feat(logging): Reconfigure logging config
  refactor(logging): Remove extraneous code
  feat(logging)!: Move logger definition to log.py
  feat(logging): Move logging config to jason file
  feat(logging): Use in-line json for logging config
  feat(logging): Convert to config file for logging
  feat(logging): Move logging config to robots.py
  feat(logging): Add simple logging to Node

## [1.0.5] - 2024-11-24

### ⚙️ Miscellaneous Tasks

- *(version)* Create VERSION file
- *(version)* Bump patch version

### 🚧 Build

- *(structure)* Conform to package structure
- *(pytest)* Use importlib for import mode
- *(style)* Add flake8 and flake8-pytest-style
- *(version)* Add bump-my-version
- *(version)* Sync versions with bump-my-version
- *(version)* Add VERSION file to bump-my-version config
- *(version)* Sync versions in prep for bump-my-config

## [1.0.4] - 2024-11-22

### ⚙️ Miscellaneous Tasks

- *(uv)* Install pdoc

### 📚 Documentation

- Update change log
- *(api)* Document API with pdoc

### 🚧 Build

- *(uv)* Move pdoc module to dev requirements

### Other

- *(other)* Merge branch 'docs'

* docs:
  build(uv): Move pdoc module to dev requirements

## [1.0.3] - 2024-11-22

### 🚀 Features

- *(node)* Add methods to read and flush buffers
- *(node)* Add activate/deactivate methods
- *(node)* Action taken on tic or tock time ticks
- Feat((robots)): Implementation of Circular doubly linked list

### 🧪 Testing

- *(node)* Expand testing of node

### 🎨 Styling

- *(node)* Fix indenting

## [1.0.2] - 2024-11-22

### 🚀 Features

- *(test)* Create __repr__ and __str__ and test()

### ⚙️ Miscellaneous Tasks

- *(uv)* Install pytput module
- *(uv)* Remove pytput module

### 🚜 Refactor

- *(test)* Reordered test output
- *(node)* Change node buffer names
- *(node)* Make repl more descriptive

### 📚 Documentation

- *(notes)* Update node output format
- *(notes)* Update node format

## [1.0.1] - 2024-11-20

### 🚀 Features

- *(node)* Create node, inc: init, repl

### 📚 Documentation

- *(changelog)* Initialize changelog configuration. Create it.
- *(GPLv3)* Add License
- *(notes)* Create node reporting format
- *(notes)* Update node format

### 🚧 Build

- *(dependencies)* Add required modules
- *(git)* Ignore Byte-compiled code
- *(gitignore)* Ignore scratch files

## [1.0.0] - 2024-11-19

### 📚 Documentation

- Initial Commit, problem definition
- Implementation notes

### 🚧 Build

- *(venv)* Create python virtual env
- Create RobotPuzzle project

<!-- generated by git-cliff -->
