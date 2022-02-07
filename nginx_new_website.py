import os
import shutil
import errno


# Working on Ubuntu 16.04 18.04 20.04
# Path of the directories
path_www = '/var/www/'
sites_enable = '/etc/nginx/sites-enabled/'

# Digit the name of the new website
name_web = input('Digit the name of the directory of the website: ')
new_dir_web = path_www + name_web

# make the new directory called with the name thtat the user has putted into the shell
try:
    os.mkdir(new_dir_web)
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass

# Copy the conf nginx for the new website
default_nginx = sites_enable + 'default'
shutil.copyfile(default_nginx, sites_enable + name_web)

conf_file = open(sites_enable + name_web, 'w') 

with conf_file as line:
    line.truncate()



