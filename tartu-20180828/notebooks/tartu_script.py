from multiply_data_access import DataAccessComponent
data_access_component = DataAccessComponent()
data_access_component.show_stores()
data_access_component.get_provided_data_types()
BARRAX_ROI = "POLYGON((-2.20397502663252 39.09868106889479,-1.9142106223355313 39.09868106889479," \
             "-1.9142106223355313 38.94504502508093,-2.20397502663252 38.94504502508093," \
             "-2.20397502663252 39.09868106889479))"
start_time = '2017-01-01'
end_time = '2017-01-20'
s2_data_infos = data_access_component.query(BARRAX_ROI, start_time, end_time, 'AWS_S2_L1C')
print(s2_data_infos)
s2_urls = data_access_component.get_data_urls_from_data_set_meta_infos(s2_data_infos)
print(s2_urls)
emu_urls = data_access_component.get_data_urls(BARRAX_ROI, start_time, end_time, 'ISO_MSI_A_EMU,ISO_MSI_B_EMU,WV_EMU')
print(emu_urls)
aster_dem_url = data_access_component.get_data_urls(BARRAX_ROI, start_time, end_time, 'Aster DEM')
print(aster_dem_url)
cams_urls = data_access_component.get_data_urls(BARRAX_ROI, '2017-1-16', '2017-1-16', 'CAMS')
cams_urls.extend(data_access_component.get_data_urls(BARRAX_ROI, '2017-1-19', '2017-1-19', 'CAMS'))
print(cams_urls)
modis_start_time = '2017-01-13'
modis_end_time = '2017-01-22'
modis_urls = data_access_component.get_data_urls(BARRAX_ROI, modis_start_time, modis_end_time, 'MCD43A1.006')
print(modis_urls)
import os
working_dir = 'E:/Produkte/multiply/working_dir/'
def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
create_dir(working_dir)
s2_l1c_dir = '{}/s2_l1c'.format(working_dir)
create_dir(s2_l1c_dir)
emus_dir = '{}/emus'.format(working_dir)
create_dir(emus_dir)
cams_dir = '{}/cams'.format(working_dir)
create_dir(cams_dir)
modis_dir = '{}/modis'.format(working_dir)
create_dir(modis_dir)
# from multiply_orchestration import create_sym_links