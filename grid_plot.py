import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
y1 = [i * 2 for i in x]
y2 = [i ** 2 for i in x]
y3 = [i ** 0.5 for i in x]      # Square root of x
y4 = [10 - i for i in x]        # 10 minus x

# Figure and subplots
plt.figure(figsize=(10, 8))

# 1st plot
plt.subplot(2, 2, 1)
plt.plot(x, y1, color='blue', marker='o')
plt.title('Double of X')
plt.xlabel('Numbers')
plt.ylabel('2 * X')
plt.grid(True)

# 2nd plot
plt.subplot(2, 2, 2)
plt.plot(x, y2, color='green', marker='s')
plt.title('Square of X')
plt.xlabel('Numbers')
plt.ylabel('X²')
plt.grid(True)

# 3rd plot
plt.subplot(2, 2, 3)
plt.plot(x, y3, color='red', marker='^')
plt.title('Square Root of X')
plt.xlabel('Numbers')
plt.ylabel('√X')
plt.grid(True)

# 4th plot
plt.subplot(2, 2, 4)
plt.plot(x, y4, color='purple', marker='d')
plt.title('10 - X')
plt.xlabel('Numbers')
plt.ylabel('10 - X')
plt.grid(True)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
