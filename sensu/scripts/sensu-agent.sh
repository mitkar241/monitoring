curl -s https://packagecloud.io/install/repositories/sensu/stable/script.deb.sh | sudo bash
sudo apt install sensu-go-agent -y
sudo curl -L https://docs.sensu.io/sensu-go/latest/files/agent.yml -o /etc/sensu/agent.yml
sudo nano /etc/sensu/agent.yml

#<<
##backend-url:
##  - "ws://127.0.0.1:8081"
#---
#backend-url:
#  - "ws://controller.mitkar.io:8081"
#>>
sudo sed -i '/backend-url/c\backend-url:' /etc/sensu/agent.yml
sudo sed -i '/127.0.0.1:8081/c\  - "ws://controller.mitkar.io:8081"' /etc/sensu/agent.yml

sudo service sensu-agent start
sudo systemctl enable sensu-agent
sudo service sensu-agent status
