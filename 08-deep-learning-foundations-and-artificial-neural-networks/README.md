# 🧠 Deep Learning Foundations and Artificial Neural Networks

### My transition from classical machine learning into neural networks, tensor thinking, and practical ANN training  
### Focused on why deep learning matters, how neural networks learn, and how I practiced ANN workflows with Fashion MNIST and CIFAR-10

<div align="center">

<p>
  <img src="https://img.shields.io/badge/Section-Deep%20Learning%20Foundations%20%26%20ANN-6A1B9A?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Lectures-22--26-8E24AA?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Studied%20and%20Practiced-00C853?style=for-the-badge" />
</p>

<p>
  <img src="https://img.shields.io/badge/Topics-Deep%20Learning%20vs%20ML%20%7C%20Neurons%20%7C%20ReLU-7B1FA2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Topics-Loss%20%7C%20Gradient%20Descent%20%7C%20Hyperparameters-5E35B1?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Topics-NumPy%20%7C%20TensorFlow%20%7C%20Fashion%20MNIST%20%7C%20CIFAR--10-3949AB?style=for-the-badge" />
</p>

</div>

---

# 📌 Section Overview

This section marks the real entry point into deep learning in my course journey.

Up to this point, I had already worked through machine learning foundations and evaluation metrics. This new block introduced the idea that classical machine learning has real limitations when the data becomes high-dimensional, unstructured, or too complex for manual feature engineering. Deep learning was presented as the response to that problem.

The section combines theory and practice:
- why deep learning rose beyond conventional ML
- how neural networks are structured
- how forward propagation and backpropagation work
- how learning rate, epochs, and batch size affect model behavior
- why NumPy matters as the mathematical backbone
- how ANN models are actually built and trained in TensorFlow/Keras

This section gave me my first strong practical understanding of what happens inside a deep learning workflow instead of just using the term “neural network” as a buzzword.

---

# 🎯 Lecture Coverage In This Section

| Lecture | Topic |
|--------|------|
| 22 | Introduction to Deep Learning |
| 23 | Basics of Deep Learning |
| 24 | Deep Learning / RAG Series 1 |
| 25 | Deep Learning - ANN |
| 26 | Artificial Neural Networks + NumPy prerequisite context |

---

# 🧠 What I Studied In This Section

This section helped me understand:

- why deep learning became necessary beyond classical ML
- the limitations of traditional feature engineering on unstructured data
- the idea of neurons as mathematical functions
- input, hidden, and output layers
- activation functions, especially ReLU
- forward pass and backward pass
- parameters versus hyperparameters
- loss minimization and gradient descent
- batch size, learning rate, and epochs
- the role of NumPy arrays, vectors, matrices, and tensors
- TensorFlow/Keras model building flow
- Fashion MNIST and CIFAR-10 as practical ANN datasets

One thing I especially liked about this block was that it kept linking theory to implementation. The lectures did not only define neural networks. They also showed how those ideas become actual code.

---

# 🧪 Notebook Coverage

```text
08-deep-learning-foundations-and-artificial-neural-networks/notebooks/
├── 01_fashion_mnist_fully_connected_baseline.ipynb
└── 02_cifar10_dense_neural_network.ipynb
```

These notebooks represent my early hands-on practice with dense neural networks. They show the shift from concept learning into actual model building, training, and evaluation.

---

# 📝 Notes Included In This Section

```text
08-deep-learning-foundations-and-artificial-neural-networks/notes/
├── 01-why-deep-learning-over-traditional-machine-learning.md
├── 02-neural-network-architecture-and-training-basics.md
├── 03-hyperparameters-loss-and-gradient-descent.md
├── 04-deep-learning-rag-series-1-and-industry-context.md
├── 05-numpy-for-deep-learning.md
└── 06-artificial-neural-networks-with-fashion-mnist-and-cifar10.md
```

---

# 🧩 Assignment Placement In This Section

```text
08-deep-learning-foundations-and-artificial-neural-networks/
└── assignments/
    └── assignment-06-simple-ann-deep-learning/
        ├── README.md
        ├── assignment-brief.pdf
        └── Assignment_06_Abdul_Rehman.ipynb
```

The ANN assignment belongs in this section because it directly matches the theoretical and practical content of lectures 22–26.

---

# 💡 Why This Section Matters

This section matters because it transformed deep learning from a vague concept into a concrete workflow.

Before this stage, I knew that neural networks existed. After this stage, I had a much clearer understanding of:
- why they are needed
- what problem they solve
- how they are structured
- how they learn
- how they are trained in code

It also gave me the mathematical and implementation confidence to continue into CNNs, autoencoders, sequence models, and transformers.

This is one of the most important foundational blocks in the later half of the course.

---

# 🔗 Connection To The Next Stage

After learning dense neural networks, the course naturally moves into Convolutional Neural Networks.

That progression also made sense to me:
- dense networks helped me understand ANN basics
- CNNs then specialized those ideas for image data
- later sections moved into representation learning and sequence learning

So this section is the core ANN foundation that supports the entire later deep learning roadmap.

Next stage in the course: **Convolutional Neural Networks**.
