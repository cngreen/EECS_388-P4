#!/usr/bin/python
import subprocess
import os
import base64
import sys
import json
stra = "A"*2097002

mydict = {}
tmp_list = []
for i in range(0,1000000):
    tmp_list.append(i)
mydict['test1'] = tmp_list
json_string = json.dumps(mydict)

pattern = 2

successTestCases = [
	'''{"a":0.14285714285714288}''',
]

while( 1 == 1):
	
	dict2 = {'a':pattern}
	#print json.dumps(dict2).replace(" ", "")
	successTestCases.append(json.dumps(dict2).replace(" ",""))
	pattern = pattern*pattern

	for testcase in successTestCases :
		
    		child = subprocess.Popen("./jsonParser", stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    		_, stdErrOut = child.communicate(input = testcase)
    		if child.returncode != 0 or stdErrOut != "" :
        		print "BROKEN SUCCESS TEST CASE (%d): %s" % (child.returncode, testcase)
        		print "|%s|" % stdErrOut
			print 'In base64:\n' + base64.b64encode(testcase)
        		sys.exit(0)

	print "EVERYTHING PASSES"
