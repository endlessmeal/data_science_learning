# дифференциальное РАВНОМЕРНОЕ распределение (или функция плотности)
def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0

# ИФР для РАВНОМЕРНОГО распределения
def uniform_cdf(x):
    """возвращает вероятность того, что равномерно распределенная случайнаявеличина <=х"""
    if x < 0:   return 0 # величина не может быть меньше 0
    elif x < 1: return x # например P(x <= 0.4) = 0.4
    else:       return 1 # величина всегда меньше 1