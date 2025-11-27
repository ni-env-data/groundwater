import numpy as np
import matplotlib.pyplot as plt

def setup(width, height, mean, std):
    body = np.random.normal(mean, std, (height, width))
    body[body < 0] = 0
    return body

def visualize(concentration, min, max):
    plt.figure(1,(10,5))
    plt.imshow(concentration, origin='upper', cmap = 'plasma', vmin=min, vmax=max)
    plt.colorbar()
    plt.show()

def pollution(body, mean, std):
    body[0,:] = body[0,:] + np.random.normal(mean, std, body.shape[1])
    body[body < 0] = 0

def diffusion(body, dx, dy, dt, D):
    m, n = body.shape
    dif_body = (body[:m-2, 1:n-1] - 2 * body[1:m-1, 1:n-1] + body[2:m, 1:n-1])/(dy**2) + (body[1:m-1, 0:n-2] - 2 * body[1:m-1, 1:n-1] + body[1:m-1, 2:n])/(dx**2)
    body[1:m-1, 1:n-1] += D * dif_body * dt

def advection(body, dx, dy, dt, v):
    m, n = body.shape
    if v >= 0:
        advec_body = (body[1:m-1, 1:n-1] - body[1:m-1, 0:n-2])/dx
    else:
        advec_body = (body[1:m-1, 2:n] - body[1:m-1, 1:n-1])/dx
    body[1:m-1, 1:n-1] -= v * advec_body * dt

def decay(body, dt, k):
    m, n = body.shape
    body[1:m-1, 1:n-1] -= k * body[1:m-1, 1:n-1] * dt

def flow(body, dx, dy, dt, D, v, k, mean, std):
    m, n = body.shape
    
   # stability checks
    if D > 0:
        if dt > 1 / (2 * D * (1/dx**2 + 1/dy**2)):
            raise ValueError("Unstable dt for diffusion")
    elif D < 0:
        raise ValueError("D out of the range of values")
    # if v != 0:
       #  if dt > dx / abs(v):
            # raise ValueError("Unstable dt for advection")
   
    dif_body = (body[:-2, 1:-1] - 2 * body[1:-1, 1:-1] + body[2:m, 1:-1])/(dy**2) + (body[1:-1, 0:-2] - 2 * body[1:-1, 1:-1] + body[1:-1, 2:n])/(dx**2)
    if v >= 0:
        advec_body = (body[1:m-1, 1:n-1] - body[1:m-1, 0:n-2])/dx
    else:
        advec_body = (body[1:m-1, 2:n] - body[1:m-1, 1:n-1])/dx
    body[1:m-1, 1:n-1] = body[1:m-1, 1:n-1] + dt * (D * dif_body - v * advec_body - k * body[1:m-1, 1:n-1])
    body[body < 0] = 0

    # borders
    body[:, 0] = np.random.normal(mean, std, m)
    body[-1, :] = body[-2, :]
    body[:, -1] = body[:, -2]

def line_plot(x, y):
    plt.plot(x, y,)
    plt.show()
