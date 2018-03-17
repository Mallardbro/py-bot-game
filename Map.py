from PIL import Image

from Colours import saved_colours


# from Error import Error

# TODO: Scale map up from 1px by 1px and improve readability of map (Grid lines, numbered axis?(

class Map:

    def __init__(self, json):

        self.width, self.height = json["size"]
        self.data = json["image_data"]
        self.image = self.init_image()

        if self.image:
            self.image.save("map0.png", format="PNG")

    def init_image(self):
        assert self.width * self.height == len(self.data), "Map data has incorrect dimensions."
        im = Image.new("RGB", (self.width, self.height), 0)
        # TODO: Improve system for colours.
        colours = list(saved_colours.values())
        pixels = im.load()
        for i, val in enumerate(self.data):
            x = i % self.width
            # y flip to make (0,0) in the bottom-left
            y = (self.height - 1) - i // self.width
            pixels[x, y] = colours[val]
        print(f"Map initialized with size [{self.width}, {self.height}].")
        return im

# m = Map({"size": [3, 3], "image_data": [1, 1, 1, 2, 2, 2, 3, 3, 3]})
