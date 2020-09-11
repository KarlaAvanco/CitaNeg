import subprocess
import os
import sys

stanza_analyzer_folder = sys.argv [1] #the folder where running_stanza.py is
stanza_input_folder = sys.argv[2] # the folder where the contexts for parsing are
output_from_stanza = sys.argv[3] #the folder where the parsed contexts will be stored
stanza_application = os.path.join (stanza_analyzer_folder,'running_stanza.py')

input_for_stanza = os.path.join (stanza_analyzer_folder,'contexts_for_parsing')

if not os.path.exists(input_for_stanza):
    print ('Lacking input for stanza to process ')
    sys.exit()

stanza_application += ' '+input_for_stanza+' '+output_from_stanza

subprocess.call ('python3 '+stanza_application, shell=True)

folder_for_evaluator_software = sys.argv[4] # the folder analyzingDataset package 

command_line = 'python3 '+os.path.join (folder_for_evaluator_software,'main.py')
command_line += ' '+output_from_stanza
command_line += ' '+sys.argv[5] #destination folder for stanza_results.csv
command_line += ' '+sys.argv[6] #destination folder for resultsForWeka.csv
command_line += ' '+sys.argv[7] #source folder for the corpus CSV file
command_line += ' '+sys.argv[8] #path for specificities CSV file

subprocess.call (command_line, shell=True)


