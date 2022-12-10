from utils.cities import Cities
from utils.state import SearchState
from search import UniformCostSearch, MCTS
import sys, getopt

if (__name__ == "__main__"):
    searchMethod = 'UniformCostSearch'
    logEnable = False
    
    try:
        opts, args = getopt.getopt(sys.argv[1:],"ls:",["search=", "log"])
    except getopt.GetoptError:
        print("route_finder.py -s <searchmethod>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-s':
            if arg == 'ucs':
                searchMethod = 'UniformCostSearch'
            elif arg == 'mcts':
                searchMethod = 'MCTS'
        elif opt == '--log' or opt == '-l':
            logEnable = True

    search = globals()[searchMethod](logEnable)

    # retrieve cities
    cities = Cities().getCities()
    keys = list(cities.keys())

    # declare start state
    startState = SearchState([keys[0]], [city for city in cities.keys()\
         if city != keys[0]])

    _, stats = search.findPath(startState)

    print(stats.toPrettyString())