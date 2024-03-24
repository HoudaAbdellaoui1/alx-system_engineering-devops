# Execute kill me now process
exec { 'kill_killmenow_process':
  command  => 'pkill killmenow',
  provider => 'shell',
  refreshonly => true,
}
