import pickle
import sys

with open('routes.pkl', 'rb') as handle:
    routes = pickle.load(handle)



# Implement a markov process, we store the probability of going from A to B
# Where A and B are some distinct points
# For now store this as a dict of dicts, so that p(A,B) = probs[A][B]

probs = {}
probs["BEGIN"] = {}
probs["TERMINATE"] = {}

for k,v in routes.items():
    # Special case for starting point
    print(k, v)
    print(f"Line {k}")
    # Write the starting token
    if v[0] not in probs["BEGIN"]:
        probs["BEGIN"][v[0]] = 1
    else:
        probs["BEGIN"][v[0]] += 1
    last_stop = v[0]
    for stop in v[1:]:
        if last_stop not in probs:
            probs[last_stop] = {}
        if stop not in probs[last_stop]:
            probs[last_stop][stop] = 1
        else:
            probs[last_stop][stop] += 1
        last_stop = stop
    # Write the end token
    if last_stop not in probs:
        probs[last_stop] = {}
    if "TERMINATE" not in probs[last_stop]:
        probs[last_stop]["TERMINATE"] = 1
    else:
        probs[last_stop]["TERMINATE"] = 1  # We dont want to have so many possibilities to terminate the stop

with open('probabilities.pkl', 'wb') as handle:
    routes = pickle.dump(probs, handle)
