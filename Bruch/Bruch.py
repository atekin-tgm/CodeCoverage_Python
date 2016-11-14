"""
@author:    TEKIN Abdurrahim Burak
@date:      2016-11-06
-- Bruch class for coverage --
"""

class Bruch(object):

    def __init__(self, *args):
        """
        GOT THIS PART WITH
        :param args: *args -> how many args?
        """
        if (len(args) == 1):
            # if Bruch
            if (isinstance(args[0], Bruch)):
                self.zaehler = args[0].zaehler
                self.nenner = args[0].nenner
            else:
                self.zaehler = args[0]
                self.nenner = 1
        else:
            if args[0] < 0 and args[1] < 0:
                self.zaehler = - args[0]
                self.nenner = - args[1]
            else:
                self.zaehler = args[0]
                self.nenner = args[1]

        # nenner == 0 -> ZeroDivisionError
        if (self.nenner == 0):
            raise ZeroDivisionError("ERROR - Division durch 0!")

        # nenner is not int -> TypeError
        if (not isinstance(self.nenner, int)):
            raise TypeError("Den nennerer ganzzählig machen!")
        # zaehler is not int -> TypeError
        if (not isinstance(self.zaehler, int)):
            raise TypeError("Den Zähler ganzzählig machen!")

    def __abs__(self):
        """
        testAbs()
        :return: absolute value of Bruch
        """
        return (abs(self.zaehler), abs(self.nenner))

    def __float__(self):
        """
        testFloat()
        :return: float value of Bruch
        """
        return float(self.zaehler) / float(self.nenner)

    def __int__(self):
        """
        testInt()
        :return: int value of Bruch
        """
        return int(self.zaehler / self.nenner)

    def __complex__(self):
        """
        testComplex()
        :return: complex value of Bruch
        """
        return complex(self.zaehler / self.nenner)

    def __invert__(self):
        """
        testInvert()
        :return: zaehler/nenner -> nenner/zaehler
        """
        return Bruch(self.nenner, self.zaehler)

    def __pow__(self, hoch):
        """
        testPow()
        :param hoch: Hochzahl
        :return: Bruch = zaehler^hoch/nenner^hoch
        """
        return Bruch(self.zaehler ** hoch, self.nenner ** hoch)

    def _Bruch__makeBruch(zaehl):
        """
        test_makeBruchInt()
        :param zaehl: make zaehler
        :return: Bruch
        """
        return Bruch(zaehl, 1)

    def __neg__(self):
        """
        testNeg()
        :return: if zaehler < 0 -> negative zaehler OR if nenner < 0 -> negative nenner
        """
        if (self.zaehler < 0):
            return Bruch(-self.zaehler, self.nenner)
        elif (self.nenner < 0):
            return Bruch(self.zaehler, -self.nenner)

    def __eq__(self, test):
        """
        testEqual()
        :param test: comparing value
        :return: if self == test -> return True
        """
        if float(self) == float(test):
            return True

    def __ge__(self, test):
        """
        testGE()
        :param test: comparing value
        :return: if self >= test -> return True
        """
        if float(self) >= float(test):
            return True

    def __le__(self, test):
        """
        testLE()
        :param test: comparing value
        :return: if self <= test -> return True
        """
        if float(self) <= float(test):
            return True

    def __lt__(self, test):
        """
        testLT()
        :param test: comparing value
        :return: if self < test -> return True
        """
        if float(self) < float(test):
            return True

    def __gt__(self, test):
        """
        testGT()
        :param test: comparing value
        :return: if self > test -> return True
        """
        if float(self) > float(test):
            return True

    def __str__(self):
        """
        teststr()
        :return: returns Bruch in string-form
        """
        return "(" + str(self.zaehler) + "/" + str(self.nenner) + ")"

    def __mul__(self, test):
        """
        self gets multiplied by test
        :param test: self * test
        :return: Bruch = self * test
        """
        test = Bruch(test)
        return Bruch(self.zaehler * test.zaehler, self.nenner * test.nenner)

    def __imul__(self, test):
        """
        :param test: self gets multiplied by test
        :return: Bruch = self * test
        """
        return self * Bruch(test)

    def __rmul__(self, test):
        """
        :param test: test gets multiplied by self
        :return: Bruch = test * self
        """
        return Bruch(test) * self

    def __truediv__(self, test):
        """
        self gets divided by test
        :param test: self / test
        :return: Bruch = self / test
        """
        test = Bruch(test)
        return Bruch(self.zaehler * test.nenner, self.nenner * test.zaehler)

    def __itruediv__(self, test):
        """
        :param test: self / test
        :return: Bruch = self / test
        """
        return self / test

    def __rtruediv__(self, test):
        """
        :param test: test / self
        :return: Bruch = test / self
        """
        return Bruch(test) / self

    def __iter__(self):
        """
        Called by z,n = Bruch(z,n)
        :return: Kind of a list which is iterable
        """
        #Iterate through self.zaehler and self.nenner
        for i in self.zaehler, self.nenner:
            #the keyword yield is basically the same as making a list, appending i each time and then returning this list
            yield i