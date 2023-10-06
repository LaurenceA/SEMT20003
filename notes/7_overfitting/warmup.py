import math
import torch as t
import torch.nn as nn
t.manual_seed(0)

import matplotlib.pyplot as plt 
plt.rcParams['text.usetex'] = True

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()

N = 20

xs = t.linspace(-5, 5, 100)[:, None]
X = t.linspace(-4, 4, N)[:, None]
y = t.sin(X) + 0.3*t.randn(N, 1)

plt.scatter(x=X, y=y, label='Data', c='tab:orange')
plt.xlabel('$x$')
plt.ylabel('$y$')
#plt.plot(xs, t.sin(xs), label='"True" (noise-free) line', c='r')

input_features = 1 
hidden_features = 100
output_features = 1 

net = nn.Sequential(
    nn.Linear(input_features, hidden_features),
    nn.ReLU(),
    nn.Linear(hidden_features, hidden_features),
    nn.ReLU(),
    nn.Linear(hidden_features, output_features)
)
#opt = t.optim.SGD(net.parameters(), lr=0.03, momentum=0.8)
opt = t.optim.Adam(net.parameters(), lr=0.03)

i = 0
lines = 5
exponent = 4
l = 1
plt.plot(xs, net(xs).detach(), c='k', alpha=1/(lines+1), label=f"NN; random init")
while l < lines:
    i +=1
    L = ((net(X) - y)**2).mean()
    L.backward()
    opt.step()
    opt.zero_grad()

    if math.log(i, exponent).is_integer() and i != 1:
        l += 1
        plt.plot(xs, net(xs).detach(), c='k', alpha=l/(lines+1), label=f"NN after {i} iters")

plt.legend()
plt.savefig(args.filename, bbox_inches='tight')
