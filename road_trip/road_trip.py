"""
You don't want to run out of gas on your road trip.

You only have the names of cities and the distance from your starting point.

Your goal is to return the distance to the nearest city and the distances between the following cities

Input value:
Rbks, 5453; Bewfs, 1245; Wkjoj, 3890; Ysodf, 5589, Twoiu, 1303;
...
...

1245, 1303, 3890, 5453, 5589

Output value:
1245, 58, 2587, 1563, 136
...
...


1245, 58, 3832, 1621, 3968
"""

from sys import argv


def find_distances(trip_stops):
    stops_list = trip_stops.split(";")

    distances_list = []

    for stop in stops_list:
        city, distance = stop.split(',')
        distances_list.append(int(distance))

    sorted_distances = sorted(distances_list)

    differences = []

    for i in range(len(sorted_distances)):
        if len(differences) < 1:
            differences.append(sorted_distances[i])
        else:
            differences.append(sorted_distances[i] - sorted_distances[i - 1])

    print ','.join(map(lambda x: str(x), differences))

with open(argv[1]) as input_file:

    for line in input_file:
        find_distances(line.strip().rstrip(";"))
