"""necessary imports"""
from flask import Flask , request,  render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """returns the mood and the scores and also the dominant mood
    based on the text provided
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is not None:
        return f"For the given statement, the system response is 'anger': {response['anger']}, \
        'disgust': {response['anger']}, 'fear': {response['fear']}, 'joy': {response['joy']} and \
        'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    return "Invalid text! Please try again!"

@app.route("/")
def home():
    """redirects to the home page for 
    interacting with the applicataion"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
