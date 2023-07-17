# Python Good-to-Knows and Data Types

This readme.md provides some important "good-to-knows" about Python.

## Good-to-Knows

- [Python is an Interpreted Language](#python-is-an-interpreted-language)
- [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
- [Standard Library and Third-Party Packages](#standard-library-and-third-party-packages)
- [Programming Paradigms](#programming-paradigms)
- [Mutable vs Immutable Data Types](#mutable-vs-immutable-data-types)
- [Call-by-Value and Call-by-Reference Semantics](#call-by-value-and-call-by-reference-semantics)
- [Sharing Modules](#sharing-modules)
- [PEP 8 Compliance](#pep-8-compliance)


## Python is an Interpreted Language

Python is an interpreted language, meaning you can run your code without compiling it beforehand. This allows for quick and interactive development, making it easy to test and experiment with your code.

## Object-Oriented Programming (OOP)

In Python, you can use object-oriented programming (OOP) to structure your code. This involves defining classes and objects to encapsulate data and behavior. OOP concepts like inheritance, encapsulation, and polymorphism are fully supported, enabling you to create reusable and modular code.

## Standard Library and Third-Party Packages

Python comes with a comprehensive standard library that provides built-in modules and functions for various tasks like file input/output, networking, and web development. Additionally, there is a vast ecosystem of third-party libraries and packages developed by the community, expanding Python's capabilities for data analysis, scientific computing, machine learning, web development, and more.

## Programming Paradigms

Python is a versatile language that supports multiple programming paradigms. While it is primarily object-oriented, you can also write code in procedural, functional, or concurrent styles. This flexibility allows you to adapt your code to different requirements and programming styles, making Python suitable for a wide range of applications.

## Data Types

Python supports various data types, each with its own characteristics and use cases. The main data types in Python include:

- [Numbers (integers, floats, complex numbers)](#numbers)
- [Strings](#strings)
- [Lists](#lists)
- [Tuples](#tuples)
- [Dictionaries](#dictionaries)
- [Sets](#sets)

Each data type has its own unique features and methods for manipulation. Understanding these data types is fundamental to writing Python programs.

### Numbers

Numbers in Python can be integers, floating-point numbers, or complex numbers. They support various arithmetic operations.

    x = 42
    y = 3.14159 
    z = complex(2, 3)

    print(x)  # Output: 42
    print(y)  # Output: 3.14159
    print(z)  # Output: (2+3j)

### Strings

Strings represent textual data. A sequence of characters that are enclosed in quotation marks signify a string. Although strings are immutable, you can perform various operations such as concatenation, slicing, and formatting.

    name = "Toby"
    greeting = "Hi, " + name

    print(name)     # Output: Toby
    print(greeting) # Output: Hi, Toby

### Tuples

Tuples are similar to lists but are immutable, meaning their elements cannot be modified once defined. They are useful for storing a fixed collection of values that should not be changed. Tuples are often used for returning multiple values from functions or as keys in dictionaries.

### Lists

Lists are mutable, unordered collections of items. They allow you to store and manipulate sequences of elements. Lists are commonly used for managing groups of related data.

    fruits = ["apple", "banana", "orange"]
    fruits.append("mango")

    print(fruits)       # Output: ['apple', 'banana', 'orange', 'mango']
    print(fruits[0])    # Output: apple
    print(len(fruits))  # Output: 4

### Dictionaries

Dictionaries are unordered, mutable key-value pairs. They provide an efficient way to store and retrieve data using keys. Dictionaries are used for mapping relationships 

### Sets

Sets are mutable unordered collections of unique elements. They support mathematical set operations such as union(), intersection(), and difference().


## Mutable vs Immutable Data Types

In Python, data types can be classified as mutable or immutable:

### Immutable Data Types

Immutable data types are those whose values cannot be modified after they are created. Any attempt to modify an immutable object results in the creation of a new object. Examples of immutable data types in Python include <i>numbers</i>, <i>strings</i>, <i>tuples</i>, and <i>frozensets</i>.

### Mutable Data Types

Mutable data types are those that can be modified after they are created. Changes made to a mutable object directly modify its value. Examples of mutable data types in Python include <i>lists</i>, <i>dictionaries</i>, and <i>sets</i>.

Understanding the distinction between mutable and immutable data types is crucial for proper data manipulation and assignment.

## <a id="call-by-value-and-call-by-reference-semantics"></a>Call-by-Value and Call-by-Reference Semantics
In Python, function arguments support both call-by-value and call-by-reference semantics.<br>Recall that variables in Python behave as "object references". So we can think of the value stored in the variable as the memory address of the value, and not its actual value.


First, the interpreter looks at the type of the value referred to by the object reference (memory address).
Call-by-Reference semantics apply if the variable in question refers to a mutable value.
Call-by-Value semantics apply if the variable in question refers to an immutable value.

Dictionaries, Lists, and Sets - which are mutable - are always passed into a function by reference. Changes that occur on the variable's data structure within the function's suite are reflected in the calling code.

Integers, Strings, and Tuples - which are immutable - are always passed by value. Changes to the variable within the function are only for the function and are not reflected in the calling code.

## Sharing Modules
When working with Python, you can easily share and reuse modules. These modules are like bundles of code that you can use in different projects. They help you organize your code and make it easier to manage.

If you have at least Python 3.4 (minimum) you can use a package called 'setuptools' which can be used to install any module into site-packages.

These are two places where you can find and share Python modules:

    PyPI (Python Package Index): PyPI is like a treasure trove of Python packages. It's a collection of ready-to-use code created by other Python developers. You can find all sorts of packages for things such as data manipulation, web development, and machine learning.

    PyPA (Python Packaging Authority): PyPA is a helpful guide for packaging your own Python code. There are tips and tricks you may find useful when it comes to creating your own modules and how to distribute them to others. If you're interested in making your code accessible to other Python developers.

### Sharing Modules - Resources

For more information about `setuptools`, you can visit the [setup tools install from PyPI link](https://pypi.org/project/setuptools/) and the [PyPA.io site](https://www.pypa.io/).  To learn more about the Python Package Index, checkout the [PyPI website](https://pypi.python.org). These resources provide comprehensive documentation for sharing modules, and information on using `setuptools` effectively.


## PEP 8 Compliance
PEP 8 Compliance is a style guide for Python code. It provides guidelines on code formatting, maintainability, and readability. Having a consistent code style improves code maitenance, collaboration, and reduces risks of bugs.

### To get started with PEP 8