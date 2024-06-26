import time

import marktwaage
from Weights import Weights


def fill_variables(name):
    n = None
    w = []
    a = []
    try:
        with open(name, "r") as file:
            lines = file.read().splitlines()
            for i, element in enumerate(lines):
                if i == 0:
                    n = element
                else:
                    v = list(map(int, element.split()))
                    w.append(v[0])
                    a.append(v[1])
        return n, w, a
    except FileNotFoundError:
        print("Could not find File.")


def start(filename):
    start_time = time.time()
    print("File: ", filename)
    filename = "gewichte/"+str(filename)
    distinct_weights, weights, amount = fill_variables(filename)
    w = Weights(distinct_weights, weights, amount)
    w.create_weight_array()

    print("Unique weights: {}\n"
          "Distinct weights: {}\n"
          "Amount: {}\n"
          "All weights: {}\n"
          .format(w.unique_weights, w.weights, w.amount, w.all_weights))

    marktwaage.calculate(w)

    print("Program took ", time.time() - start_time, " to run.")


if __name__ == '__main__':
    start("gewichtsstuecke0.txt")
