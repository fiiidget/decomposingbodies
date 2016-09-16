from xmlutils import xml2csv
import csv
import sys
import glob

inputs = "myfile.xml"
output = "myfile.csv"

converter = xml2csv(inputs, output)
converter.convert(tag="item")
