#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import time
import sys
from bs4 import BeautifulSoup


def listupAnchor(html):
	soup = BeautifulSoup(html)
	list = []
	tags = soup.findAll('a')
	for tag in tags:
		try:
			href = tag["href"]
			list.append(href)
		except:
			continue

	return list

def readAllText(path):
	f = open(path, 'r', encoding='utf8')
	txt = f.read()
	f.close()
	return txt

def writeAllLines(path, lines):
	file = open(path, 'w', encoding='utf8')
	for line in lines:
		file.write(line)
		file.write('\n')
	file.close()


if __name__ == '__main__':
	argvs = sys.argv
	argc = len(argvs)
	if (argc < 2):
		print('Usage: # python '+argvs[0]+' filename')
		quit()

	path = argvs[1]

	html = readAllText(path)
	list = listupAnchor(html)
	for line in list:
		print(line)

	writeAllLines("result.txt", list)

