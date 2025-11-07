Gradient Descent – Updates parameters by moving in the opposite direction of the gradient to minimize loss.

Stochastic Gradient Descent (SGD) – Updates weights after each training sample for faster but noisier convergence.

Mini-Batch Gradient Descent – Uses small batches of data to balance speed and stability in updates.

Momentum – Accelerates SGD by adding a fraction of the previous update to the current one.

Nesterov Accelerated Gradient (NAG) – Improves momentum by calculating the gradient after applying the momentum step.

Adagrad – Adapts learning rates for each parameter individually based on past gradients.

RMSProp – Uses a moving average of squared gradients to adjust learning rates dynamically.

Adam (Adaptive Moment Estimation) – Combines Momentum and RMSProp for efficient adaptive learning.

Adadelta – An extension of Adagrad that reduces aggressive, diminishing learning rates.

Nadam – A variant of Adam that incorporates Nesterov momentum for smoother convergence.
