import requests

def emotion_detector(text_to_analyse):
    '''
    Analyses text and produces an output of the sentiment expressed
    '''
    #URL header and payload of the tool
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    #Send a post request
    response = requests.post(url, json=myobj, headers=header)

    return response.text