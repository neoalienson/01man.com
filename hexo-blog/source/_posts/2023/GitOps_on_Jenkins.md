---
title: GitOps on Jenkins Pipelines
date: 2023-09-25 02:38:00
tags:
  - GitOps
  - Jenkins
  - Groovy
categories:
  - Development
comments: false
---

s

If you're a developer who loves automation, you might have heard of GitOps. GitOps is a way of managing your infrastructure and applications using git as the single source of truth. GitOps lets you define your desired state in code, and then use tools like Terraform to apply that state to your environments. Gitops also enables continuous delivery, as any change in your git repository triggers a pipeline that deploys the new version of your code.

In the context of Jenkins pipelines, GitOps can be used to manage pipelines by treating the pipeline configuration as code, and using Git to manage changes to that code. This allows developers to version control their pipeline configurations, collaborate on changes with other team members, and easily roll back changes if necessary.

### Managing Jenkins Pipelines with Seeder Scripts

Seeder script is a script to create and maintain your pipelines on Jenkins. It is usually written in Groovy scripts.

Here is an example of a seeder script that creates pipelines in Jenkins. The script uses the Job DSL plugin to define the pipeline jobs in a declarative way. The script loops through a list of repositories and creates a pipeline job for each one. The details of the steps of each pipeline are referenced from the Jenkinsfile in their own repository.

~~~
/ Define the list of repositories
def repos = ['repo1', 'repo2', 'repo3']

// Loop through the list and create a pipeline job for each one
repos.each { repo ->
  pipelineJob("${repo}-pipeline") {
    // Use the SCM trigger to run the job when there is a change in the repository
    triggers {
      scm('H/5 * * * *')
    }
    // Define the pipeline script path as Jenkinsfile in the root of the repository
    definition {
      cpsScm {
        scm {
          git {
            remote {
              url("https://github.com/${repo}.git")
            }
            branch('master')
          }
        }
        scriptPath('Jenkinsfile')
      }
    }
  }
}
~~~

You may not feel the script is useful by having 3 pipelines created. Consider you need to create pipeline for different environments, iteration simplier the pipeline creation,
~~~
groovy
// Define a list of repos and environments
def repos = ['repo1', 'repo2', 'repo3']
def envs = ['dev', 'test', 'prod']

// Loop through the list and create a pipeline for each combination
for (repo in repos) {
  for (env in envs) {
    // Define the pipeline name and description
    def pipelineName = "${repo}-${env}"
    def pipelineDesc = "Pipeline for ${repo} in ${env} environment"

    // Create a pipeline job using the DSL plugin
    pipelineJob(pipelineName) {
      description(pipelineDesc)
      // Use the Jenkinsfile from the repo as the source of the pipeline definition
      definition {
        cpsScm {
          scm {
            git {
              remote {
                url("https://github.com/${repo}.git")
              }
              branches('master')
            }
          }
          // Specify the path to the Jenkinsfile in the repo
          scriptPath("Jenkinsfile-${env}")
        }
      }
    }
  }
}
~~~

While Seeder scripts can be used to define detail steps in your pipeline, it's important to keep these scripts simple and focused on managing the pipeline. Keeping seeder scripts simple makes it easier to maintain and collaborate with other team members.

### Benefits of Using GitOps with Seeder Scripts

Using seeder scripts can bring several benefits, including:

- Automation: You can automate the creation and update of Jenkins pipelines based on the changes in your Git repository. This reduces manual errors and saves time and effort.
- Immutability: You can keep your Jenkins pipelines immutable, meaning that they are not modified maually after they are created. This ensures consistency and reliability across different environments and stages.
- Versioning: You can track the history and changes of your Jenkins pipelines using Git commits and branches. This enables you to roll back to previous versions, compare different versions, and audit the changes.
- Collaboration: You can collaborate with other developers and teams on your Jenkins pipelines using Git features such as pull requests, code reviews, and merge conflicts. This improves the quality and security of your pipelines.
- Recovery: If Jenkins is corrupted or deleted by accident, you can use the seeder job to redeploy the pipelines from the Git repository.
- Portability: You can use GitOps to create the same set of pipelines on other Jenkins server. This is especially useful when you would like to test your pipelines with Jenkins / plugin upgrades.

However, there are also some challenges that you need to take care of when using GitOps to generate Jenkins pipelines. When you use GitOps to generate Jenkins pipelines, you may also use GitOps to destroy them when they are no longer needed. However, this may cause problems if you need to keep the output from pipeline executions (aka console log) for auditing or troubleshooting purposes. One way to overcome this challenge is to use a separate storage system for your log files.

GitOps is a concept that you can applies to automated everything Ops by using git as a single source of truth. Jenkins is just one of the applications.