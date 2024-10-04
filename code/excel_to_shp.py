
import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
fp ="D:\Projects\precipitation_AUS\dataset\18MArch2021\18MArch2021.xlsx"
st_df = pd.read_excel(fp)

# Assuming df is your existing DataFrame with 'longitude' and 'latitude' columns

gdf = gpd.GeoDataFrame(
    st_df , geometry= gpd.points_from_xy(st_df.LONGITUDE, st_df.LATITUDE))
of = "D:\Projects\precipitation_AUS\dataset\18MArch2021\shp\18MArch2021.shp"
gdf.to_file( of)





