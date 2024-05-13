import requests
import json
import numpy as np

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input = { "raw_document": { "text": text_to_analyse } }
    if text_to_analyse == '':
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
    }
    response = requests.post(URL, json = Input, headers = Headers)
    if response.status_code == 200:
        formated_response = json.loads(response.text)
        anger_score = formated_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formated_response['emotionPredictions'][0]['emotion']['disgust']
        joy_score = formated_response['emotionPredictions'][0]['emotion']['joy']
        fear_score = formated_response['emotionPredictions'][0]['emotion']['fear']
        sadness_score = formated_response['emotionPredictions'][0]['emotion']['sadness']
        dominant_emotion_index = np.argmax([anger_score,disgust_score,fear_score,sadness_score,joy_score])
        dominant_emotion_name = list(['anger','disgust','fear','sadness','joy'])[dominant_emotion_index]
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion_name
    }
    return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
    }



