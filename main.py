import numpy as np
import matplotlib.pyplot as plt
from src import setup, visualize, pollution, diffusion, flow

if __name__ == '__main__':
    body = setup(500, 100, 17.5, 2.5)
    pollution(body, 200, 50)
    averages = []
    for t in range(3600*24*7*52):
        flow(body, 1, 1, 1, 0.05, 0.00014, 6e-9, 17.5, 2.5 )
        if t == 3600*2:
            body[0, :] = body[1, :]
        if(t%(3600*7*6*52) == 0):
            visualize(body, 0, 700)
            print(np.mean(body))
        averages.append(np.mean(body))
    plt.plot(range(3600*24*7*52), averages)
    plt.show()
