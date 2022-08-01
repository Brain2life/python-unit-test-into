# python-unit-test-intro
Introductory on Unit Testing Python Functions with Pytest, Visual Studio Code, Command-line

## Table of contents:
1. [Overview](#overview)
2. [Testing module setup](#testing-module-setup)
3. [Setting up a pytest Test module](#setting-up-a-pytest-test-module)
4. [Setting up pytest functions](#setting-up-pytest-functions)
5. [How to run pytest](#how-to-run-pytest)
6. [Test-driven development](#test-driven-development)
7. [Testing steps](#testing-steps)
8. [Important note](#important-note)

### Overview:
1. This repository shows an example of how to implement unit testing for total function
2. Total function - sums the elements of the list and returns the float type number
3. To install requirements use:
```shell
python3 -m pip install -r requirements.txt
```

### Testing module setup
To setup testing module in `pytest` in the same directory with your source files add the following suffix `[filename]_test.py`.  
For example test module for `my_program.py` will be `my_program_test.py`

### Setting up a pytest Test module
To test the definitions of a module, first create a sibling module with the same name, but ending in `_test`  
For example: module name --> `files.my_module`, test module will be --> `files.my_module_test`

### Setting up pytest functions
Add tests which are functions whose names *begin* with *test_*  
For example: `test_total_empty`

### How to run pytest
1. To run from any directory use:
```shell
python3 -m pytest -v [path_to_the_test_module.py]
```
2. In VSCode you can use GUI version for Python unit testing. Install Python extension from Microsoft - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### Test-driven development
1. Before you implement a function, write tests
2. Keep in this mind when writing tests:
    - What are some *usual* arguments? (Use cases)
    - What are some valid but *unusual* arguments (Edge cases)
    - Given those arguments, what is your *expected* return value for each set of inputs?

### Testing steps:
1. Write "dummy" function that satisfies the function definition (input parameters, return values)
2. Write test cases
3. Run tests first time. They must fail
4. Modify your dummy function, so that it passes the test
5. Re-run the tests, check results. If failed go back to step 4

### Important note:
1. Testing is no substitute for critical thinking ...
2. Passing your own tests doesn't ensure your function is correct! Your tests must cover a useful range of cases
3. **Rule of Thumb**:
    - Test 2+ use cases and 1+ edge cases
    - When a function has if-else statements, try to write a test that reaches each branch

### Reference:
1. [typing — Support for type hints](https://docs.python.org/3/library/typing.html)
2. [Python String join()](https://www.programiz.com/python-programming/methods/string/join)