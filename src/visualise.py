import matplotlib.pyplot as plt


def visualise_concentration(concentration, min, max):
    plt.figure(figsize=(12, 4))
    plt.imshow(concentration, origin='upper', cmap = 'plasma', vmin=min, vmax=max)
    plt.colorbar()
    plt.show()


def plot_avg(time, averages, labels, title, time_unit):
    plt.figure(figsize=(12, 4))
    for avg, label in zip(averages, labels):
        plt.plot(time, avg, label=label)

    plt.xlabel(f"Time [{time_unit}]")
    plt.ylabel("Avarage concentration [mg/L]")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"output/{title}.png")
    plt.show()

def plot_var(time, variances, labels, title, time_unit):
    plt.figure(figsize=(12, 4))
    for var, label in zip(variances,labels):
        plt.plot(time, var, label=label)
    plt.xlabel(f"Time [{time_unit}]")
    plt.ylabel("Variance of the concentration[(mg/L)^2]")
    plt.title(title)

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"output/{title}.png")
    plt.show()