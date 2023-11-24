def flicker(self, label: str) -> pd.DataFrame:
    """Calcula o flicker"""

    psts: list[float] = self.data_frame[label].to_list()

    pst_95 = float(np.percentile(psts, 95))

    data = {
        "Indicador": ["Pst95%"],
        "Obtido": [f"{pst_95:.2f}pu"],
        "PRODIST": [f"{prodist.P_ST_LIMIT:.2f}pu"],
    }

    return pd.DataFrame(data)