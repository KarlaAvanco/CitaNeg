# Script based on a script by Philippe Gambette
# Purpose: identify the citations and add the <cite> and </cite> tags around each citation

import re

def repeatSearch(lineSegments, regex):
   oldLength = -1
   length = len(lineSegments)
   # Look for the regular expression in all segments as long as we find occurrences:
   while length != oldLength:
      lineSegments = labelReference(lineSegments, regex)
      oldLength = length
      length = len(lineSegments)      
   return lineSegments

# For each segment in lineSegment which is not already labeled as a citation
# check if the regex is found, in which case we have found a new citation segment
def labelReference(lineSegments, regex):
   newLineSegments = []
   for segment in lineSegments:
      if segment[0:6] == "<cite>":
         # A citation was already found in the segment so no need to check the regex on this segment
         newLineSegments.append(segment)
      else:
         # No citation was found yet, try to apply the regex to find a citation
         #print("Looking for regex in "+segment)
         res = re.search('(.*'+regex+'.*)',segment)
         if res:
            # A citation was found, add the segment before, the labeled citation, and the segment after, into newLineSegments
            #print("found!")
            newLineSegments.append(res.group(1))
            newLineSegments.append("<cite>"+res.group(2)+"</cite>")
            newLineSegments.append(res.group(3))
         else:
            # No citation was found
            #print("not found!")
            newLineSegments.append(segment)
   return newLineSegments
   
def seekCitations (context_string):
    line_segments = [context_string]
    # Look for citations using the following expressions
    # each found citation will cut the context into several segments, one of which containing the citation
    line_segments = repeatSearch(line_segments,")([A-Z][^ ]+ and [A-Z][^ ]+[, ]* [(][12][0-9][0-9][0-9][a-f]*[)])(")   
    line_segments = repeatSearch(line_segments,")([A-Z][^ ]+ and [A-Z][^ ]+[, ]* [12][0-9][0-9][0-9][a-f]*)(")   
    line_segments = repeatSearch(line_segments,")([A-Z][^ ]+ & [A-Z][^ ]+[, ]* [(][12][0-9][0-9][0-9][a-f]*[)])(")   
    line_segments = repeatSearch(line_segments,")([A-Z][^ ]+ & [A-Z][^ ]+[, ]* [12][0-9][0-9][0-9][a-f]*)(")   
    line_segments = repeatSearch(line_segments,")([A-Z][^ ]+ et al[., ]*[(][12][0-9][0-9][0-9][a-f]*[)])(")   
    line_segments = repeatSearch(line_segments,")([A-Z][^ ]+ et al[., ]*[12][0-9][0-9][0-9][a-f]*)(")   
    #line_segments = repeatSearch(line_segments,")([A-Z][^ ]*[a-zàâäéèêëìîöòôùûüç][^ ]*[, ]*[12][0-9][0-9][0-9][a-f]*)(")   
    line_segments = repeatSearch(line_segments,")([A-Z][^ ]+[, ]*[12][0-9][0-9][0-9][a-f]*)(")   
    line_segments = repeatSearch(line_segments,")([A-Z][^ ]+ [(][12][0-9][0-9][0-9][a-f]*[)])(")

    output_text = ""
    for segment in line_segments:
        output_text += segment
    return output_text
