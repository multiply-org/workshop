from multiply_data_access import DataAccessComponent
import yaml
data_access_component = DataAccessComponent()
data_access_component.show_stores()
data_access_component.get_provided_data_types()
BARRAX_ROI = "POLYGON((-2.20397502663252 39.09868106889479,-1.9142106223355313 39.09868106889479," \
             "-1.9142106223355313 38.94504502508093,-2.20397502663252 38.94504502508093," \
             "-2.20397502663252 39.09868106889479))"
start_time = '2017-01-01'
end_time = '2017-01-20'
# s2_data_infos = data_access_component.query(BARRAX_ROI, start_time, end_time, 'AWS_S2_L1C')
# print(s2_data_infos)
# s2_urls = data_access_component.get_data_urls_from_data_set_meta_infos(s2_data_infos)
# print(s2_urls)
# emu_urls = data_access_component.get_data_urls(BARRAX_ROI, start_time, end_time, 'ISO_MSI_A_EMU,ISO_MSI_B_EMU,WV_EMU')
# print(emu_urls)
# wv_emu_url = data_access_component.get_data_urls(BARRAX_ROI, start_time, end_time, 'WV_EMU')[0]
# print(wv_emu_url)
# aster_dem_url = data_access_component.get_data_urls(BARRAX_ROI, start_time, end_time, 'AsterDEM')[0]
# print(aster_dem_url)
# cams_urls = data_access_component.get_data_urls(BARRAX_ROI, '2017-1-16', '2017-1-16', 'CAMS')
# cams_urls.extend(data_access_component.get_data_urls(BARRAX_ROI, '2017-1-19', '2017-1-19', 'CAMS'))
# print(cams_urls)
# modis_start_time = '2017-01-13'
# modis_end_time = '2017-01-22'
# modis_urls = data_access_component.get_data_urls(BARRAX_ROI, modis_start_time, modis_end_time, 'MCD43A1.006')
# print(modis_urls)
import os
working_dir = '/home/user/m1/'
def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
create_dir(working_dir)
# s2_l1c_dir = '{}/s2_l1c'.format(working_dir)
# create_dir(s2_l1c_dir)
# emus_dir = '{}/emus'.format(working_dir)
# create_dir(emus_dir)
# cams_dir = '{}/cams'.format(working_dir)
# create_dir(cams_dir)
# modis_dir = '{}/modis'.format(working_dir)
# create_dir(modis_dir)
# s2_l2_dir = '{}/s2_l2'.format(working_dir)
# create_dir(s2_l2_dir)
# from multiply_orchestration import create_sym_links
# create_sym_links(s2_urls, s2_l1c_dir)
# create_sym_links(emu_urls, emus_dir)
# create_sym_links(cams_urls, cams_dir)
# create_sym_links(modis_urls, modis_dir)

# import glob
# s2_dirs = glob.glob(s2_l1c_dir + "/*/*/*/*/*/*/*")

# processor_dir = '/software/atmospheric_correction-0.8/multiply_atmospheric_corection'
# os.system("sudo ln -s "+processor_dir+"/data ./data")
# command = "PYTHONPATH=$PYTHONPATH:" + processor_dir + "/util python " + processor_dir + "/Sentinel2_AtmoCor.py -f " + s2_dirs[0] + "/ -m " + modis_dir + " -e " + emus_dir + " -c " + cams_dir + " -w " + wv_emu_url + " -d " + aster_dem_url
# print(command)
# os.system(command)
# os.system("rm $(find "+s2_l1c_dir+" -type l)")
# os.system("mv "+s2_l1c_dir+" "+s2_l2_dir+"/" + s2_l2_product_name)
# exchange this with call to data access component
# os.system("rm -rf "+s2_l2_dir)
# os.system("rm $(find . -type l)")
from multiply_prior_engine import PriorEngine
import datetime
time = start_time
configuration_file='{}/config.yaml'.format(os.getcwd())
with open(configuration_file) as config_file:
    parameters = yaml.load(config_file)
variables = 'n, cab, car, cbrown, cw, cm, lai, ala, bsoil, psoil'
while time<=end_time:
    print(time)
    PE = PriorEngine(config=configuration_file, datestr=time.strftime('%Y-%m-%d'), variables=variables)
    priors = PE.get_priors()
    time = time + datetime.timedelta(days=1)
priors_dir = '{}/priors'.format(working_dir)
create_dir(priors_dir)
os.system("mv *.vrt " +priors_dir+"/")

ptype = parameters['Prior']['sm']
if 'climatology' in ptype:
    soil_moisture_dir = parameters['Prior']['sm']['climatology']['climatology_dir']
else:
    soil_moisture_dir = parameters['Prior']['General']['directory_data']
os.system("mv " + soil_moisture_dir + "/*.vrt " + priors_dir + "/")

# inference_engine_dir = '/software/inference-engine-0.4/multiply_inference_engine'
# s2_emulators_dir = '/data/archive/emulators/s2_prosail'
# inference_type = 'high'
# state_mask = parameters['General']['state_mask']

# biophys_dir = '{}/biophys'.format(working_dir)
# create_dir(biophys_dir)
# previous_state = '{}/state/2017-01-01'.format(working_dir)
# create_dir(previous_state)
# next_state = '{}/state/2017-01-10'.format(working_dir)
# create_dir(next_state)
#
# inference_engine_call = ( "python "+processor_dir+"/inference_engine.py"
#           + " -s " + str(start_time)
#           + " -e " + str(end_time)
#           + " -i " + inference_type
#           + " -em " + s2_emulators_dir
#           + " -p " + variables
#           + ((" -ps " + previous_state) if previous_state != 'none' else "")
#           + " -pd " + priors_date_dir
#           + " -d " + sdrs_rootdir_list
#           + " -sm " + state_mask
#           + " -o " + biophys_dir
#           + " -ns " + next_state )
# print(inference_engine_call)
# os.system(inference_engine_call)
