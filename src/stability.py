import numpy as np

def diffusion_stability_check(dx, dy, dt, D)-> bool:
    stable = False
    if D > 0:
        if dt > 1 / (2 * D * (1/dx**2 + 1/dy**2)):
            raise ValueError("Unstable dt for diffusion")
    elif D < 0:
        raise ValueError("D out of the range of values")
    else:
        stable = True
    return stable
        

def advection_stability_check(dx, dy, dt, v)-> bool:
    stable = False
    if v != 0:
        if np.abs(v)*dt/dx >1:
            raise ValueError("Unstable dt for advection")
    else:
        stable = True
    return stable
