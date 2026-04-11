# Hyperparameters, Loss, and Gradient Descent

This note captures the training logic of neural networks.

A neural network is not useful just because it has layers. It becomes useful only when its parameters are adjusted to reduce error. That is where loss functions and optimization enter the picture.

The loss function measures how far the model’s prediction is from the correct answer. The training objective is to reduce that loss over time. In the lectures, this was explained using the idea of moving downhill toward a lower error point, which made gradient descent easier to understand.

Gradient descent is the optimization process that updates model parameters in the direction that reduces loss. That update behavior depends heavily on hyperparameters, and this was one of the biggest practical lessons from the section.

The main hyperparameters I studied were:
- learning rate
- batch size
- number of epochs

Learning rate controls step size. If it is too high, training can become unstable. If it is too low, learning becomes slow and inefficient.

Batch size controls how much data is processed before weights are updated. It affects memory use, training speed, and gradient stability.

Epochs represent how many full passes the model makes over the dataset. More epochs can improve learning, but too many can also increase the risk of overfitting.

This topic helped me understand that neural network training is not only about architecture. It is also about controlling the learning process with the right training settings.
