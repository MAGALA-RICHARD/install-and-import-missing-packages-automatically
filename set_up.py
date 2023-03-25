'''
-*- coding: utf-8 -*-
parks_provision_18.py
Richard Magala, rmagala@iastate.edu
November 14, 2022
This program checks whether a specified package is loaded or is with the python excutable path
if the package is not loaded, it is installed. Then, imported if it is not imported successfully that means it was not installed, the program will exit
The program was tested on python version Version- 3.9.11 in windows

'''


import subprocess
import sys
import importlib
import os
import pkgutil
# Function to check if a apackage is loaded in the exctable path
def check_if_package_Loaded(package):
  load_package  = pkgutil.find_loader(package)
  if load_package != None:
    value = True
    return value
# check if the package is loaded, then install it
# This is just an example some of these packages are part of the python standard library but this depends on which version of python you are using
# Any package not found in the excutable path will be installed and tested for successfully being installed by trying to import it
for pkg in ['xmltodict', 'urllib', 'scipy', 'pandas', 'numpy', 'requests', 'winsound', 'platform']:
  if check_if_package_Loaded(pkg) !=True:
    # the safest way to install a package inside a script is to use the subprocess module
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg])
    print(f'{pkg} was installed successfully')
    # try to import the package
    try:
      globals()[pkg] = importlib.import_module(pkg)
    # print the success
      print(f'{pkg} originally not installed has been imported successfully')
    except ModuleNotFoundError:
      print(f'Package {pkg} was not installed successfully or is not suppored, Exiting the program........')
      sys.exit(1)
 # old code ignore 
# try:
#   globals()[pkg] = importlib.import_module(pkg)
#   print(f"{pkg} imported successfully")
# except ImportError:
#   #if package not found we install it
#   subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'urllib'])
#   print(f'{pkg} was installed successfully')
#   # import it again
#   globals()[pkg] = importlib.import_module(pkg)
#   # print the success
#   print(f'{pkg} originally not install has been imported successfully')
#   

#End************************************************************************


# try:
#  import xmltodict
# except ImportError:
#  from pip._internal import main as pip
#  pip(['install', '--user', 'xmltodict'])
#  import xmltodict
#  
# import pkg_resources
# installed_packages = pkg_resources.working_set
# installed_packages_list = sorted(["%s==%s" % (i.key, i.version)\
#    for i in installed_packages])
# print(installed_packages_list)





  

