---
title: Troubleshooting Terraform
date: 2023-09-27 19:41:00
tags:
  - terraform
categories:
  - Development
comments: false
prompt: You are a technology blog writer focus on software development. Write a blog with title "Troubleshooting Terraform" . The blog post introduces use of tf_log=debug that generates details log for debugging and find out root cause. Also, use of -parallelism=1 in plan and apply together with debug log, which makes the log easier to read by running one execution at a time. Provide example for log with and without -parallelism=1

---

Terraform is a great tool for managing infrastructure as code, but sometimes it can be tricky to debug when things go wrong. In this blog post, I'll share  tips on how to troubleshoot Terraform issues.

## Enabling Debug Log
The `TF_LOG` environment variable allows you to set the log level for Terraform, which can be useful for getting more details about what Terraform is doing behind the scenes. You can set it to one of these values: `TRACE`, `DEBUG`, `INFO`, `WARN`, or `ERROR`. The default is `INFO`, which only shows high-level messages. To get more verbose output, you can set it to `DEBUG` or `TRACE`. For example, you can run this command before running Terraform:

`export TF_LOG=DEBUG`

or run it in single line

`export TF_LOG=DEBUG && terraform plan`

If you specify `TF_LOG_PATH` environment variable, log will store into the file.

## TF_LOG_CORE and TF_LOG_PROVIDER

The debug log can be massive and over 100MB! If you would like to focus on debugging provider you should use `TF_LOG_PROVIDER` with arguments from `TF_LOG`. If you suspect problem with dependency you should use `TF_LOG_CORE`.

## Dependency and Parallelism
Terrafrom analyses dependencies between Terraform modules before execution. Dependency analysis ensure resources are provisioned in the correct order. Meanwhile, Terrafrom use the analysis result for efficient parallel execution of operations by identifying independent sets of resources that can be provisioned or modified concurrently. However, logs from concurrent execution is very difficult to read and we have to disable the concurrcy with parameter `-parallelism=1` on `plan` and `apply`.

With `-parallelism=1`, whe resources are created/modified/destroyed one at a time, in sequence. This allows for easier debugging and troubleshooting, as each resource is executed one at a time. eg, `terraform apply -parallelism=1`:
{% mermaid %}
graph TD
  A[Terraform Operation] --> C[Resource 1 Modification]
  C --> D[Resource 2 Modification]
  D --> E[Terraform Execution Completed]
{% endmermaid %}
This chart shows the Terraform operation with parallelism set to 1. 

When `-parallelism` is not specify, default value is 10. The resources are created/modified/destroyed in parallel, allowing for faster execution. However, this can also make it more difficult to debug and troubleshoot issues, as multiple resources are executed simultaneously. eg, `terraform apply`:
{% mermaid %}
  graph TD
  A[Terraform Operation] --> C[Resource 1 Modification]
  C --> D
  A --> D[Resource 2 Modification]
  D --> E[Terraform Execution Completed]
{% endmermaid %}
