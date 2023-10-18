---
title: Everything as Code
date: 2023-10-15 03:55:01
tags:
categories:
  - Development
comments: false
prompt: write a blog post about everything as code, which includes infrastructure as code, policy as code, diagram as code, presentation as code, Database as Code, Documentation as code, Configuration as code, Workflow as code, Process as Code, Quality as code, UI as code, AI as code. list out the pros and cons. list out whether it is justify to use as code for each use case
---

<style>
.article-entry ul li {
  margin-bottom: 20px; 
}
</style>

# Everything as Code: A Trend or a Necessity?

In the era of cloud computing, automation, and DevSecOps, the concept of "everything as code" or simply "as code" has become increasingly popular and relevant. But what does it mean, and what are the benefits and challenges of adopting it?

Everything as code (EaC) is a paradigm that treats any aspect of software development, delivery, or operation as a code artifact that can be versioned, tested, and deployed using the same tools and processes as the application code. EaC encompasses various domains, such as:

- **Infrastructure as code (IaC)**: The practice of defining and managing cloud resources, such as servers, networks, and storage, using configuration files or scripts. Terraform is the best representations of Infrastructure as code.
- **Policy as code (PaC)**: The practice of expressing and enforcing security, compliance, or governance rules as code that can be integrated into the development and deployment pipelines.
- **Diagram as code (DaC)**: The practice of creating and updating diagrams, such as architecture diagrams or flowcharts, using code that can be rendered into graphical formats.
- **Presentation as code (PrC)**: The practice of creating and updating presentations, such as slides or reports, using code that can be converted into different formats or platforms. [slidev](https://sli.dev/) is one of the tool but HTML/CSS/JS and VBA can be an less human-readable alternative.
- **Database as code (DbC)**: The practice of defining and managing database schemas, data, and migrations using code that can be executed by database engines or tools.
- **Documentation as code (DoC)**: The practice of writing and maintaining documentation using plain text formats, such as Markdown or AsciiDoc, that can be processed by documentation generators or integrated into code repositories.
- **Configuration as code (CaC)**: The practice of defining and managing application settings, such as environment variables or feature flags, using code that can be applied dynamically or statically.
- **Workflow as code (WaC)**: The practice of defining and orchestrating complex workflows, such as data pipelines or business processes, using code that can be executed by workflow engines or platforms.
- **Process as code (PaC)**: The practice of defining and automating software development or operation processes, such as testing, deployment, or monitoring, using code that can be run by process tools or frameworks.
- **Quality as code (QaC)**: The practice of defining and measuring software quality attributes, such as performance, reliability, or security, using code that can be integrated into the development and deployment pipelines.
- **UI as code (UIC)**: The practice of creating and updating user interfaces, such as web pages or mobile apps, using code that can be rendered into different devices or platforms. 
- **AI as code (AIC)**: The practice of creating and updating artificial intelligence models, such as machine learning or deep learning models, using code that can be trained and deployed using AI frameworks or platforms. Meanwhile, model can be layered" with inferencing. ollama has Dockerfile like as code that can be used for that purpose beside system prompt.

## The main advantages of EaC are:

- **Consistency**: EaC ensures that all aspects of software development, delivery, or operation are consistent with each other and with the application code. This reduces errors, conflicts, and discrepancies that may arise from manual or ad hoc interventions.
- **Reusability**: EaC enables the reuse of code artifacts across different projects, environments, or teams. This increases efficiency, productivity, and collaboration among developers and operators.
- **Traceability**: EaC provides a clear and complete history of changes made to any aspect of software development, delivery, or operation. This facilitates auditing, debugging, and troubleshooting issues that may occur during the software lifecycle.
- **Scalability**: EaC allows for the easy and rapid scaling of cloud resources, workflows, or models to meet changing demands or requirements. This improves performance, availability, and resilience of software systems.
- **Automation**: EaC enables the automation of tasks that are otherwise tedious, time-consuming, or error-prone. This frees up developers and operators to focus on more creative or strategic activities.

## The main challenges of EaC are:

- **Complexity**: EaC introduces additional layers of abstraction and complexity to software development, delivery, or operation. This requires developers and operators to learn new skills, tools, and languages to deal with different domains of EaC.
- **Integration**: EaC requires the integration of various tools and platforms to support different domains of EaC. This may pose compatibility issues,
security risks,
or maintenance overheads for developers and operators.
- **Testing**: Most as code demands rigorous testing of code artifacts to ensure their correctness,
reliability, and quality. This may require additional resources, time, or expertise for developers and operators.

## Is it justified
Is it justified to use EaC for each use case? The answer depends on several factors,
such as:

- The nature and scope of the project: Some projects may benefit more from EaC than others, depending on their size, complexity,or domain. For example, a large-scale, distributed, or data-intensive project may benefit more from IaC, WaC, or AIC than a small-scale, monolithic, or logic-intensive project.
- The maturity and availability of the tools and platforms: Some tools and platforms may support EaC better than others,depending on their features, functionality, or compatibility. For example, some cloud providers may offer more options and flexibility for IaC than others, or some AI frameworks may offer more capabilities and performance for AIC than others.
- The skills and preferences of the developers and operators: Some developers and operators may prefer EaC over others,depending on their skills, experience, or style. For example, some developers may enjoy writing code more than using graphical interfaces, or some operators may prefer using code more than using dashboards.

## Status of as code in each domain

With the above factor, below is the scale from my personal view,

| as code | status | justified (5 star max) | 
| --- | --- | --- |
| Infrastructure | Very mature and widely use | :star::star::star::star::star: |
| Policy | Mature but not being widely use | :star::star::star: |
| Diagram | Depends on diagram type. Some is difficult to adjust layout | :star::star::star: |
| Presentation | Difficult to fine tune layout and create animations | :star: | 
| Database  | | :star::star::star::star::star: |
| Documentation | | :star::star::star: |
| Configuration  | | :star::star::star: |
| Workflow   | | :star::star::star: |
| Process    | | :star::star::star: |
| Process    | HTML, Android, iOS | :star::star::star: |
| AI    | Model can be layered | :star::star: |

## Conclusion

In conclusion, EaC is a powerful and promising paradigm that can enhance software development, delivery, or operation. However, it also comes with its own challenges and trade-offs that need to be considered carefully before adopting it. EaC is not a one-size-fits-all solution, but rather a context-dependent choice that depends on the project, the tools, and the people involved.
