class Char:

    def __init__(self, name, strength=1.0):
        if type(name) != str:
            print("type ERROR")
        else:
            self._name = name

        if type(strength) != float:
            print("type ERROR")
        elif strength > 5.0:
            self._strength = 5.0
        elif strength < 0.0:
            self._strength = 0.0
        else:
            self._strength = strength

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):

        if isinstance(name, str):
            self._name = name
        else:
            print("type ERROR")

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, strength):

        if isinstance(strength, float):
            if 0.0 <= strength <= 5.0:
                self._strength = strength
            elif strength > 5.0:
                self._strength = 5.0
            elif strength < 0.0:
                self._strength = 0.0
        else:
            print("type ERROR")

    def __gt__(self, other):
        if self.strength > other.strength:
            return True
        return False

    def fight(self, other):
        if isinstance(self, Human) and isinstance(other, Human):
            print("fight ERROR")
        else:
            if self > other:
                self.strength += 1
                print(self)

            elif other > self:
                other.strength += 1
                print(other)

            else:
                self.strength -= 0.5
                other.strength -= 0.5
                print("hello")

    def __str__(self):
        char = "{} {}".format(self._name, self._strength)
        return char


class Orc(Char):

    def __init__(self, name, strength=1.0, weapon=True):
        Char.__init__(self, name, strength)

        if type(weapon) != bool:
            print("type ERROR")
           # exit()
        else:
            self._weapon = weapon

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, weapon):
        if type(weapon) is not bool:
            print("type ERROR")
        elif isinstance(weapon, bool):
            self._weapon = weapon

    def __gt__(self, other):
        if isinstance(self, Orc) and isinstance(other, Orc):        ###Dont need
            if self.weapon is True and other.weapon is True:
                if self.strength > other.strength:
                    return True
            elif self.weapon is True and other.weapon is False:
                return True
            elif self.weapon is False and other.weapon is False:
                if self.strength > other.strength:
                    return True
            else:
                return False

        elif isinstance(self, Orc) and isinstance(other, Human):
            if self.weapon is True: #Humans weapon is True
                #if self.strength > other.strength:
                return super().__gt__(other)
            return False

    def __str__(self):
        org = "{} {} {} ".format(self._name, self._strength, self._weapon)
        return org


class Human(Char):

    def __init__(self, name, strength, kingdom):
        Char.__init__(self, name, strength)

        if type(kingdom) != str:
            print("type ERROR")
            #exit()
        else:
            self._kingdom = kingdom

    @property
    def kingdom(self):
        return self._kingdom

    @kingdom.setter
    def kingdom(self, kingdom):
        if isinstance(kingdom, str):
            self._kingdom = kingdom
        else:
            print("type ERROR")

    def __gt__(self, other):
        if isinstance(self, Human) and isinstance(other, Orc):
            if other.weapon is False:
                #if self.strength > other.strength:
                return True

        return super().__gt__(other)

    def __str__(self):
        human = "{} {} {}".format(self._name, self._strength, self._kingdom)
        return human


class Archer(Human):

    def __init__(self, name, strength, kingdom):
        Human.__init__(self, name, strength, kingdom)

    def __str__(self):
        archer = "{} {} {}".format(self._name, self._strength, self._kingdom)
        return archer


class Knight(Human):

    def __init__(self, name, strength, kingdom, archers_list):
        Human.__init__(self, name, strength, kingdom)
        temp_list = []
        if isinstance(archers_list, list):
            for i in archers_list:
                if isinstance(i, Archer):
                    if i.kingdom == self.kingdom:
                        temp_list.append(i)
                else:
                    print("archers list ERROR")
                    break
            else:
                self._archers_list = temp_list
        else:
            print("type ERROR")

    @property
    def archers_list(self):
        return self._archers_list

    @archers_list.setter
    def archers_list(self, archers_list):
        temp_list = []
        if isinstance(archers_list, list):
            for i in archers_list:
                if isinstance(i, Archer):
                    if i.kingdom == self.kingdom:
                        temp_list.append(i)
                else:
                    print("archers list ERROR")
                    break
            else:
                self._archers_list = temp_list
        else:
            print("type ERROR")


    def __str__(self):
        temp_list =[]
        for i in self._archers_list:
            temp_list.append(str(i))
        temp_string = "[" + ", ".join(temp_list) + "]"
        knight = "{} {} {} {}".format(self._name, self._strength, self._kingdom, temp_string)
        return knight


def main():
    char1 = Orc(1, 3.6, True)
    char2 = Orc("Jackie", 4.4, False)
    char3 = Orc("Cian", 5.0, True)
    char4 = Archer("Mary", 3.0, "New Ross")
    char5 = Archer("Aine", 3.4, "Cork")
    char6 = Knight("Abbie", 4.0, "New Ross", [char5, char4])
    char7 = Knight("Thomas", 3.7, "Cork", [char5])



if __name__== '__main__':
    main()

