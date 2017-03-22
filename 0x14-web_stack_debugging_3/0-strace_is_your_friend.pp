# Run sed to edit line in file 'wp-settings.php'.
exec { "sed":
  command => "sed -i 's/locale.phpp/locale.php/' /var/www/html/wp-settings.php",
  cwd     => "/var/www/html",
  path    => ["/bin", "/usr/bin", "/usr/sbin"]
}
