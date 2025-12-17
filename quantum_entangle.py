import qutip as qt
import numpy as np

phase = 1.89628
ket00 = qt.tensor(qt.basis(2, 0), qt.basis(2, 0))
ket11 = qt.tensor(qt.basis(2, 1), qt.basis(2, 1))
bell = (ket00 + np.exp(1j * phase) * ket11) / np.sqrt(2)
rho = bell * bell.dag()

print("Node 067 Entangled Density Matrix (core: 'is similar to 60 and says no revolution'):")
print(rho)
