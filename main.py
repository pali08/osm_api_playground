import osmapi.OsmApi
import datetime

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_map_with_check(*coordinates):
    try:
        return osmapi.OsmApi().Map(*coordinates)
    except osmapi.ApiError as oai:
        return 0


def split_into_bins(min_coor, max_coor, number_of_bins):
    interval_size = (max_coor - min_coor) / number_of_bins
    interval_borders = [min_coor + (interval_size * i) for i in range(0, number_of_bins + 1)]
    intervals = [[interval_borders[i], interval_borders[i + 1]] for i in range(0, len(interval_borders) - 1)]
    return intervals


def get_maps(*coordinates):
    osm_maps = [get_map_with_check(*coordinates)]
    # print(osm_maps[0])
    if osm_maps != [0]:
        print('Nodes count is ' + str(len([i for i in osm_maps[0] if i['type'] == 'node'])))
        print(len(osm_maps[0]))
    counter = 2
    while 0 in osm_maps:
        # osm_maps = []
        intervals_lon = split_into_bins(coordinates[0], coordinates[2], counter)
        # print(intervals_lon)
        intervals_lat = split_into_bins(coordinates[1], coordinates[3], counter)
        osm_maps = [get_map_with_check(intervals_lon[i][0],
                                       intervals_lat[j][0],
                                       intervals_lon[i][1],
                                       intervals_lat[j][1]) for i in range(0, counter) for j in range(0, counter)]
        # print(intervals_lat)
        # for i in range(0, counter):
        #     for j in range(0, counter):
        #         osm_maps.append(get_map_with_check(intervals_lon[i][0],
        #                                            intervals_lat[j][0],
        #                                            intervals_lon[i][1],
        #                                            intervals_lat[j][1]))
        # print(osm_maps)
        # print(osm_maps)
        counter += 1
    # try:
    #     print(osm_maps == osm_maps_2)
    # except UnboundLocalError:
    #     pass
    return osm_maps


def unify_maps(all_map_dicts):
    id_set = set()
    unified_map = []
    for map_dict in all_map_dicts:
        for item in map_dict:
            if item['data']['id'] not in id_set:
                id_set.add(item['data']['id'])
                unified_map.append(item)
    return unified_map


if __name__ == '__main__':
    osm_maps = get_maps()
    unify_maps(osm_maps)
    print_hi('PyCharm')
