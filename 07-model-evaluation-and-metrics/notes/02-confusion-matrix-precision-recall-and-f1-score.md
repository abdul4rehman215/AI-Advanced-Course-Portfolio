# Confusion Matrix, Precision, Recall, and F1-Score

This note covers the core classification metrics that helped me move beyond simple accuracy.

The confusion matrix is the foundation. It breaks predictions into four parts:
- true positives
- true negatives
- false positives
- false negatives

This structure is powerful because it shows exactly where a model is succeeding and where it is failing. Instead of seeing only one final percentage, I can inspect the kinds of errors the model is making.

From that base, precision and recall become easier to understand.

## Precision
Precision asks: **when the model predicts positive, how often is it correct?**  
This matters when false positives are costly. For example, if a system keeps flagging safe transactions as fraud, it creates unnecessary disruption.

## Recall
Recall asks: **out of all actual positive cases, how many did the model find?**  
This matters when false negatives are more dangerous. In a medical problem, missing a true case can be worse than raising an extra alert.

## F1-Score
F1-score combines precision and recall into one value using a harmonic mean. I found this especially useful as a balancing metric. It is helpful when I do not want to optimize only one side of the tradeoff.

The main lesson here is that metrics are not just formulas. They reflect priorities. Precision favors cautious positive predictions. Recall favors catching as many real positives as possible. F1-score helps when both matter and I need a more balanced view.

This topic made evaluation feel more practical and more human. Instead of thinking in abstract percentages, I started thinking in terms of consequences and tradeoffs.
