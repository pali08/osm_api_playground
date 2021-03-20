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

def split_into_bins(min, max, number_of_bins):
    interval = (max - min) / number_of_bins
    return [min + (interval * i) for i in range(0,number_of_bins+1)]



def get_map(*coordinates):

    osm_map = 0
    while osm_map == 0:
        osm_map = get_map_with_check()
    # test_map = basic_osm_api.Map(15.55103, 49.23309, 16.56716, 49.23932)
    # print(test_map[0])
    # for node in test_map:
    #     try:
    #         print(node['data']['tag']['name'])
    #         print(node['type'])
    #     except KeyError as ke:
    #         pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_map()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
