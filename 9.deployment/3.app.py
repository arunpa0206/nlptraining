from flask import Flask
import tensorflow as tf
import requests

app = Flask(__name__)

@app.route('/getweight/<normalizedheight>')
def get_prediction(normalizedheight):
    url = 'https://sentimentanalysis-s3bucket.s3.ap-south-1.amazonaws.com/my_model/model.h5'
    r = requests.get(url, allow_redirects=True)
    open('model.h5', 'wb').write(r.content)

    new_model = tf.keras.models.load_model('model.h5')
    list_of_normalized_heights = []
    list_of_normalized_heights.append(float(normalizedheight))
    normalizedweight = new_model.predict(list_of_normalized_heights)
    print(normalizedweight)
    return str(normalizedweight)

if __name__ == '__main__':
    app.run(host="0.0.0.0")