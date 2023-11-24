def indicators(self) -> dict[Literal['DRP', 'DRC'], float]:
    """
    Calcula os indicadores Duracao Relativa de Transgressao
    para tensao precaria e critica
    """

    numbers = self.reading_number()

    self.__drp = (numbers[1] / 1008) * 100
    self.__drc = (numbers[2] / 1008) * 100

    return {'DRP': self.__drp, 'DRC': self.__drc}
