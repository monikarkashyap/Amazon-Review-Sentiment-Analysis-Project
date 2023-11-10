# function to perform some cleaning
import re as re
#remove html tags
def remove_tags(string):
    result = re.sub('<.*?>','',string)
    return result