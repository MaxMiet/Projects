import os
import sys

bug = input('Bug description: ')
logFile = open('bug_log.txt', 'a')
with open('bug_log.txt', 'a') as logFile:
    logFile.write('\n')
    logFile.write(bug)
logFile.close()