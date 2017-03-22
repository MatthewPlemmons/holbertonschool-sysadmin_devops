# Run sed to edit line in file 'wp-settings.php'.
exec { "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' wp-settings.php":
  command => 'sed',
  cwd     => '/var/www/html',
  path    => ['/usr/bin', '/usr/sbin']
}
