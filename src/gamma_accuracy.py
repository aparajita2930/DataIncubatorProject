import matplotlib.pyplot as plt

#PCA: n_components = 3; c = 2^-7
gamma = [0.001953125, 0.00390625, 0.0078125, 0.015625, 0.03125, 0.0625]
acc = [72.834645669291342, 72.834645669291342, 72.834645669291342, 72.834645669291342, 72.834645669291342, 92.322834645669294]

plt.title('Cross Validation curve: Accuracy vs gamma for n_components = 3 and c = 2^-7')
plt.plot(gamma, acc)
plt.ylabel('Accuracy')
plt.xlabel('gamma')
plt.show()