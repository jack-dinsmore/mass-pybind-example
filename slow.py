import numpy as np
import emcee

def model(k):
    simulated_data = np.zeros(1000)
    x = 1
    v = 0
    for i in range(1000):
        v += -k * x
        x += v
        simulated_data[i] = x
    return simulated_data

def likelihood(k, data, error):
    if not 0 < k < 0.02: return -np.inf
    simulated_data = model(k)
    return -0.5 * np.sum(((data - simulated_data) / error)**2)

def main():
    start_ks = np.random.uniform(0, 0.02, size=(32, 1))
    data, error = np.load("data.npy")
    sampler = emcee.EnsembleSampler(len(start_ks), 1,
        likelihood, args=[data, error])
    sampler.run_mcmc(start_ks, 10_000, progress=False)
    flat_samples = sampler.get_chain(discard=0, thin=1, flat=True)
    np.save("mcmc-slow.npy", flat_samples)

if __name__ == "__main__":
    import timeit
    starttime = timeit.default_timer()
    main()
    print("The slow version took:", timeit.default_timer() - starttime)

