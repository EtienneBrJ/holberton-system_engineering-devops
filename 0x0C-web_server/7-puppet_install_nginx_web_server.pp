# Installs Nginx server with redirect_me
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

file { '/var/www/html/index.html':
  content => 'Holberton School'
}

file_line { 'config':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default server;',
  line    => 'rewrite ^/redirect_me https://github.com/EtienneBrJ permanent;',
  require => Package['nginx'],
}

package { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
