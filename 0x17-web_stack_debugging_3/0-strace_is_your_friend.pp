# Fix in wp-settings.php
exec { 'settings' :
provider => shell,
command  => 'sed -i "s/\b.phpp\b/.php/g" /var/www/html/wp-settings.php'
}
