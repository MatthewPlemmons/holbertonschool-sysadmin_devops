# puppet script to configure nginx
exec { '/etc/default/nginx':
  command => '/bin/echo "ULIMIT=\'-n 4096\'" > /etc/default/nginx &&
  /etc/init.d/nginx restart',
}