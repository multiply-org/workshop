#!/usr/bin/python

import json
import os
import subprocess
import sys

in_dir = sys.argv[1]
data_type = sys.argv[2]
out_dir = sys.argv[3]
out_name = sys.argv[4]
dir_content = os.listdir(in_dir)
datasets = {}
dataset_list = []
for path in dir_content:
    if os.path.isfile(in_dir + '/' + path):
        dataset = {}
        dataset['data_type'] = data_type
        dataset['name'] = path
        # result = subprocess.check_output(['gpt Info', in_dir + '/'+ path])
        # result = os.popen('gpt Info' + in_dir + '/'+ path)
        # result = os.system('gpt Info '+  in_dir + '/'+ path)
        result = subprocess.check_output(['./', 'gpt', 'Info', in_dir + '/'+ path])
        # read = result.read()
        info_data = result.decode('utf-8').split('\r\n')
        start_time = info_data[0].split('=')[1]
        if not start_time == 'null':
            dataset['start_time'] = start_time
        end_time = info_data[1].split('=')[1]
        if not end_time == 'null':
            dataset['end_time'] = start_time
        spatial_coverage = info_data[2].split('=')[1]
        dataset['spatial_coverage'] = spatial_coverage
        dataset_list.append(dataset)
datasets['datasets'] = dataset_list
with open(out_dir +'/' + out_name, 'w') as out_file:
    json.dump(datasets, out_file)