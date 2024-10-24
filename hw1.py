import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(letters:str) -> int:
    count = 0
    vowels = "aeiouAEIOU"
    for i in letters :
        if i in vowels:
            count = count + 1
    return(count)

# Part 2
def short_lists(long_lists:list[list[int]]) -> list[list[int]]:
    templist = []
    for i in long_lists:
        if len(i) == 2:
            templist.append(i)
    return templist
# Part 3
def ascending_pairs(normal:list[list[int]]) -> list[list[int]]:
    templist = []
    for i in normal:
        if len(i) == 2 and i[0] < i[1]:
          templist.append(i)
    return templist

# Part 4
from data import Price
def add_prices(price1:Price, price2:Price) -> Price:
    total_dollars = price1.dollars + price2.dollars
    total_cents = price1.cents + price2.cents
    if total_cents >= 100:
        total_dollars = total_dollars + 1
        total_cents = total_cents % 100
    return Price(total_dollars, total_cents)

# Part 5
from data import Rectangle
from data import Point
def rectangle_area (temp: Rectangle):
    length = abs(temp.bottom_right.x - temp.top_left.x)
    width = abs(temp.top_left.y - temp.bottom_right.y)
    return length * width

# Part 6
from data import Book
def books_by_author (author:str, books:list[Book]):
    mathing_books =[]
    for i in books:
        for names in i.authors:
            if author == names:
                mathing_books.append(i.title)
    return mathing_books

# Part 7
from data import Circle
from data import Rectangle
def circle_bound(rectangle: Rectangle) -> Circle:
    x_center = (rectangle.top_left[0] + rectangle.bottom_right[0]) / 2
    y_center = (rectangle.top_left[1] + rectangle.bottom_right[1]) / 2
    radius = sqrt((x_center - rectangle.top_left[0]) ** 2 + (y_center - rectangle.top_left[1]) ** 2)
    return Circle((x_center, y_center), radius)

# Part 8
from data import Employee
def below_pay_averag(employees: list[Employee]) -> list[str]:
    average_pay=0
    for worker in employees:
        average_pay += worker.pay_rate
    average_pay = average_pay // (len(employees))
    below_average_employees = []
    for worker in employees:
       if worker.pay_rate < average_pay:
           below_average_employees.append(worker.name)
    return below_average_employees

