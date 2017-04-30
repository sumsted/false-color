from io import BytesIO
from PIL import Image


class FalseColor():
    def __init__(self, file_name=None):
        self.image = self.get_image(file_name)
        self.new_pixels = []

    def start(self):
        self.evaluate_image()
        self.create_new()

    def get_image(self, file_name=None):
        infile = 'images/vis.jpg' if file_name is None else file_name
        image_bytes = open(infile, 'rb').read()
        fp = BytesIO(image_bytes)
        return Image.open(fp)

    # actual rgb, dev, new rgb
    LEVELS = [
        (200, 200, 200, 55, 255, 0, 0)
        # ,
        # (55, 55, 55, 55, 255, 0, 0)
    ]

    def evaluate_image(self):
        image_data = self.image.getdata()
        for pixel in image_data:
            found = False
            for level in self.LEVELS:
                if (level[0] - level[3]) <= pixel[0] <= (level[0] + level[3]) and \
                                        (level[1] - level[3]) <= pixel[1] <= (level[1] + level[3]) and \
                                        (level[2] - level[3]) <= pixel[2] <= (level[2] + level[3]):
                    self.new_pixels.append((level[4], level[5], level[6]))
                    found = True
                    break
            if not found:
                self.new_pixels.append((pixel[0], pixel[1], pixel[2]))

    def create_new(self):
        new_image = Image.new("RGB", self.image.size)
        new_image.putdata(self.new_pixels)
        new_image.save('images/new.jpg')


if __name__ == '__main__':
    fc = FalseColor()
    fc.start()
