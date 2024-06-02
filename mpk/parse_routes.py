import pandas as pd
import pickle

pathprefix = 'OtwartyWroclaw_rozklad_jazdy_GTFS/'

print("stop_times...", end="", flush=True)
stop_times = pd.read_csv(pathprefix + "stop_times.txt");
print("stops...", end="", flush=True)
stops = pd.read_csv(pathprefix + "stops.txt");
print("trips...", end="", flush=True)
trips = pd.read_csv(pathprefix + "trips.txt");
print("OK", flush=True)

# stop_times with stop names
trips_names = stop_times[["trip_id", "stop_id", "stop_sequence"]].join(stops[["stop_id", "stop_name"]].set_index("stop_id"), on="stop_id")

# above with line names (route_id)
trips_names = trips_names.join(trips[["route_id", "trip_id"]].set_index("trip_id"), on="trip_id")

def stops_trip_id(trip_id):
    return trips_names[trips_names["trip_id"] == trip_id]


# Get an example route for each line
# Yes, some lines have more than 1 route but we dont really care,
# so let's take just the first route

routes_dict = {}
for line in trips_names["route_id"].unique():
#for line in ["A", "B", "D", "7", "8", "10"]:
    trip_id = trips_names[trips_names["route_id"] == line]["trip_id"].iloc[0]
    stops = stops_trip_id(trip_id)["stop_name"]
    routes_dict[line] = list(stops)
    print(line, "done")
    

with open("routes.pkl", "wb") as routes_dat:
    pickle.dump(routes_dict, routes_dat)
