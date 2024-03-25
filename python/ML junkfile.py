import time
import numpy as np
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random samples
samples = np.random.randn(1000)

# Calculate mean and standard deviation
mean = np.mean(samples)
std_dev = np.std(samples)

# Define range based on 3 standard deviations
lower_bound = mean - 3 * std_dev
upper_bound = mean + 3 * std_dev

# Count values within the range
in_range_count = np.sum((samples >= lower_bound) & (samples <= upper_bound))

# Calculate percentage within the range
percentage_in_range = (in_range_count / len(samples)) * 100

# Print results
print("Mean:", mean)
print("Standard Deviation:", std_dev)
print(f"Range (3 standard deviations): [{lower_bound:.4f}, {upper_bound:.4f}]")
print(f"Percentage of samples within range: {percentage_in_range:.2f}%")

# Optional: Plot the distribution for visualization
plt.hist(samples, bins=50, density=True)  # Normalize to show probability density
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Distribution of 1000 Samples from a Standard Normal Distribution')
plt.axvline(x=mean, color='r', linestyle='dashed', linewidth=2, label=f'Mean ({mean:.2f})')
plt.axvline(x=lower_bound, color='g', linestyle='--', linewidth=1, label=f'Lower Bound ({lower_bound:.2f})')
plt.axvline(x=upper_bound, color='g', linestyle='--', linewidth=1, label=f'Upper Bound ({upper_bound:.2f})')
plt.legend()
plt.show()

# class Perceptron:

#     def __init__(self, inputs: list, target_output: int):
#         super().__init__()  # Call the parent class constructor (if applicable)
#         self.inputs = inputs
#         self.target_output = target_output
#         self.weights = [random.randrange(-1, 2) for _ in range(len(inputs))]  # Initialize random weights between -1 and 1

#     def forward_pass(self):
#         weighted_sum = sum([x * w for x, w in zip(self.inputs, self.weights)])
#         activation = 1 / (1 + math.exp(-weighted_sum))  # Sigmoid activation function
#         output = activation
#         return output

#     def backward_pass(self):
#         output = self.forward_pass()
#         error = 0.5 * (self.target_output - output) ** 2
#         learning_rate = 0.1  # Hyperparameter to control update step size

#         # Update weights using gradient descent with sigmoid derivative
#         new_weights = []
#         for i, (x, w) in enumerate(zip(self.inputs, self.weights)):
#             delta_w = learning_rate * error * output * (1 - output) * x
#             new_w = w - delta_w
#             new_weights.append(new_w)

#         # Update weights array
#         self.weights = new_weights
#         return error

#     def train(self, epochs: int):
#         forward_pass_errors = []  # Store errors from forward pass
#         backward_pass_errors = []  # Store errors from backward pass

#         for _ in range(epochs):
#             output = self.forward_pass()
#             forward_pass_errors.append(output)  # Append forward pass error
#             error = self.backward_pass()
#             backward_pass_errors.append(error)  # Append backward pass error

#         return forward_pass_errors, backward_pass_errors  # Return both errors


# # Example usage
# inputs = [1.0, 0.7]
# output = 1
# error_fp, error_bp = Perceptron(inputs, output).train(100)  # Train for 100 epochs (iterations)
# print("Forward pass error is:", error_fp)
# print("After Backpropagation error is:", error_bp)


# a = np.random.rand(1000000)
# b = np.random.rand(1000000)

# tic = time.time()
# c=np.dot(a,b)
# toc = time.time()

# print('vectorized version'+str(1000*(toc-tic))+'ms',c)

# c=0
# tic=time.time()
# for i in range(1000000):
#     c += a[i]*b[i]
# toc=time.time()

# print('non-vectorized version'+str(1000*(toc-tic))+'ms',c)

# # Create a 1D array of 5 zeros (float by default)
# array_1d = np.zeros(5)
# print(array_1d)  # Output: [0. 0. 0. 0. 0.]

# # Create a 2D array with 2 rows and 3 columns filled with zeros
# array_2d = np.zeros((2, 3))
# print(array_2d)  # Output: [[0. 0. 0.]
#                  #        [0. 0. 0.]]

# # Create a 3D array with shape (3, 4, 2) filled with integers
# array_3d = np.zeros((3, 4, 2))
# print(array_3d.shape)  # Output: (3, 4, 2)

# # Set the random seed to 0
# np.random.seed(0)

# # Generate a random array of 5 integers between 0 and 9
# random_array = np.random.randint(0, 10, 6)

# print(random_array)

# A=np.array([[1,2,3],
#             [4,5,6]])

# B=A.reshape(3,2)
# print(B)

# a = np.array([[1,2],[3,4]])
# b=np.array([[5,6],[7,8]])
# c=np.dot(a,b)
# print(a,b,c)

# x = np.array([
#     [9, 2, 5, 0, 0],
#     [7, 5, 0, 0 ,0]])

# x_sum=np.sum(x,axis=1)
# x_sum2=np.sum(x,axis=0)
# print(x_sum,x_sum2)      

