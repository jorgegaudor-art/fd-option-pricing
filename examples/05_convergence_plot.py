from bs_fdm import price_european, price_bs
import numpy as np, matplotlib.pyplot as plt, time

S0,K,r,sigma,T = 100,100,0.02,0.20,1.0
ref = price_bs(S0,K,r,sigma,T,'call')

# a simple sequence of grids (more nodes -> smaller error)
Ms = [60, 100, 160, 240, 360]
Ns = [300, 700, 1200, 1800, 2600]  # roughly grows with M to balance dt and dS

errs, times = [], []
for M, N in zip(Ms, Ns):
    t0 = time.time()
    price, _ = price_european(S0, K, r, sigma, T, kind='call', scheme='cn', M=M, N=N)
    times.append(time.time() - t0)
    errs.append(abs(price - ref))

plt.figure()
plt.loglog(Ms, errs, marker='o')
plt.xlabel('M (space nodes)')
plt.ylabel('abs error vs BS')
plt.title('Convergence (Crank–Nicolson + Rannacher)')
plt.grid(True, which='both', ls=':')
plt.tight_layout()
plt.savefig('examples/convergence_error.png', dpi=140)
print('Saved: examples/convergence_error.png')
