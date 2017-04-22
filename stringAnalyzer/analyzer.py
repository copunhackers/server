import requests
from requests.auth import HTTPBasicAuth


#This function sends a post request to the ibm watson api,
#with the testString parameter, as the payload.
#It then get a json object back, which it returns to the caller.

def getAnalyzeJSON(textString):
    payload = {'version': '2016-05-19', 'text': textString}
    r = requests.get('https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone',
        auth=HTTPBasicAuth('f35493d9-3909-4e5f-954d-5b4fcbda253e', '82ZiZjX773At'),
        params=payload,
        headers={'Content-Type': 'text/plain'})
    print(r.url)
    print(r.text)
    return r.json()

#This function runs though the json object,
# and saves the important parts in an array, that gets returned.
def getScores(jsonObject):
    scoreArray = {}
    for score in jsonObject:
        if (score["tone_name"] == "Anger"):
            scoreArray["anger"] = score["score"]
        elif (score["tone_name"] == "Disgust"):
            scoreArray["disgust"] = score["score"]
    return scoreArray

#This function takes an value and returns a string and a boolean value,
#  depending on the value it gets.
def getRespondsMessage(name, largestScore):
    #Angry scores
    if (name == "anger"):
        if (largestScore < 0.4):
            return ("",True)
        elif (largestScore < 0.5):
            return ("You seem slightly angry, you will have to rewrite your message, to be allowed to send it.",False)
        else:
            return ("You seem too angry, this message might offend people, or put someone in distress. Please rewirte it.",False)
    #disgust scores.
    elif (name == "disgust"):
        if (largestScore < 0.4):
            return ("", True)
        elif (largestScore < 0.5):
            return ("You seem slightly disgusted, you will have to rewrite your message, to be allowed to send it.", False)
        else:
            return ("You seem too disgusted, this message might offend people or put someone in distress. Please rewrite it.",False)

#This function call the remaining functions.
#It takes a string, and returns a string descriping if its good or if its bad.
def theAnalyzer(inputString):
    bla = getAnalyzeJSON(inputString)
    bip = getScores(bla["document_tone"]["tone_categories"][0]["tones"])

    name = max(bip, key=lambda key: bip[key])

    print(getRespondsMessage(name, bip[name]))
    return getRespondsMessage(name, bip[name])


#test call
behe = theAnalyzer("i fucking love you")