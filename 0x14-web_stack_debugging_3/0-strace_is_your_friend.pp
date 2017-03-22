# Run sed to edit line in file 'wp-settings.php'.
exec { "sed -i 's/locale.phpp/locale.php/' wp-settings.php":
  command => 'sed',
  cwd     => '/var/www/html',
  path    => ['/usr/bin', '/usr/sbin']
}
