# Sous-routine swfft

import numpy as np

def swfft(s, st, n, idim, isign, ifact, xl, yl, nc):
    dx = xl / n[0]
    dy = yl / n[1]
    
    if isign == -1:
        fort2(st, n, idim, isign, ifact)
        for j in range(1, n[1] + 1):
            for i in range(1, n[0] + 1):
                k = i + (j - 1) * n[0]
                s[k - 1] = s[k - 1] / (xl * yl)
    else:
        fort2(s, n, idim, isign, ifact)
        for j in range(1, n[1] + 1):
            for i in range(1, nc + 1):
                k = i + (j - 1) * nc
                st[k - 1] = st[k - 1] * dx * dy

def fixrl(data, n, nrem, isign, iform):
    tpi = 6.28318530717956865 * isign
    
    ip0 = 2
    ip1 = ip0 * n // 2
    ip2 = ip1 * nrem
    
    if iform != 0:
        j1 = ip1 + 1
        data[1] = data[j1]
        
        if nrem != 1:
            j1 += ip0
            i2min = ip1 + 1
            for i2 in range(i2min, ip2 + 1, ip1):
                data[i2] = data[j1]
                j1 += ip0
                
                if n == 2:
                    break
                    
    ip3 = ip1
    for j in range(1, nfact + 1):
        ip2 = ip3 // 2
        ip4 = ip2 * 2
        
        ip3 = ip2
        while ip3 < ip1:
            for i4 in range(1, ip4 + 1, ip1):
                i4rev = 1
                
                for i1 in range(i4, i4 + ip1, ip0):
                    for i5 in range(i1, ip5 + 1, ip3):
                        i5rev = i4rev + i5 - i4
                        tempr = data[i5]
                        data[i5] = data[i5rev]
                        data[i5rev] = tempr
                        
                        i5rev1 = i5rev + 1
                        tempr = data[i5 + 1]
                        data[i5 + 1] = data[i5rev1]
                        data[i5rev1] = tempr
                        
                    i4rev += ip2
            ip3 *= 2
            
def symrv(data, nprev, n, nrem):
    ip0 = 2
    ip1 = ip0 * nprev
    ip4 = ip1 * n
    ip5 = ip4 * nrem
    
    for i4 in range(1, ip4 + 1, ip1):
        i4rev = 1
        ip3 = ip4
        for ifac in range(1, nfact + 1):
            ip2 = ip3 // 2
            i4rev += ip2
            if i4rev >= ip3:
                i4rev -= ip3
            ip3 = ip2
            
            while ip3 > ip2:
                ip3 = ip2
                ip2 //= 2
                
                for i1 in range(i4, i4 + ip1, ip0):
                    for i5 in range(i1, ip5 + 1, ip3):
                        i5rev = i4rev + i5 - i4
                        tempr = data[i5]
                        data[i5] = data[i5rev]
                        data[i5rev] = tempr
                        
                        i5rev1 = i5rev + 1
                        tempr = data[i5 + 1]
                        data[i5 + 1] = data[i5rev1]
                        data[i5rev1] = tempr

