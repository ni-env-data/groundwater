import numpy as np
import matplotlib.pyplot as plt
from src.stability import advection_stability_check, diffusion_stability_check


def diffusion(body, dx, dy, dt, D):
    m, n = body.shape
    dif_body = (body[:m-2, 1:n-1] - 2 * body[1:m-1, 1:n-1] + body[2:m, 1:n-1])/(dy**2) + (body[1:m-1, 0:n-2] - 2 * body[1:m-1, 1:n-1] + body[1:m-1, 2:n])/(dx**2)
    body[1:m-1, 1:n-1] += D * dif_body * dt

def advection(body, dx, dy, dt, v):
    # upwind scheme 
    m, n = body.shape
    if v >= 0:
        advec_body = (body[1:m-1, 1:n-1] - body[1:m-1, 0:n-2])/dx
    else:
        advec_body = (body[1:m-1, 2:n] - body[1:m-1, 1:n-1])/dx
    body[1:m-1, 1:n-1] -= v * advec_body * dt

def decay(body, dt, k):
    m, n = body.shape
    body[1:m-1, 1:n-1] = np.exp(-k*dt) * body[1:m-1, 1:n-1]

def flow(body, dx, dy, dt, D, v, k, mean, std, pollution_stop=False):
    m, n = body.shape
    
    # stability checks
    diffusion_stability_check(dx, dy, dt, D)
    advection_stability_check(dx, dt, v)
   
    dif_body = (body[:-2, 1:-1] - 2 * body[1:-1, 1:-1] + body[2:m, 1:-1])/(dy**2) + (body[1:-1, 0:-2] - 2 * body[1:-1, 1:-1] + body[1:-1, 2:n])/(dx**2)
    if v >= 0:
        advec_body = (body[1:m-1, 1:n-1] - body[1:m-1, 0:n-2])/dx
    else:
        advec_body = (body[1:m-1, 2:n] - body[1:m-1, 1:n-1])/dx
    body[1:m-1, 1:n-1] = (body[1:m-1, 1:n-1] + dt * (D * dif_body - v * advec_body)) * np.exp(-k*dt)
    body[body < 0] = 0

    # borders
    if pollution_stop == True:
         body[0, :] = body[1, :]
    if v > 0:
        body[:, 0] = np.random.normal(mean, std, m)
        body[:, -1] = body[:, -2]
    else:
        body[:, 0] = body[:, 1]
        body[:, -1] = np.random.normal(mean, std, m)
    body[-1, :] = body[-2, :]
