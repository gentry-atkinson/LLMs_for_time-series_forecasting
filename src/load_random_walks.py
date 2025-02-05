import numpy as np

def load_random_walks(logger=None, series_length=500, num_walks=1000):
    walk_array = np.zeros((num_walks, series_length), dtype=np.float16)
    for row, _ in enumerate(walk_array):
        val = np.random.normal(0, 1, None)
        for i in range(series_length):
            walk_array[row, i] = val
            if np.random.normal(0, 1, None) < val:
                val -= 0.1
            else:
                val += 0.1

    if logger:
        logger.info(f"Shape of synthetic walks: {walk_array.shape}")
    else:
        print(f"Shape of synthetic walks: {walk_array.shape}")
        print("Sanity checks")
        print(f"Max of converted array: {np.max(walk_array)}")
        print(f"Min of converted array: {np.min(walk_array)}") 

    return walk_array   


if __name__ == '__main__':
    rw = load_random_walks()

    import matplotlib.pyplot as plt
    plt.plot(range(100), rw[0, :])
    plt.savefig('random_walk.png')