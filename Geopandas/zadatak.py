import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, LineString, Point
import rasterio
from math import sqrt
import fiona; fiona.supported_drivers
import shapefile
import numpy as np

#user input for block number
while True:
    try:
        block_number=int(input('Block number: '))
    except ValueError:
        continue
    if block_number<1:
      continue
    else:
        break  

   

#reading data from shapefile using Geopandas
poly = gpd.read_file('Boulder polygons\Test_Manually_Picked_Boulders.shp')

# copy poly to new GeoDataFrame
poly_centroid = poly.copy()
# change the geometry
poly_centroid.geometry = poly_centroid['geometry'].centroid

#extracting Easting and Northing coord from centroid
poly_centroid['Easting'] = poly_centroid.geometry.map(lambda p: p.x)
poly_centroid['Northing'] = poly_centroid.geometry.map(lambda p: p.y)

#reading data from tiff file
src = rasterio.open('MBES grid\Test_Encoded_Depths_File.tif')

#extracting Water depth value from tiff file at centroid postion
coord_list = [(x, y) for x, y in zip(poly_centroid['geometry'].x, poly_centroid['geometry'].y)]
poly_centroid['WaterDepth'] = [x for x in src.sample(coord_list)]

#changing 'WaterDepth' type from pandas.core.series.Series to np.float64
poly_centroid['WaterDepth'] = poly_centroid['WaterDepth'].astype(np.float64)

#reading data from shapefile using shapefile
poly_s = shapefile.Reader('Boulder polygons\Test_Manually_Picked_Boulders.shp')

#getting longest lengths of polygons
lengthList = [] 
n=len(poly_s)
for p in range(n):
    feature = poly_s.shapeRecords()[p]
    points = feature.shape.points
    dmax = 0
    for i in range(len(points)-1):
        for j in range(i+1, len(points)-1):
            x0 = (points[i][0] - points[j][0])
            y0 = (points[i][1] - points[j][1])
            d = sqrt(x0*x0 + y0*y0)
            if d > dmax:
                dmax = d
    lengthList.append(dmax)

pointsDepths = []
averDepth = []
#extracting water depth for every point of polygons
for p in range(n):
    feature = poly_s.shapeRecords()[p]
    points = feature.shape.points
    pointsDepths.append([x for x in src.sample(points)])
    
    #calculating average water depth for every point of polygons
    sum = 0
    for i in range (len(pointsDepths[p])-1):
        sum = sum + pointsDepths[p][i]
    averDepth.append(sum/(len(pointsDepths[p])-1))
    #changing 'averDepth' type from numpy.ndarray to np.float64
    averDepth[p] = averDepth[p][0].astype(np.float64)
#importing data to fields 
poly_centroid['Poly_ID'] = poly_centroid.index  
poly_centroid['TargetID']='MBES_'+ str(block_number) +'_' +poly_centroid['Poly_ID'].apply(str)
poly_centroid['Block'] = 'B'+ str(block_number)
poly_centroid['Length'] = lengthList
poly_centroid['averDepth'] = averDepth
poly_centroid['Height']=abs(poly_centroid['averDepth']-poly_centroid['WaterDepth'])

#printing required attribute fields
print(poly_centroid[['Poly_ID','TargetID', 'Block','Easting', 'Northing','WaterDepth' , 'Length' , 'Height']].head(55))
#writting data to outpt file and storing the output layer in the same folder as the input vector layer
poly_centroid.to_file('Boulder polygons\output.shp')
