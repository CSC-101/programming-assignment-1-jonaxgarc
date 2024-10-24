import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def testUnitCaseOne_1(self):
        input = "Mother"
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)
    def testUnitCaseOne_2(self):
        input = "Because"
        result = hw1.vowel_count(input)
        expected = 4
        self.assertEqual(expected, result)

    # Part 2
    def testUnitCaseTwo_1(self):
        input = [[2,3], [3,4,5], [3,4], [2]]
        result = hw1.short_lists(input)
        expected = [[2,3], [3,4]]
        self.assertEqual(expected, result)
    def testUnitCaseTwo_2(self):
        input = [[3,4], [4,5,6], [4,5], [3]]
        result = hw1.short_lists(input)
        expected = [[3,4], [4,5]]
        self.assertEqual(expected, result)

    # Part 3
    def testUnitCaseThree_1(self):
        input = [[3,4], [4,3], [7,8]]
        result = hw1.ascending_pairs(input)
        expected = [[3,4], [7,8]]
        self.assertEqual(expected, result)
    def testUnitCaseThree_2(self):
        input = [[4,5], [5,4], [8,9]]
        result = hw1.ascending_pairs(input)
        expected = [[4,5], [8,9]]
        self.assertEqual(expected, result)

    # Part 4
    from data import Price
    def testUnitCaseFour_1(self):
        input1 = self.Price(24, 31)
        input2 = self.Price(37, 13)
        result = hw1.add_prices(input1,input2)
        expected = self.Price(61,44)
        self.assertEqual(expected, result)
    def testUnitCaseFour_2(self):
        input1 = self.Price(232, 1232)
        input2 = self.Price(1232, 98754)
        result = hw1.add_prices(input1, input2)
        expected = self.Price(1465, 86)
        self.assertEqual(expected, result)

    # Part 5
    from data import Rectangle
    from data import Point
    def testUnitCaseFive_1(self):
        input = self.Rectangle(self.Point(3, 4), (self.Point(6, 7)))
        result = hw1.rectangle_area(input)
        expected = 9
        self.assertEqual(expected, result)
    def testUnitCaseFive_2(self):
        input = self.Rectangle(self.Point(7, 12), (self.Point(12, 23)))
        result = hw1.rectangle_area(input)
        expected = 55
        self.assertEqual(expected, result)

    # Part 6
    from data import Book
    def testUnitCaseSix_1(self):
        authors = ["Sarah", "Daniel"]
        listOfBooks = [self.Book(authors, "Jungle Book"), self.Book(authors, "Forest Book")]
        name = "Sarah"
        result = hw1.books_by_author(name, listOfBooks)
        expected = ['Jungle Book', 'Forest Book']
        self.assertEqual(expected, result)
    def testUnitCaseSix_1(self):
        authors = ["Jack", "Mary"]
        listOfBooks = [self.Book(authors, "Swamp Book"), self.Book(authors, "Arctic Book")]
        name = "Jack"
        result = hw1.books_by_author(name, listOfBooks)
        expected = ['Swamp Book', 'Arctic Book']
        self.assertEqual(expected, result)

    # Part 7


    # Part 8
    from data import Employee
    def testUnitCasEight_1(self):
        input = [self.Employee("Jonathan Garcia", 24), self.Employee("Ricky Garcia", 5), self.Employee("Dray", 4)]
        result = hw1.below_pay_average(input)
        expected = ["Jason Williams", "Dray"]
        self.assertEqual(expected, result)

