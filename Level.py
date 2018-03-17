import json

from Map import Map
from Security import Security


class Level:

    def __init__(self, filename):
        with open(filename) as f:
            self.data = json.load(f)

        self.map = Map(self.data["map"])
        self.security = Security(self.data["security"])

        self.init_disk(self.data["disk"])

    def init_password(self, password):
        pass

    def init_disk(self, disk_dict):
        pass


l = Level("level0.json")
