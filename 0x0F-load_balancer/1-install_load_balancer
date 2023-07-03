#!/usr/bin/env bash
# configures a new HAproxy as a load balancer

# Install HAproxy on a server
apt-get -y update
apt-get -y install haproxy=1.6.\*

# Configure haproxy configuration file to distribute requests using a roundrobin algorithm
echo '
frontend sammykingx.tech
        bind 0:80
        default_backend web_servers

backend web_servers
        balance roundrobin
        server 64820-web-01 100.26.152.157:80
        server 64820-web-02 52.86.102.6:80
' >> /etc/haproxy/haproxy.cfg

# Restart HAproxy service
service haproxy restart
