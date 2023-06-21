---
title: Pair Programming with ChatGPT - A Developer's Dream Come True
date: 2023-03-30 13:35:46
tags:
  - Terraform
categories:
  - Development
comments: false
---

![](pair_programming.png)

As a full stack developer, I have practiced pair programming with many humans over the years. However, recently I had the opportunity to work with ChatGPT, a large language model trained by OpenAI, and it was a game-changer. I found that ChatGPT was not replacing my role, but rather working as a pair programming companion, providing me with valuable insights and perspectives. Let's dive into how it transformed my pair programming experience!

## Human and ChatGPT: A Perfect Synergy
The partnership between a human developer and ChatGPT is quite unique. Here's my typical loop:

1. Requirements Gathering: We human developer provides the requirements for a specific feature or function. ChatGPT write code and we human review.
2. Summarizing Requirements: I found it very useful to ask ChatGPT summarizes my requirements, as I usually not provide my requirements in one go. This helps me to check if we are in the same page.
3. Unit Test Template: ChatGPT generates a unit test template based on the summarized requirements.
4. Human Completes and Refines Unit Test: We human developer completes and refines the unit test and provides feedback to ChatGPT, refining their understanding of the task.

## Its turn for ChatGPT to review my code
In reverse, the human can write a program and ask ChatGPT to review and summarize the code. This process helps identify potential issues and ensures that the code meets the desired requirements. However, sometime you may need to help ChatGPT a little instead of throwing a piece of code. For example, 

### Try #1, simply ask to review
Prompt
```
review following terraform code in main.tf.

resource "some_resource" "resource_name" {
  name = "some_name"
  value = condition == true ? "aaa,bbb,ccc,${var.b}" : "${var.a},aaa,bbb,ccc,${var.b}"
}
```
Response

> The code you provided creates a resource named "some_resource" with the name "resource_name" and sets the "name" attribute to "some_name". Additionally, it sets the "value" attribute based on a condition. If the "condition" variable is true, then "value" is set to "aaa,bbb,ccc,${var.b}". If "condition" is false, then "value" is set to "${var.a},aaa,bbb,ccc,$${var.b}".
>
> The code appears to be valid and functional, assuming that the variables "a", "b", and "condition" have been properly defined. However, it's important to ensure that the resource type and its attributes are correct and properly configured for your infrastructure needs. Additionally, it's a good practice to use descriptive names for resources and attributes to make it easier to understand the purpose of the code.

The above sounds meaningless. Lets refine our question a little bit

### Try #2, tell what you want from code review

Prompt
```
review following terraform code in main.tf. can you propose better coding?

resource "some_resource" "resource_name" {
  name = "some_name"
  value = condition == true ? "aaa,bbb,ccc,${var.b}" : "${var.a},aaa,bbb,ccc,${var.b}"
}
```
Response

> The code seems fine in terms of syntax, but if you're looking for suggestions, here are a few:
> 
> It's always a good idea to use meaningful names for your resources, so you can easily identify them later. Instead of "some_resource" and "resource_name", try to come up with more descriptive names.
> 
> In the value attribute, it's generally better to avoid using ternary operators for complex expressions, as they can make the code harder to read and understand. Instead, consider breaking the expression into multiple lines, or creating a separate variable that holds the computed value.
> 
> Consider using interpolation syntax (${...}) only when necessary. In this case, since var.a and var.b are already variables, you can simply concatenate them with the other strings using the + operator.
> 
> Here's an example of how you could refactor the code with these suggestions:
>
> ```
> resource "some_resource" "example" {
>   name  = "example_resource"
>   value = compute_value(var.a, var.b, condition)
> }
> 
> // Define a separate function to compute the value
> // This makes the code easier to read and understand
> // and allows for reuse if needed
> locals {
>   compute_value = (a, b, condition) => {
>     if condition {
>       "aaa,bbb,ccc," + b
>     } else {
>       a + ",aaa,bbb,ccc," + b
>     }
>   }
> }
> ```
> This code uses a local variable to define a separate function that computes the value based on the input variables and the condition flag. This makes the code easier to read and understand, and also allows for reuse if needed.