def cool(data, nprev, n, nrem, isign):
    tpi = 6.2831853071795865 * isign
    ipo = 2
    ip1 = ipo * nprev
    ip4 = ip1 * n
    ip5 = ip4 * nrem
    ifact = 0
    ip2 = ip1
    
    while ip2 - ip4 < 0:
        ifact += 1
        ifcur = 2 if (4 * ip2 - ip4) else 4
        
        ip3 = ip2 * ifcur
        rootr = -2. * np.sin(tpi / (2. * float(ifcur))) ** 2
        rooti = np.sin(tpi / float(ifcur))
        wstpr = -2. * np.sin(tpi / (float(ip3 / ip1) * 2.)) ** 2
        wstpi = np.sin(tpi / float(ip3 / ip1))
        wr = 1.
        wi = 0.
        
        for i2 in range(1, ip2 + 1, ip1):
            if ifcur == 4:
                if (i2 - 1) * (ifcur - 2) >= 0:
                    ip2 = ip3
                else:
                    w2r = wr * wr - wi * wi
                    w2i = 2. * wr * wi
                    w3r = w2r * wr - w2i * wi
                    w3i = w2r * wi + w2i * wr
                    
                    i1max = i2 + ip1 - ipo
                    for i1 in range(i2, i1max + 1, ipo):
                        i5 = i1
                        j0 = i5
                        j1 = j0 + ipo
                        j2 = j1 + ipo
                        j3 = j2 + ipo
                        
                        if i2 <= 1:
                            if ifcur < 3:
                                tempr = data[j3]
                                data[j3] = w3r * tempr - w3i * data[j3 + 1]
                                data[j3 + 1] = w3r * data[j3 + 1] + w3i * tempr
                                
                                tempr = data[j2]
                                data[j2] = wr * tempr - wi * data[j2 + 1]
                                data[j2 + 1] = wr * data[j2 + 1] + wi * tempr
                                
                                tempr = data[j1]
                                data[j1] = w2r * tempr - w2i * data[j1 + 1]
                                data[j1 + 1] = w2r * data[j1 + 1] + w2i * tempr
                            else:
                                tempr = data[j1]
                                data[j1] = wr * tempr - wi * data[j1 + 1]
                                data[j1 + 1] = wr * data[j1 + 1] + wi * tempr
                        else:
                            if ifcur > 3:
                                tor = data[j0] + data[j1]
                                toi = data[j0 + 1] + data[j1 + 1]
                                t1r = data[j0] - data[j1]
                                t1i = data[j0 + 1] - data[j1 + 1]
                                t2r = data[j2] + data[j3]
                                t2i = data[j2 + 1] + data[j3 + 1]
                                t3r = data[j2] - data[j3]
                                t3i = data[j2 + 1] - data[j3 + 1]
                                
                                data[j0] = tor + t2r
                                data[j0 + 1] = toi + t2i
                                data[j2] = tor - t2r
                                data[j2 + 1] = toi - t2i
                                
                                if isign == 1:
                                    t3r = -t3r
                                    t3i = -t3i
                                    
                                data[j1] = t1r - t3i
                                data[j1 + 1] = t1i + t3r
                                data[j3] = t1r + t3i
                                data[j3 + 1] = t1i - t3r
                            else:
                                tor = data[j0] + data[j1]
                                toi = data[j0 + 1] + data[j1 + 1]
                                t1r = data[j0] - data[j1]
                                t1i = data[j0 + 1] - data[j1 + 1]
                                t2r = data[j2] + data[j3]
                                t2i = data[j2 + 1] + data[j3 + 1]
                                t3r = data[j2] - data[j3]
                                t3i = data[j2 + 1] - data[j3 + 1]
                                
                                data[j0] = tor + t2r
                                data[j0 + 1] = toi + t2i
                                data[j2] = tor - t2r
                                data[j2 + 1] = toi - t2i
                                
                                if isign == 1:
                                    t3r = -t3r
                                    t3i = -t3i
                                    
                                data[j1] = t1r - t3i
                                data[j1 + 1] = t1i + t3r
                                data[j3] = t1r + t3i
                                data[j3 + 1] = t1i - t3r
                        wr, wi = wstpr * wr - wstpi * wi + wr, wstpr * wi + wstpi * wr

def fort2(data, n, ndim, isign, iform):
    ntot = 1
    for idim in range(ndim):
        ntot *= n[idim]
    nrem = ntot
    
    if iform != 0:
        nrem = 1
        ntot = ntot // n[0] * (n[0] // 2 + 1)
    
    for jdim in range(1, ndim + 1):
        if iform != 0:
            idim = ndim + 1 - jdim
        else:
            idim = jdim
            nrem = nrem // n[idim - 1]
            
        ncurr = n[idim - 1]
        
        if idim == 1:
            if iform != 0:
                fixrl(data, n[0], nrem, isign, iform)
                ntot = ntot // (n[0] // 2 + 1) * n[0]
            else:
                ncurr = ncurr // 2
                
        if ncurr <= 1:
            continue
            
        nprev = ntot // (n[idim - 1] * nrem)
        symrv(data, nprev, ncurr, nrem)
        cool(data, nprev, ncurr, nrem, isign)
        
        if iform != 0 and idim == 1:
            fixrl(data, n[0], nrem, isign, iform)
            ntot = ntot // n[0] * (n[0] // 2 + 1)