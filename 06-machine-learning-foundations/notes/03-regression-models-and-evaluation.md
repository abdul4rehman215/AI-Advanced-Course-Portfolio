# Regression Models and Evaluation

This note covers the regression lecture of the course and the shift from category prediction to numeric prediction.

Regression is used when the target is a continuous value, such as:
- house price
- sales amount
- score
- progression value

One of the main concepts introduced was linear regression. The course explained it as learning the best-fit relationship between features and the target variable. I also learned that the model tries to minimize prediction error through its cost function.

Another useful distinction was between univariate and multivariate regression:
- univariate uses one input feature
- multivariate uses multiple input features

The notebook section also introduced regression alternatives beyond linear regression:
- decision tree regressor
- random forest regressor
- gradient boosting regressor

This made it clear that regression is a broader modeling family, not just one formula.

Evaluation was also an important part of this lecture. A model should not only be trained. It should also be checked through performance metrics such as Mean Squared Error. Residual analysis also helps understand whether the model systematically overestimates or underestimates.

The biggest lesson from this topic is that model quality depends on the full chain:
- data preparation
- feature handling
- model selection
- evaluation

That makes regression a complete workflow rather than a single algorithm.
