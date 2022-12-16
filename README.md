<div align="center">
  <img src="https://drive.google.com/uc?id=14obsLoVYIPi_l9rf1roEVXqmnpUPmq8u">
</div>
<hr/>

[routeaccess](https://github.com/rajatkrishna/search-tsp) is a route planning application that can be used for calculating optimal routes to visit a set of locations exactly once and return to the starting location. The optimal route is defined as the route that spans the least distance. The approach used here presents the problem statement as a search problem, and applies search algorithms that can generate a reasonably optimal solution in limited time/memory constraints. To this end, this application can be also be used to study the feasibility of search algorithms in solving variations of the Travelling Salesman problem.

## Approach

The Uniform Cost Search algorithm is an uninformed search algorithm, meaning it operates in a brute-force manner, ignoring any additional information about the state/search space. The search tree is expanded symmetrically, as the algorithm looks for terminal states with the lowest costs seen so far.

In contrast to this, Monte Carlo Tree Search (MCTS) method gathers insights about the search space by playing out simulations of the tour before picking an optimal path. Thus, in a way, the algorithm guides the search tree expansion to focus on subtrees that show promising results in the future. 

In this application, you can use either of these techniques for path discovery, thereby explore the effectiveness of these techniques.

## Usage

- Clone the repository and navigate to the folder `search-tsp/route-finder`
- Run the following command
```
python3 route_finder.py
```

By default, Uniform Cost Search algorithm is used for discovering the optimal path. This behaviour can be changed by passing appropriate [arguments](#arguments).

![cli-screenshot1](https://user-images.githubusercontent.com/61770314/208029897-937549f2-48a6-4990-aafb-c24c5a4922ac.jpg)

The search tree generated can be seen in `./route-finder/resources/graphs`

![mcts-search-tree](https://user-images.githubusercontent.com/61770314/208030141-b0d6c9e3-2806-4644-b180-26549c0931c0.png)


## Search Configuration
The config file `config/config.yml` can be used to modify program behaviour. The following settings can be configured:
- logEnable: Enable/disable log output to the console.
- printGraph: Generate search graph. The search tree will be generated and saved to `route-finder/graph.html`
- explorationWeight: The exploration weight parameter for MCTS search.
- rewardWeight: The reward weight for the inner function used in MCTS search. 
- noIterationsRollout: The number of rollouts in each iteration performed by the MCTS algorithm.
## Arguments 
- -s/--search (optional): Search algorithm to use. Accepted values for this argument are `ucs` and `mcts`
