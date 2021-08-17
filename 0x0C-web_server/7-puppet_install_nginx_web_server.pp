# Installs Nginx server with redirect_me (oops)

package {'nginx':
  provider => present,
}

file { '/var/www/html/index.html':
  content => 'Holberton School'
}

file_line { 'add redirect_me':
  path => '/etc/nginx/sites-available/default',
  after => 'listen 80 default server;',
  line => 'rewrite ^/redirect_me https://github.com/EtienneBrJ permanent;,
}

exec { 'restart':
  command => 'service nginx restart'
  provider => 'shell',
}
