from matplotlib import pyplot as plt
import time


class Plot:
    def __init__(self, x, y):
        plt.plot(x, y)
        plt.title('Time to crack/password length correlation')
        plt.xlabel('Password length')
        plt.ylabel('Time to crack')
        ask = input("Save plot? [y/n] ")
        if ask == 'y':
            figure1 = plt.gcf()
            figure1.savefig(f'figures/plot{time.time()}.png', bbox_inches='tight')
        plt.show()
