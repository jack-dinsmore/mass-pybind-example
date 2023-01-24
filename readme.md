# PyBind11 Example Code

By Jack Dinsmore, Jan 24, 2023

PyBind11 allows you to run compiled C++ code in a Python script. Combining the speed of C++ with Python's ease of development, you can vastly improve the speed of your calculations such as fits with little effort. We'll look at a simple example of doing an MCMC fit with PyBind11 and compare the speed of the result to pure Python code (which is about 33x slower) and pure Rust code (which is about 11x faster).

## Files

Look at the presentation `pybind.key` for a description of the project.

* All-python code:
    - PythonL `slow.py`.
    - Results: `slow.png`
    - The results don't give the correct value of `k`, but I haven't bothered to fix this yet.

* Pybind code:
    - Python: `fast.py`
    - C++: `cpp-half.cpp`
    - Build script: `build.sh`
    - Results: `fast.png`

* Rust code:
    - All Rust files: `fast/`
    - Results: `rust.png`

* Display and data generation code: 
    - Fit result display: `display.py`
    - Data generation: `make_data.py`
