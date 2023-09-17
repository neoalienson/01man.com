---
title: Hexo Blogging Cheatsheet
date: 2022-12-08 09:56:37
comments: false
---

@[toc]

## Useful links
* [Hexo Docs](https://hexo.io/docs)
* [List of XML and HTML character entity references on Wikipedia](https://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references)

## My blog's information
* [Check if my domain is blocked in mainland](http://www.viewdns.info/chinesefirewall/?domain=01man.com)

## Design
* [Font Awesome](http://fontawesome.io/icons/#brand)

## Frequently used Emoji
|                         |                                |        |
| ----------------------- | ------------------------------ | ------ |
| :smile: ````:smile:```` | :blush: ````:blush:```` | :heart_eyes: ````:heart_eyes:```` |
| :sweat: ````:sweat:```` | :thumbsup: ````:thumbsup:```` | :yum: ````:yum:```` |
| :cold_sweat: ````:cold_sweat:```` | :scream: ````:scream:```` | :sob: ````:sob:```` |
| :stuck_out_tongue_winking_eye: ````:stuck_out_tongue_winking_eye:```` | :kissing: ````:kissing:```` | :sleepy: ````:sleepy:```` |
| :poop: ````:poop:````   | :v: ````:v:```` | :100: ````:100:```` |
| :see_no_evil: ````:see_no_evil:```` | :hear_no_evil: ````:hear_no_evil:```` | :speak_no_evil: ````:speak_no_evil:```` |
| :kiss: ````:kiss:````   | :skull: ````:skull:```` | :droplet: ````:droplet:```` |
| :fireworks: ````:fireworks:```` | :loudspeaker: ````:loudspeaker:```` | :warning: ````:warning:```` |
| :no_entry_sign: ````:no_entry_sign:```` | :white_check_mark: ````:white_check_mark:```` | :x: ````:x:```` |
| :secret: ````:secret:```` | :interrobang: ````:interrobang:```` | :bangbang: ````:bangbang:```` |

and more from [Emoji Cheatsheet](https://www.webpagefx.com/tools/emoji-cheat-sheet/)

## CSS
### Keys
* <kbd>Control</kbd> &lt;kbd&gt;Contro&lt;/kbd&gt;
* <kbd>Shift &#x21E7;</kbd> &lt;kbd&gt;Shift &amp;#x21E7;&lt;/kbd&gt; - use Unicode characters

## Markdown (with Markdown plus)
* `++Inserted++` ++Inserted++ (disabled)
* Footnote ```[^1]``` for the mark, ```[^1]:``` for the note
* Use {% raw %}{% raw %}{% endraw %}{% endraw %} if the markdown cause you trouble on {% raw %}{{}} or {%%}{% endraw %}
* Youtube Video {% raw %}{% youtube [youtube id] %}{% endraw %}

| Action | Markdown | Sample |
| ------ | -------- | ------ |
| sub | `H~2~0` | H~2~0 |
| sup | `x^2^` | x^2^ |
| Bold | `**bold**` | **bold** |
| Italic | `*italic*` | *italic* |
| Bold and Italic | `***bold and italic***` | ***bold and italic*** |
| Strikethrough | `~~strikethrough~~` | ~~strikethrough~~ |
| Inline code | `` `inline code` `` | `inline code` |
| Link | `[link text](https://example.com)` | [link text](https://example.com) |
| Image | `![alt text](https://example.com/image.jpg)` | ![alt text](https://example.com/image.jpg) |

| Action | Markdown | 
| ------ | -------- |
| Blockquote | `> blockquote` | 
> blockquote

| Action | Markdown | 
| ------ | -------- |
| Ordered list | `1. item 1` |
1. item 1
2. item 2

| Action | Markdown | 
| ------ | -------- | 
| Unordered list | `- item 1` |
- item 1
- item 2

| Action | Markdown | 
| ------ | -------- | 
| Horizontal rule | `---` |

| Action | Markdown | 
| ------ | -------- | 
| Code block | `~~~`|
~~~
Code block 
~~~

## Github Card
{% codeblock %}
{% raw %}{% githubCard user:neoalienson repo:pachinko %}{% endraw %}
{% endcodeblock %}
{% githubCard user:neoalienson repo:pachinko %}

## Mermaid Flowchart

{% codeblock %}
{% raw %}
{% mermaid %}
flowchart TD
    A[Christmas] -->|Get money| B(Go shopping)
    B --> C{Let me think}
    C -->|One| D[Laptop]
    C -->|Two| E[iPhone]
    C -->|Three| F[fa:fa-car Car]
{% endmermaid %}
{% endraw %}
{% endcodeblock %}

{% mermaid %}flowchart TD
    A[Christmas] -->|Get money| B(Go shopping)
    B --> C{Let me think}
    C -->|One| D[Laptop]
    C -->|Two| E[iPhone]
    C -->|Three| F[fa:fa-car Car]
{% endmermaid %}

## Barchart
Barchart from [easy charts](https://www.npmjs.com/package/hexo-tag-easy-charts)
{% barchart 'Sample Chart' %}
Apple | Orange | Banana | Lemon
50 | 740 | 218 | 193
{% endbarchart %}

{% codeblock %}
{% raw %}{% barchart 'Sample Chart' %}
Apple | Orange | Banana | Lemon
50 | 740 | 218 | 193
{% endbarchart %}{% endraw %}
{% endcodeblock %}
