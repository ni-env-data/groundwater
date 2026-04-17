import numpy as np
import matplotlib.pyplot as plt
from src.flow import setup, pollution, flow
from src.visualise import visualise_concentration, plot_avg, plot_var
from src.analyse import average, variance

if __name__ == '__main__':
    body = setup(500, 100, 17.5, 2.5)
    body_2 = setup(500, 100, 17.5, 2.5)
    pollution(body, 200, 50)
    pollution(body_2, 400, 50)
    averages = []
    averages_2 = []
    variances = []
    variances_2 = []
    end_of_pollution = False
    duration = 3600*12*2
    time_span = range(duration)
    number_of_maps = 6
    for t in time_span:
        flow(body, 1, 1, 1, 0.05, 0.00014, 6e-9, 17.5, 2.5, end_of_pollution)
        flow(body_2, 1, 1, 1, 0.05, 0.00014, 6e-9, 17.5, 2.5, end_of_pollution)
        if t == duration//12:
           end_of_pollution = True
        if(t%(duration/number_of_maps) == 0):
            visualise_concentration(body, 0, 400)
            print(average(body))
            visualise_concentration(body_2, 0, 400)
            print(average(body_2))
        averages.append(average(body))
        variances.append(variance(body))
        averages_2.append(average(body_2))
        variances_2.append(variance(body_2))
    
    plot_avg(np.arange(len(averages)) / 3600, [averages, averages_2], ["200mg/L pollution", "400mg/L pollution"],
                  "Avarage concentration of nitrat after pollution", "h")
    plot_var(np.arange(len(variances)) / 3600, [variances, variances_2], ["200mg/L pollution", "400mg/L pollution"],
                  "Variance of nitrat concentration after pollution", "h")
