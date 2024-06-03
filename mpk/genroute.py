import pickle
import sys
import random
import time

# BUG: There are some cases which a stop A is pointing to a next stop B
# but there is no probability map for B, ex
# >>> probs["Graniczna (Strachowicka)"]
# {'Rdestowa': 1}
# >>> probs["Rdestowa"]
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# KeyError: 'Rdestowa'
# This could be due to a fact not all routes were analyzed
# if Rdestowa was a last stop it would point to the TERMINATE token
# For now just terminate the process prematurely if we pick a stop like this

def next_stop(stop, probs):
    N = 0
    for k,v in probs[stop].items():
        N += v
    while True:
        R = random.randint(0, N)
        for k,v in probs[stop].items():
            R -= v
            if R <= 0:
                if k in probs.keys():  # Avoid returning a stop we cannot move from
                    return k
                else:
                    return "TERMINATE" #


if len(sys.argv) < 2:
    print("Usage: ", sys.argv[0], "<probabilities> [first stop]")
    sys.exit(1)
first_stop = "BEGIN"
if len(sys.argv) > 2:
    first_stop = sys.argv[2]
                
handle = open('probabilities.pkl', 'rb')
probs = pickle.load(handle)

last_stop = first_stop
route = [last_stop]
print(0, "\t", last_stop)

for i in range(300):
    # There are some missing keys in the markov chain - likely due to the fact not all routes were taken into account.
    stop = next_stop(last_stop, probs)
    while stop in route[-3:]:  # prevent loops - for some routes, this freezes the program
        stop = next_stop(last_stop, probs)
    print(i+1, "\t", stop)
    route.append(stop)
    last_stop = stop
    if stop == "TERMINATE":
        break
print(route)
