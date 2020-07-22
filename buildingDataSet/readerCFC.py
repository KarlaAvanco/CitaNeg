from readerXML import *
from xml.dom import minidom

class cfcReader (XMLreader): # Class to processes the CFC dataset.
                             # Dataset format: xml
                             # Size: 1 folder with multiple files
    def getPaperId (self, root_node):
    # This function processes the CFC dataset.
    # Treatment: get a paper id
    # The function takes one parameter: a xml node.

        # focus on the <FILENO> tag
        paperIds = root_node.getElementsByTagName('FILENO')
        for paperId in paperIds:
            paper_Id_text = displayNodeText(paperId)
        return paper_Id_text

    #The following functions get the lables specific to the CFC dataset
    def getDataSourceName (self):
        return 'CFC'

    # focus on <S AZ="BKG" ID="S-0"> 
    def getContextTag (self):
        return 'S'

    # focus on <REF CFunc="Weak" ID="R-5" SELF="YES" TYPE="A">Dagan et al. 1993</REF>
    def getCitationTag (self):
        return 'REF'

    def getOriginalLabelTag (self):
        return "CFunc" 

    def getContextIdTag (self):
        return "ID"

    def isNegativePolarity (self, label):
        return label == "Weak" or label == 'CoCo-' 

    def getFilesList (self, path):
        return glob.glob(path)