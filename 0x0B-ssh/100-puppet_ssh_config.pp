# ssh configuration file

file{ 'ssh configuration':
  ensure  => file,
  path    => '~/.ssh',
  content => PasswordAuthentication no,
}

file { 'identity file':
  ensure  => file,
  content => 'IdentityFile ~/.ssh/school',
  path    => '~/.ssh',
}