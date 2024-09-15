""" This module implements a Flask web application for detecting emotions from text input """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Deploy as web application using Flask
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """ Takes text input to pass to emotion_detector function for analysis """

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Extract emotions from response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if dominant_emotion is None
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Build f-string with emotion scores if dominant_emotion is valid
    displayed_response = (f"For the given statement, the system reponse is 'anger': {anger}, "
    f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. "
    f"The dominant emotion is {dominant_emotion}.")

    # Return constructed response
    return displayed_response

@app.route("/")
def render_index_page():
    """ Render HTML template """
    return render_template('index.html')

# Run application on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
