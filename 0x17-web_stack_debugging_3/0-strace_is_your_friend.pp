# Automate the fix for the 500 error caused by a typo in the WordPress configuration

exec { 'Correct WordPress configuration typo':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}

