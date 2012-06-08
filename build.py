import os
import re
import json
import glob
import tarfile

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

archive_name = os.path.join(BUILD_PATH, "%s_%s.tar.gz" % (name, version))
print("Building package: %s..." % archive_name)

if(not os.path.exists(BUILD_PATH)):
    os.makedirs(BUILD_PATH)

with tarfile.open(archive_name, "w:gz") as tar:
    for file_name in glob.glob(os.path.join(SRC_PATH, "*")):
        print("  Adding %s..." % file_name)
        tar.add(file_name, os.path.basename(file_name))

print("Done.")

print("Building package: %s..." % archive_name)
archive_name = "%s_%s.zip" % (name, version)
cmd = "7za a -tzip -r -xr!.svn* %s\/%s %s\/*" % (BUILD_PATH, archive_name, SRC_PATH);
print(cmd)
os.system(cmd)
print("Done.")
