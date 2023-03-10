# -*- coding: utf-8 -*-
import argparse


parser = argparse.ArgumentParser(
    description="This file is the main configuration of the file"
)
arg_lists = []


# helper function to manipulate string data
def add_argument_group(name):
    arg = parser.add_argument_group(name)
    arg_lists.append(arg)
    return arg


def str2bool(v):
    return v.lower() in ("true", "1")


def str2list(v):
    v = v.split(",")
    return v


def str2float(v):
    v = v.split(",")
    v = list(map(float, v))
    return v


# Environment
env_arg = add_argument_group("Environment")
env_arg.add_argument(
    "--version", type=str, default="Version 1.12.1", help="Program version"
)
env_arg.add_argument(
    "--mode", type=str, default="k_n", help="modes: k_n, n, k"
)  # this is applied to network

env_arg.add_argument(
    "--train_mode",
    type=str2bool,
    default=False,
    help="switch between training and testing",
)
env_arg.add_argument(
    "--save_model", type=str2bool, default=False, help="whether or not model is loaded"
)
env_arg.add_argument(
    "--load_model",
    type=str2bool,
    default=False,
    help="whether or not model is retrieved",
)

# Network
net_arg = add_argument_group("Network")
net_arg.add_argument(
    "--extraElements",
    type=str,
    default="elementsInBatch",
    help="elementsInBatch (if batch norm), afterDecoder (after decoding face)",
)
net_arg.add_argument(
    "--hidden_dim", type=int, default=128, help="agent LSTM num_neurons"
)  # memoria interna de las neuronas
net_arg.add_argument(
    "--num_stacks", type=int, default=3, help="agent LSTM num_stacks"
)  # cantidad de redes de mneuronas de LSTM
net_arg.add_argument("--C", type=float, default=10, help="clipping values")

# Data
data_arg = add_argument_group("Data")
data_arg.add_argument("--batch_size", type=int, default=2, help="batch size")
data_arg.add_argument(
    "--input_dim", type=int, default=1, help="Dimencion of data (Cloud properties)"
)
data_arg.add_argument(
    "--input_embed",
    type=int,
    default=64,
    help="embedding dimention of the convulution layer",
)
data_arg.add_argument(
    "--max_length",
    type=int,
    default=4,
    help="maximum quantity of CSP in a batch element",
)  # estaba en 10
data_arg.add_argument(
    "--parameters",
    type=int,
    default=1,
    help="paramters quantity (pr_error, vel_d, vel_up), max = 3",
)
data_arg.add_argument(
    "--normal", type=bool, default=True, help="batch normaliztion, type: bool"
)

# Training / test parameters
train_arg = add_argument_group("Training")
train_arg.add_argument(
    "--whatToGraph",
    type=str2list,
    default="prError,redundancy",
    help="What plots are displayed and saved when is used the evalutiond",
)
train_arg.add_argument("--num_epoch", type=int, default=10, help="number of epochs in the training phase")
train_arg.add_argument(
    "--learning_rate", type=float, default=0.001, help="learning rate to use during the training phase"
)
train_arg.add_argument(
    "--beta", type=float, default=10, help="Penalization for constraints"
)
train_arg.add_argument("--weight_decay", type=float, default=0, help="Weight decay")
train_arg.add_argument(
    "--objective_to_optimize",
    type=str,
    default="ponderate",
    help="These are the option to use in as objectives in the training phase:\
                        'prError' : Error probability,\
                        'normError' : normalized probability error, \
                        'redundancy' : redundancy reward, \
                        'normRed' : normalized redundancy,\
                        'ponderate' : For multiobjetive configuration"
)
train_arg.add_argument(
    "--selection",
    type=str,
    default="categorical",
    help="this control the way how it select elements\n\
                                                                            argmax:  is agressive\n\
                                                                            categorical is for explorations propuses",
)
train_arg.add_argument(
    "--log",
    type=str2bool,
    default=False,
    help="To apply natural log to pr_error because has exponential growing",
)
train_arg.add_argument(
    "--monoObjetive",
    type=str,
    default=None,
    help="key to print in comparation graph the objetive selected and ignore wo\
                            (prError or redundancy), default values is None and uses wo value",
)
# train_arg.add_argument('--lr_decay_step', type=int, default=5000, help='lr decay step')
# train_arg.add_argument('--lr_decay_rate', type=float, default=0.96, help='lr decay rate')

train_arg.add_argument(
    "--temperature",
    type=float,
    default=1,
    help="temperature for confidence in the network for take actions",
)
train_arg.add_argument(
    "--graphicComparation",
    type=bool,
    default=True,
    help="evaluation graphic option to compare values",
)
train_arg.add_argument(
    "--item_in_memory",
    type=str2bool,
    default=False,
    help="Use an element saved in memory to make system evaluations",
)
train_arg.add_argument(
    "--shape_at_disk",
    type=str,
    default="singleelement",
    help="Two values, the first with one value (singleelement) the other with 20 values(batchelements)",
)
train_arg.add_argument(
    "--replace_element_in_memory",
    type=str2bool,
    default=False,
    help="[optional] parameter default False, to create a new element for evaluation",
)
train_arg.add_argument(
    "--wo",
    type=str2float,
    default=[0.5, 0.5],
    help="array for multiobjective ponderation",
)
train_arg.add_argument(
    "--load_optim", type=str2bool, default=False, help="Load optimizer paramters"
)
train_arg.add_argument(
    "--variable_length",
    type=str2bool,
    default=False,
    help="Batch with padding elements (0)",
)


# Performance
perf_arg = add_argument_group("Training")
# perf_arg.add_argument('--enable_performance', type=str2bool, default=False, help='compare performance agains Gecode solver')

# Misc
misc_arg = add_argument_group("User options")
misc_arg.add_argument(
    "--save_to",
    type=str,
    default="./save/ponderateNormalOne.ph",
    help="saver sub directory",
)
misc_arg.add_argument(
    "--load_from",
    type=str,
    default="./save/ponderateNormalOne.ph",
    help="loader sub directory",
)
misc_arg.add_argument(
    "--graphPath",
    type=str,
    default="./graphPyplot/",
    help="path to save the graph for evaluation",
)
misc_arg.add_argument(
    "--log_dir", type=str, default="./log.txt", help="summary writer log directory"
)
misc_arg.add_argument(
    "--debugcomments",
    type=str2bool,
    default=False,
    help="Display comments in evaluatio mode",
)
misc_arg.add_argument(
    "--statistic", type=str2bool, default=False, help="statistic for a batch of values"
)
misc_arg.add_argument(
    "--plot", type=str2bool, default=True, help="bool to display and save plots"
)


def get_config():
    """
    This object contain all the configurations. The configuration
    can be passed thorugh the terminal as any program to overwrite
    the original configuration this is very useful to make scripts
    to make different confurations.All for replication propouses.
    """
    config, unparsed = parser.parse_known_args()
    return config, unparsed


def print_config():
    config, _ = get_config()

    print("[INFO] Datos de configuracion")
    for arg in vars(config):
        blank_space = 30 - len(arg)
        print("      ", arg + ("-" * blank_space), getattr(config, arg))


if __name__ == "__main__":
    print_config()
