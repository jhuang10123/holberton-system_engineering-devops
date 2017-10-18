#!/usr/bin/env ruby
# regex matching string start with "h" end with "n" w/ 1 character in middle
puts ARGV[0].scan(/h.n/).join
