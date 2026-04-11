# CNN Training and CIFAR-10 Practice

This note covers the practical side of the CNN section.

The course used CIFAR-10 as the working dataset, which was useful because it contains small color images from multiple classes. That made it a realistic introduction to image classification without being too advanced too early.

The workflow included:
- loading the CIFAR-10 dataset
- normalizing pixel values
- formatting labels properly
- defining a sequential CNN model
- adding convolutional layers
- using activation functions like ReLU
- reducing dimensions through pooling
- flattening the learned feature maps
- using dense layers for final classification
- compiling, fitting, and evaluating the model

What I liked in this practice was that it clearly showed how CNNs extend earlier ANN logic. The training loop, optimizer selection, and loss definition still matter, but now the architecture is more image-aware.

The lecture also reinforced that preprocessing still matters in deep learning. Normalization helps learning stability, and label formatting affects how the output layer and loss function behave.

Another useful takeaway was that CNN performance is not only about adding more layers. It is about choosing a sensible structure that extracts meaningful features while keeping training manageable.

This practical block gave me my first concrete implementation experience with an image-focused architecture instead of a general dense network.
