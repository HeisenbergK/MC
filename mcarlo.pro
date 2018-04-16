function mcarlo, probe, inputed, probes, exc, llimit, ulimit

results=RANDOMN(seed, probes)

results=(results*inputed[1])+inputed[0]
results=probe(results)



end