import math

def distanciaEntrePontos(latInicial, longInicial, latFinal, longFinal):
    d2r = 0.017453292519943295769236
    dlong = (longFinal - longInicial) * d2r
    dlat = (latFinal - latInicial) * d2r
    temp_sin = math.sin(dlat / 2.0);
    temp_cos = math.cos(latInicial * d2r)
    temp_sin2 = math.sin(dlong / 2.0)

    a = (temp_sin * temp_sin) + (temp_cos * temp_cos) * (temp_sin2 * temp_sin2)
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))

    return 6371.0 * c

print(distanciaEntrePontos(-23.541756, -46.416247, -23.543302, -46.410291))