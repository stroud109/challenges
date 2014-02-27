import math
import sys

RADIANS = 180 / 3.14169


def kilometers_between(lat1, lng1, lat2, lng2):

    a1 = lat1 / RADIANS
    a2 = lng1 / RADIANS
    b1 = lat2 / RADIANS
    b2 = lng2 / RADIANS

    t1 = math.cos(a1) * math.cos(a2) * math.cos(b1) * math.cos(b2)
    t2 = math.cos(a1) * math.sin(a2) * math.cos(b1) * math.sin(b2)
    t3 = math.sin(a1) * math.sin(b1)

    return 6366 * math.acos(t1 + t2 + t3)


class City(object):
    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng

    def kilometers_to(self, other):
        return kilometers_between(self.lat, self.lng, other.lat, other.lng)

    def roads(self):
        return filter(lambda road: road.a is self or road.b is self, ROADS)

    def adjacent_cities(self):
        return [road.the_city_opposite(self) for road in self.roads()]

    def __repr__(self):
        return self.name


class Road(object):
    def __init__(self, a, b):
        if a is b:
            raise Exception('Road must have two distinct cities')
        self.a = a
        self.b = b
        self.distance = a.kilometers_to(b)

    def the_city_opposite(self, city):
        if city is self.a:
            return self.b
        elif city is self.b:
            return self.a
        else:
            raise Exception(
                'You tried going from %s to %s but there\'s no road!'
                % (self, city)
            )

    def __repr__(self):
        return '%s - %s (%.0f) km' % (self.a, self.b, self.distance)

    @staticmethod
    def between(a, b):
        for road in ROADS:
            if (road.a is a and road.b is b) or (road.a is b and road.b is a):
                return road
        raise Exception('There is no road between %s and %s' % (a, b))


Berlin = City('Berlin', 52.482668, 13.359275)
Paris = City('Paris', 48.980405, 2.2851849)
Milan = City('Milan', 45.520543, 9.1419459)
Frankfurt = City('Frankfurt', 50.078848, 8.6349115)
Munich = City('Munich', 48.166229, 11.558089)
Zurich = City('Zurich', 47.383444, 8.5254142)
Tours = City('Tours', 47.413572, 0.6810506)
Lyon = City('Lyon', 45.767122, 4.8339568)
Vienna = City('Vienna', 48.224431, 16.389240)
Prague = City('Prague', 50.092396, 14.436144)
Krakow = City('Krakow', 50.050363, 19.928578)
Warsaw = City('Warsaw', 52.254756, 21.005968)
Hamburg = City('Hamburg', 53.539699, 9.9977143)
Antwerp = City('Antwerp', 51.220613, 4.3954882)
Torino = City('Torino', 45.105321, 7.6451957)
Rome = City('Rome', 42.032845, 12.390408)


ROADS = set()
ROADS.add(Road(Hamburg, Berlin))
ROADS.add(Road(Hamburg, Antwerp))
ROADS.add(Road(Hamburg, Frankfurt))
ROADS.add(Road(Berlin, Warsaw))
ROADS.add(Road(Berlin, Prague))
ROADS.add(Road(Antwerp, Paris))
ROADS.add(Road(Paris, Tours))
ROADS.add(Road(Paris, Lyon))
ROADS.add(Road(Paris, Zurich))
ROADS.add(Road(Paris, Frankfurt))
ROADS.add(Road(Frankfurt, Prague))
ROADS.add(Road(Krakow, Warsaw))
ROADS.add(Road(Krakow, Prague))
ROADS.add(Road(Krakow, Vienna))
ROADS.add(Road(Vienna, Munich))
ROADS.add(Road(Vienna, Prague))
ROADS.add(Road(Zurich, Milan))
ROADS.add(Road(Lyon, Torino))
ROADS.add(Road(Torino, Milan))
ROADS.add(Road(Torino, Rome))
ROADS.add(Road(Milan, Rome))

#
# Write your code here
#
# make a list of cities from Rome to Berlin


def get_paths(start_city, end_city, path=[]):
    '''
    For this bit, I referred to this: http://www.python.org/doc/essays/graphs/
    '''
    path = path + [start_city]

    if start_city == end_city:
        return [path]

    paths = []

    for adjacent_city in start_city.adjacent_cities():
        if adjacent_city not in path:
            newpaths = get_paths(adjacent_city, end_city, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths


def get_shortest_route(start_city, end_city):

    paths = get_paths(start_city, end_city)

    shortest_path = paths[0]
    shortest_distance = 1000000000

    for path in paths:
        total_distance = 0
        for position, city in enumerate(path):
            if position + 1 < len(path):
                total_distance += city.kilometers_to(path[position + 1])
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_path = path
    return shortest_path

itinerary = get_shortest_route(Rome, Berlin)
#
# Let's see how you did
#

if __name__ == '__main__':

    total_distance = 0

    if len(itinerary) == 0:
        print 'Not done yet!'
        print 'You need the "itinerary" variable to be a list of cities'
        sys.exit(1)

    if itinerary[0] is not Rome or itinerary[-1] is not Berlin:
        print 'Not done yet!'
        print 'You need the "itinerary" variable to start with Rome and end with Berlin'
        sys.exit(1)

    for idx, city in enumerate(itinerary):
        if idx < len(itinerary) - 1:
            next_city = itinerary[idx + 1]
            distance = Road.between(city, next_city).distance
            total_distance += distance
            print '%s - %s (%.0f) km' % (city, next_city, distance)

    print 'arrived in %d steps (%.0f km)' % (len(itinerary), total_distance)
    print ''
    print ''
