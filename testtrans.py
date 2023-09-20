import glob, os, re, subprocess, time
from pathlib import Path
counter = 0
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
dir = "./examples"
oracles = {}
start = False
# traverse the examples dir and all of its subdirs in search of spthy files
for root, dirs, files in os.walk(dir):
# sort dirs by name for consistency
  dirs.sort()
  #files.sort()
  for file in sorted(files):
  # analyze a theory for exists-lemmas
    if not (file.endswith('.spthy')):
      continue
  filepath = os.path.join(root, file)
  filepath_lowercase = filepath.lower()
  try:
    output = subprocess.check_output("tamarin-prover" + " -m=proverif " + filepath, timeout=900 , shell=True, stderr=subprocess.STDOUT)
    output_str = str(output.decode('utf-8'))
    with open(os.path.join(__location__, "fastertranslations.txt"), 'a+') as f:
     f.write(filepath_lowercase)
     f.write(output_str)
  except Exception as e:
     print(e.output)
