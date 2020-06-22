import PyPDF2
from PyPDF2 import PdfFileReader
import pandas as pd

opener = open("mitpress2.pdf", "rb")
reader = PyPDF2.PdfFileReader(opener)
reader.numPages 	# Prints 7

# Our goal is to now get the text from each page in the form of a dataframe

data = []
for i in range(7):
	page = reader.getPage(i)
	data.append(page.extractText())

# Creating a dictionary where the key is text and value is the data extracted

d = {'text': data}

df = pd.DataFrame(data = d)

df.to_excel("MyData.xlsx", sheet_name = "Sheet1")
	
	


