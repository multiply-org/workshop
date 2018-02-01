from multiply_data_access import DataAccessComponent

dac = DataAccessComponent()
dac.read_data_stores('frascati_data_stores.yml')
sm_dir = dac.get_data_urls('', '2017-01-01', '2017-01-10', 'SoilMoisture')
print(sm_dir)
veg_dir = dac.get_data_urls('', '2017-01-01', '2017-01-10', 'Vegetation')
print(veg_dir)
