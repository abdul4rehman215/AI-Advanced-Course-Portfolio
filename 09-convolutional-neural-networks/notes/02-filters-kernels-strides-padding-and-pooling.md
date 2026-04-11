# Filters, Kernels, Strides, Padding, and Pooling

This note covers the main operational concepts inside a CNN.

The lecture explained that filters, kernels, and feature detectors are closely related terms. They refer to small matrices that slide across the image and detect patterns. When the filter interacts with the image, it produces a feature map that highlights where certain patterns appear.

This helped me understand convolution in a more visual way. Instead of imagining the model as reading one huge image array, I started imagining it scanning for useful local signals.

Two other concepts were especially important:

## Stride
Stride defines how far the filter moves at each step. A larger stride reduces output size faster, but it can also skip information.

## Padding
Padding adds extra border values around the image. This helps preserve information near the edges and can keep output dimensions more stable.

Then the lecture moved to pooling. Pooling reduces dimensionality by summarizing local regions. Max pooling keeps the strongest signal in a region, while average pooling takes the mean. The main idea is to reduce redundant detail while retaining important features.

Together, these operations make CNNs efficient:
- convolution extracts patterns
- stride controls movement and output size
- padding protects edge information
- pooling compresses the representation

This topic made the internal mechanics of CNNs much easier to picture.
