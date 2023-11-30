import matplotlib.pyplot as plt
from matplotlib import animation


def animate(simulation, x):
    fig, ax = plt.subplots()
    scat1 = ax.scatter(simulation.get_sheep_x(), simulation.get_sheep_y(), color='b')
    scat2 = ax.scatter(simulation.wolf.position[0], simulation.wolf.position[1], color='r')

    def update(frame):
        simulation.simulate_round()
        ax.axis([min(simulation.get_sheep_x() + [simulation.wolf.position[0]]) - 2,
                 max(simulation.get_sheep_x() + [simulation.wolf.position[0]]) + 2,
                 min(simulation.get_sheep_y() + [simulation.wolf.position[1]]) - 2,
                 max(simulation.get_sheep_y() + [simulation.wolf.position[1]]) + 2])
        scat1.set_offsets(simulation.get_sheep_coords())
        scat2.set_offsets([simulation.wolf.position[0], simulation.wolf.position[1]])
        if simulation.noRound == x:
            exit(str(x) + " rounds passed")

        return scat1, scat2

    ani = animation.FuncAnimation(fig, update, frames=30, interval=100)

    plt.show()
