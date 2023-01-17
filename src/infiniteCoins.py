from typing import List

def count_generation(step: int = 1) -> int:
    """
    Generation function utilizada para realizar a contagem.

    :param step (int):  utilizado para controlar o passao da contagem.
    :return (int): sempre que a função for chaamda por um iterator
                    retorna o valor que está armazenado em count e após faz a soma entre o valor atual e o step.
    """
    count = 0
    while True:
        yield count
        count += step


def make_change(number: int) -> List[List[int]]:
    """
    A função utiliza a generation function count_generation() para iterar sobre os valores das moedas de
    25, 10, 5 e 1 centavos, chegando se a combinação entre elas resulta no numero inserido e retorna uma
    lista contendo as listas de todas as combinações possíveis.
    uma
    :param number (int): Valor inteiro que deseja-se decompor nas moedas de 25, 10, 5 e 1 centavos.
    :return (List[list]: lista contendo as listas de todas as combinações possíveis.
    """
    list_of_combinations = []
    sum_of_combination = 0

    for quarters in count_generation():
        for dimes in count_generation():
            for nickels in count_generation():
                sum_of_combination = nickels * 5 + dimes * 10 + quarters * 25
                pennies = number - sum_of_combination

                if sum_of_combination <= number:
                    combinations = [quarters, dimes, nickels, pennies]
                    list_of_combinations.append(combinations)

                else:
                    break
            if dimes * 10 + quarters * 25 > number:
                break
        if quarters * 25 > number:
            break

    return list_of_combinations


if __name__ == "__main__":

    #Valores testados

    number = 5
    print(make_change(number))
    number = 10
    print(make_change(number))
    number = 12
    print(make_change(number))
    number = 25
    print(make_change(number))

    #Descomentar a linhas abaixo para testar outros valores
    #input_number = int(input("Informe um valor: "))
    #print(make_change(input_number))
