# class Person

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start


You have a list of dicts `people`, every dict means
a **person**, it has keys: `name`, `age`, 
`wife`/`husband` - depends on person is male or 
female. All `names` are different. Key 
`wife`/`husband` can be either `None` or 
name of another person.

Create class `Person`. It's constructor takes
and store `name`, `age` of a person.
This class also should have a class attribute
`people`, it is a dict that stores `Person` 
instances by their `name`. Constructor should 
add elements to this attribute.

Write function `create_person_list`, this function
takes list `people` and return list with
`Person` instances instead of dicts.

**Note:**

If **person's** key `wife`/`husband` is not 
`None` - `create_person_list` should add 
attribute `wife`/`husband` respectively
to its instance. This attribute should
be a link to a `Person` instance with `name` the
same as `wife`/`husband` key in person's dict.


Example:
```python
people = [
    {'name': 'Ross', 'age': 30, 'wife': 'Rachel'},
    {'name': 'Joey', 'age': 29, 'wife': None},
    {'name': 'Rachel', 'age': 28, 'husband': 'Ross'}
]

person_list = create_person_list(people) 
isinstance(person_list[0], Person) # True
person_list[0].name == 'Ross'
person_list[0].wife is person_list[2] # True
person_list[0].wife.name == 'Rachel'

person_list[1].name == 'Joey'
person_list[1].wife
# AttributeError

isinstance(person_list[2], Person) # True
person_list[2].name == 'Rachel'
person_list[2].husband is person_list[0] # True
# The same as person_list[0]
person_list[2].husband.name == 'Ross'
person_list[2].husband.wife is person_list[2]  # True

Person.people == {
    'Ross': <__main__.Person object at 0x10c20ca60>,
    'Joey': <__main__.Person object at 0x10c180a00>,
    'Rachel': <__main__.Person object at 0x10c1804f0>

}
```
`Hint` - use `pytest` for testing