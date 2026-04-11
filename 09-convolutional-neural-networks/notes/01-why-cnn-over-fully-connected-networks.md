# Why CNN Over Fully Connected Networks

This note captures the main intuition behind the move from dense neural networks to convolutional neural networks.

A fully connected network treats every input value as equally connected to the next layer. That works for many structured problems, but with images it becomes inefficient very quickly. If every pixel is flattened into a long vector, the model loses the local structure of the image and also ends up with too many parameters.

That was one of the strongest ideas in this lecture: image data is spatial. Nearby pixels often matter together. Dense networks do not naturally preserve that relationship after flattening.

CNNs solve this by using small filters that slide across the image. Instead of learning from the whole image at once, they learn local patterns such as edges, corners, textures, and simple shapes. As layers go deeper, those patterns combine into more meaningful visual representations.

This makes CNNs more efficient and more aligned with the nature of the data. They use parameter sharing and local receptive fields, which reduces computational cost and helps the network focus on relevant visual structure.

My biggest takeaway is that CNNs are not just “bigger neural networks.” They are better structured for image learning because they preserve and exploit spatial relationships that dense networks tend to flatten away.
