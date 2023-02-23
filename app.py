from flask import Flask,request,jsonify,abort,render_template
from flair.models import TextClassifier
from flair.data import Sentence

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/endpoint',methods=['POST','GET'])
def ai_endpoint():
    body = request.get_json()['data']
    data = {"pos": None,
"neg": None,
"neu": None,
"message": []
}

    try:
        sentence = Sentence(body)
        classifier = TextClassifier.load('sentiment')
        classifier.predict(sentence)
        for lable in sentence.labels:
            if lable.value == 'NEGATIVE':
                data['neg'] = lable.score
            elif lable.value == 'POSITIVE':
                data['neg'] = lable.score
            elif lable.value == 'NEUTRAL':
                data['neg'] = lable.score
            data['message'].append(lable.value)
    except:
        abort(500)
    return jsonify(data)


@app.errorhandler(500)
def bad_req(err):
    return jsonify({"neg":None,"pos":None,"neu":None,"message":"Could not processed request"})