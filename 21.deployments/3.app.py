csfrom flask import Flask
import tensorflow as tf
import requests

app = Flask(__name__)

@app.route('/pred/<x>')
def get_prediction(x):
    url = 'https://sentimentanalysis-s3bucket.s3.ap-south-1.amazonaws.com/my_model/model.h5'
    r = requests.get(url, allow_redirects=True)
    open('model.h5', 'wb').write(r.content)

    new_model = tf.keras.models.load_model('model.h5')
    temp = []
    temp.append(float(x))
    y = new_model.predict(temp)
    print(y)
    return str(y)

if __name__ == '__main__':
    app.run(host="0.0.0.0")