import sys

##Final Program for Day 1 Google Excercises for python


def getwordcount(filename):
	dict={}
	file= open(filename)
	for line in file:
		words=line.split()
		for word in words:
			word=word.lower()
			if not word in dict:
				dict[word] = 1
			else:
				dict[word] = dict[word]+1
	return dict

def print_words(filename):
	dict=getwordcount(filename)
	for word in dict:
		print word,dict[word]

def print_top(filename):
  dict={}
  dict=getwordcount(filename)
  value={}
  value=sorted(dict.values(),reverse=True)
  items = sorted(dict.items(), key=gettuple, reverse=True)
  for i in items[:20]:
  	print i[0],i[1]

def gettuple(dict):
	return dict[1]

# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
