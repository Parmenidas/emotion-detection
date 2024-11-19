''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package 
from flask import Flask, render_template, request

# Import the emotion detector function
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it.
        The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion detector
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    label = response['dominant_emotion']
    
    # Check if the label is None, indicating an error or invalid input
    if label is None:
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the sentiment label and score
        return (f'''For the given statement, the system response is 'anger': {response['anger']}, 
        'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 
        'sadness': {response['sadness']}. The dominant emotion is <b>{response['dominant_emotion']}</b>.''')

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000 '''
    app.run(host="0.0.0.0", port=5000)
