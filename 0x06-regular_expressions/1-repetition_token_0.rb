#!/usr/bin/env ruby
# regex matching "hbtn" with 2-5 "t"s
puts ARGV[0].scan(/hbt{2,5}n/).join
