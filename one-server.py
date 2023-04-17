import numpy as np
import scipy.stats as st

rnd = np.random
rnd.seed(1)

end_time = 60 * 8
fel = [{'Type': 'Llegada', 't': st.expon.ppf(rnd.rand(), loc=0, scale=3)}]
clock = 0
Q = 0
Cajero = 0
Cliente = 0
lq = [(0, 0)]
Tiempo_espera = [(0, 0)]

while clock <= end_time:
    fel = sorted(fel, key=lambda e: e['t'])
    current_event = fel.pop(0)
    clock = current_event['t']

    if current_event['Type'] == 'Llegada':
        Cliente += 1
        if Cajero == 0:
            Cajero = 1
            fel.append({'Type': 'Atencion', 't': clock + st.expon.ppf(rnd.rand(), loc=0, scale=4)})

        else:
            Q += 1

        fel.append({'Type': 'Llegada', 't': clock + st.expon.ppf(rnd.rand(), loc=0, scale=3)})


    elif current_event['Type'] == 'Atencion':
        if Q > 0:
            Q -= 1
            Cajero = 1
            fel.append({'Type': 'Atencion', 't': clock + st.expon.ppf(rnd.rand(), loc=0, scale=4)})

        else:
            Cajero = 0

    lq.append((clock, Q))
    Tiempo_espera.append(())
