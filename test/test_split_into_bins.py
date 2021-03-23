import unittest

from main import split_into_bins, get_maps, unify_maps
import numpy.testing as nptest
import datetime

class MyTestCase(unittest.TestCase):
    def test_split_into_bins(self):
        nptest.assert_almost_equal(split_into_bins(5.5, 6.8, 1), [[5.5, 6.8]])
        nptest.assert_almost_equal(split_into_bins(5.5, 6.8, 2), [[5.5, 6.15], [6.15, 6.8]])
        nptest.assert_almost_equal(split_into_bins(2.5478, 6.8748, 10),
                                   [[2.5478, 2.9805], [2.9805, 3.4132], [3.4132, 3.8459], [3.8459, 4.2786],
                                    [4.2786, 4.7113], [4.7113, 5.144], [5.144, 5.5767], [5.5767, 6.009399999999999],
                                    [6.009399999999999, 6.4421], [6.4421, 6.8748000000000005]])

    def test_get_maps(self):
        print(get_maps(16.6827, 49.4149, 16.6927, 49.4249))
        self.assertEqual(1, len(get_maps(16.6827, 49.4149, 16.6927, 49.4249)))

    def test_get_maps_4_submaps(self):
        self.assertTrue(len(get_maps(16.6227, 49.3749, 16.7027, 49.4349)) > 1)
        # print(len(get_maps(16.6027, 49.3349, 16.7227, 49.4349)))

    def test_unify_maps(self):
        test_list = [[{'type': 'node', 'data': {'id': 247066433, 'visible': True, 'version': 3, 'changeset': 24260590, 'timestamp': datetime.datetime(2014, 7, 20, 19, 19, 19), 'user': 'lcapka', 'uid': 714609, 'lat': 49.4206586, 'lon': 16.6695852, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111885, 'visible': True, 'version': 2, 'changeset': 37162310, 'timestamp': datetime.datetime(2016, 2, 12, 7, 58, 27), 'user': 'Milancer', 'uid': 1189910, 'lat': 49.4481958, 'lon': 16.6496567, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111888, 'visible': True, 'version': 1, 'changeset': 96264, 'timestamp': datetime.datetime(2008, 8, 6, 16, 2, 45), 'user': 'jttt', 'uid': 25176, 'lat': 49.448389, 'lon': 16.650051, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111891, 'visible': True, 'version': 2, 'changeset': 29712185, 'timestamp': datetime.datetime(2015, 3, 24, 20, 7, 10), 'user': 'kwiecpav', 'uid': 1125908, 'lat': 49.4471243, 'lon': 16.6460363, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111894, 'visible': True, 'version': 1, 'changeset': 96264, 'timestamp': datetime.datetime(2008, 8, 6, 16, 2, 45), 'user': 'jttt', 'uid': 25176, 'lat': 49.447505, 'lon': 16.649201, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111900, 'visible': True, 'version': 1, 'changeset': 96264, 'timestamp': datetime.datetime(2008, 8, 6, 16, 2, 45), 'user': 'jttt', 'uid': 25176, 'lat': 49.44625, 'lon': 16.644224, 'tag': {}}}] , [{'type': 'node', 'data': {'id': 247066433, 'visible': True, 'version': 1, 'changeset': 96264, 'timestamp': datetime.datetime(2008, 8, 6, 16, 2, 45), 'user': 'jttt', 'uid': 25176, 'lat': 49.446801, 'lon': 16.643104, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111906, 'visible': True, 'version': 1, 'changeset': 96264, 'timestamp': datetime.datetime(2008, 8, 6, 16, 2, 46), 'user': 'jttt', 'uid': 25176, 'lat': 49.447403, 'lon': 16.643, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111909, 'visible': True, 'version': 2, 'changeset': 29712185, 'timestamp': datetime.datetime(2015, 3, 24, 20, 7, 10), 'user': 'kwiecpav', 'uid': 1125908, 'lat': 49.4529514, 'lon': 16.6568095, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111912, 'visible': True, 'version': 2, 'changeset': 29712185, 'timestamp': datetime.datetime(2015, 3, 24, 20, 7, 10), 'user': 'kwiecpav', 'uid': 1125908, 'lat': 49.4535632, 'lon': 16.6570619, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111915, 'visible': True, 'version': 1, 'changeset': 96264, 'timestamp': datetime.datetime(2008, 8, 6, 16, 2, 46), 'user': 'jttt', 'uid': 25176, 'lat': 49.452159, 'lon': 16.65595, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111918, 'visible': True, 'version': 2, 'changeset': 29712185, 'timestamp': datetime.datetime(2015, 3, 24, 20, 7, 10), 'user': 'kwiecpav', 'uid': 1125908, 'lat': 49.4524728, 'lon': 16.65595, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111921, 'visible': True, 'version': 2, 'changeset': 29712185, 'timestamp': datetime.datetime(2015, 3, 24, 20, 7, 10), 'user': 'kwiecpav', 'uid': 1125908, 'lat': 49.4512132, 'lon': 16.6561397, 'tag': {}}}]]
        self.assertEqual(len(unify_maps(test_list)), 12)
        test_list_2 = [[{'type': 'node', 'data': {'id': 247066433, 'visible': True, 'version': 3, 'changeset': 24260590, 'timestamp': datetime.datetime(2014, 7, 20, 19, 19, 19), 'user': 'lcapka', 'uid': 714609, 'lat': 49.4206586, 'lon': 16.6695852, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111885, 'visible': True, 'version': 2, 'changeset': 37162310, 'timestamp': datetime.datetime(2016, 2, 12, 7, 58, 27), 'user': 'Milancer', 'uid': 1189910, 'lat': 49.4481958, 'lon': 16.6496567, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111888, 'visible': True, 'version': 1, 'changeset': 96264, 'timestamp': datetime.datetime(2008, 8, 6, 16, 2, 45), 'user': 'jttt', 'uid': 25176, 'lat': 49.448389, 'lon': 16.650051, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111891, 'visible': True, 'version': 2, 'changeset': 29712185, 'timestamp': datetime.datetime(2015, 3, 24, 20, 7, 10), 'user': 'kwiecpav', 'uid': 1125908, 'lat': 49.4471243, 'lon': 16.6460363, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111894, 'visible': True, 'version': 1, 'changeset': 96264, 'timestamp': datetime.datetime(2008, 8, 6, 16, 2, 45), 'user': 'jttt', 'uid': 25176, 'lat': 49.447505, 'lon': 16.649201, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111900, 'visible': True, 'version': 1, 'changeset': 96264, 'timestamp': datetime.datetime(2008, 8, 6, 16, 2, 45), 'user': 'jttt', 'uid': 25176, 'lat': 49.44625, 'lon': 16.644224, 'tag': {}}}] , [{'type': 'node', 'data': {'id': 285111903, 'visible': True, 'version': 1, 'changeset': 96264, 'timestamp': datetime.datetime(2008, 8, 6, 16, 2, 45), 'user': 'jttt', 'uid': 25176, 'lat': 49.446801, 'lon': 16.643104, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111906, 'visible': True, 'version': 1, 'changeset': 96264, 'timestamp': datetime.datetime(2008, 8, 6, 16, 2, 46), 'user': 'jttt', 'uid': 25176, 'lat': 49.447403, 'lon': 16.643, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111909, 'visible': True, 'version': 2, 'changeset': 29712185, 'timestamp': datetime.datetime(2015, 3, 24, 20, 7, 10), 'user': 'kwiecpav', 'uid': 1125908, 'lat': 49.4529514, 'lon': 16.6568095, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111912, 'visible': True, 'version': 2, 'changeset': 29712185, 'timestamp': datetime.datetime(2015, 3, 24, 20, 7, 10), 'user': 'kwiecpav', 'uid': 1125908, 'lat': 49.4535632, 'lon': 16.6570619, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111915, 'visible': True, 'version': 1, 'changeset': 96264, 'timestamp': datetime.datetime(2008, 8, 6, 16, 2, 46), 'user': 'jttt', 'uid': 25176, 'lat': 49.452159, 'lon': 16.65595, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111918, 'visible': True, 'version': 2, 'changeset': 29712185, 'timestamp': datetime.datetime(2015, 3, 24, 20, 7, 10), 'user': 'kwiecpav', 'uid': 1125908, 'lat': 49.4524728, 'lon': 16.65595, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111921, 'visible': True, 'version': 2, 'changeset': 29712185, 'timestamp': datetime.datetime(2015, 3, 24, 20, 7, 10), 'user': 'kwiecpav', 'uid': 1125908, 'lat': 49.4512132, 'lon': 16.6561397, 'tag': {}}}]]
        self.assertEqual(len(unify_maps(test_list_2)), 13)
        test_list_3 = [[{'type': 'node', 'data': {'id': 247066433, 'visible': True, 'version': 3, 'changeset': 24260590, 'timestamp': datetime.datetime(2014, 7, 20, 19, 19, 19), 'user': 'lcapka', 'uid': 714609, 'lat': 49.4206586, 'lon': 16.6695852, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111885, 'visible': True, 'version': 2, 'changeset': 37162310, 'timestamp': datetime.datetime(2016, 2, 12, 7, 58, 27), 'user': 'Milancer', 'uid': 1189910, 'lat': 49.4481958, 'lon': 16.6496567, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111921, 'visible': True, 'version': 1, 'changeset': 96264, 'timestamp': datetime.datetime(2008, 8, 6, 16, 2, 45), 'user': 'jttt', 'uid': 25176, 'lat': 49.448389, 'lon': 16.650051, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111891, 'visible': True, 'version': 2, 'changeset': 29712185, 'timestamp': datetime.datetime(2015, 3, 24, 20, 7, 10), 'user': 'kwiecpav', 'uid': 1125908, 'lat': 49.4471243, 'lon': 16.6460363, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111894, 'visible': True, 'version': 1, 'changeset': 96264, 'timestamp': datetime.datetime(2008, 8, 6, 16, 2, 45), 'user': 'jttt', 'uid': 25176, 'lat': 49.447505, 'lon': 16.649201, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111900, 'visible': True, 'version': 1, 'changeset': 96264, 'timestamp': datetime.datetime(2008, 8, 6, 16, 2, 45), 'user': 'jttt', 'uid': 25176, 'lat': 49.44625, 'lon': 16.644224, 'tag': {}}}] , [{'type': 'node', 'data': {'id': 285111903, 'visible': True, 'version': 1, 'changeset': 96264, 'timestamp': datetime.datetime(2008, 8, 6, 16, 2, 45), 'user': 'jttt', 'uid': 25176, 'lat': 49.446801, 'lon': 16.643104, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111906, 'visible': True, 'version': 1, 'changeset': 96264, 'timestamp': datetime.datetime(2008, 8, 6, 16, 2, 46), 'user': 'jttt', 'uid': 25176, 'lat': 49.447403, 'lon': 16.643, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111909, 'visible': True, 'version': 2, 'changeset': 29712185, 'timestamp': datetime.datetime(2015, 3, 24, 20, 7, 10), 'user': 'kwiecpav', 'uid': 1125908, 'lat': 49.4529514, 'lon': 16.6568095, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111912, 'visible': True, 'version': 2, 'changeset': 29712185, 'timestamp': datetime.datetime(2015, 3, 24, 20, 7, 10), 'user': 'kwiecpav', 'uid': 1125908, 'lat': 49.4535632, 'lon': 16.6570619, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111915, 'visible': True, 'version': 1, 'changeset': 96264, 'timestamp': datetime.datetime(2008, 8, 6, 16, 2, 46), 'user': 'jttt', 'uid': 25176, 'lat': 49.452159, 'lon': 16.65595, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111894, 'visible': True, 'version': 2, 'changeset': 29712185, 'timestamp': datetime.datetime(2015, 3, 24, 20, 7, 10), 'user': 'kwiecpav', 'uid': 1125908, 'lat': 49.4524728, 'lon': 16.65595, 'tag': {}}}, {'type': 'node', 'data': {'id': 285111921, 'visible': True, 'version': 2, 'changeset': 29712185, 'timestamp': datetime.datetime(2015, 3, 24, 20, 7, 10), 'user': 'kwiecpav', 'uid': 1125908, 'lat': 49.4512132, 'lon': 16.6561397, 'tag': {}}}]]
        self.assertEqual(len(unify_maps(test_list_3)), 11)



if __name__ == '__main__':
    unittest.main()
