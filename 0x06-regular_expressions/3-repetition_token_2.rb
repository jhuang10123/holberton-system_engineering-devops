#!/usr/bin/env ruby
# regex matching at least 1 "t" in "hbtn"
puts ARGV[0].scan(/hbt+n/).join
