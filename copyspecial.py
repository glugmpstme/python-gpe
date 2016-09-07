#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands



def get_locations(dirname):
  locations = []
  for file in os.listdir(dirname):
    filepath = re.search(r'__(\w+)__', file)
    if filepathpath:
      locations.append(os.path.abspath(os.path.join(dirname, file)))
  return locations



def copy(locations, todir):
  if not os.path.exists(todir):
    os.mkdir(to_dir)
  for location in locations:
    file = os.path.basename(location)
    shutil.copy(location, os.path.join(todir, file))
  return



def zip(locations, zipfile):
  pass


def main():
  args = sys.argv[1:]
  if not args:
    print ("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)
  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print ("error: must specify one or more dirs")
    sys.exit(1)

  locations = []
  for dirname in args:
    locations.extend(get_locations(dirname))

  if todir:
    copy(locations, todir)
  elif tozip:
    zip(locations, tozip)
  
if __name__ == "__main__":
  main()
