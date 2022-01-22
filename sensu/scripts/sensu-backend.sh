curl -s https://packagecloud.io/install/repositories/sensu/stable/script.deb.sh | sudo bash
sudo apt install sensu-go-backend -y
sudo curl -L https://docs.sensu.io./sensu-go/latest/files/backend.yml -o /etc/sensu/backend.yml
sudo service sensu-backend start
sudo systemctl enable sensu-backend
#service sensu-backend status
# len(password) and len(api-key) >= 6
sensu-backend init --cluster-admin-username raktim --cluster-admin-password 12345678 --cluster-admin-api-key API12345678
