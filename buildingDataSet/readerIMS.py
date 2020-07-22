from readerXML import *
from xml.dom import minidom

class imsReader (XMLreader): # Class to processes the IMS dataset.
                             # Dataset format: xml
                             # Size: 1 folder with multiple files
    def getPaperId (self, node):
    #This function processes the IMS dataset.
    #Treatment: get a paper id
    #The function takes one parameter: a xml node.
    

        # focus on <acldoc acl_id="P04-1005">
        paperIds = node.getElementsByTagName('acldoc')
        for paperId in paperIds:
           paper_Id_text = paperId.attributes['acl_id'].value
        return paper_Id_text

    #The following functions get the lables specific to the IMS dataset
    def getDataSourceName (self):
        return 'IMS'
    
    # focus on <s id="10">
    def getContextTag (self):
        return 's'
    
    # focus on <ref citStr="Shriberg and Stolcke ( 1998 )" id="1" label="CEPF" position="1645">
    def getCitationTag (self):
        return 'ref'

    def getOriginalLabelTag (self):
        return "label" 

    def getContextIdTag (self):
        return "id"

    def isNegativePolarity (self, label):
        return label == "CEPN" or label == 'CJPN' or label =='OJPN'

    def getFilesList (self, path):
        return glob.glob(path)