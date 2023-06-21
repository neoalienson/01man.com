---
title: Using custom validation to validate other variables in Terraform
date: 2022-12-09 19:35:46
tags:
  - Terraform
categories:
  - Development
comments: false
---

![](terraform.png)

**This blog post is generated with ChatGPT**

In Terraform, you can use custom validation blocks to define your own custom validation rules for Terraform variables. These validation blocks allow you to specify a validation function that Terraform will use to validate the value of the variable. You can also use these custom validation blocks to validate other variables in your Terraform configuration.

To validate other variables from a custom validation function, you can use the `var` keyword followed by the name of the variable you want to validate. For example, if you have two variables named `subnet_id` and `vpc_id`, and you want to validate that the `subnet_id` is associated with the `vpc_id`, you could define a custom validation block like this:

```
variable "subnet_id" {
  type = string
}

variable "vpc_id" {
  type = string
}

validation {
  condition = can_associate_subnet_with_vpc(var.subnet_id, var.vpc_id)
  error_message = "The specified subnet is not associated with the specified VPC."
}

function can_associate_subnet_with_vpc(subnet_id, vpc_id) {
  // perform validation logic here
}
```

In the example above, we define a custom validation block that calls the `can_associate_subnet_with_vpc` function to validate that the `subnet_id` is associated with the `vpc_id`. The `can_associate_subnet_with_vpc` function takes two arguments, `subnet_id` and `vpc_id`, which are both passed using the `var` keyword.

Inside the function, you can perform any validation logic you need to validate the variables. If the validation is successful, the function should return `true`, and if the validation fails, it should return `false`.

By using the `var` keyword and passing the variables to your custom validation function, you can easily validate multiple variables in your Terraform configuration and ensure that they meet your requirements.

In summary, to validate other variables from a custom validation function in Terraform, you can use the `var` keyword followed by the name of the variable you want to validate. This allows you to easily validate multiple variables in your Terraform configuration and ensure that they meet your requirements.