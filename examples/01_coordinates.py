from alltheutils.utils import parent_dir_nth_times
from PIL import Image, ImageDraw

from imagesmacker.models.coordinates import XYXY

image_size = (500, 500)
image = Image.new("RGB", image_size, color="black")
draw = ImageDraw.Draw(image)
rectangle_coords = XYXY(100, 100, 400, 400)

draw.rectangle(rectangle_coords.list(), fill="purple")

image.save(f"{parent_dir_nth_times(__file__, 2)}/docs/examples/coordinates-test.png")
