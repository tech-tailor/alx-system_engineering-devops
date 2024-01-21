# ssh configuration file

file{ 'ssh configuration':
  path => '~/.ssh',
  ensure => file,
  content => PasswordAuthentication no,
}

file { 'identity file':
  ensure => file,
  content => 'IdentityFile ~/.ssh/school'
  path => '~/.ssh',
}