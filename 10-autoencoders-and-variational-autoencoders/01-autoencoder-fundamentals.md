# Autoencoder Fundamentals

This note covers the core idea of an autoencoder.

An autoencoder is a neural network built around two main parts:
- an encoder
- a decoder

The encoder compresses the input into a smaller representation. The decoder then tries to reconstruct the original input from that compressed form. This makes the architecture different from classification models, where the goal is usually to predict an external target label.

What I found interesting is that the training target is the input itself. The model is essentially learning an identity-like function, but under a compression constraint. That compression forces the network to keep only the most useful information.

The course described this compact internal representation using terms like:
- latent representation
- bottleneck
- hidden representation

That helped me understand that the most important thing is not only the final reconstruction, but also what the model learns in that compressed middle space.

Another useful idea was that once the encoder is trained well, it can be reused as a feature extractor. That means autoencoders are not only for reconstruction. They can also support downstream tasks where a compact learned representation is useful.

My biggest takeaway is that autoencoders train a network to understand structure, not just labels.
