from dataset import *
from readerAthar import *
from readerDFKI import *
from readerLiu import *
from readerIMS import *
from readerCFC import *
from readerConcit import *

import csv
import os
import sys

# Creat an instance of each object
citanegDataset = dataset()
athar = atharReader()
dfki = dfkiReader()
liu = liuReader()
ims = imsReader()
cfc = cfcReader()
concit = concitReader()

input_folder = sys.argv[1]
output_folder = sys.argv[2]

citanegDataset.append (athar.read (os.path.join(input_folder,'ATHAR','*')))
citanegDataset.append (dfki.read (os.path.join(input_folder,'DFKI','*')))
citanegDataset.append (liu.read (os.path.join(input_folder,'LIU','*')))
citanegDataset.append (cfc.read (os.path.join(input_folder,'CFC','*xml')))
citanegDataset.append (ims.read (os.path.join(input_folder,'IMS','*')))
citanegDataset.append (concit.read (os.path.join(input_folder,'Concit')))

citanegDataset.exportCSVwithoutDuplicates(os.path.join(output_folder,"citaneg.csv"))
citanegDataset.exportCSVwithDuplicates(os.path.join(output_folder,"citaneg_untrimmed.csv"))
print ('taille avec doublons : '+str(len(citanegDataset.complete_list_of_contexts)))
print ('taille sans doublons : '+str(len(citanegDataset.trimmed_list)))
citanegDataset.exportDuplicatesAsTxt (os.path.join(output_folder,"duplicates.txt"))
#citanegDataset.exportCSVNegWithoutDuplicates(os.path.join(output_folder,"citaneg_neg.csv"))
#citanegDataset.exportCSVNegWithDuplicates(os.path.join(output_folder,"citaneg_neg_untrimmed.csv"))
citanegDataset.exportMulPol(os.path.join(output_folder,"citaneg_mult_pol.csv"))

