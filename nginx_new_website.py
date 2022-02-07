import os
import shutil
import errno

path_www = '/var/www/'
sites_enable = '/etc/nginx/sites-enabled/'

name_web = input('Digit the name of the directory of the website: ')
new_dir_web = path_www + name_web

try:
    os.mkdir(new_dir_web)
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass


default_nginx = sites_enable + 'default'

shutil.copyfile(default_nginx, sites_enable + name_web)

