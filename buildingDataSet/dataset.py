import csv
import string
#from string import maketrans

# Helper functions
def isDuplicateContext (line_1, line_2):
    return (line_1 in line_2) or (line_2 in line_1)

def contextId (line):
    return line['integral_index']

# Dataset class ----------------------------------------------------------

class dataset():

    def __init__ (self):
        self.complete_list_of_contexts = []
        self.list_of_multiple_polarities = []
        self.trimmed_list = []
        self.duplication_register = []

    def append (self, lists):
        self.complete_list_of_contexts += lists[0]
        self.list_of_multiple_polarities += lists[1]
    
    def buildComparisonContexts (self):
    # This function prepares the contexts to be compared in the seekDuplicate function.
    # It eliminates spaces, punctiation and replace upper case letters by lower case.
        self.cleaned_contexts = []
        
        for i in range (len(self.complete_list_of_contexts)):
            cleaned_text = (self.complete_list_of_contexts[i]['citeContext']).lower()
            translation_table = cleaned_text.maketrans ('','', ' '+string.punctuation) 
            self.cleaned_contexts.append (cleaned_text.translate (translation_table))

    def contextLength (self, i):
    # This function gets the len of the context.
    # It will be used in the seekDuplicates function to store the longest context. This allows to 
    # eliminate the contexts that contain only a citation, such as
    # "(<cite>Cutting et al. , 1992</cite>) and (<cite>Feldweg, 1995</cite>)"
        return len (self.complete_list_of_contexts[i]['citeContext'])    

    def seekDuplicates (self):
    # This function seeks for duplicated contexts dans in the list 
        #create integer indices to be able to sort the trimmed list, this is temporary
        for i in range (len(self.complete_list_of_contexts)):
            self.complete_list_of_contexts[i]['integral_index'] = i

        #create the simplified contexts to allow comparison
        self.buildComparisonContexts()


        not_already_identified_as_duplicate = [True]*len(self.complete_list_of_contexts)

        for i in range (len(self.complete_list_of_contexts)):
            if not_already_identified_as_duplicate [i]: # only proceed  if this item [i] is not already identified as a duplicate
                list_of_duplicates = []
                retained_line_index = i #Index of the line that will be stored (if not duplicated) 

                for j in range (i+1, len (self.complete_list_of_contexts)):
                    if not_already_identified_as_duplicate [j]: # only proceed if this item [j] is not already identified as a duplicate
                        if isDuplicateContext (self.cleaned_contexts [i], self.cleaned_contexts[j]):
                            if  not_already_identified_as_duplicate [i]:
                                not_already_identified_as_duplicate [i] = False
                                entry = {'line' : self.complete_list_of_contexts[i], 'index' : i}
                                list_of_duplicates.append (entry)
                                retained_line_index = i

                            not_already_identified_as_duplicate[j] = False
                            entry = {'line' : self.complete_list_of_contexts[j], 'index' : j}
                            list_of_duplicates.append(entry)
                            #check that we retain the biggest context length
                            if self.contextLength(j) > self.contextLength(retained_line_index):
                                retained_line_index = j

                if (len (list_of_duplicates) != 0):
                    self.duplication_register.append(list_of_duplicates)
                self.trimmed_list.append(self.complete_list_of_contexts[retained_line_index])
        self.trimmed_list.sort(key = contextId)

        #remove the temporary numbering used to sort the lines 
        for line in self.complete_list_of_contexts:
            del (line['integral_index']) 

    def creatingContextIdForTrimmedList(self):
    #This function creates a unique id for each context of the CitaNeg dataset after trimming.
    #The funciton takes one parameter: a list.
    
        id_num = 0 

        for line in self.trimmed_list:
            id_num +=1
            line['id'] = 'CitaNeg-'+str(id_num)

    def creatingContextIdForDuplicatedList(self):
    #This function creates a unique id for each context of the CitaNeg dataset before trimming.
    #The funciton takes one parameter: a list.

        id_num = 0

        for line in self.complete_list_of_contexts:
            id_num +=1
            line['id'] = 'CitaNeg-'+str(id_num)
    
    def getTheLen(self):
        
        for line in self.trimmed_list:
            contextLength = len(line['citeContext'])
            line['contextLength'] = contextLength
            

    def exportCSVwithDuplicates (self, output_file):
    # This function produces a csv file containing all the citation contexts
    # retrieved and their respective metadata, including possible duplicates
    # The function takes two parameters: a file path and a list
        
        if len(self.complete_list_of_contexts) == 0: 
            return
        else:                                           # if the list of contexts is not empty,
            self.creatingContextIdForDuplicatedList()   # create a context id 

        self.getTheLen()

        with open(output_file, mode='w', newline='') as csvfile:  #open a new file to write
            fieldnames = ['id','dataSource', 'contextID', 'paperID', 'citeContext', 'originalLabel', 'polarity', 'contextLength']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter= '\t')
            writer.writeheader() # Write the headers. The filednames correspond to the keys in the dictionary.
            
            for dict in self.complete_list_of_contexts:
                writer.writerow(dict)

    def exportCSVwithoutDuplicates (self, output_file):
    # This function produces a csv file containing all the citation contexts
    # retrieved and their respective metadata, after trimming duplicates
    # The function takes two parameters: a file path and a list

        if len(self.trimmed_list) == 0: 
            if len(self.complete_list_of_contexts) == 0:
                return
            else:                                           # if trimmed list is empty,
                self.seekDuplicates()                       # seek for duplicates
                self.creatingContextIdForDuplicatedList()   # and create a context id for the untrimmed list
                self.creatingContextIdForTrimmedList()      # and for the trimmed list
        else:   
            self.creatingContextIdForDuplicatedList()       # if the lists are not empty,
            self.creatingContextIdForTrimmedList()          # create context id
        
        self.getTheLen()

        with open(output_file, mode='w', newline='') as csvfile:  #open a new file to write
            fieldnames = ['id','dataSource', 'contextID', 'paperID', 'citeContext', 'originalLabel', 'polarity', 'contextLength']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter= '\t')
            writer.writeheader() # Write the headers. The filednames correspond to the keys in the dictionary.
            
            for dict in self.trimmed_list:
                writer.writerow(dict)
    
    # def exportCSVNegWithDuplicates (self, output_file):
    # # This function produces a csv file containing only the negative citation contexts
    # # retrieved and their respective metadata, including possible duplicates
    # # The function takes two parameters: a file path and a list
       
    #     if len(self.complete_list_of_contexts) == 0:
    #         return
    #     else:
    #         self.creatingContextIdForDuplicatedList()

    #     self.getTheLen()

    #     with open(output_file, mode='w', newline='') as csvfile:
    #         fieldnames = ['id','dataSource', 'contextID', 'paperID', 'citeContext', 'function', 'originalLabel', 'polarity', 'contextLength']
    #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter= '\t')
    #         writer.writeheader()
            
    #         for dict in self.complete_list_of_contexts:
    #             if dict['polarity'] == '1': # Use only the negative contexts.
    #                 writer.writerow(dict)
   
    # def exportCSVNegWithoutDuplicates (self, output_file):
    # # This function produces a csv file containing only the negative citation contexts
    # # retrieved and their respective metadata, after trimming the list
    # # The function takes two parameters: a file path and a list
        
    #     if len(self.trimmed_list) == 0:
    #         if len(self.complete_list_of_contexts) == 0:
    #             return
    #         else:
    #             self.seekDuplicates()
    #             self.creatingContextIdForDuplicatedList()
    #             self.creatingContextIdForTrimmedList()
    #     else:
    #         self.creatingContextIdForDuplicatedList()
    #         self.creatingContextIdForTrimmedList()

    #     self.getTheLen()

    #     with open(output_file, mode='w', newline='') as csvfile:
    #         fieldnames = ['id','dataSource', 'contextID', 'paperID', 'citeContext', 'function', 'originalLabel', 'polarity','contextLength']
    #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter= '\t')
    #         writer.writeheader()
            
    #         for dict in self.trimmed_list:
    #             if dict['polarity'] == '1': # Use only the negative contexts.
    #                 writer.writerow(dict)

    def exportMulPol (self, output_file):
    # This function produces a csv file containing the contexts that present multiple polarities.
    # The function takes two parameters: a file path and a list
       
        with open(output_file, mode='w', newline='') as csvfile:
            fieldnames = ['dataSource', 'contextID', 'paperID', 'citeContext', 'originalLabel', 'polarity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter= '\t')
            writer.writeheader()

            for dict in self.list_of_multiple_polarities:
                writer.writerow(dict)
      
    def exportDuplicatesAsTxt (self, file_path):
    # This function produces a txt file containing the list of repeated contexts
    # The function takes two parameters: a file path and a list

        with open(file_path, mode='w', encoding='utf-8') as file:
            for list_of_duplicates in self.duplication_register:
                file.write ("Duplicates of : "+list_of_duplicates[0]['line']['id']+"\n")
                for duplicate in list_of_duplicates:
                    file.write(duplicate['line']['id']+" : "+duplicate['line']['citeContext']+"\n")
                file.write("\n")