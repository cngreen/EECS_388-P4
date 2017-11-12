#!/usr/bin/python
import subprocess
import os
import base64
import sys

successTestCases = [
    '''{"a":"b\\""}''',
    '''{"a":"b"}''',
    '''{"a":["b",1]}''',
    '''{"asdf":"qwer","zxcv":[1,2,3,4],"fdsa":{"a":"b"}}''',
    '''{"a":1.234,"b":"c"}''',
    '''{"a":true,"b":false,"c":null}''',
    '''{"status": [2147483647, 21474864]}'''
#             "2": "val"
#         },
#         {
#             "0": "val",
#             "1": "val",
#             "2": "val"
#         }
#     ]
# }

#     '''{"-1":[2147483647]}''',
#     '''{"-1":[2147483648]}''',
#     '''{"-1":[4294967295]}''',
#     '''{"-1":[4294967296]}''',
#     '''{2147483647:2147483647}''',
#     '''{2147483648:2147483648}''',
#     '''{4294967296:4294967296}''',
#     '''{4294967295:4294967295}'''


]

for testcase in successTestCases :
    child = subprocess.Popen("./jsonParser", stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    _, stdErrOut = child.communicate(input = testcase)
    if child.returncode != 0 or stdErrOut != "" :
        print "BROKEN SUCCESS TEST CASE (%d): %s" % (child.returncode, testcase)
        print "|%s|" % stdErrOut
        sys.exit(0)