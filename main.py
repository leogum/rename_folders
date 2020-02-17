import os
import re

# connect to main folder
os.chdir(r"\\nas.prodam\SL0104_Fichas_Numeracao")
# return a path
path = os.getcwd()
# list all items inside main folder
folders = os.listdir(path)


for f in folders:
    # regular expression to find all files that i want(see regular expressions doc file to see how create one RE to you)
    old_re = r'\d{6}\_\d+.*'
    old_name = re.findall(old_re, f)

    if old_name:
        for o in old_name:
            print('old name: ' + o)
            # my mask pattern for new name
            f = f[:2] + "." + f[2:5] + "-" + f[5:]
            # command to rename using "o" to find files and "f" to rename with new pattern
            os.renames(o, f)
        print('new name: ' + f)
    re.split(r'\d\*', f)

