#!/usr/bin/env ruby
=begin
   Ruby script
   Requirements: The regular expression must match School
   accepts one argument and pass it to a regular expression matching method
=end
puts ARGV[0].scan(/^\d{10}/).join
