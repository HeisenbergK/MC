import numpy as np


def montecarlo(probe, inputed, limit):
    results = []
    for i in range(1, (limit+1)):
        inputsrand = []
        for j in range(0, len(inputed)):
            locat = inputed[j][0]
            stdev = inputed[j][1]
            value = np.random.normal(loc=locat, scale=stdev)
            inputsrand.append(value)
        result = probe(inputsrand)
        results.append(result)
    return results


def montecarlolaplace(probe, inputed, limit):
    results = []
    for i in range(1, (limit+1)):
        inputsrand = []
        for j in range(0, len(inputed)):
            locat = inputed[j][0]
            stdev = inputed[j][1]
            value = np.random.laplace(loc=locat, scale=stdev)
            inputsrand.append(value)
        result = probe(inputsrand)
        results.append(result)
    return results


def montecarlopoisson(probe, inputed, limit):
    results = []
    for i in range(1, (limit+1)):
        inputsrand = []
        for j in range(0, len(inputed)):
            locat = inputed[j][0]
            value = np.random.poisson(lam=locat)
            inputsrand.append(value)
        result = probe(inputsrand)
        results.append(result)
    return results
