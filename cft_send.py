#!/usr/bin/python
 
 
import os
import getopt, sys
 
def print_help():
    print("The script is called in the format ./cft_send.py <options>")
    print("")
    print("Options:")
    print("-h, --part   - The CFTPART name you are sending to")
    print("-i, --idf    - The IDF identifier")
    print("-s, --fname  - The source filename")
    print("-d, --nfname - The destination filename")
    print("-p, --parm   - The transfer PARM value, please escape back slashes")
    print("")
    sys.exit(1)
 
full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
short_options = "d:h:i:p:s:?"
long_options = ["nfname=", "part=", "idf=", "parm=", "fname="]
 
try:
  arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
  print (str(err))
  sys.exit(2)
 
cftsend_opts = ''
cftfname = ''
for current_argument, current_value in arguments:
    if current_argument in ("-d", "--nfname"):
        cftsend_opts = cftsend_opts + " ,nfname={}".format(current_value)
    elif current_argument in ("-h", "--part"):
        cftsend_opts = cftsend_opts + " ,part={}".format(current_value)
    elif current_argument in ("-i", "--idf"):
        cftsend_opts = cftsend_opts + " ,idf={}".format(current_value)
    elif current_argument in ("-s", "--fname"):
        cftfname = current_value
        cftsend_opts = cftsend_opts + " ,fname={}".format(current_value)
   elif current_argument in ("-p", "--parm"):
        cftsend_opts = cftsend_opts + " ,parm={}".format(current_value)
    elif current_argument in ("-?"):
        print_help()
 
if not os.path.isfile(cftfname):
    print("Source file (--fname) {} does not exist".format(cftfname))
    sys.exit(2)
 
cftsend_base = ". /axway/Synchrony/Transfer_CFT/runtime/profile ;/axway/Synchrony/Transfer_CFT/home/bin/cftutil send"
cftsend_cmd = cftsend_base + cftsend_opts.replace(',','',1)
 
print(cftsend_cmd)
 
# execute the cftsend command and stream the output into log var
log=os.popen(cftsend_cmd)
 
# for now output the log to screen
output = log.read()
print(output.strip())
 
sys.exit()
