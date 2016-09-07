#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/



def verbing(s):
  if len(s)>=3:
    if s[-3:]!="ing": s+="ing"
    else: s+="ly"
  return s



def not_bad(s):
  nots=s.find("not")
  bads=s.find("bad")
  if bads>nots:
    s=s[:nots]+"good"+s[bads+3:]
  return s



def front_back(a, b):
  mida=len(a)/2
  if mida%2==1: mida+=1
  midb=len(b)/2
  if midb%2==1: midb+=1
  return a[:mida]+b[:midb]+a[mida:]+b[midb:]



def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))



def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print ('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
