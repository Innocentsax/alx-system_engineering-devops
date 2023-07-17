#!/usr/bin/env bash
# Running nginx as nginx and fixing port from 80 to 8080
pkill apache2
sed -i 's/80/8080/g' /etc/nginx/sites-available/default
chmod 644 /etc/nginx/nginx.conf
sudo -u nginx service nginx restart
