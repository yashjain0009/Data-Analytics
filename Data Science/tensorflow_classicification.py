import tensorflow as tf
import pandas as pd
train=pd.read_csv('/Users/yashjain/Downloads/Project/iris_training.csv')
test=pd.read_csv('/Users/yashjain/Downloads/Project/iris_test.csv')
train_y=train.pop("Species")
test_y=test.pop("Species")
def input_fn(features,labels,training=True,batch_size=256):
    dataset=tf.data.Dataset.from_tensor_slices((dict(features),labels))
    if training:
        dataset=dataset.shuffle(1000).repeat()
    return dataset.batch(batch_size)
my_feature_coloums=[]

for key in train.keys():
    my_feature_coloums.append(tf.feature_column.numeric_column(key=key))
classifier=tf.estimator.DNNClassifier(feature_columns=my_feature_coloums,hidden_units=[30,10],n_classes=3)
classifier.train(input_fn=lambda:input_fn(train,train_y,training=True),steps=5000)
eval_result =classifier.evaluate(input_fn=lambda:input_fn(test,test_y,training=False))
print eval_result
def input_fn2(features,batch_size=256):
    return tf.data.Dataset.from_tensor_slices(dict(features)).batch(batch_size)
features=['SepalLength','SepalWidth','PetalLength','PetalWidth']
predict={}
print 'Enter numeric values'
for feature in features:
    val=raw_input()
    predict[feature]=[float(val)]
print predict
result=classifier.predict(input_fn=lambda :input_fn2(predict))
for pred_dict in result:
    class_id=pred_dict['class_ids'][0]
    probability=pred_dict['probabilities'][class_id]
print probability
