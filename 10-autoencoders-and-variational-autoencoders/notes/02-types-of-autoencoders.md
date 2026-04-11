# Types of Autoencoders

This note covers the main autoencoder variants discussed in the course.

## Vanilla Autoencoder
This is the simplest version. It usually relies on dense layers and is useful for basic compression, dimensionality reduction, and anomaly-style reconstruction tasks.

## Denoising Autoencoder
This version takes a corrupted input and learns to reconstruct the clean version. I found this especially practical because it shows how autoencoders can be trained to ignore noise rather than simply memorize raw input.

## Convolutional Autoencoder
This version uses convolutional layers, which makes it much stronger for image data. Instead of relying only on dense compression, it learns spatial structure more effectively.

## Variational Autoencoder
This was the most important variant in the section because it pushed the topic toward generative AI. Instead of mapping an input to a single fixed point in latent space, a VAE learns a probability distribution and samples from it.

The main lesson from this topic is that autoencoders are not a single rigid model. The same encoder-decoder idea can be adapted based on the task:
- compression
- denoising
- feature extraction
- image representation
- data generation

This made the architecture feel much more flexible and useful than I initially expected.
