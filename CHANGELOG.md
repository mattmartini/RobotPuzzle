# Changelog for Robot Puzzle

All notable changes to this project will be documented in this file.

## [unreleased]

### 📚 Documentation

- *(api)* Rebuild API docs

### 🚧 Build

- *(docs)* Script to create docs

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

## [1.0.3] - 2024-11-22

### 🚀 Features

- *(node)* Add methods to read and flush buffers
- *(node)* Add activate/deactivate methods
- *(node)* Action taken on tic or tock time ticks

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
