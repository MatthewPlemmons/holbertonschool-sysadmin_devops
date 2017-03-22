# Run sed to edit line in file 'wp-settings.php'.
exec { "sed":
  command => "sed -ie 's/locale.phpp/locale.php/' /var/www/html/wp-settings.php",
  path    => ["/bin", "/usr/bin", "/usr/sbin"]
}
