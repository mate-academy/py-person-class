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
  
}
```
`Hint` - use `pytest` for testing