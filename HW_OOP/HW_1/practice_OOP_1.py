# practice

class Element:
    # I took the first element (Hydrogen) as primal element
    FREEZING = -259.2
    MELTING = -259
    EVAPORATION = -252.9
    __Absolute_Zero = -273.16


    def agg_state(self, temp, scale):
        """
        This method can tell you what exactly element doing for temperature you set.
        :param temp: integer
        :param scale: string "F" for Fahrenheit, "C" for Celsius, "K" for Kelvin
        :return: string with message
        """

        if scale == "K":
            temp += 273.15
            Element.MELTING += 273.15
            Element.MELTING += 273.15
            Element.EVAPORATION += 273.15
        elif scale == "F":
            temp = (9 / 5) * temp + 32
            Element.FREEZING = (9 / 5) * Element.FREEZING + 32
            Element.MELTING = (9 / 5) * Element.MELTING + 32
            Element.EVAPORATION = (9 / 5) * Element.EVAPORATION + 32
        elif scale == "C":
            temp = temp


        if temp <= Element.FREEZING:
            return f"{Element.__name__} is freezing"
        elif Element.FREEZING < temp < Element.EVAPORATION:
            return f"{Element.__name__} is melting"
        elif temp >= Element.EVAPORATION:
            return f"{Element.__name__} is evaporating"

    def convertation(self, temp, first_scale, second_scale):
        """
        This method can convert temperature from one
        :param temp: integer
        :param first_scale: string "F" for Fahrenheit, "C" for Celsius, "K" for Kelvin
        :param second_scale: string "F" for Fahrenheit, "C" for Celsius, "K" for Kelvin
        :return: integer
        """
        if first_scale == "C":
            if second_scale == "F":
                temp = (9/5)* (temp + 32)
                return temp
            elif second_scale == "K":
                temp = temp + 273.15
                return temp
            elif second_scale == "C":
                return "Ooou we have a special star here!) I have a prise for you, please visit " \
                       "'https://youtu.be/Qf5Ue1GVWu0?t=5' "
        elif first_scale == "K":
            if second_scale == "F":
                temp = (temp - 273.15) * (9/5) + 32
                return temp
            elif second_scale == "C":
                temp -= 273.15
                return temp
            elif second_scale == "K":
                return "Ooou we have a special star here!) I have a prise for you, please visit " \
                "'https://youtu.be/Qf5Ue1GVWu0?t=5' "
        elif first_scale == "F":
            if second_scale == "C":
                temp = (temp - 32) * (5/9)
                return temp
            elif second_scale == "K":
                temp = (temp - 32) * (5/9) + 273.15
            elif second_scale == "F":
                return "Ooou we have a special star here!) I have a prise for you, please visit " \
                "'https://youtu.be/Qf5Ue1GVWu0?t=5' "

    @property
    def get_Abosute_zero(self):
        return Element.__Absolute_Zero

class Oxygen(Element):
    FREEZING = -218
    MELTING = -217.9
    EVAPORATION = -182
    _ATOMIC_MASS = 15.999
    __MOLAR_VOLUME = 14.0

    def agg_state(self, temp, scale):
        """
        This method can tell you what exactly element doing for temperature you set.
        :param temp: integer
        :param scale: string "F" for Fahrenheit, "C" for Celsius, "K" for Kelvin
        :return: string with message
        """

        if scale == "K":
            temp += 273.15
            Oxygen.MELTING += 273.15
            Oxygen.MELTING += 273.15
            Oxygen.EVAPORATION += 273.15
        elif scale == "F":
            temp = (9 / 5) * temp + 32
            Oxygen.FREEZING = (9 / 5) * Oxygen.FREEZING + 32
            Oxygen.MELTING = (9 / 5) * Oxygen.MELTING + 32
            Oxygen.EVAPORATION = (9 / 5) * Oxygen.EVAPORATION + 32
        elif scale == "C":
            temp = temp


        if temp <= Oxygen.FREEZING:
            return f"{Oxygen.__name__} is freezing"
        elif Oxygen.FREEZING < temp < Oxygen.EVAPORATION:
            return f"{Oxygen.__name__} is melting"
        elif temp >= Oxygen.EVAPORATION:
            return f"{Oxygen.__name__} is evaporating"

    def make_brrrr(self):
        return f"Haha {Oxygen.__name__} make brrrrrrrr"

    @property
    def get_atomic_mass(self):
        return Oxygen._ATOMIC_MASS

    @property
    def get_molar_volume(self):
        return Oxygen.__MOLAR_VOLUME

    def how_toxic(self, percent, days):
        """
        This method return you result if you put the percentage of oxygen and how long you breathe
        :param percent:
        :param days:
        :return:
        """
        if percent > 90 and days >= 3:
            return "You will die ASAP"
        else:
            return "It's fine. You will not die, just don't be a silly"



def run():
    x = Element()
    print(x.convertation(35, "C", "K"))
    y = Oxygen()
    print(y.agg_state(-150, "F"))
    print(y.make_brrrr())
    print(y.get_Abosute_zero)
    print(y.how_toxic(75,4))


if __name__ == '__main__':
    run()
