#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:14:58 2020

@author: karlavanco
"""

############Imports
import glob
import csv
import os
import re


############Functions

def processing_athar_dataset(file_path, contexts_list):
    """
    This function processes the Athar dataset.
    Dataset format: txt
    Size: 1 single file
    The function takes two parameters: a .txt file and a list.
    """
    

    for concrete_file in glob.glob(file_path):  
        with open (concrete_file) as file:       # Open the data set file
            for line in file:
                if re.search('^\w', line):       # Exclude the first lines which contain metadata
                    data = {}                    # Empty dictionary to store the data
                    tokenized_line = line.split('\t')   # Tokenize the lines to find and store the different information
                    data['dataSource'] = 'Athar'
                    data['contextID'] = tokenized_line[0].strip()
                    data['paperID'] = tokenized_line[1].strip()
                    data['citeContext'] = tokenized_line[3].strip()
                    data['originalLabel'] = tokenized_line[2].strip()
                    if data['originalLabel'] == 'n':    # Create a new label
                        data['polarity'] = "1"
                    else:
                        data['polarity'] = "0"
                
            
                    contexts_list.append(data)
    
    
#######################################################################


def processing_dfki_dataset (file_path, contexts_list):
    """
    This function processes the DFKI dataset.
    Dataset format: txt
    Size: 1 folder with 3 files
    Treatment: produce a context id
    The function takes two parameters: a folder containing .txt files and a list.
    """
        
    previousID = ""
    repeat_counter = 1
    
    for concrete_file in glob.glob(file_path): 
        with open (concrete_file, 'r', encoding='latin-1') as input_file:
            for line in input_file:
                data = {}
                tokenized_line = line.split('\t')
                data['dataSource'] = 'DFKI'
                cite = tokenized_line[0].strip() # Create a context id
                if  cite == previousID:
                    repeat_counter += 1
                else:
                    repeat_counter = 1
                data['contextID'] = cite+'_'+str(repeat_counter)
                data['paperID'] = cite.split('_')[0]
                previousID = cite
                data['citeContext'] = tokenized_line[1].strip()
                data['originalLabel'] = tokenized_line[5].strip()
                if data['originalLabel'] == 'Negative':
                    data['polarity'] = "1"
                else:
                    data['polarity'] = "0"
                            
                contexts_list.append(data)
                    
    
######################################################################
    

def processing_liu_dataset(file_path, contexts_list):
    """
    This function processes the Liu dataset.
    Dataset format: csv
    Size: 1 single file   
    The function takes two parameters: a .csv file and a list. 
    """

    for concrete_file in glob.glob(file_path):  
        with open(concrete_file) as csv_object: 
            csv_reader = csv.reader(csv_object, delimiter = ',') 
            next (csv_reader) # skip the first line (headers)
            for row in csv_reader:
                data = {}
                data['dataSource'] = 'Liu'
                data['contextID'] = row[0]
                data['paperID'] = "NA"
                citeContext = re.sub('_comma_', ',',row[2])
                data['citeContext'] = citeContext
                data['originalLabel'] = row[1]
                if data['originalLabel'] == '0':
                    data['polarity'] = "1"
                else:
                    data['polarity'] = "0"
                contexts_list.append(data)

    
######################################################################


def processing_cfc_dataset(file_path, contexts_list):
    """
    This function processes the CFC dataset.
    Dataset format: csv
    Size: 1 single file   
    The function takes two parameters: a .csv file and a list. 
    """

    for concrete_file in glob.glob(file_path):  
        with open(concrete_file) as csv_object: 
            csv_reader = csv.reader(csv_object, delimiter = '\t') 
            next (csv_reader) # skip the first line (headers)
            for row in csv_reader:
                    data = {}
                    data['dataSource'] = 'CFC_paperTraining'
                    data['contextID'] = row[1]
                    paper = row[0].split('.')
                    data['paperID'] = paper[0]
                    data['citeContext'] = row[2]
                    data['originalLabel'] = row[3]
                    if data['originalLabel'] == 'Weak' or data['originalLabel'] == 'CoCo-':
                        data['polarity'] = "1"
                    else:
                        data['polarity'] = "0"
                    contexts_list.append(data)


######################################################################


def processing_concit_dataset(file_path, contexts_list):
    """
    This function processes the CFC dataset.
    Dataset format: csv
    Size: 1 single file   
    The function takes two parameters: a .csv file and a list. 
    """

    for concrete_file in glob.glob(file_path):  
        with open(concrete_file) as csv_object: 
            csv_reader = csv.reader(csv_object, delimiter = '\t') 
            next (csv_reader) # skip the first line (headers)
            for row in csv_reader:
                data = {}
                data['dataSource'] = 'Concit'
                data['contextID'] = row[1]
                data['paperID'] = row[0]
                data['citeContext'] = row[2]
                data['originalLabel'] = row[3]
                if data['originalLabel'] == 'neg':
                    data['polarity'] = "1"
                else:
                    data['polarity'] = "0"
                contexts_list.append(data)


######################################################################

def creating_context_id(contexts_list):
    """
    This function crates a unique id for each context of the CitaNeg dataset.
    The funciton takes one parameter: a list.
    """

    id_num = 0 

    for line in contexts_list:
        id_num +=1
        line['id'] = 'CitaNeg-'+str(id_num)  


######################################################################


def export_csv_file_all(output_file, contexts_list):
    """
    This funcitons produces a csv file containing all the citation contexts
    retrieved and their respective metadata.
    The function takes two parameters: a file path and a list
    """
    


    with open(output_file, mode='w', newline='') as csvfile:  #open a new file to write
        fieldnames = ['id','dataSource', 'contextID', 'paperID', 'citeContext', 'originalLabel', 'polarity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter= '\t')
        writer.writeheader() # Write the headers. The filednames correspond to the keys in the dictionary.
        
        for dict in contexts_list:
            writer.writerow(dict)




def export_csv_file_neg(output_file, contexts_list):
    """
    This funcitons produces a csv file containing only the negative citation contexts
    retrieved and their respective metadata.
    The function takes two parameters: a file path and a list
    """

    with open(output_file, mode='w', newline='') as csvfile:
        fieldnames = ['id','dataSource', 'contextID', 'paperID', 'citeContext', 'originalLabel', 'polarity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter= '\t')
        writer.writeheader()
        
        for dict in contexts_list:
            if dict['polarity'] == '1': # Use only the negative contexts.
                writer.writerow(dict)
