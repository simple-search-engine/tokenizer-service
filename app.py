from flask import Flask, request, Response
# from konlpy.tag import Okt 
from kiwipiepy import Kiwi 
import json
from config import Config

# okt = Okt()
kiwi = Kiwi()

def morphs(text):
    morphs = []
    for token in kiwi.tokenize(text):
        morphs.append(token.form)
    return morphs

app = Flask(__name__)

@app.route('/tokenizer', methods=['POST'])
def create():
    payload = request.json
    text = payload['text']
    # tokens = okt.morphs(text)
    tokens = morphs(text)

    results = {"tokens" : tokens}
    json_data = json.dumps(results)
    response = Response(json_data, content_type='application/json')
    return response


@app.route('/multiDocuments', methods=['POST'])
def getMultiTokenizedDocuments():
    payload = request.json
    print(payload)
    documents = payload['documents']
    tokenizedDocuments = []
    for text in documents:
        tokenizedDocument = ''
        # tokens = okt.morphs(text)
        tokens = morphs(text)
        for token in tokens:
            tokenizedDocument += " " + token 
        tokenizedDocuments.append(tokenizedDocument)

    results = {"tokenizedDocuments" : tokenizedDocuments}
    json_data = json.dumps(results)
    response = Response(json_data, content_type='application/json')
    return response

if __name__ == '__main__':
    app.run(host=Config.HOST_IP, port=7000, debug=True) 