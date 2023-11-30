import sys
import os
args = sys.argv
arg = args[1]##argument #2 is always the first argument given
prog_file = args[0]#argument #1 is always the name of the program
print (f'Hello {arg} from {prog_file}')
host = os.environ.get('HOST')



#appdev  -> appdbdev (retail_db, retail_user, retaildevpassowrd)
#appuat  -> appdbuat (retail_db, retail_user, retailuatpassowrd)
