import re
import os

src_path = './sources'
manifest_file = src_path + '/manifest.json'
versions_path = './versions'

print('Manifest: ' + manifest_file)

def extract_version(manifest_file_name):
    try:
        f = open(manifest_file_name, 'r')
        for line in f.readlines():
            m = re.match('\s*"version"\s*:\s*"([\d\.]+)"', line)
            if(m):
                return m.group(1)
    except:
        return ''

        
ver = extract_version(manifest_file)
if(not ver):
    print('Error reading manifest file or version not defined.')
    exit(1)

if(not os.path.exists(versions_path)):
    os.makedirs(versions_path)
    
    
print('Building version ' + ver)
cmd = '7za a -tzip -r -xr!.svn* %s/b23_%s.zip %s/*' % (versions_path, ver, src_path);
print(cmd)
os.system(cmd)
