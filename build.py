import os
import re
import json
from pprint import pprint

SRC_PATH = './sources'
MANIFEST_FILE = SRC_PATH + '/manifest.json'
BUILD_PATH = './versions'

def get_extension_info(manifest_file):
    try:
        f = open(manifest_file, "rt")
        manifest = json.load(f)
        f.close()
        return manifest["name"], manifest["version"]

    except:
        print("Error reading manifest file or version not defined.")
        exit(1)


name, version = get_extension_info(MANIFEST_FILE)
name = re.sub(r"\s+", '-', name).lower()
print("Building %s %s..." % (name, version))

if(not os.path.exists(BUILD_PATH)):
    os.makedirs(BUILD_PATH)
    
cmd = "7za a -tzip -r -xr!.svn* %s\/%s_%s.zip %s\/*" % (BUILD_PATH, name, version, SRC_PATH);
print(cmd)
os.system(cmd)
