import sys
import re

def extract_names(filename):
  fw= open(filename, 'rU')
  year=[]
  names=[]
  text=fw.read()
  year_find=re.search(r'Popularity\sin\s(\d\d\d\d)' ,text)
  if not year_find:
	  print 'Year not found, try again'
  else:
	  year_found = year_find.group(1)
	  year.append(year_found)
  names_found=re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)
  names_rank={}
  for namesr  in names_found:
	  (rank,boyname,girlname) = namesr
	  if boyname not in names_rank:
		  names_rank[boyname]=rank
	  if girlname not in names_rank:
		  names_rank[girlname]= rank
  sorted_names= sorted(names_rank.keys())
  for name in sorted_names:
	  year.append(name + " " + names_rank[name])
  return year



def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  # LAB(begin solution)
  for filename in args:
    names = extract_names(filename)

    # Make text out of the whole list
    text = '\n'.join(names)

    if summary:
      outf = open(filename + '.summary', 'w')
      outf.write(text + '\n')
      outf.close()
    else:
      print text
  # LAB(end solution)

if __name__ == '__main__':
  main()
