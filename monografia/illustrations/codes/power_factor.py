class PowerFactor:
    """Fator de potencia"""

    def __init__(self, value: float) -> None:
        self.value = value

    def classify(self) -> PowerFactorClassifyType:
        """Classifica o fator de potencia"""

        if self.value < prodist.FP_INDUTIVO:
            return 'Critico'
        else:
            return 'Adequado'
