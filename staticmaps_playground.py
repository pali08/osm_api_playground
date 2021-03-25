import numpy as np
import staticmaps
from s2sphere import LatLng
from staticmaps import cli, Area

context = staticmaps.Context()
context.set_tile_provider(staticmaps.tile_provider_OSM)
# context.set_center(LatLng(0.837213673, 0.135969003))
context.add_object(Area([staticmaps.create_latlng(49.4750, 15.8611),
                         staticmaps.create_latlng(49.4750, 15.9178),
                         staticmaps.create_latlng(49.5005, 15.9178),
                         staticmaps.create_latlng(49.5005, 15.8611)]))

# freiburg_polygon = [
#     (47.96881, 7.79045),
#     (47.96866, 7.78610),
#     (47.97134, 7.77874),
#     (47.96881, 7.79045)
#     # , ...
# ]
#
# context.add_object(
#     staticmaps.Area(
#         [staticmaps.create_latlng(lat, lng) for lat, lng in freiburg_polygon],
#         fill_color=staticmaps.parse_color("#00FF003F"),
#         width=2,
#         color=staticmaps.BLUE,
#     )
# )

# render png
image = context.render_cairo(10, 10)
image.write_to_png("freiburg_area.png")

# render svg
svg_image = context.render_svg(800, 500)
with open("freiburg_area.svg", "w", encoding="utf-8") as f:
    svg_image.write(f, pretty=False, indent=0)
