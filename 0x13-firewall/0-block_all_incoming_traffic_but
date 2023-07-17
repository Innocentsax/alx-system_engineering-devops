sudo apt-get -y update
sudo apt-get -y install ufw
sudo ufw disable
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo systemctl stop ufw
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp
sudo ufw allow 80/tcp
sudo ufw enable
