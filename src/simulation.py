import numpy as np
from src.flow import flow
from src.visualise import visualise_concentration, plot_avg, plot_var
from src.analyse import average, variance

def setup(width, height, mean, std):
    body = np.random.normal(mean, std, (height, width))
    body[body < 0] = 0
    return body


def pollution_std_line(body, mean, std):
    body[0,:] = body[0,:] + np.random.normal(mean, std, body.shape[1])
    body[body < 0] = 0


def pipeline(domain_width: int,
             domain_height: int,
             mean_noise: float,
             std_noise: float,
             mean_pollution: list[float],
             std_pollution: list[float],
             damped: list[float],
             number_of_charts: int,
             duration_sim: int,
             duration_poll: int,
             dx: int,
             dy: int,
             dt: int,
             D: list[float],
             v: list[float],
             k: list[float]):
    
    if len(mean_pollution) != len(std_pollution):
        raise ValueError("mean_pollution and std_pollution must have the same length")
    
    bodies = []
    averages = [[] for _ in range(len(mean_pollution))]
    variances = [[] for _ in range(len(mean_pollution))]
    labels = [f"{mean_pollution[i]} mg/L pollution" for i in range(len(mean_pollution))]
    end_of_pollution = False


    for i in range(len(mean_pollution)):
        body = setup(domain_width, domain_height, mean_noise, std_noise)
        pollution_std_line(body, mean_pollution[i], std_pollution[i])
        bodies.append(body)

    for t in range(duration_sim):
        for  i in range(len(mean_pollution)):
            flow(bodies[i], dx, dy, dt, float(D[i]), float(v[i]), float(k[i]), mean_noise, std_noise, end_of_pollution, damped[i])
            averages[i].append(average(bodies[i]))
            variances[i].append(variance(bodies[i]))


            if(t%(duration_sim/number_of_charts) == 0):
                visualise_concentration(bodies[i], 0, np.max(mean_pollution))

        if t == duration_poll:
           end_of_pollution = True
    
    plot_avg(np.arange(len(averages[0])) / 3600, averages, labels, "Average concentration of nitrate after pollution", "h")
    plot_var(np.arange(len(variances[0])) / 3600, variances, labels, "Variance of nitrate concentration after pollution", "h")
