import numpy as np
import progressbar


def montecarlo(probe, inputed, limit, exc, llimit=(-np.inf), ulimit=np.inf):
    results = []
    if not exc:
        exc = []
        for i in range(0, len(inputed)):
            exc.append([])
    with progressbar.ProgressBar(widgets=[progressbar.Bar(), ' ', progressbar.RotatingMarker(), ' ',
                                          progressbar.Percentage(), ' ', progressbar.SimpleProgress(), ' ',
                                          progressbar.Timer(), ' ', progressbar.ETA()], max_value=limit) as bar:
        for i in range(0, limit):
            inputsrand = []
            for j in range(0, len(inputed)):
                locat = inputed[j][0]
                stdev = inputed[j][1]
                while True:
                    value = np.random.normal(loc=locat, scale=stdev)
                    if (llimit < value < ulimit) and (value not in exc[j]):
                        inputsrand.append(value)
                        break
            result = probe(inputsrand)
            results.append(result)
            bar.update(i)
    return results


def montecarlolaplace(probe, inputed, limit, llimit, ulimit):
    results = []
    with progressbar.ProgressBar(widgets=[progressbar.Bar(), ' ', progressbar.RotatingMarker(), ' ',
                                          progressbar.Percentage(), ' ', progressbar.SimpleProgress(), ' ',
                                          progressbar.Timer(), ' ', progressbar.ETA()], max_value=limit) as bar:
        for i in range(0, limit):
            inputsrand = []
            for j in range(0, len(inputed)):
                locat = inputed[j][0]
                stdev = inputed[j][1]
                while True:
                    value = np.random.laplace(loc=locat, scale=stdev)
                    if llimit < value < ulimit:
                        inputsrand.append(value)
                        break
            result = probe(inputsrand)
            results.append(result)
            bar.update(i)
    return results


def montecarlopoisson(probe, inputed, limit, llimit, ulimit):
    results = []
    with progressbar.ProgressBar(widgets=[progressbar.Bar(), ' ', progressbar.RotatingMarker(), ' ',
                                          progressbar.Percentage(), ' ', progressbar.SimpleProgress(), ' ',
                                          progressbar.Timer(), ' ', progressbar.ETA()], max_value=limit) as bar:
        for i in range(0, limit):
            inputsrand = []
            for j in range(0, len(inputed)):
                locat = inputed[j][0]
                while True:
                    value = np.random.poisson(lam=locat)
                    if llimit < value < ulimit:
                        inputsrand.append(value)
                        break
            result = probe(inputsrand)
            results.append(result)
            bar.update(i)
    return results
