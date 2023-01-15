from flask import Flask 
import logging 
import json 

app = Flask(__name__) 

@app.route('/palindrome/<word>', methods = ['GET']) 
def palindrome(word): 
    logging.info("Word received: [" + str(word) + "]") 
    jsonResponse = buildJSON(word) 
    logging.info("JSON obtained: {" + jsonResponse + "}") 
    return jsonResponse

def buildJSON(word):
    reverse = word[::-1]              
    counter = {}
    if word == reverse:
        wr = bool(reverse)  
        for i in word:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1

        for letter, number in counter.items():
            "{}:{}".format(letter, number)
            file_json = {
                    "name": word,
                    "palindrome": wr,
                    "sorted": counter,
                    "length": len(word)
                    }
            return json.dumps(file_json, indent=0)
    else:
        wr = bool(counter)
        file_json = {
                "name": word,
                "palindrome": wr
                }
        return json.dumps(file_json, indent=0)  # Convert into JSON the indent=0 is giving the format of the JSON
        #print(y) 
# 
#                                                     
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=81, debug = False)