sudo apt install default-jdk curl -y

wget -q O - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb http://packages.elastic.co/elasticsearch/7.x/debian stable main" | sudo tee -a /etc/apt/sources.list.d/elasticsearch-7.x.list
sudo apt update

sudo apt install elasticsearch -y
sudo systemctl daemon-reload
sudo systemctl enable elasticsearch.service
sudo systemctl start elasticsearch.service

sudo apt install logstash -y
sudo systemctl daemon-reload
sudo systemctl enable logstash.service
sudo systemctl start logstash.service

sudo apt install kibana -y
sudo systemctl daemon-reload
sudo systemctl enable kibana.service
sudo systemctl start kibana.service

#sudo apt install metricbeat -y
#sudo service metricbeat start
