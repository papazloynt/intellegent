import matplotlib.pyplot as plt


def show_graph(y_axis_list):
    fig, ax = plt.subplots()
    plt.plot(y_axis_list)
    ax.set_ylabel('Total Errors')
    ax.set_xlabel('Era')
    plt.show()
