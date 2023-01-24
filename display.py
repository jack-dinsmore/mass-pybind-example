import numpy as np
import matplotlib.pyplot as plt

def display(tag):
    plt.rcParams["text.usetex"] = True
    plt.rcParams["font.family"] = "serif"
    flat_samples = np.load(f"mcmc-{tag}.npy")
    width = 1e-5

    low_half = flat_samples[flat_samples < 0.011]
    high_half = flat_samples[flat_samples > 0.011]

    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(7, 4), sharey=True)

    ax1.hist(flat_samples, bins=np.linspace(
        np.median(low_half) - width,
        np.median(low_half) + width, 40),
        histtype="step"
    )
    ax1.axvline(0.01, color='k')
    ax1.set_xlabel("k")
    ax1.set_ylabel("Posterior Probability")

    ax2.hist(flat_samples, bins=np.linspace(
        np.median(high_half) - width,
        np.median(high_half) + width, 40),
        histtype="step"
    )
    ax2.set_xlabel("k")

    fig.savefig(f"{tag}.png")

if __name__ == "__main__":
    display("fast")
    display("slow")
    display("rust")