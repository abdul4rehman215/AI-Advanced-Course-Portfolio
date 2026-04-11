# 🖼️ Convolutional Neural Networks

### My first focused computer vision block, where dense neural networks evolved into image-specialized architectures  
### Centered on CNN intuition, filters, kernels, pooling, and practical CIFAR-10 implementation

<div align="center">

<p>
  <img src="https://img.shields.io/badge/Section-Convolutional%20Neural%20Networks-00897B?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Lectures-27--28-26A69A?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Studied%20and%20Practiced-00C853?style=for-the-badge" />
</p>

<p>
  <img src="https://img.shields.io/badge/Topics-Filters%20%7C%20Kernels%20%7C%20Feature%20Maps-00796B?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Topics-Strides%20%7C%20Padding%20%7C%20Pooling-00695C?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Topics-CIFAR--10%20%7C%20Conv2D%20%7C%20Image%20Classification-3949AB?style=for-the-badge" />
</p>

</div>

---

# 📌 Section Overview

This section captures the point where the course moved from general artificial neural networks into a deep learning architecture designed specifically for image data.

After learning dense networks, it became clear why they are not ideal for image tasks. Flattening every pixel into a single long vector causes loss of spatial structure and creates a large number of parameters. CNNs solve that by learning local patterns with filters and then building increasingly complex feature hierarchies.

This block gave me both intuition and code-level understanding of computer vision basics:
- why fully connected networks are inefficient for images
- how filters and kernels move across an image
- how feature maps are generated
- why stride and padding matter
- how pooling reduces redundancy
- how a CNN is built and trained in practice on CIFAR-10

This was one of the most visually intuitive parts of the course and helped me understand how deep learning adapts to specific data types.

---

# 🎯 Lecture Coverage In This Section

| Lecture | Topic |
|--------|------|
| 27 | Introduction to Convolutional Neural Network |
| 28 | Convolutional Neural Network |

---

# 🧠 What I Studied In This Section

This section helped me understand:

- the limits of fully connected networks for image inputs
- how convolution preserves local spatial patterns
- filters, kernels, and feature detectors
- feature maps and hierarchical feature learning
- stride as movement step size
- padding as a way to preserve edge information
- max pooling and average pooling
- flattening before the dense classification head
- Conv2D-based modeling in TensorFlow/Keras
- CIFAR-10 workflow for image classification

One important lesson from this section is that CNNs do not “look at an image all at once” the same way a dense network does. They learn local structure first and then combine those local signals into higher-level visual understanding.

---

# 🧪 Notebook Coverage

```text
09-convolutional-neural-networks/notebooks/
└── 01_cifar10_cnn_basics.ipynb
```

This notebook represents my hands-on CNN practice and shows the move from ANN-based image handling toward a more image-native architecture.

---

# 📝 Notes Included In This Section

```text
09-convolutional-neural-networks/notes/
├── 01-why-cnn-over-fully-connected-networks.md
├── 02-filters-kernels-strides-padding-and-pooling.md
└── 03-cnn-training-and-cifar10-practice.md
```

---

# 🧩 Assignment Placement In This Section

```text
09-convolutional-neural-networks/
└── assignments/
    └── assignment-08-advanced-cnn-techniques/
        ├── README.md
        ├── assignment-brief.pdf
        └── Assignment_08_Abdul_Rehman.ipynb
```

The advanced CNN assignment belongs here because it extends the same image-focused architecture block introduced in lectures 27 and 28.

---

# 💡 Why This Section Matters

This section matters because CNNs are one of the most important building blocks in modern computer vision.

They show how neural network design changes depending on the structure of the data. That idea is important beyond images. It teaches me a bigger lesson: architecture should match the problem, not the other way around.

This section also strengthened my intuition for later topics such as:
- convolutional autoencoders
- image feature extraction
- deep learning model specialization
- practical visual pattern learning

---

# 🔗 Connection To The Next Stage

After CNNs, the course moves into autoencoders and then variational autoencoders.

That sequence made sense:
- ANN taught me general neural network training
- CNN taught me image-aware feature extraction
- autoencoders then reused neural network ideas for compression, reconstruction, and representation learning

So this section acts as the computer vision bridge into representation learning.

Next stage in the course: **Autoencoders and Variational Autoencoders**.
