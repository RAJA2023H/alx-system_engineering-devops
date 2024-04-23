# Remove existing Flask and Werkzeug packages, and install Flask version 2.1.0i
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
