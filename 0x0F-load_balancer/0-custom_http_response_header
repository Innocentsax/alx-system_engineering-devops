#!/usr/bin/env bash
# configures a new Ubuntu machine

# Install nginx on web-01 server
apt-get -y update
apt-get -y install nginx

# Add custom response header to know the server name for debugging
HOST_NAME=$(hostname)
HEADER="\\\n\tadd_header X-Served-By $HOST_NAME;\n"
FIND=$(grep "X-Server-by" /etc/nginx/sites-available/default)
if [[ -z $FIND ]]; then
    sed -i "23i $HEADER" /etc/nginx/sites-available/default
fi

# Create a firts index.html page
echo "Hello World!" > /var/www/html/index.html

# Add to the nginx configuration file a redirection to another page
FIND=$(grep "redirect_me" /etc/nginx/sites-available/default)
STRING="\\\n\tlocation /redirect_me {\n\t\t return 301 https://www.youtube.com/watch?v=3MbaGJN2ioQ;\n\t}\n"
if [[ -z $FIND ]]; then
    sed -i "42i $STRING" /etc/nginx/sites-available/default
fi

# Add to the nginx configuration file a error page 404
FIND=$(grep "error_page 404" /etc/nginx/sites-available/default)
ERROR="\\\n\terror_page 404 /custom_404.html;\n"
if [[ -z $FIND ]]; then
    echo "Ceci n'est pas une page" > /var/www/html/custom_404.html
    sed -i "40i $ERROR" /etc/nginx/sites-available/default
fi

service nginx restart
