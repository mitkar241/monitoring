##########
# sensu-backend
##########
cd
git clone https://github.com/raktimhalder241/monitoring.git
cd monitoring/sensu/scripts/
sudo bash sensu-backend.sh
cd
rm -rf monitoring/

##########
# sensuctl
##########
cd
git clone https://github.com/raktimhalder241/monitoring.git
cd monitoring/sensu/scripts/
sudo bash sensuctl.sh
cd
rm -rf monitoring/

##########
# influxdb
##########
cd
git clone https://github.com/raktimhalder241/database.git
cd database/InfluxDB/scripts
sudo bash influxdb.sh
cd
rm -rf database/
#sudo sed -i '/# bind-address = "127.0.0.1:8088"/c\bind-address = "127.0.0.1:8090"' /etc/influxdb/influxdb.conf
#sudo service influxdb restart

##########
# grafana-server
##########
cd
git clone https://github.com/raktimhalder241/monitoring.git
cd monitoring/Grafana/scripts/
sudo bash grafana-server.sh
cd
rm -rf monitoring/
sudo sed -i '/;http_port = 3000/c\http_port = 4000' /etc/grafana/grafana.ini
sudo service grafana-server restart
#<<
#;http_port = 3000
#---
#http_port = 4000
#>>>
