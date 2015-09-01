import hexchat
import binascii
from thread import start_new_thread

__module_name__ = "auto-crc32"
__module_author__ = "Wurzeltroll"
__module_version__ = "0.2"
__module_description__ = "Calculate CRC32 after finishing DCC Download"

def calcThread(fname):
    buf = open(fname,'rb').read()
    buf = (binascii.crc32(buf) & 0xFFFFFFFF)
    print("CRC32: %08X" % buf)

def completeHandler(word, word_eol,userdata):
    start_new_thread(calcThread,(word[1],))
    return hexchat.EAT_NONE

hexchat.hook_print("DCC RECV Complete",completeHandler)
