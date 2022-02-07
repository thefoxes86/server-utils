import os
import shutil

dir_web = input('Digit the name of the directory of the website: ')
dir_web = '/Users/thefoxes86/Desktop/' + dir_web

os.mkdir(dir_web)

default_nginx = '/etc/nginx/sites-enables/default'

