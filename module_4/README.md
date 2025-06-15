# Module 4

## Overview

This module contains documentation and source code for the project. The documentation is built using Sphinx and can be found in the `build/html` directory. The source code is located in the `src` directory, and tests are located in `tests`.
Documentation can be found at https://jhu-software-concepts-sphix-documentation.readthedocs.io/en/latest/
(as a note i could not figure out how to have the .yaml reside in module_4 sorry.)

## Directory Structure

- `source/` – Sphinx documentation source files
- `build/` – Generated documentation (HTML, doctrees, etc.)
- `src/` – Source code for the module
- `tests/` – Unit and integration tests for the module

## Building the Documentation

To build the HTML documentation, run the following command from the `module_4` directory:

```
make html
```

or on Windows:

```
make.bat html
```

The generated documentation will be available in `build/html/index.html`.

## Running the Tests

Pytest is used for testing. To run all tests run:

```
pytest module_4
```
