exec { 'change-max-open-files':
     cwd => '/etc/default/',
     command => 'echo "ULIMIT=\"-n 5000\"" > nginx',
     path    => '/usr/local/bin/:/bin/',
}