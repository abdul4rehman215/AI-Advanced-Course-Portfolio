# Artificial Neural Networks with Fashion MNIST and CIFAR-10

This note covers the practical ANN work from the section.

The lectures used datasets like Fashion MNIST and CIFAR-10 to turn theory into implementation. That was important because it showed how neural network ideas become an actual workflow in TensorFlow and Keras.

The process included:
- loading the dataset
- splitting training and testing data
- visualizing samples
- normalizing pixel values
- flattening image inputs where needed
- defining a sequential model
- adding dense layers with activation functions
- compiling the model
- fitting the model
- evaluating performance

Fashion MNIST was a useful starting point because it allowed the model to classify clothing images using a relatively straightforward structure. CIFAR-10 added more complexity because the images are color-based and the classification space is broader.

I also learned why preprocessing matters even in deep learning. Normalization helps the model train more efficiently. Flattening changes the representation so it can be consumed by dense layers. Label formatting also matters for the output structure and loss function.

Another strong takeaway was the comparison between training accuracy and testing accuracy. That comparison helps reveal whether the network is generalizing well or only memorizing the training set.

This practical block was valuable because it made ANN training feel real. I was no longer only learning definitions. I was seeing the full model-building pipeline from data to predictions.
