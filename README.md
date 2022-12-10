# search-tsp
 
The aim of this project is to compare the performances of different tree search algorithms on the travelling salesman problem. The travelling salesman problem (also called the travelling salesperson problem or TSP) asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?" 

## Usage
To start this application, navigate to the `route-finder` directory. Use the following command to begin execution.
```
python3 route_finder.py
```
### Arguments
- -l/--log (optional): Enable/disable logging output. 
- -s/--search (optional): Search algorithm to use. Accepted values for this argument are `ucs` and `mcts`