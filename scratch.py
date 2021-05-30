import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import matplotlib.pyplot as plt
learning_rate =0.01
epochs=1000
display_test=200
train_X = np.asarray([3.3, 4.4, 5.5, 6.71, 6.93, 4.168, 9.779, 6.182, 7.59, 2.167,
                      7.042, 10.791, 5.313, 7.997, 5.654, 9.27, 3.1])
train_y = np.asarray([1.7, 2.76, 2.09, 3.19, 1.694, 1.573, 3.366, 2.596, 2.53, 1.221,
                      2.827, 3.465, 1.65, 2.904, 2.42, 2.94, 1.3])
n_samples = train_X.shape[0]

# Test Data
test_X = np.asarray([6.83, 4.668, 8.9, 7.91, 5.7, 8.7, 3.1, 2.1])
test_y = np.asarray([1.84, 2.273, 3.2, 2.831, 2.92, 3.24, 1.35, 1.03])
x=tf.placeholder(tf.float32)
y=tf.placeholder(tf.float32)
w=tf.Variable(np.random.randn(),name="weight")
b=tf.Variable(np.random.randn(),name='bias')
linear_model=w*x+b
cost=tf.reduce_sum(tf.square(linear_model-y)/2*n_samples)
optimizer=tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
init=tf.global_variables_initializer()
sess=tf.Session()
sess.run(init)
for epoch in range(epochs):
    sess.run(optimizer,feed_dict={x:train_X,y:train_y})
    if(epoch+1)%display_test==0:
        c=sess.run(optimizer,feed_dict={x:train_X,y:train_y})
        print("Epoch:{0:6} \t Cost:{1:10.4} \t W:{2:6.4} \t b:{3:6.4}".
            format(epoch+1, c, sess.run(w), sess.run(b)))
print("Optimization Finished")
training_cost=sess.run(cost,feed_dict={x:train_X,y:train_y})
print(training_cost, "W:", sess.run(w), "b:",
      sess.run(b), '\n')
plt.plot(train_X, train_y, 'ro', label='Original data')
plt.plot(train_X, sess.run(w) * train_X + sess.run(b), label='Fitted line')
plt.legend()
plt.show()
testing_cost = sess.run(tf.reduce_sum(tf.square(linear_model - y)) / (2 * test_X.shape[0]),
                        feed_dict={x: test_X, y: test_y})

print("Final testing cost:", testing_cost)
print("Absolute mean square loss difference:", abs(training_cost - testing_cost))

# Display fitted line on test data
plt.plot(test_X, test_y, 'bo', label='Testing data')
plt.plot(train_X, sess.run(w) * train_X + sess.run(b), label='Fitted line')
plt.legend()
plt.show()
