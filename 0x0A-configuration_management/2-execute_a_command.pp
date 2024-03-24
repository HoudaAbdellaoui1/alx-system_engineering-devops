# Execute kill me now process

exec { 'kill_killmenow_process':
    path    => '/bin/',
    command => 'pkill killmenow',
}
