#!/usr/bin/env python

import sys

current_title = None
current_count = 0
title = None
sum = 0
limit = 100000
# limit = 0
datecounts={}
for x in range(20141101, 20141131):
	datecounts[str(x)]=int(0)
for line in sys.stdin:
	line = line.strip()
	title,date,count=line.split("\t")
	try:
		count = int(count)
	except ValueError:
		continue
	date = str(date)
	if current_title == title:
		sum += count
 		datecounts[date] += count
 	else: 
		if current_title and sum>limit:
			print str(sum) + "\t" + current_title + "\t",
			for key in sorted(datecounts):
				print "%s:%s\t" % (key, datecounts[key]),
			print ""

		current_title = title
		sum = count
		datecounts.clear()
		for x in range(20141101, 20141131):
			datecounts[str(x)]=int(0)
        	datecounts[date] = count

if current_title and sum>limit:
		print str(sum) + "\t" + current_title + "\t",
		for key in sorted(datecounts):
			print "%s:%s\t" % (key, datecounts[key]),
		print ""
	
