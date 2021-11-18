import numpy as np

if __name__ == '__main__':
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([3, 2, 1])
    print(arr1 * arr2.reshape(3, 1))
