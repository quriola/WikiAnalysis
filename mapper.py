#!/usr/bin/env python

import sys
import os
import re
filename = os.environ["mapreduce_map_input_file"]
# filename="201306-gz/pagecounts-20130601-000000"
split = filename.split("-")
pattern = "^en\s(?!(404_error/|Main_Page|Hypertext_Transfer_Protocol|Search)\s)(?![a-z]|Media:|Special:|Talk:|User:|User_talk:|Project:|Project_talk:|File:|File_talk:|MediaWiki:|MediaWiki_talk:|Template:|Template_talk:|Help:|Help_talk:|Category:|Category_talk:|Portal:|Wikipedia:|Wikipedia_talk:)(.+)(?<!\.jpg|\.gif|\.png|\.JPG|\.GIF|\.PNG|\.txt|\.ico)\s(\d+)\s\d+$"
prog = re.compile(pattern)
for line in sys.stdin:
	line = line.strip()
	result=prog.match(line)
	if result:
		print '%s\t%s\t%s' % (result.group(2),split[2],result.group(3))
