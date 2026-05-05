import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=header)

    # formatted_response = json.loads(response)
    # print(formatted_response)
    # anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    # disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    # fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    # joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    # sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    # my_dict = formatted_response['emotionPredictions'][0]['emotion']
    # max_value = float('-inf') 
    # for key, value in my_dict.items():
    #     if value > max_value:
    #         max_value = value
    #         my_dict = {"name": "Alice"}
    #         my_dict["dominant_emotion"] = key
    # print(f"The highest value is: {max_value}")

    return response.text