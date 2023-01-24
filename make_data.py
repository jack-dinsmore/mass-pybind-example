import numpy as np
import matplotlib.pyplot as plt
import slow

TRUE_PARAM = 0.01
ERROR = 0.1

plt.rcParams["text.usetex"] = True
plt.rcParams["font.family"] = "serif"

data = np.array(slow.model(TRUE_PARAM))
xs = np.arange(len(data))

data += np.random.normal(size=(len(data))) * ERROR

plt.scatter(xs, data, marker='.')
plt.xlabel("Time (arbitrary units)")
plt.ylabel("$x$ (arbitrary units)")
plt.savefig("data.png")

np.save("data.npy", [data, [ERROR] * 1000])
