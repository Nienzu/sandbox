# -*- coding: utf-8 -*-
"""
name: Peter
student number:F74027036
description:
This is Homework 4 for TOC class.
This program consist in finding the top-k degree nodes
with a positive integer k as an input argument.
"""

import sys
import csv

num = sys.argv[1];

word = {"" : 0}

file = open(sys.argv[2],'r')
while 1:
	string=file.readline()
	if not string:break
	temp=string.split('\t')
	
	if word.has_key(temp[0]):
		word[temp[0]] += 1;
	else:
		word[temp[0]] = 1;
	
	if word.has_key(temp[2][:-1]):
		word[temp[2][:-1]] += 1;
	else:
		word[temp[2][:-1]] = 1;

word = sorted(word.iteritems(), key=lambda a:a[1], reverse = True)

i=0
degree = -1
while 1:
	if int(num) == 0:
		break
	print word[i][0] + "," + str(word[i][1])
	degree = int(word[i][1])
	i+=1
	if i >= int(num):
		if degree != int(word[i][1]):
			break
