# Installs Nginx server with redirect_me
package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Holberton School'
}

file_line { 'add redirect_me':
  path => '/etc/nginx/sites-available/default',
  after => 'listen 80 default server;',
  line => 'rewrite ^/redirect_me https://github.com/EtienneBrJ permanent;',
}

package { 'nginx':
  hasrestart => true,
  require => Package['nginx],
}