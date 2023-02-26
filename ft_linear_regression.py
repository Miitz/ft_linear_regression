import sys
import argparse
import matplotlib.pyplot as plt
import pandas as pd


def save_thetas(theta0, theta1):
    f = open("thetas.py", "w+")
    f.write("theta0 = " + str(theta0) + "\r\n" + "theta1 = " + str(theta1) + "\r\n")
    f.close()
    print("Thetas save complete! -> thetas.py")


class ft_linear_regression:
    def __init__(self):
        try:
            self.data = pd.read_csv('data.csv')
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)
        self.theta0 = 0.0
        self.theta1 = 0.0
        self.tmp_theta0 = 0.0
        self.tmp_theta1 = 0.0
        self.learning_rate = 0.1
        self.max_price = None
        self.min_price = None
        self.max_km = None
        self.min_km = None

    def plot_real_data(self):

        tmp_theta0 = self.tmp_theta0
        tmp_theta1 = self.tmp_theta1

        self.tmp_theta0 = self.theta0
        self.tmp_theta1 = self.theta1

        self.data['km'] = self.min_km + (self.max_km - self.min_km) * self.data['km']
        self.data['price'] = self.min_price + (self.max_price - self.min_price) * self.data['price']

        plt.title('Real values')
        plt.xlabel('Mileage')
        plt.ylabel('Price')
        plt.scatter(x=self.data['km'], y=self.data['price'], color="black")
        plt.plot([self.min_km, self.max_km], [((self.tmp_theta1 * self.min_km) +
                                               self.tmp_theta0), ((self.tmp_theta1 * self.max_km) + self.tmp_theta0)])

        plt.axis([self.min_km - abs(self.max_km * 0.1), self.max_km +
                  abs(self.max_km * 0.1), self.min_price - abs(self.max_price * 0.1),
                  self.max_price + abs(self.max_price * 0.1)])
        plt.show()
        self.tmp_theta0 = tmp_theta0
        self.tmp_theta1 = tmp_theta1

    def plot_normalized_data(self):
        plt.title('Standardized values')
        plt.xlabel('Mileage')
        plt.ylabel('Price')
        plt.scatter(x=self.data['km'], y=self.data['price'], color="black")
        plt.plot([0, 1], [((self.tmp_theta1 * 0.0) + self.tmp_theta0), ((self.tmp_theta1 * 1.0) + self.tmp_theta0)])
        plt.show()

    def normalize_data(self):
        self.min_km = self.data['km'].min()
        self.max_km = self.data['km'].max()
        self.min_price = self.data['price'].min()
        self.max_price = self.data['price'].max()

        self.data['km'] = (self.data['km'] - self.min_km) / (self.max_km - self.min_km)
        self.data['price'] = (self.data['price'] - self.min_price) / (self.max_price - self.min_price)

    def gradient_descent(self):
        n = self.data.shape[0]
        for i in range(n):
            x = self.data.iloc[i].km
            y = self.data.iloc[i].price
            tmp_theta1 = ((self.tmp_theta0 + self.tmp_theta1 * x) - y) * x
            tmp_theta0 = (self.tmp_theta0 + self.tmp_theta1 * x) - y
            self.tmp_theta1 -= self.learning_rate * (1 / n) * tmp_theta1
            self.tmp_theta0 -= self.learning_rate * (1 / n) * tmp_theta0
        return self.tmp_theta0, self.tmp_theta1

    def ft_training(self, ep):
        epochs = 10000

        self.normalize_data()
        for i in range(epochs):
            self.theta0, self.theta1 = self.gradient_descent()
            if (i % 1000) == 0 and ep:
                print(f"{i} / {epochs} -- theta1={self.theta1} theta0={self.theta0}")
            elif (i % 1000) == 0:
                print("Processing thetas...")

        self.theta1 = (self.max_price - self.min_price) * self.theta1 / (self.max_km - self.min_km)
        self.theta0 = self.min_price + ((self.max_price - self.min_price) * self.theta0) + self.theta1 * (
                1 - self.min_km)
        save_thetas(self.theta0, self.theta1)


parser = argparse.ArgumentParser()
# parser.add_argument('-lr', nargs='?', const=0.1, type=float, default=0.1)
parser.add_argument('-np', action='store_true', help="Plot normalized data on graph")
parser.add_argument('-rp', action='store_true', help="Plot real data on graph")
parser.add_argument('-ep', action='store_true', help="Print thetas after each epoch")
args = parser.parse_args()

data = ft_linear_regression()
data.ft_training(args.ep)

if args.np:
    data.plot_normalized_data()
if args.rp:
    data.plot_real_data()
