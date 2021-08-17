# Installs Nginx server with redirect_me (oops)

exec {'install':
  provider => shell,
  command  => 'apt-get -y update ; apt-get -y install nginx ; ufw allow 80 ; echo "Holberton School" > /var/www/html/index.nginx-debian.html ; sed -i "/listen \[::\]:80 default_server;/a \\n    rewrite ^/redirect_me / permanent;" /etc/nginx/sites-available/default ; service nginx restart'
}