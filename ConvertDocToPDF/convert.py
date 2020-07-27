import sys 
import os
import comtypes.client
import argparse

def getFields():
    parser = argparse.ArgumentParser(description="Convert doc to PDF")
    parser.add_argument("docfile", action="store", type=str, help="convert doc to PDF")
    parser.add_argument("pdffile", action="store", type=str, help="convert doc to PDF")
    arg = parser.parse_args()
    return [arg.docfile, arg.pdffile]

def convert(infile, outfile):
    word = comtypes.client.CreateObject("Word.Application")
    infile = os.getcwd() + "\\" + infile
    infile = infile.replace("\\", "\\\\")
    outfile =  os.getcwd() + "\\" + outfile
    outfile = outfile.replace("\\", "\\\\")
    doc = word.Documents.Open(infile)
    doc.SaveAs(outfile, FileFormat=17)
    doc.Close()
    word.Quit()

def start(): 
    infile, outfile = getFields() 
    convert(infile, outfile)

start()
