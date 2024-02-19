import math


def fake_bin(x):   # для чисел меньше 5 возвращает 0 б бля больше 5 возвращает 1
    return ''.join('0' if c < '5' else '1' for c in x)
##################################
def is_square(n):   # проверяет можно ли вычесть корень из числа
    return n >= 0 and math.sqrt(n) % 1 == 0
#############################
def get_sums(a,b):  # складывает 2 числа если они не одинаковые и возвращает сумму
    return a+b if a!=b else a
###############
def get_sum(a,b):
    return a if a == b else sum(range(a, b+1)) if a < b else sum(range(b, a+1))
################################

def accum(st):
    return '-'.join(st[i].upper() + st[i].lower() * i for i in range(len(st)))
#################print(accum("AbC"))

def find_short(s):  #  нати самое короткое слово в строке и вернуть его длинну
    return len(min(s.split(), key=len))
######## print(find_short("Wtf is THISSS"))

def century(year):
    return year // 100 if year % 100 == 0 else (year // 100)+1
    return (year + 99) // 100
#   print(century(1001))

def solution(text, ending):
    # return ending in text  роверет есть ли в строке сабстрока (подстрока)
    return text.endswith(ending)  # проверить оканчивается ли строка на сабстроку
#### print(solution( "samurai", "a" ))

def are_you_playing_banjo(name):
    #return name + " play banjo" if name.lower().startswith("r") else name + " does not plays banjo"
    #return name + " plays banjo" if name[0].lower() == 'r' else name + " does not play banjo"
    return "{} {} banjo".format(name, "plays" if name.lower().startswith("r") else "does not play")
##############print(are_you_playing_banjo("Rike"))
def DNA_strand(dna):  # ЗАМЕНА букв одних на другие
    return "".join(["A" if char == "T" else "C" if char == "G" else "T" if char == "A" else "G" if char == "C" else char for char in dna])
    #return "".join({"T": "A", "A": "T", "G": "C", "C": "G"}.get(char, char) for char in dna)
    #return dna.translate(string.maketrans("ATCG","TAGC")) - тоже что ниже но нужен экспорт стринга
    return dna.translate(str.maketrans("ATCG", "TAGC"))
    return dna.translate(dna.maketrans("ATCG", "TAGC"))
#print(DNA_strand("ATTGC"))
def number(bus_stops):
    # inside = 0
    # out = 0
    # for i :
    #     inside += bus_stops[i][0]
    #     out += bus_stops[i][1]
    # return inside-out
#     return sum(i[0] - i[1] for i in bus_stops)
    return sum(on - off for on, off in bus_stops)
# print(number([[10,0],[3,5],[5,8]]))
def bmi(weight, height):
    b = weight / height**2
    return "Underweight" if b <= 18.5 else "Normal" if b <= 25.0 else "Overweight" if b <= 30.0 else "Obese"
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]
#print(bmi(50, 1.80))

def count_by(x, n):
    return list(x*(i+1) for i in range(n))
    return [x*(i+1) for i in range(n)]
#####################################

def better_than_average(class_points, your_points):
    return (sum(class_points) / len(class_points)) < your_points
############print(better_than_average([5,6,7], 0))
def basic_op(operator, value1, value2):
    return eval(str(value1)+operator+str(value2))
########################
def count_positives_sum_negatives(arr):
    #     a, b = 0, 0
    #     if len(arr) == 0:
    #         return []
    #     else:
    #         for i in range(len(arr)):
    #             if arr[i] > 0:
    #                 a += 1
    #             else:
    #                 b = b + arr[i]
    #     return [a, b]

    return [sum(1 for i in arr if i > 0), sum(i for i in arr if i < 0)] if arr else [] # либо [] if arr == [] else
def no_space(x):
    return x.replace(" ", "")  # убираем пробелы из строки
    return "".join(x.split())  # тоже самое


def get_grade(s1, s2, s3):
    return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) / 30, 'F')
    return 'FFFFFFDCBAA'[sum(s)//30]