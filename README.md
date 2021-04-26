# cdm-lens-locust-tester
Locust load tests for cdm-lens app

## Example setup and usage

```
cd /vagrant-shares/ceda-wps/
. ./setup-env.sh

cd cdms-lens-locust-tests/
locust -f tests/swarm/locustfile.py
```

Then go to browser:

http://192.168.50.70:8089/

Specify (in browser form):

Number of total users to simulate: 10
Swarm rate: 2
http://glamod2.ceda.ac.uk

