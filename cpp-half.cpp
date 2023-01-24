#include<vector>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h> // For returning vectors

std::vector<double> model_fn(double param) {
    // Do something complicated
    std::vector<double> simulated_data;
    simulated_data.reserve(1000);
    double x = 1.0;
    double v = 0.0;
    for (int i = 0; i < 1000; i++) {
        v += -param * x;
        x += v;
        simulated_data.push_back(x);
    }
    return simulated_data;
}

PYBIND11_MODULE(model, m) {
    m.def("model", &model_fn, "The forward model");
}

