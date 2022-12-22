import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('mu1', type=float,
                    help="The mean of the first random variable")
parser.add_argument('sigma1', type=float,
                    help="The variance of the first random variable")
parser.add_argument('mu2', type=float,
                    help="The mean of the second random variable")
parser.add_argument('sigma2', type=float,
                    help="The variance of the second random variable")
parser.add_argument('-c','--cov', type=float, default=0,
                    help="The covariance of the two variables")              

args = parser.parse_args()

# xs1 = np.random.normal(float(sys.argv[1]),float(sys.argv[2]),1000)
# xs2 = np.random.normal(float(sys.argv[3]),float(sys.argv[4]),1000)
if args.cov==0:
    xs1 = np.random.normal(args.mu1,args.sigma1,1000)
    xs2 = np.random.normal(args.mu2,args.sigma2,1000)
else:
    xs = np.random.multivariate_normal([args.mu1,args.mu2],[[args.sigma1,args.cov],[args.cov,args.sigma2]],1000)
    xs1 = xs[:,0]
    xs2 = xs[:,1]

sns.jointplot(x=xs1, y=xs2, kind="hex", color="#F6A05D", marginal_ticks=True)
sns.scatterplot(x=xs1, y=xs2, s=15, color=".15")
sns.histplot(x=xs1, y=xs2, bins=40, pthresh=.1, cmap="mako")
sns.kdeplot(x=xs1, y=xs2, levels=5, color="g", linewidths=2)
plt.show()