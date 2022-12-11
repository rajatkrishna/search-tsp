from utils.cities import Cities
from utils.state import SearchState
from search import UniformCostSearch, MCTS
import sys, getopt
import yaml

def readConfig(path : str):
    with open(path, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print("Invalid config yaml!")
            exit()

if (__name__ == "__main__"):
    # default search method
    searchMethod = 'UniformCostSearch'
    
    # load config
    pathToConfig = "config/config.yml"
    config = readConfig(pathToConfig)
    
    logEnable = config["logEnable"] if "logEnable" in config else False
    searchArgs = {
        "logEnable":logEnable
        }

    # read command line args
    try:
        opts, args = getopt.getopt(sys.argv[1:],"s:",["search="])
    except getopt.GetoptError:
        print("route_finder.py -s <searchmethod>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-s':
            if arg == 'ucs':
                searchMethod = 'UniformCostSearch'
            elif arg == 'mcts':
                searchMethod = 'MCTS'

                expWeight = config["mcts"]["explorationWeight"] if "mcts" in config and "explorationWeight" in config["mcts"]\
                                 else 1
                rewardWeight = config["mcts"]["rewardWeight"] if "mcts" in config and "rewardWeight" in config["mcts"]\
                                 else 1
                noIterationsRollout = config["mcts"]["noIterationsRollout"] if "mcts" in config and "noIterationsRollout" in config["mcts"]\
                                 else 1

                searchArgs['expWeight'] = expWeight
                searchArgs['rewardWeight'] = rewardWeight
                searchArgs['noIterationsRollout'] = noIterationsRollout

    search = globals()[searchMethod](**searchArgs)

    # retrieve cities
    cities = Cities().getCities()
    keys = list(cities.keys())

    # declare start state
    startState = SearchState([keys[0]], [city for city in cities.keys()\
         if city != keys[0]])

    path, stats = search.findPath(startState)

    print("Discovered Path:")
    for i, state in enumerate(path):
        if i == len(path) - 1:
            print(state)
        else:
            print(state, "-->", end=" ")

    print("\n" + stats.toPrettyString())