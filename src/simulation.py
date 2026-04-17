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
             mean_pollution: list,
             std_pollution: list,
             number_of_cases: int,
             number_of_charts: int,
             duration_sim: int,
             duration_poll: int,
             dx: int,
             dy: int,
             dt: int,
             D: float,
             v: float,
             k:float):
    
    bodies = []
    averages = []
    variances = []
    end_of_pollution = False


    for i in range(number_of_cases):
        body = setup(domain_width, domain_height, mean_noise, std_noise)
        bodies.append(body)
        pollution_std_line(body, mean_pollution[i], std_pollution[i])
        bodies.append(body)

    for t in range(duration_sim):
        for  i in range(number_of_cases):
            flow(bodies[i], dx, dy, dt, D, v, k, mean_noise, std_noise, end_of_pollution)
            averages[i].append(average(bodies[i]))
            variances[i].append(variance(bodies[i]))


            if(t%(duration_sim/number_of_charts) == 0):
                visualise_concentration(bodies[i], 0, mean_pollution)

        if t == duration_poll:
           end_of_pollution = True
    
    plot_avg(np.arange(len(averages[0])) / 3600, averages, ["200mg/L pollution", "400mg/L pollution"],
                  "Avarage concentration of nitrat after pollution", "h")
    plot_var(np.arange(len(variances[0])) / 3600, variances, ["200mg/L pollution", "400mg/L pollution"],
                  "Variance of nitrat concentration after pollution", "h")
