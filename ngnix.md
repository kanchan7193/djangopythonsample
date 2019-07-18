
###How To Install and configure Nginx


```
sudo apt-get update
```
```
sudo apt-get install nginx
```
```
sudo ufw enable
```
```
nginx -v
```
```
sudo ufw app list
```
```
sudo ufw allow 'Nginx Full'
```
```
sudo ufw allow 'Nginx HTTP'
```
```
sudo ufw allow 'Nginx HTTPS'
```
```
sudo ufw status
```
```
sudo systemctl status nginx
```
```
sudo vi /etc/hosts
```
Make an entry of 

```
0.0.0.0 sample1.com
```

After that
```
sudo apt-get remove openssh-client openssh-server
sudo apt-get install openssh-client openssh-server
```

Copy your application
```
scp -r * 0.0.0.0:/var/www/sample-app-master
```
```
cd /etc/nginx
```
Create file
```
sudo vi sites-available/sample
```
Content
```
server {
listen 80 default_server;
listen [::] default_server;
root /var/www/sample-app-master;
index index.html;
server_name sample;
location / {
try_files $uri $uri/ =404;
}
}
```

symlink between available and enabled
```
sudo ln -s /etc/nginx/sites-available/sample /etc/nginx/sites-enabled/sample
```
remove default nginx folder
```
sudo mv /etc/nginx/sites-enabled/default ~/DjangoPythonSample/
```

restart nginx so we get our app running
```
sudo systemctl restart nginx
```

For future deploys only replace code using
```
scp -r * 0.0.0.0:/var/www/sample-app-master
```
Incase of major changes restart ngnix