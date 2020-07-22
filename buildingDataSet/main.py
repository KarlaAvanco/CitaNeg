from dataset import *
from readerAthar import *
from readerDFKI import *
from readerLiu import *
from readerIMS import *
from readerCFC import *
from readerConcit import *

import csv

# Creat an instance of each object
citanegDataset = dataset()
athar = atharReader()
dfki = dfkiReader()
liu = liuReader()
ims = imsReader()
cfc = cfcReader()
concit = concitReader()


#Replace ### by file paths
citanegDataset.append (athar.read ('/home/karla/Documentos/M2_Stage_TAL/1_buildingDataset/originalDatasets/ATHAR/*'))
citanegDataset.append (dfki.read ('/home/karla/Documentos/M2_Stage_TAL/1_buildingDataset/originalDatasets/DFKI/*'))
citanegDataset.append (liu.read ('/home/karla/Documentos/M2_Stage_TAL/1_buildingDataset/originalDatasets/LIU/*'))
citanegDataset.append (cfc.read ('/home/karla/Documentos/M2_Stage_TAL/1_buildingDataset/originalDatasets/CFC/*.xml'))
citanegDataset.append (ims.read ('/home/karla/Documentos/M2_Stage_TAL/1_buildingDataset/originalDatasets/IMS/*'))
citanegDataset.append (concit.read ('/home/karla/Documentos/M2_Stage_TAL/1_buildingDataset/originalDatasets/Concit/'))

citanegDataset.creating_context_id() 

citanegDataset.exportCSV('/home/karla/Documentos/M2_Stage_TAL/1_buildingDataset/scripts/buildingCitaneg_v2_results/citaneg.csv')
citanegDataset.exportCSVNeg('/home/karla/Documentos/M2_Stage_TAL/1_buildingDataset/scripts/buildingCitaneg_v2_results/citaneg_neg.csv')
citanegDataset.exportMulPol('/home/karla/Documentos/M2_Stage_TAL/1_buildingDataset/scripts/buildingCitaneg_v2_results/citaneg_mul_pol.csv')


