import networkx as nx
from typing import Dict
from typing import List
from enum import Enum
import random
import matplotlib.pyplot as plt


class GeoLocation(object):

    def __init__(self, latitude: int, longitude: int):

        if latitude < 0:
            raise ValueError("latitude cannot be < 0")
        if longitude < 0:
            raise ValueError("longitude cannot be < 0")

        self.latitude = latitude
        self.longitude = longitude

    def latitude(self) -> int:
        return self.latitude

    def longitude(self) -> int:
        return self.longitude

    def __str__(self) -> str:
        return "({}, {})".format(self.latitude, self.longitude)


class CityLocationType(Enum):
    residence = 1
    business = 2
    blockage = 3
    walkway = 4


class CityLocation(object):

    def __init__(self, location: GeoLocation, location_type: CityLocationType, location_description: str = ""):
        self.location = location
        self.location_type = location_type
        self.location_description = location_description

    def location(self) -> GeoLocation:
        return self.location

    def location_type(self) -> CityLocationType:
        return self.location_type

    def location_description(self) -> str:
        return self.location_description

    def is_residence(self) -> bool:
        return self.location_type == CityLocationType.residence

    def is_business(self) -> bool:
        return self.location_type == CityLocationType.business

    def is_walkway(self) -> bool:
        return self.location_type == CityLocationType.walkway

    def is_blocked(self) -> bool:
        return self.location_type == CityLocationType.blockage

    def __str__(self) -> str:
        return "{}, {}".format(self.location_type, self.location.__str__())


class City:

    def __init__(self, grid_map: List[List[CityLocation]], city_graph: nx.Graph):
        self.grid_map = grid_map
        self.city_graph = self.generate_graph_from_grid_map(grid_map)

    @classmethod
    def generate_graph_from_grid_map(cls, grid_map: List[List[CityLocation]]) -> nx.Graph:

        city_graph = nx.Graph()

        # Add nodes for each point in the city
        for row in range(0, len(grid_map)):
            for column in range(0, len(grid_map[0])):
                city_graph.add_node(grid_map[row][column])

        # connect city nodes
        for row in range(0, len(grid_map)):
            for column in range(0, len(grid_map[0])):
                if row + 1 < len(grid_map):
                    cls.add_edge(city_graph, grid_map[row][column], grid_map[row + 1][column])
                if row - 1 >= 0:
                    cls.add_edge(city_graph, grid_map[row][column], grid_map[row - 1][column])
                if column + 1 < len(grid_map[0]):
                    cls.add_edge(city_graph, grid_map[row][column], grid_map[row][column + 1])
                if column - 1 >= 0:
                    cls.add_edge(city_graph, grid_map[row][column], grid_map[row][column - 1])

        return city_graph

    @classmethod
    def add_edge(cls, city_graph: nx.Graph, source: CityLocation, destination: CityLocation):
        city_graph.add_edge(source, destination, blocked=source.is_blocked() or destination.is_blocked())

    @classmethod
    def generate_random_city(cls, rows: int, columns: int):

        city_grid = []
        for row in range(0, rows):
            row_list = []
            for column in range(0, columns):
                location = CityLocation(GeoLocation(row, column), cls.get_random_location_type(rows * columns))
                row_list.append(location)
            city_grid.append(row_list)

        return City(city_grid, nx.Graph())

    @classmethod
    def get_random_location_type(cls, range: int) -> CityLocationType:

        is_walkway = cls.get_random(50, range)
        is_residence = cls.get_random(25, range)
        is_business = cls.get_random(20, range)
        is_blockage = cls.get_random(5, range)

        if is_walkway:
            return CityLocationType.walkway
        elif is_residence:
            return CityLocationType.residence
        elif is_business:
            return CityLocationType.business
        elif is_blockage:
            return CityLocationType.blockage
        else:
            return CityLocationType.walkway

    @classmethod
    def get_random(cls, probability: float, range: int) -> bool:
        return random.randrange(0, range) <= probability

    def print(self, as_graph: bool = False, as_grid: bool = True):

        if as_grid:
            city = ""
            for row in self.grid_map:
                city_lane = "| "
                for location in row:
                    if location.is_walkway():
                        city_lane = city_lane + "  | "
                    if location.is_blocked():
                        city_lane = city_lane + "* | "
                    if location.is_business():
                        city_lane = city_lane + "B | "
                    if location.is_residence():
                        city_lane = city_lane + "R | "
                city = city + city_lane + "\n"

            print(city)

        if as_graph:

            pos = nx.random_layout(self.city_graph)

            walkway_locations = []
            business_locations = []
            residence_locations = []
            blocked_locations = []

            for location in self.city_graph.nodes():
                if location.is_walkway():
                    walkway_locations.append(location)
                if location.is_residence():
                    residence_locations.append(location)
                if location.is_business():
                    business_locations.append(location)
                if location.is_blocked():
                    blocked_locations.append(location)

            nx.draw_networkx_nodes(self.city_graph, pos, nodelist=walkway_locations, node_color="green", node_size=20,
                                   node_shape="x", alpha=0.8)
            nx.draw_networkx_nodes(self.city_graph, pos, nodelist=residence_locations, node_color="yellow",
                                   node_size=250, node_shape="s", alpha=0.8)
            nx.draw_networkx_nodes(self.city_graph, pos, nodelist=business_locations, node_color="blue", node_size=250,
                                   node_shape="o", alpha=0.8)
            nx.draw_networkx_nodes(self.city_graph, pos, nodelist=blocked_locations, node_color="red", node_size=200,
                                   node_shape="*", alpha=0.8)

            nx.draw_networkx_edges(self.city_graph, pos, width=0.2, alpha=0.4)

            labels = dict([(loc, "({}, {})".format(loc.location.latitude, loc.location.longitude)) for loc in
                           self.city_graph.nodes()])

            if len(self.grid_map) * len(self.grid_map[0]) <= 100:
                nx.draw_networkx_labels(self.city_graph, pos, labels, font_size=5, alpha=0.8)

            nx.write_gexf(self.city_graph, "city-gephi.gexf", encoding="utf-8")
            plt.axis('off')
            plt.savefig("city.png")  # save as png
            plt.show()
