from enum import Enum
import matplotlib.pyplot as plt
import numpy as np


class VL(Enum):
    V110 = '110'
    V120 = '120'
    V127 = '127'
    V208 = '208'
    V215 = '215'
    V220 = '220'
    V230 = '230'
    V240 = '240'
    V254 = '254'
    V380 = '380'
    V440 = '440'


class Prodist():
    def __init__(self):
        self.__vvr: dict[str, dict[str, int]] = self.voltage_variation_range()

    def voltage_variation_range(self):
        return {
            '110': {
                'cr-sup': 117,
                'ad-sup': 116,
                'ad-inf': 101,
                'cr-inf': 96,
            },
            '120': {
                'cr-sup': 127,
                'ad-sup': 126,
                'ad-inf': 110,
                'cr-inf': 104,
            },
            '127': {
                'cr-sup': 135,
                'ad-sup': 133,
                'ad-inf': 117,
                'cr-inf': 110,
            },
            '208': {
                'cr-sup': 220,
                'ad-sup': 218,
                'ad-inf': 191,
                'cr-inf': 181,
            },
            '215': {
                'cr-sup': 122,
                'ad-sup': 121,
                'ad-inf': 106,
                'cr-inf': 100,
            },
            '220': {
                'cr-sup': 233,
                'ad-sup': 231,
                'ad-inf': 202,
                'cr-inf': 191,
            },
            '230': {
                'cr-sup': 244,
                'ad-sup': 242,
                'ad-inf': 212,
                'cr-inf': 200,
            },
            '240': {
                'cr-sup': 254,
                'ad-sup': 252,
                'ad-inf': 221,
                'cr-inf': 209,
            },
            '254': {
                'cr-sup': 269,
                'ad-sup': 267,
                'ad-inf': 234,
                'cr-inf': 221,
            },
            '380': {
                'cr-sup': 403,
                'ad-sup': 399,
                'ad-inf': 350,
                'cr-inf': 331,
            },
            '440': {
                'cr-sup': 466,
                'ad-sup': 462,
                'ad-inf': 405,
                'cr-inf': 383,
            },
        }

    def classify_voltage(self, vl: VL) -> dict[str, int]:
        vvr = {
            'cr-inf': np.array([self.__vvr[vl]['cr-inf']]),
            'pr-inf': np.array([self.__vvr[vl]['ad-inf'] - self.__vvr[vl]['cr-inf']]),
            'ad-inf': np.array([int(vl) - self.__vvr[vl]['ad-inf']]),
            'ad-sup': np.array([self.__vvr[vl]['ad-sup'] - int(vl)]),
            'pr-sup': np.array([self.__vvr[vl]['cr-sup'] - self.__vvr[vl]['ad-sup']]),
            'cr-sup': np.array([10]),
        }

        width = 0.6

        fig, ax = plt.subplots()
        bottom = np.zeros(3)

        for key, value in vvr.items():
            p = ax.bar((vl), value, width, label=key, bottom=bottom)
            bottom += value

            # ax.bar_label(p, label_type='center')

        ax.set_xticklabels([vl])
        ax.set_ylabel('V (volts)')
        ax.set_title('Faixas de tensão em relação à de referência')
        ax.legend(loc="upper right")

        # plt.tight_layout()
        plt.show()
