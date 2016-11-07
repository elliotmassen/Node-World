# Node World

A very small project to simulate an extremely basic evolutionary system. I had the idea after following a train of thought from a seminar on current trends in cognitive science.

The project simulates a "world" which contains "nodes". The nodes have the very basics to allow them to "evolve". The only aspect that evolves is their lifespan, which can - with each reproducation - mutate to be either higher, lower or the same.

When you run the simulation you'll see some statistics, try messing around with the input values (as described below) to see how they affect the statistics.

## Running the simulation
You'll need [Python 2](https://www.python.org/downloads/) installed on your machine to run this simulation.

Once you've installed Python, locate the project in the terminal and run:

	$ python node_world.py 100 3 1000

You can swap the integers to be whatever you like, they represent the following values:

	$ python node_world.py [Life span of first node] [Maximum potential mutation] [Maximum number of nodes allowed]