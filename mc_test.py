from mc_main import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# define functions to probe through monte carlo
def tandeg(inputed):
    result = np.tan(inputed[0]*(np.pi/180.0))
    return result


def logfunc(inputed):
    result = np.log10(inputed[0])
    return result


# define functions for fitting
def gauss_function(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

# define the inputs of functions
inputs = [[147.0, 20.0]]

# monte carlo test
results = montecarlo(logfunc, inputs, 1000000)

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

# re-histogram with kept results
hist, edges = np.histogram(results, bins=1000)
edges = np.subtract(edges, ((edges[2]-edges[1])/2.0))
edges = np.delete(edges, 0)
# hist = np.divide(hist, newle)
plt.clf()
plt.plot(edges, hist)
plt.show()


# fit a gauss and a laplace
gopt, gcov = curve_fit(gauss_function, edges, hist)

plt.clf()
plt.plot(edges, hist)
plt.plot(edges, gauss_function(edges, *gopt))
plt.show()

print("Gaussian: Amplitude=%.5f, Mean=%.5f, Sigma=%.5f" % (gopt[0], gopt[1], gopt[2]))
