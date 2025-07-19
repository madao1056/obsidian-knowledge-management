---
notion_id: 214ade4a-d294-80f3-82a8-c7b8f4cdd79b
created_time: 2025-06-16T07:47:00.000Z
last_edited_time: 2025-06-16T07:56:00.000Z
url: https://www.notion.so/GitHub-214ade4ad29480f382a8c7b8f4cdd79b
parent_type: page_id
archived: False
sync_time: 2025-07-19T12:48:13.432441
---

# GitHub

https://github.com/microsoft/pxt/tree/master/common-docs/javascript
# Classes
Traditional JavaScript focuses on functions and prototype-based inheritance as the basic means of building up reusable components,
but this may feel a bit awkward to programmers more comfortable with an object-oriented approach, where classes inherit functionality
and objects are built from these classes.
Starting with ECMAScript 2015, also known as ECMAScript 6, JavaScript programmers will be able to build their applications using
this object-oriented class-based approach. TypeScript, allows you to use these techniques.
Let's take a look at a simple class-based example:
```typescript
class Greeter {
    greeting: string;
    constructor(message: string) {
        this.greeting = message;
    }
    greet() {
        return "Hello, " + this.greeting;
    }
}

let greeter = new Greeter("world");

```
We declare a new class Greeter. This class has three members: a property called greeting, a constructor, and a method greet.
You'll notice that in the class when we refer to one of the members of the class we prepend this..
This denotes that it's a member access.
In the last line we construct an instance of the Greeter class using new.
This calls into the constructor we defined earlier, creating a new object with the Greeter shape, and running the constructor to initialize it.
## Inheritance
In TypeScript, we can use common object-oriented patterns.
Of course, one of the most fundamental patterns in class-based programming is being able to extend existing classes to create new ones using inheritance.
Let's take a look at an example:
```typescript
class Animal {
    name: string;
    constructor(theName: string) { this.name = theName; }
    move(distanceInMeters: number = 0) {
        console.log(`${this.name} moved ${distanceInMeters}m.`);
    }
}

class Snake extends Animal {
    constructor(name: string) { super(name); }
    move(distanceInMeters = 5) {
        console.log("Slithering...");
        super.move(distanceInMeters);
    }
}

class Horse extends Animal {
    constructor(name: string) { super(name); }
    move(distanceInMeters = 45) {
        console.log("Galloping...");
        super.move(distanceInMeters);
    }
}

let sam = new Snake("Sammy the Python");
let tom: Animal = new Horse("Tommy the Palomino");

sam.move();
tom.move(34);

```
This example covers quite a few of the inheritance features in TypeScript that are common to other languages.
Here we see the extends keywords used to create a subclass.
You can see this where Horse and Snake subclass the base class Animal and gain access to its features.
Derived classes that contain constructor functions must call super() which will execute the constructor function on the base class.
The example also shows how to override methods in the base class with methods that are specialized for the subclass.
Here both Snake and Horse create a move method that overrides the move from Animal, giving it functionality specific to each class.
Note that even though tom is declared as an Animal, since its value is a Horse, when tom.move(34) calls the overriding method in Horse:
```plain text
Slithering...
Sammy the Python moved 5m.
Galloping...
Tommy the Palomino moved 34m.

```
## Public, private, and protected modifiers
### Public by default
In our examples, we've been able to freely access the members that we declared throughout our programs.
If you're familiar with classes in other languages, you may have noticed in the above examples
we haven't had to use the word public to accomplish this; for instance,
C# requires that each member be explicitly labeled public to be visible.
In TypeScript, each member is public by default.
You may still mark a member public explicitly.
We could have written the Animal class from the previous section in the following way:
```typescript
class Animal {
    public name: string;
    public constructor(theName: string) { this.name = theName; }
    public move(distanceInMeters: number) {
        console.log(`${this.name} moved ${distanceInMeters}m.`);
    }
}

```
### Understanding private
When a member is marked private, it cannot be accessed from outside of its containing class. For example:
```typescript
class Animal {
    private name: string;
    constructor(theName: string) { this.name = theName; }
}

new Animal("Cat").name; // Error: 'name' is private;

```
TypeScript is a structural type system.
When we compare two different types, regardless of where they came from, if the types of all members are compatible, then we say the types themselves are compatible.
However, when comparing types that have private and protected members, we treat these types differently.
For two types to be considered compatible, if one of them has a private member,
then the other must have a private member that originated in the same declaration.
The same applies to protected members.
Let's look at an example to better see how this plays out in practice:
```typescript
class Animal {
    private name: string;
    constructor(theName: string) { this.name = theName; }
}

class Rhino extends Animal {
    constructor() { super("Rhino"); }
}

class Employee {
    private name: string;
    constructor(theName: string) { this.name = theName; }
}

let animal = new Animal("Goat");
let rhino = new Rhino();
let employee = new Employee("Bob");

animal = rhino;
animal = employee; // Error: 'Animal' and 'Employee' are not compatible

```
In this example, we have an Animal and a Rhino, with Rhino being a subclass of Animal.
We also have a new class Employee that looks identical to Animal in terms of shape.
We create some instances of these classes and then try to assign them to each other to see what will happen.
Because Animal and Rhino share the private side of their shape from the same declaration of
private name: string in Animal, they are compatible. However, this is not the case for Employee.
When we try to assign from an Employee to Animal we get an error that these types are not compatible.
Even though Employee also has a private member called name, it's not the one we declared in Animal.
### Understanding protected
The protected modifier acts much like the private modifier with the exception that members
declared protected can also be accessed by instances of deriving classes. For example,
```typescript
class Person {
    protected name: string;
    constructor(name: string) { this.name = name; }
}

class Employee extends Person {
    private department: string;

    constructor(name: string, department: string) {
        super(name);
        this.department = department;
    }

    public getElevatorPitch() {
        return `Hello, my name is ${this.name} and I work in ${this.department}.`;
    }
}

let howard = new Employee("Howard", "Sales");
console.log(howard.getElevatorPitch());
console.log(howard.name); // error

```
Notice that while we can't use name from outside of Person,
we can still use it from within an instance method of Employee because Employee derives from Person.
---
# Functions
Functions are the fundamental building block of programs. Here is the simplest
way to make a function that adds two numbers:
```typescript
// Named function
function add(x : number, y : number): number {
    return x + y;
}

let sum = add(1, 2);

```
### ~ hint
### Parameter types
You must specify a type for each function parameter.
### ~
Functions can refer to variables outside of the function body.
When they do so, they're said to capture these variables.
```typescript
let z = 100;

function addToZ(x: number, y: number) {
    return x + y + z;
}

let sum = addToZ(1, 2);

```
Let's add a return type to our add function:
```typescript
function add(x: number, y: number): number {
    return x + y;
}

```
TypeScript can figure the return type out by looking at the return statements, so you can optionally leave this off in many cases.
## Optional and Default Parameters
In TypeScript, the number of arguments given to a function has to match the number of parameters the function expects.
```typescript
function buildName(firstName: string, lastName: string) {
    return firstName + " " + lastName;
}

let result1 = buildName("Bob");                  // error, too few parameters
let result2 = buildName("Bob", "Adams", "Sr.");  // error, too many parameters
let result3 = buildName("Bob", "Adams");         // ah, just right

```
In JavaScript, every parameter is optional, and users may leave them off as they see fit.
When they do, their value is undefined.
We can get this functionality in TypeScript by adding a ? to the end of parameters we want to be optional.
For example, let's say we want the last name parameter from above to be optional:
```typescript
function buildName(firstName: string, lastName?: string) {
    if (lastName)
        return firstName + " " + lastName;
    else
        return firstName;
}

let result1 = buildName("Bob");                  // works correctly now
let result2 = buildName("Bob", "Adams", "Sr.");  // error, too many parameters
let result3 = buildName("Bob", "Adams");         // ah, just right

```
Any optional parameters must follow required parameters.
Had we wanted to make the first name optional rather than the last name, we would need to change the order of parameters in the function, putting the first name last in the list.
In TypeScript, we can also set a value that a parameter will be assigned if the user does not provide one, or if the user passes undefined in its place.
These are called default-initialized parameters.
Let's take the previous example and default the last name to "Smith".
```typescript
function buildName(firstName: string, lastName = "Smith") {
    return firstName + " " + lastName;
}

let result1 = buildName("Bob");                  // works correctly now, returns "Bob Smith"
let result2 = buildName("Bob", undefined);       // still works, also returns "Bob Smith"
let result3 = buildName("Bob", "Adams", "Sr.");  // error, too many parameters
let result4 = buildName("Bob", "Adams");         // ah, just right

```
Default-initialized parameters that come after all required parameters are treated as optional, and just like optional parameters, can be omitted when calling their respective function.
This means optional parameters and trailing default parameters will share commonality in their types, so both
```typescript
function buildName(firstName: string, lastName?: string) {
    // ...
}

```
and
```typescript
function buildName(firstName: string, lastName = "Smith") {
    // ...
}

```
share the same type (firstName: string, lastName?: string) => string.
The default value of lastName disappears in the type, only leaving behind the fact that the parameter is optional.
Unlike plain optional parameters, default-initialized parameters don't need to occur after required parameters.
If a default-initialized parameter comes before a required parameter, users need to explicitly pass undefined to get the default initialized value.
For example, we could write our last example with only a default initializer on firstName:
```typescript
function buildName(firstName = "Will", lastName: string) {
    return firstName + " " + lastName;
}

let result1 = buildName("Bob");                  // error, too few parameters
let result2 = buildName("Bob", "Adams", "Sr.");  // error, too many parameters
let result3 = buildName("Bob", "Adams");         // okay and returns "Bob Adams"
let result4 = buildName(undefined, "Adams");     // okay and returns "Will Adams"

```
## Arrow Functions
Arrow functions, also known as lambda functions, provide a lightweight syntax for functions. Arrow functions are used extensively to provide event handlers for many APIs. For example:
```typescript
function foo(handler: Action) {
    // call handler ...
}

foo(() => { // arrow function!
   // do something
})

```
Often, a function like foo() will save the arrow function handler in a variable to run the code inside the function later when a certain condition occurs. Arrow functions serve as a kind of shortcut to provide extra code to run without having to write a separate formal function for that purpose. In this way arrow, or lambda, functions are thought of as "anonymous" functions.
Read more about arrow functions...
## Anonymous Functions
Anonymous functions are used just like arrow functions. They're called "anonymous" because the function doesn't have a name and isn't called using a name. The function is remembered by it's reference. This means that a variable is used to remember the function or the function is used directly ("inline").
Here's an example similar to the one shown for arrow functions but this time the foo() function uses an anonymous function directly:
```typescript
function foo(handler: Action) {
    // call handler ...
}

foo(function() { // use an inline function
   // do something
})

```
Also, you can set a variable to remember the function and use that variable as a reference to the anonymous function:
```typescript
function foo(handler: Action) {
    // call handler ...
}

let anon = function() { // anonymous function, set it to a variable
    // do something
}

foo(anon)

```
---

## 🏷️ タグ
#Web制作_技術

## 🔗 関連ナレッジ
- [[MakeCode言語: ブロック、静的TypeScript]] - カテゴリ: Web制作・技術 キーワード: JavaScript, TypeScript
- [[課題について]] - カテゴリ: Web制作・技術 キーワード: JavaScript, TypeScript
- [[まさた_実務レベルのJavaScriptスキルを身につける学習法]] - カテゴリ: Web制作・技術 キーワード: JavaScript
- [[まさた_2児のママがたった3ヶ月でWeb制作者へ転身した話]] - カテゴリ: Web制作・技術 キーワード: JavaScript
- [[まさた_才能なしでもWeb制作で月収50万以上が可能な理由]] - カテゴリ: Web制作・技術 キーワード: JavaScript
