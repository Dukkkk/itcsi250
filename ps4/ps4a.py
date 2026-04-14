###########################
# 6.0002 Problem Set 1a: Space Cows
# Name:
# Collaborators:
# Time:

import time

from ps4_partition import get_partitions

# ================================
# Part A: Transporting Space Cows
# ================================


# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cows = {}
    with open(filename) as f:
        for line in f:
            name, weight = line.strip().split(",")
            cows[name] = int(weight)
    return cows


# Problem 2
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cows_copy = cows.copy()
    trips = []

    while cows_copy:
        trip = []
        total_weight = 0

        for cow in sorted(cows_copy, key=cows_copy.get, reverse=True):
            if total_weight + cows_copy[cow] <= limit:
                trip.append(cow)
                total_weight += cows_copy[cow]

        for cow in trip:
            del cows_copy[cow]

        trips.append(trip)

    return trips


# Problem 3
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cows_copy = cows.copy()
    best_partition = None

    for partition in get_partitions(list(cows_copy.keys())):
        valid_partition = True

        for trip in partition:
            total_weight = sum(cows_copy[cow] for cow in trip)
            if total_weight > limit:
                valid_partition = False
                break

        if valid_partition:
            if best_partition is None or len(partition) < len(best_partition):
                best_partition = partition

    return best_partition


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows("C:\\git\\itcsi250\\ps4\\ps4_cow_data.txt")

    start_time = time.time()
    greedy_trips = greedy_cow_transport(cows)
    greedy_time = time.time() - start_time

    start_time = time.time()
    brute_force_trips = brute_force_cow_transport(cows)
    brute_force_time = time.time() - start_time

    print("Greedy algorithm:")
    print("Number of trips:", len(greedy_trips))
    print("Time taken:", greedy_time, "seconds")

    print("\nBrute force algorithm:")
    print("Number of trips:", len(brute_force_trips))
    print("Time taken:", brute_force_time, "seconds")
compare_cow_transport_algorithms()
