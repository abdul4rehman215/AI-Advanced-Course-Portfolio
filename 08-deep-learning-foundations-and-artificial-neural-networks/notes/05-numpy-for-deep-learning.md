# NumPy for Deep Learning

This note covers the NumPy prerequisite concepts that support later deep learning practice.

The lecture made it clear that NumPy is not optional for serious AI work. It is the base mathematical tool for representing and manipulating arrays, which means it sits underneath much of deep learning practice.

The main structures I studied were:
- scalars
- vectors
- matrices
- tensors

This progression was important because deep learning models work with high-dimensional numerical representations. If I do not understand shapes and dimensions, it becomes much harder to debug preprocessing or model input problems later.

Another useful concept was reshaping. The lecture showed that the same data can be reorganized into different structures as long as the total number of elements remains the same. That is very relevant in deep learning, especially when flattening image data or adapting arrays before feeding them into a model.

Indexing and slicing were also important because model inputs are often subsets, batches, or transformed pieces of larger arrays.

What I liked about this lecture is that it made the math feel more operational. Instead of thinking abstractly about tensors, I started seeing them as actual data objects that I can inspect, reshape, and prepare for models.

My biggest takeaway is simple: if I want to be strong in deep learning, I need to be comfortable with NumPy shapes, dimensions, and transformations.
