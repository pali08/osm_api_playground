# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import osmapi.OsmApi


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_map_with_check(*coordinates):
    try:
        return osmapi.OsmApi().Map(*coordinates)
    except osmapi.OsmApi.ApiError as oai:
        return 0


def split_into_bins(min_coor, max_coor, number_of_bins):
    interval_size = (max_coor - min_coor) / number_of_bins
    interval_borders = [min_coor + (interval_size * i) for i in range(0, number_of_bins + 1)]
    intervals = [[interval_borders[i], interval_borders[i + 1]] for i in range(0, len(interval_borders) - 1)]
    return intervals


def get_map(*coordinates):
    osm_maps = [get_map_with_check(*coordinates)]
    counter = 2
    while 0 in osm_maps:
        osm_maps = []
        intervals_lon = split_into_bins(coordinates[0], coordinates[2], counter)
        intervals_lat = split_into_bins(coordinates[1], coordinates[3], counter)
        for i in range(0, counter):
            osm_maps.append(get_map_with_check(intervals_lon[0], intervals_lat[0], intervals_lon[1], intervals_lat[1]))
        counter += 1
    return osm_maps

def unify_maps(map_dicts):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_map()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
