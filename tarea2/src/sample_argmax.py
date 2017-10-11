from RNN2 import *
import sys
from datetime import datetime
from build_data import *

args = sys.argv
if len(args) < 2:
    print "Usage: python sample_std.py <filename>"
    sys.exit()

sample_filename = sys.argv[1]
n = 50000

rnn = RNN(True)
sam = rnn.sample_argmax(data.char_to_index['#'], n)
txt = ''.join(data.index_to_char[c] for c in sam)
txt=txt.decode('utf-8','ignore').encode("utf-8")
txt = txt.replace("&", "\n")
txt = txt.replace("%", "\n\n")
txt = txt.replace("#", "\n\n==\n\n")
with open("samples/argmax_"+datetime.now().strftime('%s')+"_"+sample_filename, "w+") as f:
    f.write(txt)

