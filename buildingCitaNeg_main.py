
########## Imports
## Import all the funcitons form the buildingCitaNeg module 
from buildingCitaNeg import *


########## Variables
## Each path variable corresponds to the path to the directory 
## where dataset to be treated is stored.
file_path_athar = # path to the input file
file_path_dfki = # path to the input file
file_path_liu = # path to the input file
file_path_cfc = # path to the input file
file_path_concit = # path to the input file

## Each file variable corresponds to the path to the csv file produced.
output_file_all = # path to the output file
output_file_neg = # path to the output file


## Empty list to store the citation contexts retrieved.
citaDataset = []

########## Functions calling
## Function to process the Athat dataset.
processing_athar_dataset (file_path_athar,citaDataset)

## Function to process the DFKI dataset.
processing_dfki_dataset (file_path_dfki,citaDataset)

## Function to process the Liu dataset.
processing_liu_dataset (file_path_liu,citaDataset)

## Function to process the CFC dataset.
processing_cfc_dataset(file_path_cfc, citaDataset)

## Function to process the Concit dataset.
processing_concit_dataset(file_path_concit, citaDataset)

## Function to creat a unique ID for each citation context retrieved.
creating_context_id (citaDataset)

## Function to produce a csv file containing all the citation contexts.
## Untoggle in case this is the expected result
export_csv_file_all (output_file_all, citaDataset)

## Function to produce a csv file containing only the negative citation contexts.
## Untoggle in case this is the expected result
export_csv_file_neg (output_file_neg, citaDataset)


    
    
    
