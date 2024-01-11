import re
import sys
import fileinput

filePath = sys.argv[1]
delta = list(map(int, sys.argv[2:6]))
outFilePath = re.sub(".sbv$", "_out.sbv", filePath)

def minutesTime(time, delta):
  carry = False
  carryAmount = [0, 60, 60, 1000]
  for i in reversed(range(4)):
    digit = time[i] - delta[i] - (1 if carry else 0)
    carry = digit < 0
    if carry:
      digit += carryAmount[i]
    time[i] = digit
  return time

with open(outFilePath, 'w', encoding="utf-8") as f:
  for l in fileinput.input(filePath):
    matches = re.match("^(\d+):(\d+):(\d+)\.(\d+),(\d+):(\d+):(\d+)\.(\d+)$", l)
    if matches != None:
      matches = list(map(int, matches.groups()))
      fh, fm, fs, fss = minutesTime(matches[0:4], delta)
      th, tm, ts, tss = minutesTime(matches[4:], delta)
      l = f"{fh}:{fm:02d}:{fs:02d}.{fss:03d},{th}:{tm:02d}:{ts:02d}.{tss:03d}\n"
    f.write(l)
