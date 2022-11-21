from utils.cities import Cities
from utils.state import UcsState
from uniform_cost_search import UniformCostSearch
import sys, getopt

if (__name__ == "__main__"):
    searchMethod = 'UniformCostSearch'
    try:
        opts, args = getopt.getopt(sys.argv[1:],"s:",["search="])
    except getopt.GetoptError:
        print("route_finder.py -s <searchmethod>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-s':
            if arg == 'ucs':
                searchMethod = 'UniformCostSearch'

    search = globals()[searchMethod]()
    cities = Cities().getCities()
    keys = list(cities.keys())
    startState = UcsState([keys[0]], [city for city in cities.keys()\
         if city != keys[0]])
    _, stats = search.findPath(startState)
    print("Time taken: " + str(stats.totalTime) + "\nTotal cost: " + str(stats.totalCost)\
        + "\nNodes expanded: " + str(stats.nodeCount))