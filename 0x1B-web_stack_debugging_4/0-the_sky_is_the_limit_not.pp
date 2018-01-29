exec { 'change-max-open-files':
  cwd     => '/etc/default/',
  command => 'echo "ULIMIT=\"-n 5000\"" > nginx',
  path    => '/usr/local/bin/:/bin/',
}

exec { 'restart nginx':
  command => 'service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}