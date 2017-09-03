#CODED BY NATE J, 2017. Do not use for malicious purposes. 
#Based for use on Kali Linux, but can be run on any Linux OS with python2 and pygeoip (obtainable via pip)
import os
os.system("wget -N -q http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz")
os.system("gzip -d GeoLiteCity.dat.gz")
print("Database downloaded")
print("Installing Dependancies")
os.system("wget http://pygeoip.googlecode.com/files/pygeoip-0.1.3.zip")
os.system("pip install pygeoip")
os.system("wget http://svn.python.org/projects/sandbox/trunk/setuptools/ez_setup.py")
os.system("wget http://pypi.python.org/packages/2.5/s/setuptools-0.6c11-py2.5.egg")
os.system("pip install setuptools")
import pygeoip
gip = pygeoip.GeoIP('GeoLiteCity.dat')
print("Setup complete. Ready to query.")
raw_input("Please press enter to begin.")
os.system("clear")
while True:
	IP = str(raw_input("IP address: "))
	rec = gip.record_by_addr(IP)
	for key,val in rec.items():
		print(str(key)+": "+str(val))
	print("\n")
