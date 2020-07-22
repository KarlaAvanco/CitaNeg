import csv

class dataset ():
    def __init__ (self):
        self.complete_list_of_contexts = []
        self.list_of_multiple_polarities = []

    def append (self, lists):
        #self.complete_list_of_contexts += lists['complete']
        #self.list_of_multiple_polarities += lists['multiple polarities']
        self.complete_list_of_contexts += lists[0]
        self.list_of_multiple_polarities += lists[1]
        #return complete_list_of_contexts
        #return list_of_multiple_polarities

    
    def creating_context_id(self):
    #This function creates a unique id for each context of the CitaNeg dataset.
    #The funciton takes one parameter: a list.
    
        id_num = 0 

        for line in self.complete_list_of_contexts:
            id_num +=1
            line['id'] = 'CitaNeg-'+str(id_num)  
    
    
    def exportCSV (self, output_file):
    # This funcitons produces a csv file containing all the citation contexts
    # retrieved and their respective metadata.
    # The function takes two parameters: a file path and a list
        
        with open(output_file, mode='w', newline='') as csvfile:  #open a new file to write
            fieldnames = ['id','dataSource', 'contextID', 'paperID', 'citeContext', 'originalLabel', 'polarity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter= '\t')
            writer.writeheader() # Write the headers. The filednames correspond to the keys in the dictionary.
            
            for dict in self.complete_list_of_contexts:
                writer.writerow(dict)

    
    def exportCSVNeg (self, output_file):
    # This funcitons produces a csv file containing only the negative citation contexts
    # retrieved and their respective metadata.
    # The function takes two parameters: a file path and a list
    
        with open(output_file, mode='w', newline='') as csvfile:
            fieldnames = ['id','dataSource', 'contextID', 'paperID', 'citeContext', 'originalLabel', 'polarity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter= '\t')
            writer.writeheader()
            
            for dict in self.complete_list_of_contexts:
                if dict['polarity'] == '1': # Use only the negative contexts.
                    writer.writerow(dict)
    
    
    def exportMulPol (self, output_file):
    # This funcitons produces a csv file containing the contexts that present multiple polarities.
    # The function takes two parameters: a file path and a list
    
        
        with open(output_file, mode='w', newline='') as csvfile:
            fieldnames = ['dataSource', 'contextID', 'paperID', 'citeContext', 'originalLabel', 'polarity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter= '\t')
            writer.writeheader()

            for dict in self.list_of_multiple_polarities:
                writer.writerow(dict)
   
   
   
    
    
