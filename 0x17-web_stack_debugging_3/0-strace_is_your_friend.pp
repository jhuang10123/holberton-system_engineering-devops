# fixing type in wp-settings.php
exec { 'remove typo':
    cwd     => '/var/www/html',
    command => '/bin/sed -i -e "s/.phpp/.php/g" wp-settings.php',
}