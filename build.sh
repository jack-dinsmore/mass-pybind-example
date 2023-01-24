c++ -O3 -Wall -shared -std=c++11 -undefined dynamic_lookup $(python3 -m pybind11 --includes) cpp-half.cpp -o model$(python3-config --extension-suffix)


