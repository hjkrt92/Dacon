
from pyproj import Proj
from pyproj import transform

WGS84 = { 'proj':'latlong', 'datum':'WGS84', 'ellps':'WGS84', }

# conamul
TM127 = { 'proj':'tmerc', 'lat_0':'38N', 'lon_0':'127.0028902777777777776E',
   'ellps':'bessel', 'x_0':'200000', 'y_0':'500000', 'k':'1.0',
   'towgs84':'-146.43,507.89,681.46'}
'''
+proj=tmerc +lat_0=38 +lon_0=128 +k=0.9999 +x_0=400000 +y_0=600000 +ellps=bessel +units=m +no_defs 
+towgs84=-115.80,474.99,674.11,1.16,-2.31,-1.63,6.43 "
'''
# naver
katec = {'proj':'tmerc', 'lat_0':'38N','lon_0':'128E', 'ellps':'bessel',
   'x_0':'400000', 'y_0':'600000', 'k':'0.9999',
   'towgs84':'-115.80,474.99,674.11,1.16,-2.31,-1.63,6.43 '}

proj_4326 = Proj(init='epsg:4326')
proj_5178 = Proj(init="epsg:5178")
def katec_to_4326(longitude, latitude):
    return transform(Proj(**katec), proj_4326, longitude, latitude)
def proj5178_to_proj4326(longitude, latitude):
    return transform(proj_5178, proj_4326, longitude, latitude)