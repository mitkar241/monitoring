curl -s https://packagecloud.io/install/repositories/sensu/stable/script.deb.sh | sudo bash
sudo apt install sensu-go-cli -y
sensuctl configure --non-interactive --url http://controller.mitkar.io:8080 --format tabular --namespace default --username raktim --password 12345678
sensuctl config view
