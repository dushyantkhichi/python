#importing libraries
import geopandas as gpd 
import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns

# set the filepath and load in a shapefile
fp = "District_boundary\\District_Boundary.shp"
map_df = gpd.read_file(fp)
# check data type so we can see that this is not a normal dataframe, but a GEOdataframe

map_df.head()
#ploting map

map_df.plot()
df = gpd.read_file(fp)
df.head()

#coverting dataframe to a small dataframe
df = df[['DIST_NAME','POPULATION']]

#changing columns name
data_for_map = df.rename(index=str, columns={'DIST_NAME':'DIST','POPULATION':'POPU'})

# check dataframe
data_for_map.head()

# join the geodataframe with the cleaned up csv dataframe
merged = map_df.set_index('DIST_NAME').join(data_for_map.set_index('DIST'))
merged.head()

# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(10, 6))

# create map
merged.plot( cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')

# remove the axis
ax.axis('off')

# add a title
ax.set_title('Heat map of Rajasthan(Population)', fontdict={'fontsize': '25', 'fontweight' : '3'})

# create an annotation for the data source
ax.annotate('Source: Rajasthan Datastore, 2011',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')

# set the range for the choropleth
vmin, vmax = 120, 220

# Create colorbar as a legend
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))

# empty array for the data range
sm._A = []

# add the colorbar to the figure
cbar = fig.colorbar(sm)
fig.savefig('map_export.png', dpi=300)
