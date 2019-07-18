
####How To Install and configure Nginx

sudo apt-get update

sudo apt-get install nginx

sudo ufw enable

nginx -v

sudo ufw app list

sudo ufw allow 'Nginx Full'

sudo ufw allow 'Nginx HTTP'

sudo ufw allow 'Nginx HTTPS'

sudo ufw status

sudo systemctl status nginx
