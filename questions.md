# Python

- What is the difference between a list and a tuple in Python?
    - Lists are mutable, therefore more flexible when needing to modify datasets
    - Tuples are immutable, therefore faster and memory efficent for larger datasets

- Could you explain the concept of arguments and keyword arguments?
    - Arguments are based on literal position in the function defination
    - Keyword Arguments are passed in with parameter names and will have a default value when nothing supplied

- What is a decorator and how do you use it?
    - A function that takes another function as an argument, and returns a new function
    - Allows you to add functionality to exsiting functions without modify code directly

- Could you list some python libraries you have used?

# SQL

- Could you identity different types of joins and what they do
    - LEFT [OUTER]
    - RIGHT [OUTER]
    - INNER
    - FULL OUTER

- Could you explain the difference between primary keys and foreign keys
    - Primary keys force uniqueness within a table. Cannout be null
    - Foreign keys establish relationships between two tables
        - Typically referencing the primary key of one of them
        - Enforces integrity in the other table

# JavaScript

- **What's the difference between `==` and `===`?**  
    `==` (equality) will (attempt) to convert both sides to the same type effectively ignoring type when checking for equality  
    `===` (strict equality) only returns true if both sides are also the same type as well as the same value  
``` 
    (2 == '2') // true  
    (2 === '2') // false
```
 
- **What's the difference between `let` and `var`?**  
    `var` is functionally scoped  
    `let` is block scoped  
```
    foo();
    function foo() {
        if (true) {
            var a = "foo";
            let b = "bar";
        }
        console.log(a);  // "foo"
        console.log(b);  // error
    }
```
 
- **What's hoisting?**  
    Function and variable declarations are moved to the beginning of their scope, so they can be used before the line where they are declared.  
```
    a = "foo";  // no errors
    console.log(a);  // "foo"
    var a;
```

# Change Management

- Have you worked in an Agile environment, and if so what did the process look like?
    - (kanban/scrum/etc)
- Do you have experience with capacity planning with a team?
    - story points, etc
