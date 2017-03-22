# Run sed to edit line in file 'wp-settings.php'.
exec { "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' var/www/html/wp-settings.php"
  command => 'sed'
}
