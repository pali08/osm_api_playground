import staticmaps


def create_area(*coords):
    context = staticmaps.Context()
    context.set_tile_provider(staticmaps.tile_provider_OSM)
    rectangle = [(coords[0], coords[1]), (coords[2], coords[1]), (coords[2], coords[3]), (coords[0], coords[3]),
                 (coords[0], coords[1])]

    context.add_object(
        staticmaps.Area(
            [staticmaps.create_latlng(lat, lng) for lat, lng in rectangle],
            fill_color=staticmaps.parse_color("#FFFFFF00"),
            width=2,
            color=staticmaps.BLUE,
        )
    )
    return context


def write_png(context):
    image = context.render_cairo(800, 600)
    image.write_to_png("rectangle_area_map.png")


def write_svg(context):
    svg_image = context.render_svg(800, 600)
    with open("rectangle_area_map.svg", "w", encoding="utf-8") as f:
        svg_image.write(f, pretty=True)


def get_image(*coords, png_or_svg='png'):
    context = create_area(*coords)
    if png_or_svg == 'png':
        write_png(context)
    elif png_or_svg == 'svg':
        write_svg(context)


get_image(49.4750, 15.8611, 49.5005, 15.9178)
