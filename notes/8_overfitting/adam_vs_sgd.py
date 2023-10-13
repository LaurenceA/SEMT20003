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
y = t.sin(X) + 0.5*t.randn(N, 1)

plt.scatter(x=X, y=y, label='Data', c='k')
plt.xlabel('$x$')
plt.ylabel('$y$')
#plt.plot(xs, t.sin(xs), label='"True" (noise-free) line', c='r')

input_features = 1 
hidden_features = 100
output_features = 1 

def train(opt, opt_kwargs, col, label, alpha=1):
    net = nn.Sequential(
        nn.Linear(input_features, hidden_features),
        nn.ReLU(),
        nn.Linear(hidden_features, hidden_features),
        nn.ReLU(),
        nn.Linear(hidden_features, output_features)
    )
    opt = opt(net.parameters(), **opt_kwargs)

    for i in range(1000):
        i +=1
        L = ((net(X) - y)**2).mean()
        L.backward()
        opt.step()
        opt.zero_grad()

    plt.plot(xs, net(xs).detach(), c=col, label=label, alpha=alpha)

train(t.optim.SGD, {'lr': 0.03, 'momentum':0.8}, 'tab:blue', 'SGDM, lr=0.03, mom=0.03')
train(t.optim.Adam, {'lr': 0.03}, 'tab:orange', 'Adam, lr=0.03')


plt.legend()
plt.savefig(args.filename, bbox_inches='tight')
