exec { 'change-max-open-files':
  cwd     => '/etc/default/',
  command => 'sudo sed -i "s/15/15000/" nginx',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

exec { 'restart nginx':
  command => 'service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}