'''
This is a python code for creating a function to read multiple PDF files which have been stored as "MyData1.pdf", "MyData2.pdf", so on.

Instead of manually changing the code for each new PDF file, this code creates a list of all the files and then uses PDF File reader to read the contents. The advantage of such a code is that 
'''

import PyPDF2
from PyPDF2 import PdfFileReader

data = []
mydata = "MyData"
ext = ".pdf"

# There are 37 pdf files that need to be read. 
# The list creation starts at this point

for i in range(0,37):
	data.append(mydata)

print("The updated list after merely appending file name without number and extension is of the form:")
print(data[0])

#Next goal is to modify each list item with the numbering. 
# The pdf numbering starts at 1. For eg, "MyData1.pdf". 
# The numbering in our data file startsat 1, the indexing of a list, however, starts at 0. So, 
# the index number will be one less than the number to be appended to the item at that point. Hence
# the loop starts at 1 and runs till 38, 38 not included

for i in range(1,38):
	data[i-1] = data[i-1] + str(i) + ext

print("The final list contains data in the form of:")
print(data[0], data[1], data[3])

#datafile = open("datafile.xlsx", 'w+')
#datafile.read()
#datafile.close()

def file_read_write(filename):
	
	pdf = open(filename, 'rb')
	pdf_reader = PyPDF2.PdfFileReader(pdf)
	with open('datafile.txt', 'w+') as datafile:
		totalpages = pdf_reader.numPages
		for i in range(totalpages):
			datafile.write(pdf_reader.getPage(i).extractText())


for i in range(0,36):
	file_read_write(data[i])






























