# Run sed to edit line in file 'wp-settings.php'.
exec { "sed":
  command => "sed -i 's/locale.phpp/locale.php/' wp-settings.php",
  cwd     => "/var/www/html",
  path    => ["/bin", "/usr/bin", "/usr/sbin"]
}
