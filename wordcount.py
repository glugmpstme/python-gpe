#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/



import sys


def build_dict(filename):
  diction = {}
  file = open(filename, 'r')
  for lines in file:
    words = lines.split()
    for word in words:
      word = word.upper()
      if not word in diction:
        diction[word] = 1
      else:
        diction[word]+=1
  file.close()  
  return diction



def print_words(filename):
  diction = build_dict(filename)
  for word in sorted(diction.keys()):
    print (str(word).ljust(10), str(diction[word]).ljust(10)) #fancy formatting
  return



def print_top(filename):
  diction = build_dict(filename)
  
  def get_number(diction):
    return diction[-1]

  listtop = sorted(diction.items(), key=get_number, reverse=True)
  for i in listtop[:20]:
    print (str(i[0]).ljust(10), str(i[1]).ljust(10)) #fancy formatting
  return



def main():
  if len(sys.argv) !=3:
    print ('usage: python wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print ("unknown option: ") + option
    sys.exit(1)

if __name__ == '__main__':
  main()
