import numpy as np
indexes = np.cumsum(np.random.randint(0, 1000, 200)).reshape(-1, 2)
for start, end in indexes:
    print("chr1\t%s\t%s" % (start, end))





