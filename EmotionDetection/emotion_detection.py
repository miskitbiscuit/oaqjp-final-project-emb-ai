import requests # Import requests library to handle HTTP requests
import json

# Define emotion_detector function that takes string input (text_to_analyze)
def emotion_detector(text_to_analyze):
    # Define url for emotion prediction API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Construct request payload in expected format
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Set headers with required model ID for API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Send POST request to API with text and headers
    response = requests.post(url, json = myobj, headers=header)
    # Parse JSON response from API
    formatted_response = json.loads(response.text)

    # Check response status code
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Extract emotion scores from response
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions ['fear']
    joy_score = emotions ['joy']
    sadness_score = emotions['sadness']

    # Create dictionary of emotion scores
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    # Determine highest score in emotion_scores
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return dictionary containing emotion detection results
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }