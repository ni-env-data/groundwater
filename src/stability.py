import numpy as np

def diffusion_stability_check(dx, dy, dt, D)-> None:
    if D > 0:
        if dt > 1 / (2 * D * (1/dx**2 + 1/dy**2)):
            raise ValueError("Unstable dt for diffusion")
    elif D < 0:
        raise ValueError("D out of the range of values")

        

def advection_stability_check(dx, dt, v)-> None:
    if v != 0:
        if np.abs(v)*dt/dx >1:
            raise ValueError("Unstable dt for advection")
