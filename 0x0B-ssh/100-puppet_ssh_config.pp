file { '/root/.ssh/config': # Update the path if necessary
  ensure => present,
  mode   => '0600', # Set permissions to 600
  owner  => 'root', # Set owner to root
  group  => 'root', # Set group to root
  content => "\
# SSH client configuration
Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
}
