# ROC, AUC, Specificity, and Model Evaluation Tradeoffs

This note covers the second evaluation lecture, where the course expanded from basic confusion-matrix metrics to more advanced analysis tools.

A major idea in this lecture was that binary classification often involves thresholds. A model may produce probabilities, and the final class label depends on where the cutoff is placed. Changing that cutoff changes the balance between true positives and false positives.

That is where the ROC curve becomes useful. It plots the true positive rate against the false positive rate across different thresholds. I understood it as a way to see how the model behaves across multiple operating points rather than at only one fixed decision boundary.

AUC, or Area Under the Curve, provides a single summary of that ROC behavior. A higher AUC means the model is generally better at separating positive and negative classes across thresholds. It is not the whole story, but it is a strong comparative signal.

Another useful term from this section was specificity. If recall focuses on how well the model catches actual positives, specificity focuses on how well it correctly identifies negatives. This made me realize that evaluation is often symmetric: one side of the problem looks at catching positives, and the other looks at protecting negatives from being mislabeled.

The lecture also reinforced the importance of false positive rate. This metric matters because it describes the cost of mistaken alerts. In some systems, too many false alarms can make the model impractical even if recall is high.

My main takeaway from this topic is that evaluation is a design choice. Different thresholds create different behaviors. So the real question is not only whether the model is strong, but also how I want it to behave in a real deployment setting.
