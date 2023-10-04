def classify(self) -> FrequencyClassifyType:
    """Classifica a frequencia"""

    if self.value < prodist.FREQUENCY_LIMIT[0]:
        self.__classify = "Baixa"
    elif self.value > prodist.FREQUENCY_LIMIT[1]:
        self.__classify = "Alta"
    else:
        self.__classify = "Adequada"

    return self.__classify
