
import os

import numpy as np
import tensorflow as tf

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # No error handline in this example, just simple query params

    x = request.args.get('x') or 3.0
    y = request.args.get('y') or 4.0

    # Getting Started with TensorFlow
    # https://www.tensorflow.org/get_started/get_started

    node1 = tf.constant(float(x), dtype=tf.float32)
    node2 = tf.constant(float(y))
    node3 = tf.add(node1, node2)

    with tf.Session() as sess:
        output = sess.run(node3)
        return jsonify(float(output))

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
