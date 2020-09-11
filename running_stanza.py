# Purpose: run stanford NLP from python

import os
import stanza
import glob
import json
import sys

input_folder = sys.argv[1]
output_folder = sys.argv[2]

# make directory
if not os.path.exists(output_folder):
    os.mkdir (output_folder)

NLP_reader = stanza.Pipeline('en') # Initialize English neural pipeline

for file_name in glob.glob (os.path.join(input_folder,'*')):
    with open (file_name) as file:
        text_analysed = file.readline()
        doc = NLP_reader (text_analysed) # Parse le text
    input_file_name = os.path.basename(file_name)
    file_name_without_extension = input_file_name.split('.')[0]
    output_file_name = os.path.join(output_folder,file_name_without_extension+'.json')
    with open (output_file_name, 'w') as json_file:
        json.dump(doc.to_dict(), json_file, indent=4)


