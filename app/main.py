from __future__ import annotations


class Person:
    people = {}  # people collection, key=name, value = ref to a person

    def __init__(self, name: str, age: int, wife: str = None, husband: str = None) -> None:
        # fill data
        self.name = name
        self.age = age

        if wife:
            self.wife = self.find_partner(wife)
        if husband:
            self.husband = self.find_partner(husband)

        self.people[self.name] = self

    def find_partner(self, person_to_find: str | None) -> Person | str | None:
        # if the person exists
        if person_to_find and person_to_find in self.people.keys():
            partner = self.people[person_to_find]
            # write this person as a partner`s partner
            if hasattr(partner, "wife") and partner.wife == self.name:
                partner.wife = self
            elif hasattr(partner, "husband") and partner.husband == self.name:
                partner.husband = self
            return self.people[person_to_find]
        else:  # return str if partner non exists
            return person_to_find


def create_person_list(people: list) -> list:
    return [Person(
            name=human_being["name"],
            age=human_being["age"],
            wife=human_being["wife"] if "wife" in human_being.keys() else None,
            husband=human_being["husband"] if "husband" in human_being.keys() else None)
            for human_being in people]


test = [
        {"name": "Ross", "age": 30, "wife": "Rachel"},
        {"name": "Joey", "age": 29, "wife": None},
        {"name": "Phoebe", "age": 31, "husband": None},
        {"name": "Chandler", "age": 30, "wife": "Monica"},
        {"name": "Monica", "age": 32, "husband": "Chandler"},
        {"name": "Rachel", "age": 28, "husband": "Ross"},
    ]

# lst = create_person_list(test)
# for index, persn in enumerate(lst, 0):
#     print(f"{index}. {persn.name}")
#
# # 0. Ross <__main__.Person object at 0x000001BE361F85C0> None
# # 1. Joey None None
# # 2. Phoebe None None
# # 3. Chandler <__main__.Person object at 0x000001BE361F8560> None
# # 4. Monica None <__main__.Person object at 0x000001BE361F84D0>
# # 5. Rachel None <__main__.Person object at 0x000001BE361F8440>
#
# print(lst[0].wife.name)  # Rachel
# print(lst[5].husband.name)  # Ross
#
# print(lst[0].wife is lst[5] and lst[5].husband is lst[0])  # true
#
# print("*"*20)

