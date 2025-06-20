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
        Person.people[partner_name].cancel_marriage()

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
        if self.__dict__.get("wife"):
            del self.wife.husband
            del self.wife
            return True

        if self.__dict__.get("husband"):
            del self.husband.wife
            del self.husband
            return True

        return False


def create_person_list(people: list) -> list[Person]:
    ans = []
    for person in people:
        ans.append(Person(person["name"], person["age"]))
        if person.get("wife"):
            ans[-1].get_married(person["wife"], "wife")
        elif person.get("husband"):
            ans[-1].get_married(person["husband"], "husband")

    return ans
