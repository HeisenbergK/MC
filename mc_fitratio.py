from mc_main import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# useful defs
def find_nearest(array, value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]


# define functions to probe through monte carlo
def ratfunc(inputed):
    result = np.sqrt(np.power(inputed[0], 2.0)+np.power(inputed[1], 2.0))
    return result


def thetafunc(inputed):
    result = (1.0/2.0)*np.arctan(inputed[0]/inputed[1])
    return result


# define functions for fitting
def gauss_function(x, a, x0, sigma):
    return a*(np.sqrt(1.0/(2.0*np.pi*np.power(sigma, 2.0))))*np.exp(-np.power((x-x0), 2.0)/(2.0*np.power(sigma, 2.0)))

# define the inputs of functions
inputs = [[0.1, 0.1], [0.95, 0.1]]
exc = [[], [0.0]]

# monte carlo test
results = montecarlo(thetafunc, inputs, 10000000, exc=exc, llimit=-np.inf, ulimit=np.inf)

# statistics on results
newmn = np.mean(results)
newst = np.std(results)
newle = float(len(results))
print('Monte Carlo Probes: %d' % int(newle))
print('Mean of results: %.5f' % newmn)
print('STD of results: %.5f' % newst)

# histogram
plt.clf()
plt.hist(results, bins=1000)
plt.show()

# calculate percentages between multiples of STD
initial1 = 0
for i in results:
    if (newmn-newst) <= i <= (newmn+newst):
        initial1 += 1
initial1 = float(initial1)
initial2 = 0
for i in results:
    if (newmn-(2.0*newst)) <= i <= (newmn+(2.0*newst)):
        initial2 += 1
initial2 = float(initial2)
initial3 = 0
for i in results:
    if (newmn-(3.0*newst)) <= i <= (newmn+(3.0*newst)):
        initial3 += 1
initial3 = float(initial3)
print('Percentage within 1 std: %.2f %%' % ((initial1/newle)*100.0))
print('Percentage within 2 std: %.2f %%' % ((initial2/newle)*100.0))
print('Percentage within 3 std: %.2f %%' % ((initial3/newle)*100.0))

# re-histogram in range kept results
hist, edges = np.histogram(results, bins=1000)
edges = np.subtract(edges, ((edges[2]-edges[1])/2.0))
edges = np.delete(edges, 0)
maxhis = max(hist)
maxloc = hist.tolist().index(maxhis)
newmd = edges[maxloc]
print('Mode of results: %.5f' % newmd)
# hist = np.divide(hist, newle)
mintofit = newmn-(4.0*newst)
maxtofit = newmn+(4.0*newst)
mintofit = find_nearest(edges, mintofit)
maxtofit = find_nearest(edges, maxtofit)
minindex = edges.tolist().index(mintofit)
maxindex = edges.tolist().index(maxtofit)
edges = edges[minindex:maxindex]
hist = hist[minindex:maxindex]
plt.clf()
plt.plot(edges, hist)
plt.show()


# fit a gauss and a laplace
gopt, gcov = curve_fit(gauss_function, edges, hist, p0=[max(results), newmn, newst])

plt.clf()
plt.plot(edges, hist)
plt.plot(edges, gauss_function(edges, *gopt))
plt.show()

print("Gaussian: Amplitude=%.5f, Mean=%.5f, Sigma=%.5f" % (gopt[0], gopt[1], np.abs(gopt[2])))
