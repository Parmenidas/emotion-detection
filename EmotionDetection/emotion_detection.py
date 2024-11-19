# Import the requests library to handle HTTP requests
import requests  

# Import the JSON library to format response
import json

# Define a function named emotion detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):      
    # URL of the emotion prediction
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }  
    
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Extracting emotion and score from the response
        emotion_dict = formatted_response['emotionPredictions'][0]['emotion']

        # Find dominant emotion
        score = 0.0
        for key in emotion_dict:
            if (emotion_dict[key] > score):
                score = emotion_dict[key]
                dominant = key
        emotion_dict['dominant_emotion'] = dominant

    # If the response status code is 400, set score to None
    elif response.status_code == 400:
        emotion_dict = {'dominant_emotion':None}

    # Returning a dictionary containing the emotion analysis
    return emotion_dict
