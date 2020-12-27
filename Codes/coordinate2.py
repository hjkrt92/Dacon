from pyproj import Proj, transform
from pyproj import Transformer
import folium
inProj = Proj('+proj=tmerc +lat_0=38 +lon_0=128 +k=0.9999 +x_0=400000 +y_0=600000 +ellps=bessel +units=m +no_defs +towgs84=-115.80,474.99,674.11,1.16,-2.31,-1.63,6.43')
outProj = Proj('epsg:4326')
x1,y1 = 936288.3731000003, 1499041.8584
# transformer = Transformer.from_crs(inProj, outProj)
# x,y = transformer.transform(x1, y1)
# print(x, y)
# 936288.3731000003 1499041.8584
proj_UTMK = Proj('epsg:5178')
proj_WGS84 = Proj('epsg:4326')
# x1, y1 = 877005.9834, 1.479766e+06
# x2, y2 = transform(proj_UTMK, proj_WGS84, x1, y1)
def U_W(x,y):
    return transform(proj_UTMK, proj_WGS84, x, y)
def title(m,x):
    loc = x
    title_html = '''
                 <h3 align="center" style="font-size:16px"><b>{}</b></h3>
                 '''.format(loc)
    m.get_root().html.add_child(folium.Element(title_html))
    return m