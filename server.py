''' Executing this function initiates the application of emotion
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.  
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    '''Detects emotions from input statement. Outputs score for each emotion
       and intifies dominant emotion    
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!"
    # Return a formatted string with the sentiment label and score
    return f"For the given statement, the system response is \
    'anger': {response['anger']},'disgust': {response['disgust']},\
    'fear': {response['fear']}, 'joy': {response['joy']} and \
    'sadness': {response['sadness']}.The dominant emotion is <b>{response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    '''Renders HTML page index.html
    '''
    return render_template('index.html')

if __name__ == "__main__":
    #This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
