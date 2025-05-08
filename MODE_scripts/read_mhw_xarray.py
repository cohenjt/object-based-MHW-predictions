import numpy as np
import xarray as xr
import pandas as pd
import cftime
import os
import sys

print("Python Script:\t" + repr(sys.argv[0]))
if len(sys.argv) != 4:
    print('ERROR: read_mhw_xarray.py -> Must specify exactly one input file and a name for the data.')
    sys.exit(1)

# Read the input file as the first argument
input_file, init, valid, shift_right = sys.argv[1].split(':')
data_name = sys.argv[2]
level = sys.argv[3]
name_opts = ['FCST', 'OBS']
if not np.isin(data_name, name_opts):
    print('ERROR: data_name must be FCST or OBS')
    sys.exit(1)

try:
    # Print some output to verify that this script ran
    # print("Input File:\t" + repr(input_file))
    # print("Data Name:\t" + repr(data_name))
    input_data = xr.open_dataset(input_file)['TEMP']
    # print("Data Shape:\t" + repr(input_data.shape))
    # print("Data Type:\t" + repr(input_data.dtype))
except NameError:
    print(NameError)
    print("Can't find the input file.")

t_init_pd = pd.to_datetime(init, format='%Y%m%d')
t_init = cftime.datetime(
    t_init_pd.year,
    t_init_pd.month,
    t_init_pd.day,
    calendar='noleap')
t_valid_pd = pd.to_datetime(valid, format='%Y%m%d')
t_valid = cftime.datetime(
    t_valid_pd.year,
    t_valid_pd.month,
    t_valid_pd.day,
    calendar='noleap')
lead = (t_valid_pd.to_period('M') - t_init_pd.to_period('M')).n

if data_name == 'OBS':
    level = 'Surface'
    met_data = input_data.sel(time=t_valid)
    name_str = 'Observed'
else:
    met_data = input_data.sel(
        init=init, lead=lead).squeeze(
        dim='init').transpose(
        'member', 'lat', 'lon')
    met_data['member'] = [f'm{m.values:02d}' for m in met_data['member']]
    met_data = met_data.sel(member=level)
    name_str = 'Forecast'

grid_info = {
    'type': 'LatLon',
    'name': '1deg',
    'Nlat': 180,
    'Nlon': 360,
    'lat_ll': -89.5,
    'lon_ll': 20.5,  # this only applies for shift_right = 160
    'delta_lat': 1.,
    'delta_lon': 1.
}
attrs = {
    'valid': valid,
    'init': init,
    'lead': f'0000{lead:02d}',
    'accum': '000000',
    'name': 'TEMP',
    'long_name': f'{name_str} marine heatwave sea surface temperatures',
    'level': level,
    'units': 'degrees_Celsius',
    'grid': grid_info
}
met_data = met_data.roll(
    lon=int(shift_right), roll_coords=True).reindex(
    lat=list(reversed(met_data.lat)))
met_data.attrs = attrs
