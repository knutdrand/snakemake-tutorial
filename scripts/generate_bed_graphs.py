import numpy as np
indexes = np.cumsum(np.random.randint(0, 1000, 200))
starts = np.hstack(([0], indexes))
values = np.random.randint(-3, 3, 200)
for start, end, v in zip(starts[:-1], starts[1:], values):
    print("chr1\t%s\t%s\t%s" % (start, end, v))
