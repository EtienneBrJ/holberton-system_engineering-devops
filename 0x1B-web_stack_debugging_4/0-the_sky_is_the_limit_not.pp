# Fix nginx limit request, set it to 2000 in the default file

exec { 'ULIMIT':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

exec { 'restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
