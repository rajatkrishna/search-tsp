# search-tsp
 
The aim of this project is to compare the performances of different tree search algorithms on the travelling salesman problem. The travelling salesman problem (also called the travelling salesperson problem or TSP) asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?" 

## Usage
To start this application, navigate to the `route-finder` directory. Use the following command to begin execution.
```
python3 route_finder.py
```
By default, Uniform Cost Search algorithm is used for discovering the optimal path. This behaviour can be changed by passing appropriate [arguments](#arguments).

## Search Configuration
The config file `config/config.yml` can be used to modify program behaviour. The following settings can be configured:
- logEnable: Enable/disable log output to the console.
- printGraph: Generate search graph. The search tree will be generated and saved to `route-finde/graph.html`
- explorationWeight: The exploration weight parameter for MCTS search.
- rewardWeight: The reward weight for the inner function used in MCTS search. 
- noIterationsRollout: The number of rollouts in each iteration performed by the MCTS algorithm.
## Arguments 
- -s/--search (optional): Search algorithm to use. Accepted values for this argument are `ucs` and `mcts`