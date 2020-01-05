from flask import Flask, render_template, request
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import pickle


app = Flask(__name__)

@app.route("/predict/<string:pickle_file_id>/",methods= ['POST'] )
def predict(pickle_file_id):
    if request.method == 'POST':
        x = request.form['inp']
        print(x)
    pickle_file = pickle_file_id + ".h5"
    model2 = load_model(pickle_file)
    model2._make_predict_function()

    with open('tokenizer2.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    with open('word_index2.pkl', 'rb') as handle:
      word_index = pickle.load(handle)

    MAX_SEQUENCE_LENGTH=200
    new_complaint = [x]
    seq = tokenizer.texts_to_sequences(new_complaint)
    padded = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH, padding='post')
    pred = model2.predict(padded)

    labels = ['Central Board of Direct Taxes (Income Tax)',
 'Central Board of Indirect Taxes and Customs',
 'Department of Defence',
 'Department of Defence Finance',
 'Department of Financial Services (Banking Division)',
 'Department of Financial Services (Insurance Division)',
 'Department of Health & Family Welfare',
 'Department of Higher Education',
 'Department of Personnel and Training',
 'Department of Posts',
 'Department of Telecommunications',
 'Government of Gujarat',
 'Government of Haryana',
 'Government of Madhya Pradesh',
 'Government of NCT of Delhi',
 'Government of Puducherry',
 'Government of Tamil Nadu',
 'Ministry of External Affairs',
 'Ministry of Home Affairs',
 'Ministry of Housing and Urban Affairs',
 'Ministry of Labour and Employment',
 'Ministry of Petroleum and Natural Gas',
 'Ministry of Railways ( Railway Board)']
    print(pred, labels[np.argmax(pred)])
    output1=labels[np.argmax(pred)]
    return output1

if __name__ == '__main__':
    app.run(debug=True)

