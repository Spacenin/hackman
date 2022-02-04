import requests

def getWord():
    #Get key from key.txt file
    with open("key.txt") as f:
        line = f.readline().strip()

    #Set query as the key and value JSON
    parameter = {"key":line}

    #Get random word
    response = requests.get("http://clemsonhackman.com/api/word", params=parameter)

    return(response.json()["word"])