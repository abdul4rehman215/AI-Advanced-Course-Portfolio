# Why Accuracy Is Not Enough

This note captures one of the most important mindset shifts in machine learning: a model cannot be judged only by its accuracy.

At first, accuracy feels like the easiest metric to trust. It simply tells me how many predictions were correct out of the total predictions. The problem is that this number can hide serious weaknesses when the dataset is imbalanced. If one class dominates the data, a model can predict that majority class again and again and still appear successful.

That is why this lecture mattered. It showed that high accuracy does not automatically mean a model has learned useful patterns. In some cases, the model may only be taking the easiest shortcut available in the data.

The lecture also connected this issue to underfitting and overfitting. Underfitting happens when the model is too simple and fails to capture the signal in the data. Overfitting happens when the model memorizes the training data too closely and cannot generalize well to unseen examples. A good model needs balance. It should learn enough to perform well without becoming too rigid or too dependent on training noise.

Another key takeaway was that evaluation should always be tied to the practical consequences of errors. A model used for a harmless recommendation system is very different from a model used in fraud detection or medical screening. In those high-stakes cases, the type of mistake matters as much as the number of mistakes.

My biggest lesson from this topic is that evaluation should start with a question: **what kind of failure would hurt the most in the real problem?** Once that is clear, the right metrics become easier to choose.
