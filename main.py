from proyecto import *

if __name__ == "__main__":
    # mejoras 1
    """
    lista_numeros = [2,5,6,7,9,6]
    print(sum_even(lista_numeros),'\n')
    texto = "    Un momento. Un momento, Doc. ¿Me estás diciendo que has construido una máquina del tiempo con un DeLorean?    "
    print(normalize_str(texto), '\n')
    texto = "El amo le ha dado a Dobby un calcetín... Dobby es libre"
    print(count_words(texto), '\n')
    """
    # mejoras 2
    """
    print(safe_divide(6,5), '\n')
    print(safe_divide(6, 0), '\n')
    print(read_csv_sum_revenue('./prueba_ventas.csv'), '\n')
    print(filter_customers_json('./users.json', './users_correct.txt'), '\n')
    """
    # mejoras 3
    print(squares_of_odds(11), '\n')
    print(random_color(33),'\n')
    days_between('2025-12-12', '2025-12-13')
    vector1 = Vector2D(5.6,7.9)
    vector2 = Vector2D(9,3.7)
    print(vector1.__add__(vector2),'\n')
    print(vector1.__eq__(vector2), '\n')
    print(vector1, '\n')
    print(vector2, '\n')
    print(vector1.length(), '\n')
    print(vector2.length(), '\n')