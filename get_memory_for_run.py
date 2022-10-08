import time
import os, sys, psutil
import pandas as pd
import subprocess as sp

method, substring, fname = sys.argv[1], sys.argv[2], "" if len(sys.argv) < 4 else sys.argv[3]
pid = int(
    [row.strip().split()[0]
      for row in sp.run('ps ax'.split(), stdout=sp.PIPE).stdout.decode().split('\n')
      if substring in row
    ][0]
)
if method == 'output':
  while True:
    print(f'{psutil.Process(pid).memory_info().rss / 1024 ** 2} MB')
    time.sleep(1)
elif method == 'csv':
  res = []
  while True:
    try:
      mem = psutil.Process(pid).memory_info().rss / 1024 ** 2
      res.append(int(mem))
      time.sleep(1)
    except:
      print("process dead now, please see csv for data on memory consumption")
      break
  res = pd.DataFrame({'mem': res})
  res.to_csv(fname, index=False)
  print("done.")
