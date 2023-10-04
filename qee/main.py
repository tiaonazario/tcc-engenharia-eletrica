from qee.functions.get_files_by_extension import get_files_by_extension
from qee.constants import PRODIST_M8
import matplotlib.pyplot as plt
import pandas as pd

files = get_files_by_extension('./data', 'csv')
file = files[0]

df = pd.read_csv(file, sep=';')
times = df['Time']
V1_Avg = df['V1_Avg [V]']


# for voltage in V1_Avg:
#     classify_voltage(voltage, '220')

# Plotar o gráfico
fig, ax = plt.subplots()

cr_sup = PRODIST_M8['220']['cr-sup']
ad_sup = PRODIST_M8['220']['ad-sup']
ad_inf = PRODIST_M8['220']['ad-inf']
cr_inf = PRODIST_M8['220']['cr-inf']

ax.plot(times, V1_Avg, label='V1_Avg')
ax.axhline(y=cr_sup, color='r', linestyle='--')
ax.axhline(y=ad_sup, color='y', linestyle='--')
ax.axhline(y=220, color='g', linestyle='--')
ax.axhline(y=ad_inf, color='y', linestyle='--')
ax.axhline(y=cr_inf, color='r', linestyle='--')

ax.axhspan(cr_sup, ad_sup, facecolor='yellow', alpha=0.3)
ax.axhspan(ad_inf, ad_sup, facecolor='green', alpha=0.3)
ax.axhspan(cr_inf, ad_inf, facecolor='yellow', alpha=0.3)

ax.set_xlabel('Tempo (s)')
ax.set_ylabel('Tensão (V)')
ax.set_title('Tensão em função do tempo')
ax.legend(loc="upper right")

plt.show()
