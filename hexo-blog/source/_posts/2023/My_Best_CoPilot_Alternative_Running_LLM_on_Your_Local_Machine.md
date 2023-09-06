---
title: My Best CoPilot Alternative - Running LLM on Your Local Machine
date: 2023-09-03 20:41:00
tags:
categories:
  - Development
comments: false
prompt: You are a technology blog writer focus on software development. Write a blog with title "My Best CoPilot Alternative - Code Llama Local" . The blog introduce my code llama setup on my local machine with a nVidia display card 3060 12GB ram. With ollama I can set it run on wsl2 and integrate with visual studio code with extension "Continue". this solution is free. and can be faster than service like copilot. use a table to describe pros and cons between code llama running locally and copilot. you are a technology blog writer focus on software development. Write a blog with title "My Best CoPilot Alternative - Code Llama Local" .  you are writing a paragraph about ollama, which uses a Dockerfile like configuration and Docker layer to manage LLM. ollama helps a lot to setup and run Code Llama on Windows WSL 2.
---

As a software development blogger, I'm always on the lookout for new and innovative tools to help me improve my coding skills and increase my productivity. Recently, I stumbled upon Code Llama, a free, open-source large lauguage model (LLM) developed by Meta that allows you to set up on your low-cost gaming desktop. In this blog post, I'll be sharing my experience with Code Llama and how it can serve as a great alternative to CoPilot.

## Setup Code Llama with ollama

ollama (https://ollama.ai/), which uses a Dockerfile like configuration and Docker layer to manage LLM. ollama helps a lot to setup and run Code Llama on Windows WSL 2. Although the website says Windows is coming soon, I follow steps in https://github.com/jmorganca/ollama and running it successfully. The following are my setup,
1. Windows 11
2. WSL 2 with Ubuntu
3. nvidia 3060 12GB
4. https://github.com/jmorganca/ollama

If you do not have enough video RAM, it falls back to system RAM and CPU.

There are many model for you to choose (https://ollama.ai/library) but you should first try Code Llama. Same as the github guide you can pull the Code Llama with `ollama pull codellama`. However, there are license agreemenet to accept (https://ai.meta.com/resources/models-and-libraries/llama-downloads/). Once you have request, accept and approve, you can start using it. If you do not there are many others library you can try.

## How to Set Up Code Llama with Visual Studio Code

Setting up Code Llama with Visual Studio Code is easy and straightforward. Search and install an Visual Studio Code extension "Continue". This extension allows you use LLM from the service provider and local LLM service like ollama. "Continue" starts an interactively tutorial and you should start to use it happily.

## Local vs CoPilot (or anyother subscription base service)

There are many other CoPilot-like service provider that is free. Quality from free service usually poor so I will not compare on below table,

| Feature | Local | CoPilot (or anyother subscription based service) |
| --- | --- | --- |
| Cost of Ownership | USD 200 for a second hand nvidia 3060 12GB. Excluding the PC deskop that I already have | Nil |
| Price | Free. It costs me around 1kWh a month, which is negligible | Subscription-based, starting from USD 10 a month|
| ROI | 20 months | - |
| LLM for you to choose | Many. There are programming language specific model. | Depends on the provider |
| Input token limit | 100k (Code Llama) | 1500 (Copilot) |
| Integration with Visual Studio Code | Yes | Yes |
| Setup | Quite easy with ollama | Easy |
| Speed | Faster | Slower |
| Privacy | Your data stays on your local machine | Data is sent to third party for processing |
| Copyright | Depends on the model | Depends on service provider |

Input token is the "memory" of the context. GPT4's input token is 8k thats why you feel the code generated is better than CoPilot when your requirements is complex. Please note the number could be inaccurate as technology is advancing quick.

I will not go into detail comparison for now. This is because there are so many models you can use, and prompt could matter more than a model. You can customize system prompts that fits you best and switch between the model like hell from Continue. For example, below poor code could be generated from both Code Llama and GPT4 if you do not have a proper system prompt or even your context has been messed up,

> write a python script to generate six unique numbers from 1 to 49 

```
import random

def generate_numbers():
    numbers = []
    for i in range(6):
        number = random.randint(1, 49)
        while number in numbers:
            number = random.randint(1, 49)
        numbers.append(number)
    return numbers

# Call the function to generate six unique numbers
numbers = generate_numbers()

print(numbers)
```

Compare with prompt
> You are a seasoned programmer with a focus on use a single line of code to solve a problem if possible. Write a python script to generate six unique numbers from 1 to 49."

```
print(*random.sample(range(50), 6))
```

## Conclusion

Security and privacy are my top concern. Running LLM is my best choice.
