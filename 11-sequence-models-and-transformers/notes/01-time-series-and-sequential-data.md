# Time Series and Sequential Data

This note covers the first lecture in the sequence-model block.

The key idea is that some data has an internal order that cannot be ignored. In time-series and language tasks, the meaning of the current input depends on what came before it. That makes these problems different from standard tabular learning, where rows are often treated more independently.

The lecture gave examples such as:
- stock prices
- daily temperature records
- sentences in natural language

In all of these cases, sequence matters. A data point is not fully meaningful without its context.

This was also the lecture where I understood the term **time step** more clearly. A time step is simply one point in an ordered sequence. But the bigger lesson is that the model must preserve some memory of previous steps if it wants to perform well.

The lecture also used demand forecasting as an example of practical value. That made the topic feel grounded in business use cases rather than only theory.

My biggest takeaway is that sequential data requires architectures that respect order and carry memory forward. That is exactly why RNN-style models were introduced.
