import sys
import matplotlib.pyplot as plt

nums = [float(c.strip()) for c in sys.stdin.read().strip().split()]
plt.hist(nums)
plt.savefig(sys.argv[1])
