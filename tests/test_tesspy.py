from unittest import TestCase
import tesspy.tesspy as tp


class TestTessObj(TestCase):
    def test_quad_key(self):
        print("Test for string input")
        for res in [i for i in range(8, 17)]:
            qk = tp.TessObj.quadKey(self, "Frankfurt am Main", res)
            print(qk.shape)

        print("Test for GeoDataFrame")
        admin_polygon = tp.get_admin_polygon("Frankfurt am Main")
        qk_GeoDF = tp.TessObj.quadKey(self, admin_polygon, 15)
        print(qk_GeoDF.shape)

        print("Test for Shapely Polygon")
        admin_polygon = tp.get_admin_polygon("Frankfurt am Main")
        polygon = admin_polygon.geometry.values[0]
        qk_polygon = tp.TessObj.quadKey(self, polygon, 15)
        print(qk_polygon.shape)

    def test_hexagon(self):
        print("Test for string input")
        for res in [i for i in range(5, 10)]:
            h3 = tp.TessObj.hexagon(self, "Frankfurt am Main", res)
            print(h3.shape)

        print("Test for GeoDataFrame")
        admin_polygon = tp.get_admin_polygon("Frankfurt am Main")
        h3_GeoDF = tp.TessObj.hexagon(self, admin_polygon, 8)
        print(h3_GeoDF.shape)

        print("Test for Shapely Polygon")
        admin_polygon = tp.get_admin_polygon("Frankfurt am Main")
        polygon = admin_polygon.geometry.values[0]
        h3_polygon = tp.TessObj.hexagon(self, polygon, 8)
        print(h3_polygon.shape)

    # def test_voronoi(self):
    #     self.fail()

    # def test_cityblocks(self):
    #     self.fail()

    def test_admin_polygon(self):
        city = tp.get_admin_polygon("Frankfurt am Main")
        print(city)

    def test_get_bbox(self):
        bbox = tp.get_bbox("Frankfurt am Main")
        print(bbox)

    def test_explode(self):
        qk = tp.TessObj.hexagon(self, "Frankfurt am Main", 14)
        exploded_qk = qk.explode()
        print(exploded_qk.head())