# Terminate a process called 'killmenow'.
exec { "pkill 'killmenow'":
  command => 'pkill'
}
