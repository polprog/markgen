"""
             D - E
            /
   a - b - c - d - e - f
          /           /
    A - B - 1 - 2 - 3
"""
import pickle
ll = [
    ['a', 'b', 'c', 'd', 'e', 'f'],
    ['a', 'b', 'c', 'D', 'E'],
    ['A', 'B', '1', '2', '3', 'f'],
    ['A', 'B', 'c', 'd', 'e', 'f']]

for i in range(len(ll)):
    ll.append(ll[i][::-1])

routedict = {}
for i in range(len(ll)):
    ll[i] = ["BEGIN"] + ll[i] + ["TERMINATE"]
    routedict[str(i)] = ll[i]
    
with open("routes_small.pkl", "wb") as routes_dat:
    pickle.dump(routedict, routes_dat)

    
