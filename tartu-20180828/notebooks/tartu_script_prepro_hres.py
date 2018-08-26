from multiply_data_access import DataAccessComponent
data_access_component = DataAccessComponent()
data_access_component.show_stores()
data_access_component.get_provided_data_types()
BARRAX_ROI = "POLYGON((-2.20397502663252 39.09868106889479,-1.9142106223355313 39.09868106889479," \
             "-1.9142106223355313 38.94504502508093,-2.20397502663252 38.94504502508093," \
             "-2.20397502663252 39.09868106889479))"
start_time = '2017-05-05'
end_time = '2017-05-25'
s2_data_infos = data_access_component.query(BARRAX_ROI, start_time, end_time, 'AWS_S2_L1C')
print(s2_data_infos)
s2_urls = data_access_component.get_data_urls_from_data_set_meta_infos(s2_data_infos)
print(s2_urls)
emu_urls = data_access_component.get_data_urls(BARRAX_ROI, start_time, end_time, 'ISO_MSI_A_EMU,ISO_MSI_B_EMU,WV_EMU')
print(emu_urls)
wv_emu_url = data_access_component.get_data_urls(BARRAX_ROI, start_time, end_time, 'WV_EMU')[0]
print(wv_emu_url)
aster_dem_url = data_access_component.get_data_urls(BARRAX_ROI, start_time, end_time, 'AsterDEM')[0]
print(aster_dem_url)
cams_urls = data_access_component.get_data_urls(BARRAX_ROI, '2017-05-05', '2017-05-25', 'CAMS')
# cams_urls.extend(data_access_component.get_data_urls(BARRAX_ROI, '2017-06-08', '2017-06-08', 'CAMS'))
print(cams_urls)
modis_start_time = '2017-05-02'
modis_end_time = '2017-05-28'
modis_urls = data_access_component.get_data_urls(BARRAX_ROI, modis_start_time, modis_end_time, 'MCD43A1.006')
print(modis_urls)
import os
working_dir = '/home/user/m4/'
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
s2_l2_dir = '{}/s2_l2'.format(working_dir)
create_dir(s2_l2_dir)
from multiply_orchestration import create_sym_links
create_sym_links(s2_urls, s2_l1c_dir)
create_sym_links(emu_urls, emus_dir)
create_sym_links(cams_urls, cams_dir)
create_sym_links(modis_urls, modis_dir)

import glob
s2_dirs = glob.glob(s2_l1c_dir + "/*/*/*/*/*/*/*")

for s2_dir in s2_dirs:
    input_parts = s2_dir.split('/')
    s2_l2_product_name = 'S2-{}{}{}'.format(input_parts[-4], input_parts[-3], input_parts[-2])

    processor_dir = '/software/atmospheric_correction-0.8/multiply_atmospheric_corection'
    os.system("sudo ln -s "+processor_dir+"/data ./data")
    command = "PYTHONPATH=$PYTHONPATH:" + processor_dir + "/util python " + processor_dir + "/Sentinel2_AtmoCor.py -f " + s2_dir + "/ -m " + modis_dir + " -e " + emus_dir + " -c " + cams_dir + " -w " + wv_emu_url + " -d " + aster_dem_url
    os.system(command)
    s2_l2_product_dir = s2_l2_dir + "/" + s2_l2_product_name
    create_dir(s2_l2_product_dir)
    os.system('sudo cp -b ' + s2_dir + '/metadata.xml ' + s2_l2_product_dir)
    os.system("rm $(find "+s2_dir+" -type l)")
    os.system('mv ' + s2_dir + '/* ' + s2_l2_product_dir)
# data_access_component.put(s2_l2_product_dir)
# maybe later for cleanup
# os.system("rm -rf "+s2_dir)
# os.system("sudo rm $(find . -type l)")
