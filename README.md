# Title: Testing City Hotspots Using Monte Carlo Simulations of Pedestrian Traffic

# Monte Carlo Simulation Scenario & Purpose:

Businesses and city planners often need to address where best to locate ameneties in order to maximize foot traffic. One way to solve this problem is to run multiple simulations of pedestrians traversing a city grid, treating such a grid as a network of pathways connecting businesses, residences, and occasionally blocked paths, and looking at where pedestrians frequently cross paths.

However, such simulations can be time consuming if a model of a city grid must be constructed for each scenario. Moreover, the goal is to present multiple layout possibilities for a section of the city and to quickly assess what locations will get the most traffic.

This program will handle both the rapid construction of a city model and the modeling of pathways of pedestrians seeking to minimize walking distances from start to destination, all for the purpose of seeking the maximal place to locate a business or amenity to maximize foot traffic.



## Simulation's variables of uncertainty

Uncertainty for this simulation occurs in two places: the construction of the city model and the pathways of pedestrians.

 1. Each city model generated by the program has a set proportion of businesses, residences, walkways (throughways), and blocked path (e.g. construction zones, closed paths). However, the simulation will use pseudo-random numbers to locate the placement of each of those elements when it constructs the model city grid.

 2. Pedestrians who are initiated for the purpose of the model will be assigned a starting location (a residence) and a destination (a business) using a random sample without replacement of all available residences/businesses in the city model.

The idea behind these parameters, as with any Monte Carlo simulation, is to consider a wider range of possibilities then a simulation using a pre-determined layout or pedestrian behavior might uncover. Using pseudo-randomly generated layouts and pedestrian pathways widens the number of cases to consider.


## Hypothesis or hypotheses before running the simulation:

Our central question for this particular simulation was whether the nodes/locations with the optimal pedestrian traffic would be those that were also residences and businesses, or near them, or whether walkways would be more likely to prove to be high traffic points.

To test this multiple simulations were run on a several city grids, each with a different proportion of businesses, residences, and walkways.

## Analytical Summary of your findings:

The following multiple runs of multiple simulations seems to indicate a convergence around walkway node types as the optimal place to situated a location for maximum foot traffic. This isn't necessarily intuitive. We would assume perhaps that given the assumption in this model (and in real life) that a pedestrian orginates and has a destination in a residence/business, one might expect hotspots to be at those locations. However, the parameters for this model suggest that in fact hotspots take place in the unoccuped walkways between those locations.

These simulations were run with a city grid generated with probability of .35 for a node being a walkway, .25 for it to be a residence, .35 for it to be a business, and .05 to be a blocked node.

Results for 10 and 20 size grids, multiple selections for pedestrians and number of simulations produced:

| Gridsize | # Pedestrians | # Simulations | Top Location | Location Type |
|----------|---------------|---------------|--------------|---------------|
| 10       | 10            | 100           | (4,3)        | Residence     |
| 10       | 10            | 1000          | (3,2)        | Walkway       |
| 10       | 10            | 5000          | (6,1)        | Walkway       |
| 10       | 10            | 10000         | (2,6)        | Business      |
| 10       | 20            | 100           | (4,4)        | Walkway       |
| 10       | 20            | 1000          | (4,5)        | Business      |
| 10       | 20            | 5000          | (2,5)        | Walkway       |
| 10       | 20            | 10000         | (5,4)        | Residence     |
| 10       | 20            | 20000         | (4,3)        | Walkway       |
| 10       | 30            | 100           | (6,4)        | Walkway       |
| 10       | 30            | 1000          | (4,1)        | Residence     |
| 10       | 30            | 5000          | (3,4)        | Walkway       |
| 10       | 30            | 10000         | (3,5)        | Business      |
| 10       | 30            | 20000         | (2,1)        | Business      |
| 10       | 40            | 100           | (4,1)        | Walkway       |
| 10       | 40            | 1000          | (5,3)        | Walkway       |
| 10       | 40            | 5000          | (5,6)        | Walkway       |
| 10       | 40            | 10000         | (3,5)        | Business      |
| 10       | 40            | 20000         | (4,3)        | Walkway       |
| 20       | 10            | 100           | (8,14)       | Walkway       |
| 20       | 10            | 1000          | (11,9)       | Walkway       |
| 20       | 10            | 5000          | (6,6)        | Walkway       |
| 20       | 10            | 10000         | (10,7)       | Walkway       |
| 20       | 10            | 20000         | (4,10)       | Business      |
| 20       | 20            | 100           | (13,10)      | Walkway       |
| 20       | 20            | 1000          | (11,10)      | Walkway       |
| 20       | 20            | 5000          | (10,5)       | Walkway       |
| 20       | 20            | 10000         | (9,5)        | Walkway       |
| 20       | 20            | 20000         | (8,8)        | Walkway       |
| 20       | 30            | 100           | (7,27)       | Walkway       |
| 20       | 30            | 1000          | (13,9)       | Walkway       |
| 20       | 30            | 5000          | (12,9)       | Walkway       |
| 20       | 30            | 10000         | (5,11)       | Walkway       |
| 20       | 30            | 20000         | (9,5)        | Walkway       |

