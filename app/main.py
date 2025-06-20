class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def get_married(self, partner_name: str, partner_type: str) -> bool:
        if partner_name not in Person.people or partner_name == self.name:
            return False

        self.cancel_marriage()

        if partner_type == "husband":
            self.husband = Person.people[partner_name]
            Person.people[partner_name].wife = self
            return True
        elif partner_type == "wife":
            self.wife = Person.people[partner_name]
            Person.people[partner_name].husband = self
            return True

        return False

    def cancel_marriage(self) -> bool:
        if "wife" in self.__dict__:
            temp = self.wife
            del self.wife
            temp.cancel_marriage()
            return True

        if "husband" in self.__dict__:
            temp = self.husband
            del self.husband
            temp.cancel_marriage()
            return True

        return False


def create_person_list(people: list) -> list[Person]:
    ans = []
    for person in people:
        ans.append(Person(person["name"], person["age"]))
        if "wife" in person:
            ans[-1].get_married(person["wife"], "wife")
        elif "husband" in person:
            ans[-1].get_married(person["husband"], "husband")

    return ans
