sudo apt install default-jre -y

curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
sudo apt update
sudo apt install elasticsearch -y
sudo systemctl daemon-reload
sudo systemctl enable elasticsearch.service
sudo systemctl start elasticsearch.service

echo "deb http://packages.elastic.co/kibana/4.5/debian stable main" | sudo tee -a /etc/apt/sources.list.d/kibana-4.5.x.list
sudo apt update
sudo apt install kibana -y
sudo systemctl daemon-reload
sudo systemctl enable kibana.service
sudo systemctl start kibana.service

echo 'deb http://packages.elastic.co/logstash/2.2/debian stable main' | sudo tee /etc/apt/sources.list.d/logstash-2.2.x.list
sudo apt update
sudo apt install logstash -y
sudo systemctl daemon-reload
sudo systemctl enable logstash.service
sudo systemctl start logstash.service

sudo apt install metricbeat -y
sudo service metricbeat start
