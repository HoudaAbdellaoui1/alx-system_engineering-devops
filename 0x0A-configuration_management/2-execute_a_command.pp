# Execute kill me now process
exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill killmenow',
  refreshonly => true,
}
