import numpy as np
import matplotlib.pyplot as plt

def bateman_ratio(t, lambda_parent, lambda_child):
    return lambda_parent / (lambda_child - lambda_parent) \
        * (np.exp(-lambda_parent * t) - np.exp(-lambda_child * t))

t = np.linspace(0, 2, 1000)

ratio_case1 = bateman_ratio(t, 1, 2)
ratio_case2 = bateman_ratio(t, 1, 10)

plt.figure(figsize=(10, 6))
plt.plot(t, ratio_case1, label=r"$\lambda_p=1$, $\lambda_c=2$", linewidth=2)
plt.plot(t, ratio_case2, label=r"$\lambda_p=1$, $\lambda_c=10$", linewidth=2)
plt.xlabel("Time", fontsize=12)
plt.ylabel(r"$n_{\mathrm{child}}(t) / n_{\mathrm{parent}}(0)$", fontsize=12)
plt.title("Bateman Decay", fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.xlim(0, 2)
plt.ylim(0, None)
plt.tight_layout()
plt.savefig("bateman_decay.png", dpi=300, bbox_inches="tight")
plt.show()
