import sys
import os

DirPath_str = os.path.dirname(
            os.path.abspath(os.path.dirname(
                        os.path.abspath(os.path.dirname(__file__)))))
sys.path.append(DirPath_str+'/flask')

'''
for path in list(sys.path):
    print(path)
'''
