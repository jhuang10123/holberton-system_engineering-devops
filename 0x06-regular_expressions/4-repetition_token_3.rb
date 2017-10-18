#!/usr/bin/env ruby
# regex matching "htn" or "hbtn" w/ varied # of "t"
puts ARGV[0].scan(/htn|hbt+n/).join
