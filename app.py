'''Text Extraction From Images and Pdf using Python
    Install two python modules named PyPDF2 and  easyocr
    Using the command "pip install PyPDF2" and "pip install easyocr" respectively
'''
#Text Extraction from Pdf
from asyncore import read
import PyPDF2 #Module for working with pdf files such as performing splitting, merging, cropping, and transforming the pages of PDF files
a=PyPDF2.PdfFileReader('Theories.pdf') #Give the essential pdf name with .pdf extension
str=''
for i in range(1,4):
    str+=a.getPage(i).extract_text()

with open("Text.txt","w",encoding='utf-8') as f:
    f.write(str)


#Text Extraction from Image
import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image
rcParams['figure.figsize']=8,16
reader=easyocr.Reader(['en'])
output=reader.readtext("Sample.png")
print(output)
cord=output[-1][0]
x_min,y_min=[min(idx) for idx in zip(*cord)]
x_max,y_max=[min(idx) for idx in zip(*cord)]
image=cv2.imread('Sample.png')
cv2.rectangle(image,(x_min,y_min),(x_max,y_max),(0,0,225),2)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
