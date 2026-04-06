# Classification Models

This note covers the lecture where several core classification models were explained and compared.

## Logistic Regression
Despite the name, logistic regression is used for classification. It models probabilities and often uses a threshold to decide between classes. It is especially useful for binary classification problems.

## Decision Trees
Decision trees split the data based on conditions at each node. They are intuitive because they resemble human decision-making paths. Metrics like Gini impurity and information gain help decide how splits are made.

## Random Forest
Random forest improves on a single decision tree by creating many trees and combining their decisions. This helps reduce instability and improve robustness.

## Gradient Boosting
Gradient boosting builds trees sequentially, where each new tree tries to improve the mistakes made by the previous ones. This often leads to strong predictive performance.

The notebook workflow also reinforced important steps:
- separating features and target
- scaling when needed
- train-test splitting
- fitting multiple models
- comparing performance

This topic helped me understand that classification is not only about choosing one algorithm. It is about understanding how different models behave and why one may perform better than another for a given dataset.
