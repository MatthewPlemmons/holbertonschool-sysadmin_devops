# run sed to edit line in file wp-settings.php
exec { 'sed':
  command => "sed -i 's/phpp/php/' wp-settings.php",
  cwd     => '/var/www/html',
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
