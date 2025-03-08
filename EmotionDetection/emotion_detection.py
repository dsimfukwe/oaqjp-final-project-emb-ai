import requests
import json

def emotion_detector(text_to_analyse):
    '''  Analyses text and produces an output of the sentiment expressed
    '''
    #URL header and payload of the tool
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    #Send a post request
    response = requests.post(url, json=myobj, headers=header)
    # Parsing the JSON response from the API
    if response.status_code == 400:
        emotions_out = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }
    else:
        formatted_response = json.loads(response.text)
        response_emotions = formatted_response["emotionPredictions"][0]["emotion"]
        val_max = 0
        emo_max = ''
        for (key,val) in response_emotions.items():
            if val >= val_max:
                val_max = val
                emo_max = key

        emotions_out = response_emotions
        emotions_out['dominant_emotion'] = emo_max

    return emotions_out