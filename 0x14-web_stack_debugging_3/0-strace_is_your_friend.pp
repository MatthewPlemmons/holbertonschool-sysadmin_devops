# run sed to edit line in file wp-settings.php
exec { 'sed':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
