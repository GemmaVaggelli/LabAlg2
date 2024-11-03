from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt
from  AlberoBinario import  ABR
from AlberoRossoNero import  ARN
import sys
import random

def create_random_list(l):
    a = []
    for j in range(0, l):
        a.append(random.randint(0, l))
    return a

################################################

def random_ABR(number_elements):
    a = create_random_list(number_elements)
    tree = ABR()
    for j in range(0, len(a)):
        tree.insert(a[j])
    return tree

def random_ARN(number_elements):
    a = create_random_list(number_elements)
    tree = ARN()
    for j in range(0, len(a)):
        tree.insert(a[j])
    return tree

################################################

def random_same_data(number_elements):
    a = create_random_list(number_elements)
    abr = ABR()
    arn = ARN()

    for j in range(0, number_elements):
        abr.insert(a[j])
        arn.insert(a[j])
    return [abr, arn]

def ascending_same_data(number_elements):
    abr = ABR()
    arn = ARN()

    for j in range(0, number_elements):
        abr.insert(j)
        arn.insert(j)
    return [abr, arn]

################################################

def test_time_construction_randomized_abr():
    dimension = 1
    stop = False
    while not stop:
        dimension *= 100
        start = timer()
        tree = random_ABR(dimension)
        end = timer()
        time = end - start

        print('Tempo speso per costruire un ABR randomizzato con dimensione {} è {} '.format(dimension, time))

        if time > 10:
           stop = True

def test_time_construction_randomized_arn():
    dimension = 1
    stop = False
    while not stop:
        dimension *= 100
        start = timer()
        tree = random_ARN(dimension)
        end = timer()
        time = end - start

        print('Tempo speso per costruire un ARN randomizzato con dimensione {} è {} '.format(dimension, time))

        if time > 10:
            stop = True

########################FIND_TESTS#####################################

def test_search_random(number_elements):
    y = [[], []]

    for j in range(1, number_elements + 1):
        [abr, arn] = random_same_data(j)
        #per cercare un elemento non presente nell'albero
        start = timer()
        abr.find(number_elements)
        end = timer()

        y[0].append(end - start)

        start = timer()
        arn.find(number_elements)
        end = timer()

        y[1].append(end - start)

    return y

#######################################################################

def test_search_ascending(number_elements):
    y = [[], []]

    for j in range(1, number_elements + 1):
        trees = ascending_same_data(j)

        start = timer()
        trees[0].find(number_elements)
        end = timer()

        y[0].append(end - start)

        start = timer()
        trees[1].find(number_elements)
        end = timer()

        y[1].append(end - start)

    return y

def abr_vs_arn(times, number_elements, type_of_input):
    y_avg = [[], []]
    y = []
    for i in range(times):
        # ritorna per ogni elemento i tempi di inserimento e i tempi di merge 
        if type_of_input == "RANDOMIZZATO":
            y.append(test_search_random(number_elements))
        if type_of_input == "CRESCENTE":
            y.append(test_search_ascending(number_elements))

    #si calcola la media per ogni dimensione
    for i in range(len(y[0][0])):
        avg_find_abr = 0
        avg_find_arn = 0
        for j in range(len(y)):
            avg_find_abr += y[j][0][i]
            avg_find_arn += y[j][1][i]
        avg_find_abr = avg_find_abr / len(y)
        avg_find_arn = avg_find_arn / len(y)
        y_avg[0].append(avg_find_abr)
        y_avg[1].append(avg_find_arn)

    for i in range(99, len(y_avg[0]), 100):
        print(i + 1, ' & ', '{:0.3e}'.format(y_avg[0][i]), ' & ', '{:0.3e}'.format(y_avg[1][i]))
    print("----------------------------------------------------")

    x = np.arange(1, number_elements + 1, 1)
    plt.title("ABR vs ARN {}".format(type_of_input))
    plt.grid()
    plt.xlabel("# di nodi ")
    plt.ylabel('tempo medio in secondi di {} compilazioni'.format(times))
    plt.plot(x, y_avg[0])
    plt.plot(x, y_avg[1])
    plt.legend(['ABR', 'ARN'])
    plt.savefig('ABR_vs_ARN_{}.png'.format(type_of_input), bbox_inches='tight')
    plt.clf()


#################running_script##################

elements = 500
number_of_experiments = 20
abr_vs_arn(number_of_experiments, elements, "RANDOMIZZATO")
abr_vs_arn(number_of_experiments, elements, "CRESCENTE")
