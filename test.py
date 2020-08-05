import geopandas
import plotly
import matplotlib
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

print(world.head())

world = world[(world.pop_est>0) & (world.name!="Antarctica")]

world['gdp_per_cap'] = world.gdp_md_est / world.pop_est

world.plot(column='gdp_per_cap');