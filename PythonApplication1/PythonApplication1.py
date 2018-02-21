import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello).decode('utf-8'))

a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a + b))
