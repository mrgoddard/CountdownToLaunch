# Recommended imports for all problems
# Some problems may require more
import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())
for case in range(cases):
   launchTimes = int(sys.stdin.readline().rstrip())
   launchList = []
   launched = False
   for launchTime in range(launchTimes):
       line = sys.stdin.readline().rstrip().split()
       date = line[0]
       time = line[1]
       cloudThickness = int(line[2])
       windSpeed = float(line[3])
       windDir = int(line[4])
       windNS = abs(windSpeed*math.cos(math.radians(windDir)))
       windEW = abs(windSpeed * math.sin(math.radians(windDir)))
       if (cloudThickness <= 1000 and windNS <= 20 and windEW <= 40 and launched == False):
           goLaunchDate = date
           goLaunchTime = time
           launched = True
   if (launched == True):
       print(goLaunchDate,goLaunchTime)
   else:
       print("ABORT LAUNCH")
   launched = False










