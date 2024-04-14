# Définition des constantes et des variables partagées

# Vous pouvez définir ici toutes les variables communes et les constantes
# utilisées dans les sous-routines.

import numpy as np

# Définition des paramètres
nmodel = 128
nn = nmodel
m = nmodel
nc = nmodel // 2 + 1
idi = 2
irsiz = 4 * nmodel * nmodel

# Définition des tableaux
uu1 = np.zeros((nn, m), dtype=float)
vv1 = np.zeros((nn, m), dtype=float)
eta1 = np.zeros((nn, m), dtype=float)
zeta1 = np.zeros((nn, m), dtype=float)
ekin1 = np.zeros((nn, m), dtype=float)

uu2 = np.zeros((nn, m), dtype=float)
vv2 = np.zeros((nn, m), dtype=float)
eta2 = np.zeros((nn, m), dtype=float)
zeta2 = np.zeros((nn, m), dtype=float)
ekin2 = np.zeros((nn, m), dtype=float)

wk = np.zeros((nn, m), dtype=float)
wk2 = np.zeros((nn, m), dtype=float)
wk3 = np.zeros((nn, m), dtype=float)
wk4 = np.zeros((nn, m), dtype=float)
wk5 = np.zeros((nn, m), dtype=float)
wk6 = np.zeros((nn, m), dtype=float)

wl = np.zeros((nn, m), dtype=float)
wl2 = np.zeros((nn, m), dtype=float)
wl3 = np.zeros((nn, m), dtype=float)
wl4 = np.zeros((nn, m), dtype=float)
wl5 = np.zeros((nn, m), dtype=float)
wl6 = np.zeros((nn, m), dtype=float)

wv = np.zeros((nc, m), dtype=float)
frc1 = np.zeros((nc, m), dtype=float)
frc2 = np.zeros((nc, m), dtype=float)
trunc = np.zeros((nc, m), dtype=float)

fnau = 0.0
bet = 0.0
gp1 = 0.0
gp2 = 0.0
epasl = 0.0
ddtm1 = 0.0
ddtm1s2 = 0.0

uu1c = np.zeros((nc, m), dtype=complex)
vv1c = np.zeros((nc, m), dtype=complex)
eta1c = np.zeros((nc, m), dtype=complex)
zeta1c = np.zeros((nc, m), dtype=complex)
ekin1c = np.zeros((nc, m), dtype=complex)

uu2c = np.zeros((nc, m), dtype=complex)
vv2c = np.zeros((nc, m), dtype=complex)
eta2c = np.zeros((nc, m), dtype=complex)
zeta2c = np.zeros((nc, m), dtype=complex)
ekin2c = np.zeros((nc, m), dtype=complex)

wk6c = np.zeros((nc, m), dtype=complex)
wl6c = np.zeros((nc, m), dtype=complex)

uu1mc = np.zeros((nc, m), dtype=complex)
vv1mc = np.zeros((nc, m), dtype=complex)
eta1mc = np.zeros((nc, m), dtype=complex)

uu2mc = np.zeros((nc, m), dtype=complex)
vv2mc = np.zeros((nc, m), dtype=complex)
eta2mc = np.zeros((nc, m), dtype=complex)

uu1o2c = np.zeros((nc, m), dtype=complex)
uu1o1c = np.zeros((nc, m), dtype=complex)
vv1o2c = np.zeros((nc, m), dtype=complex)
vv1o1c = np.zeros((nc, m), dtype=complex)
eta1o2c = np.zeros((nc, m), dtype=complex)
eta1o1c = np.zeros((nc, m), dtype=complex)

uu2o2c = np.zeros((nc, m), dtype=complex)
uu2o1c = np.zeros((nc, m), dtype=complex)
vv2o2c = np.zeros((nc, m), dtype=complex)
vv2o1c = np.zeros((nc, m), dtype=complex)
eta2o2c = np.zeros((nc, m), dtype=complex)
eta2o1c = np.zeros((nc, m), dtype=complex)

kc = np.zeros(nc, dtype=complex)
lc = np.zeros(m, dtype=complex)

n = np.zeros(2, dtype=int)
neul = 0
nstep = 0
ndif1 = 0
ndifa1 = 0
ndif2 = 0
ndifa2 = 0
ntot = 0
nout = 0

# Équivalences
uu1c = uu1
vv1c = vv1
eta1c = eta1
uu2c = uu2
vv2c = vv2
eta2c = eta2
zeta1c = zeta1
ekin1c = ekin1
zeta2c = zeta2
ekin2c = ekin2
wkc = wk
wk2c = wk2
wk3c = wk3
wk4c = wk4
wk5c = wk5
wk6c = wk6
wlc = wl
wl2c = wl2
wl3c = wl3
wl4c = wl4
wl5c = wl5
wl6c = wl6

# Variables communes
xl = 0.0
yl = 0.0
fnau = 0.0
bet = 0.0
epasl = 0.0
h10 = 0.0
h20 = 0.0
gp1 = 0.0
gp2 = 0.0
ddt = 0.0
ddtm1 = 0.0
ddtm1s2 = 0.0
drk1 = 0.0
drka1 = 0.0
drk2 = 0.0
drka2 = 0.0
n = np.zeros(2, dtype=int)
ntot = 0
nout = 0
nstep = 0
neul = 0
ndif1 = 0
ndifa1 = 0
ndif2 = 0
ndifa2 = 0

# Fonctions utilitaires communes
def get_arg(index):
    # Implémentez la logique pour obtenir les arguments du programme ici
    pass