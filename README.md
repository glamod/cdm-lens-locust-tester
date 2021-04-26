cd /vagrant-shares/ceda-wps/
. ./setup-env.sh

cd cdms-lens-locust-tests/
locust -f tests/swarm/locustfile.py

Then go to browser:

http://192.168.50.70:8089/

Specify:

5 
5
glamod2.ceda.ac.uk


