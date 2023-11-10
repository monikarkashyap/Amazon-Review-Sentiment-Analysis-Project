#function used by models
#--------------TextBlob---------
def blob_senti(x):
     # decide sentiment as positive, negative and neutral
    senti=''
    if x > 0 :
        senti="POSITIVE"
 
    elif x < 0 :
        senti="NEGATIVE"
 
    else :
        senti="NEUTRAL"
    return senti

#---------Vader------------------
# create a categorical sentiment
def vader_senti(x):
     # decide sentiment as positive, negative and neutral
    senti=''
    if x >= 0.05 :
        senti="POSITIVE"
 
    elif x <= - 0.05 :
        senti="NEGATIVE"
 
    else :
        senti="NEUTRAL"
    return senti