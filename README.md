### Hexlet tests and linter status:
[![Actions Status](https://github.com/gordienkoas/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/gordienkoas/python-project-50/actions)
[![CI check](https://github.com/gordienkoas/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/gordienkoas/python-project-50/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/8a0d61df77390d5df8a6/maintainability)](https://codeclimate.com/github/gordienkoas/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8a0d61df77390d5df8a6/test_coverage)](https://codeclimate.com/github/gordienkoas/python-project-50/test_coverage)

# ABOUT PROJECT 

This project focuses on working with collections. Methods for constructing and traversing trees are studied. You will become familiar with different data formats (JSON, YAML), learn how to parse and form them. Start writing tests (pytest) and master development using them. Learn about continuous integration (CI) and elements of extreme programming (XP)

## Requirements 
- Python 3.12
- Poetry
- make
- pip
- pipx(optional)

## INSTALLATION

To install, clone the repository and install using `poetry`:
```sh
git clone https://github.com/gordienkoas/python-project-50
cd gendiff
poetry install
```
## Usage

To display usage information:

```sh
poetry run gendiff -h
```

Example of comparing two files:

```sh
poetry run gendiff filepath1.json filepath2.json
```

The output will appear in the following format:

```json
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

## Command Line Options

- `-h, --help` — display this help message and exit.
- `-f FORMAT, --format FORMAT` — set the output format (supported formats: `plain`, `json`, `stylish`).

## Output Formats

### Stylish

The default format. Shows changes in a tree structure.

### Plain

A flat text format, convenient for human reading:

```sh
Property 'common.follow' was added with value: false
```

### JSON

Outputs the changes in JSON format, convenient for machine processing.

## Development

### Tests

To run tests, use the following command:

```sh
poetry run pytest
```

### Linter

To check the code with the linter, execute:

```sh
make lint
```

**Comparison of two-flat files: JSON.**

![asciicast](https://github.com/gordienkoas/python-project-50/blob/main/asciinema/json.gif)

**Comparison of two flat files: YAML(YML).**

[![asciicast](https://github.com/gordienkoas/python-project-50/blob/main/asciinema/yaml3.gif)](https://github.com/gordienkoas/python-project-50/blob/main/asciinema/yaml3.gif)

**Comparison of two files with a recursive structure: YAML(YML) or JSON.**

[![asciicast](https://github.com/gordienkoas/python-project-50/blob/main/asciinema/step3.gif)](https://github.com/gordienkoas/python-project-50/blob/main/asciinema/step3.gif)

**Comparison of two files  (flat format)**

[![asciicast](https://github.com/gordienkoas/python-project-50/blob/main/asciinema/step3.gif)](https://github.com/gordienkoas/python-project-50/blob/main/asciinema/step3.gif)

**Output the comparison result in JSON format.**

[![asciicast](https://github.com/gordienkoas/python-project-50/blob/main/asciinema/step4.gif)](https://github.com/gordienkoas/python-project-50/blob/main/asciinema/step4.gif)