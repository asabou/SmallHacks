import PyPDF2
import argparse 
import docx
import os

def getFields():
    parser = argparse.ArgumentParser(description="Convert PDF to doc")
    parser.add_argument("pdffile", action="store", type=str, help="convert PDF to doc")
    parser.add_argument("docfile", action="store", type=str, help="convert PDF to doc")
    arg = parser.parse_args()
    return [arg.pdffile, arg.docfile]

def readBytes(infile):
    infile = open(infile, "rb")
    text = ""
    readPDF = PyPDF2.PdfFileReader(infile)
    pages = readPDF.numPages
    for i in range(pages):
        page = readPDF.getPage(i)
        text += page.extractText()
    return text 

def writeBytes(infile, outfile):
    text = readBytes(infile)
    print(text)
    doc = docx.Document()
    doc.add_paragraph(text)
    doc.save(outfile) 

def start():
    infile, outfile = getFields()
    writeBytes(infile, outfile)

start()
