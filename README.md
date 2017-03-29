# Python
#include codes
import urllib

thisurl = "http://www-rohan.sdsu.edu/~gawron/index.html"

handle = urllib.urlopen(thisurl)

html_gunk =  handle.read()


# PDF Parse

download: https://pypi.python.org/pypi/pdfminer3k
do: 
python setup.py install

pdf2txt.py -O myoutput -o myfile5.html -t html -p 5 name.pdf
run search_columns.py




