from src.simulation import pipeline
import yaml


def load_config(path="config.yaml"):
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    return config

if __name__ == '__main__':
    config = load_config("config.yaml")

    pipeline(
        domain_width=config["domain"]["width"],
        domain_height=config["domain"]["height"],

        mean_noise=config["noise"]["mean"],
        std_noise=config["noise"]["std"],

        mean_pollution=config["pollution"]["mean"],
        std_pollution=config["pollution"]["std"],
        damped=config["pollution"]["damped"],

        number_of_charts=config["simulation"]["number_of_charts"],
        duration_sim=config["simulation"]["duration_sim"],
        duration_poll=config["pollution"]["duration_poll"],

        dx=config["grid"]["dx"],
        dy=config["grid"]["dy"],
        dt=config["grid"]["dt"],

        D=config["physical_parameters"]["D"],
        v=config["physical_parameters"]["v"],
        k=config["physical_parameters"]["k"],
    )