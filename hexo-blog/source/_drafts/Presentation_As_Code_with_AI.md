---
title: Presentation as Code with AI
date: 2023-11-01 20:27:18
tags:
  - AI
categories:
  - Development
comments: false
prompts: write a conclusion about presentation as code using slidev. even with the help of large language model, we still have a lot of difficulties on using code to prepare a presentation in most case, especially on moving elements to resize and fit for human reading. not to mention to make the presentation more awesome with animations. 
---

Have you ever heard of the concept of "everything as code"? It means that we can use code to define, manage, and automate various aspects of our systems, such as infrastructure, diagrams, policies, and more. But what about presentations? Can we also use code to create beautiful and interactive slides?

The answer is yes, thanks to Slidev, a presentation framework that lets you write slides using Markdown and Vue.js. Slidev is based on the idea of presentation as code, which means that you can use your favorite code editor, version control system, and development tools to create and share your slides.

In this blog post, I will introduce you to Slidev and show you how it compares to traditional presentation tools like PowerPoint. I will also explore the possiblity of generating prensentation code with large language model (LLM) AI.

## What is Presentation as Code?

Presentation as code is a way of creating presentations using code instead of graphical user interfaces. It has several advantages over traditional presentation tools, such as:

- You can use your preferred code editor and syntax highlighting
- You can leverage the power and flexibility of programming languages and frameworks
- You can reuse and modularize your slides and components
- You can collaborate and version control your slides using Git or other tools
- You can automate and customize your presentation workflow
- You can integrate your slides with external data sources and APIs

Of course, presentation as code also has some drawbacks, such as:

- You need to learn a new syntax or framework
- You may lose some visual feedback and interactivity
- You may have less control over the layout and design of your slides
- You may face compatibility issues with different browsers and devices
- Difficult to add animations

One of the benefits of presentation as code is that you can use any programming language or framework that you like. For example, you can use HTML, CSS, and JavaScript to create web-based slides, or you can use LaTeX to create PDF slides.

However, if you are looking for a specific framework that is designed for presentation as code, you may want to check out Slidev (https://github.com/slidevjs/slidev).

Another alternative is using VBA in PowerPoint to create slides. VBA is less human readable compare with markdown. As this post focus on presentation as code so I will focus on Slidev.

## Slidev with LLM

Slidev markdown for presentation is cleaner than HTML/CSS/Javascript in most case. The markdown is more human readible. LLM such as ChatGPT could generate markdown with prompt, eg, 
use slidev to generate a presentation about solar system for primary school student. use fade out for transition.

The result is a clean Slidev markdown in 4 slides,
~~~
---
title: Solar System
transition: fade-out
---

# The Solar System

---

## What is the Solar System?

The Solar System is made up of the Sun and all the objects that orbit around it. Let's explore the planets and other fascinating things in our Solar System!

---

## The Sun

The Sun is a star at the center of our Solar System. It is a giant ball of hot, glowing gases. The Sun provides light and heat to all the planets.

---

## The Planets

| Planet   | Description                                        |
|----------|----------------------------------------------------|
| Mercury  | Closest to the Sun, small and rocky                 |
| Venus    | Known as the "evening star," has a thick atmosphere |
| Earth    | Our home planet, with land, water, and atmosphere   |
| Mars     | Red planet with polar ice caps and dusty storms     |
| Jupiter  | Largest planet, with colorful stripes and big storms|
| Saturn   | Known for its beautiful rings made of ice and dust  |
| Uranus   | Tilted on its side, with icy blue color             |
| Neptune  | Cold, blue planet with strong winds                 |

---

## Other Objects

Apart from the Sun and planets, the Solar System also has other interesting objects:

- **Moon**: Earth's natural satellite
- **Asteroids**: Rocky objects that orbit the Sun
- **Comets**: Icy objects that leave a glowing trail when they get close to the Sun

---

## Fun Facts

- The Sun is so big that you can fit more than a million Earths inside it!
- Jupiter has a famous storm called the Great Red Spot, which is larger than Earth.
- Saturn's rings are not solid but made up of billions of small pieces of ice and rock.
- The Moon is about 1/4th the size of Earth and is our closest neighbor in space.

---

## Conclusion

The Solar System is a fascinating place with the Sun, planets, and other interesting objects. It's incredible to learn about the wonders of space!

---

# Questions?

Feel free to ask any questions you have about the Solar System!
~~~

Like other image generation AI, LLM AI does not have perspective from human being. It is quite often text overflow because AIs are usually tuned to be wordly.

### What about images?

The only way to add image is very labour intesive with LLM alone. You have to search for suitable image and then download. Update the prompt with the filename and placement works but again result can be unexpected.

### What about charts?

You can create charts with Mermaid but known LLM are not optimized with such task. Manual.

### What about animation?

Slidev comes with Latex support but it has a steep learning curve. Not recommended for now.

# Conclusion

In conclusion, slidev is a great tool for creating presentations with code, but it is not without its challenges. Even with the help of a large language model, we still have to deal with the complexity of coding the layout, design, and animation of our slides. Sometimes, it can be frustrating and time-consuming to get the desired result. However, slidev also offers many benefits, such as flexibility, interactivity, and compatibility with other web technologies. Therefore, we think slidev is worth trying if you are looking for a new way to present your ideas with code.