With the magic question *can you propose better coding?* you have much meaningful result. Althougth it is not able to spot I am repeating part of the variable (`,aaa,bbb,ccc,${var.b}`), which against DRY principle. I have rewritten a bit and ask again as below,

### Try #3, ask for opinion from 2 pieces of my code

Prompt
```
which terraform code is better, can you propose better coding?

code 1,
  resource "some_resource" "resource_name" {
  name = "some_name"
  value = condition == true ? "aaa,bbb,ccc,${var.b}" : "${var.a},aaa,bbb,ccc,${var.b}"
}

code2,
  locals {
    a = {
      "aaa",
      "bbb",
      "ccc",
      var.b,
    }
  }
  resource "some_resource" "resource_name" {
  name = "some_name"
  value = join(",", condition == true ? [] : var.a, local.a)
}

```

Response

> Both code examples are valid and functional, but they have different purposes and implementations.
> 
> Code 1 uses a ternary operator to set the "value" attribute of the "some_resource" resource based on a condition. It's a concise way of setting the attribute, but it can be less readable for more complex expressions.
> 
> Code 2 uses a local variable to create a list of values to be joined together. It uses the "join" function to concatenate the values in the list with a comma as a separator. This approach can be more readable for longer lists of values and expressions.
> 
> Ultimately, the choice between these two code examples depends on the specific needs and requirements of your infrastructure. If you have a small list of values and a simple condition, Code 1 might be more appropriate. If you have a longer list of values and a more complex expression, Code 2 might be more appropriate.
> To propose a better coding, I would suggest combining the best parts of both code examples to create a more readable, maintainable, and extensible code.
> 
> ```
> locals {
>   some_values = [
>     "aaa",
>     "bbb",
>     "ccc",
>     var.b,
>   ]
> }
> 
> resource "some_resource" "resource_name" {
>   name  = "some_name"
>   value = join(",", concat(var.a, condition ? [] : local.some_values))
> }
> ```
> In this code, we use a local variable to store the hardcoded values and the "var.b" variable. Then, we concatenate the values of the "var.a" and local variable using the "concat" function. Finally, we use the "join" function to concatenate the values with a comma separator.
> 
> This code is more readable, maintainable, and extensible than the previous examples. It separates the hardcoded values from the variables, uses a more readable "concat" function instead of the ternary operator, and uses a more concise "join" function.
> 

Which combines improvements from both human and AI! However, I will use try #2 most likely as is effortless.

## Advantages of ChatGPT in Pair Programming
Here are some of the key advantages of using ChatGPT in pair programming, instead of another human:

1. 24/7 Availability: ChatGPT is always available, allowing you to work on projects whenever inspiration strikes, without waiting for a fellow developer.
2. Instant Feedback: Receive feedback on your code in real-time, streamlining your development process.
3. Consistency: ChatGPT offers consistent feedback quality, free from human bias or mood fluctuations.
4. Diversity: ChatGPT can provide diverse perspectives and insights that a human pair programmer may not have. This can lead to more creative and innovative solutions.
6. Learning Opportunities: By observing ChatGPT's suggestions and code reviews, developers can learn new coding techniques and best practices.

## Potential drawback

As shown in the example you should notice if you don't provide enough background or ask the correct question, the review result is not satisfactory.

## GitHub Copilot with Visual Stutio Code
I found it helps in code complete but it lack interactivitly for now.

## A New Era of Collaboration
Pair programming with ChatGPT is a game-changer. It offers a powerful synergy between human developers and AI, streamlining the development process and offering new learning opportunities. While it can never replace the creativity and problem-solving capabilities of a human developer, ChatGPT is an invaluable tool in the modern developer's arsenal. So, give it a try and experience the future of pair programming for yourself!
