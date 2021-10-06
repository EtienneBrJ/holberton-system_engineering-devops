# Set a new soft and hard value to the limit of max open files for holberton user

exec { 'change-max-open-files-hard-limit':
  command => "sed -i 's/holberton hard nofile 5/holberton hard nofile 1024/' /etc/security/limits.conf"
  path    => '/usr/local/bin/:/bin/'
}

exec { 'change-max-open-files-soft-limit':
  command => "sed -i 's/holberton soft nofile 4/holberton soft nofile 1024/' /etc/security/limits.conf"
  path    => '/usr/local/bin/:/bin/'
}
