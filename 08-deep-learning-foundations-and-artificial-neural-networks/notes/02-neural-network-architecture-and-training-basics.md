# Neural Network Architecture and Training Basics

This note covers the basic structure of neural networks and how information moves through them.

The course explained neural networks as systems built from neurons, where each neuron acts like a mathematical transformation unit. Those neurons are arranged into layers:
- input layer
- one or more hidden layers
- output layer

This architecture helps the model gradually transform raw input into a prediction. Each layer learns a different level of representation, and the hidden layers are where much of the useful pattern learning happens.

I also learned that these networks are sometimes referred to with different names depending on the context:
- fully connected neural networks
- feed-forward neural networks
- dense neural networks

That naming clarity was useful because I had seen these terms before and was not always sure whether they referred to the same idea or different ones.

The lecture also drew a line between training and inference. During inference, the model performs a forward pass to generate predictions. During training, a backward pass updates parameters so the predictions become better over time.

What made this topic strong was that it broke neural networks into understandable blocks. Instead of seeing them as mysterious black boxes, I started viewing them as layered computational systems with a learnable flow.
