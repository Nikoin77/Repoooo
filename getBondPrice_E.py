def getBondPrice_E(face, couponRate, m, yc):
    pvcfsum = 0
    for t, i in enumerate(yc, 1):
        if t <= m:
            pvf = (1 + i) ** -t
            pvcf = pvf * couponRate * face
            pvcfsum += pvcf
    pvcfsum += face * (1 + yc[m-1]) ** -m
    return pvcfsum







