# Run sed to edit line in file 'wp-settings.php'.
exec { "sed":
  command => "sed -ni 's/locale.phpp/locale.php/' wp-settings.php",
  cwd     => "/var/www/html",
  path    => ["/usr/bin", "/usr/sbin"]
}
