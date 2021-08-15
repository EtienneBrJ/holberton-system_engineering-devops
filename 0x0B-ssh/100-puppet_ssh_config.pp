# set up your client SSH configuration file
file_line { 'Declare identity file':
  path    => '/etc/ssh/config',
  line    => '    IdentityFile ~/.ssh/holberton',
  ensure => present,
}

file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/config',
  line    => '    PasswordAuthentication no',
  ensure => present,
}