Note the increasing number of walkways that proved to be hotspots, especially as the size of the city, number of pedestrians, and number of simulations grew.


## Instructions on how to use the program:

This program is reliant on having the following modules installed:

[```networkx```](https://networkx.github.io/documentation/latest/install.html) (>2.0)

[```beautifultable```](https://pypi.org/project/beautifultable/)

Run `ped_collisions.py` within directory to set parameters and run simulation.

User will be prompted for the number of simulations to run, size of city grid to model, a range of number of pedestrians to consider, whether to display an image of the city grid being used, and whether output files of the city grid network are desired.

Once run, if selected the program will output a basic ASCII rendition of the city grid generated, like this:

![Sample Table](https://github.com/nmwolf/Final_Project/blob/master/imgs/sample-city-grid.png)

R = Residences

B = Businesses

`X` = Blockage

| | = Walkway

If selected, an image (.png) of the network graph will also be generated, along with a Gephi file (.gefx) to assist users with a richer view of the grid being modeled.

Example:

![Sample Network Graph](https://github.com/nmwolf/Final_Project/blob/master/imgs/network-image-example.png)

## Program structure

The simulation relies on several Python classes. The `City` object is a `networkx` graph representing the city layout to be tested. Each `City` consists of a series of `CityLocation` nodes; a `CityLocation` is connected to other nodes, and has attributes such as a `GeoLocation` (latitude-longitude) and type (residence, business, walkway, blockage).

The `Pedestrian` object has a start (`Pedestrian.start_location`), an end (`Pedestrian.end_location`), and a shortest simple path (`networkx` simple paths) between those two points (`Pedestrian.list_short_paths`).

When the simulation is run, it first builds the `City` object, then a set of `Pedestrian` objects. Lastly, it investigates the relationship of each pedestrian's paths to each others given the contours of the city.


## Program Results

When run, the program will generate for the user a table summarizing each simulation like this example:

![Sample Table](https://github.com/nmwolf/Final_Project/blob/master/imgs/sample-results.png)


```The location with most foot traffic from all the simulations for pedestrian traffic is located at the node located at business, (8, 12) with 13 collisions (saved as city-with-marked_locations.png).```

Each row represents one simuluation of *n* pedestrians (in this case, 4 and 5), on a city grid of a size *k*, here 10.

The program looks at which locations (nodes, i.e. `CityLocation`) occurred most often in shortest pathways (the column "Number of Times Node in a Pedestrian Path")


## All Sources Used:

No pedestrian simulation models were consulted prior to designing this program. However, further reading and alternative approaches to such modeling might be found at:

Mehdi Moussaïd, Niriaska Perozo, Simon Garnier, Dirk Helbing, and Guy Theraulaz (2010), "The walking behaviour of pedestrian social groups and its impact on crowd dynamics" *PLoS One*, [10.1371/journal.pone.0010047](https://doi.org/10.1371/journal.pone.0010047).

Jörg Dallmeyer, Andreas Lattner, and Ingo Timm (2012), "Pedestrian Simulation for Urban Traffic Scenarios," *Proceedings of the 2012 - Summer Computer Simulation Conference, SCSC 2012, Part of SummerSim 2012 Multiconference* 44 [Research Gate](https://www.researchgate.net/publication/251879780_Pedestrian_Simulation_for_Urban_Traffic_Scenarios).
