sudo apt install default-jdk curl -y

wget -q O - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb http://packages.elastic.co/elasticsearch/7.x/debian stable main" | sudo tee -a /etc/apt/sources.list.d/elasticsearch-7.x.list
sudo apt update

sudo apt install elasticsearch -y
#sudo vi /etc/elasticsearch/elasticsearch.yml
#network.host: localhost
sudo systemctl daemon-reload
sudo systemctl enable elasticsearch.service
sudo systemctl start elasticsearch.service
#http://localhost:9200

sudo apt install logstash -y
#sudo vi /etc/logstash/conf.d/covid_19.conf
#sudo /usr/share/logstash/bin/logstash --debug --path.settings /etc/logstash -f /etc/logstash/conf.d/covid_19.conf -t
sudo systemctl daemon-reload
sudo systemctl enable logstash.service
sudo systemctl start logstash.service
#http://localhost:9200/_cat/indices?v

sudo apt install kibana -y
#sudo vi /etc/kibana/kibana.yml
#network.host: localhost
sudo systemctl daemon-reload
sudo systemctl enable kibana.service
sudo systemctl start kibana.service
#http://localhost:5601

#sudo apt install metricbeat -y
#sudo service metricbeat start
