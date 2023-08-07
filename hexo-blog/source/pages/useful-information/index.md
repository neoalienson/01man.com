---
title: Useful Information
id: 2148
comments: false
date: 2023-04-04 21:03:05
---

@[toc]

## About
This page contains useful information to myself. It also serve as a testing page for this blog.

## Software Development

### Architecture
* [Microsoft Azure Architecture Center](https://docs.microsoft.com/en-us/azure/architecture/)

### Security
* [Instrumentation tookit](https://www.frida.re/)
* Mask sensitive information such as Proxy-Authorization when running command, 
  `curl -v https://somewhere.need.authenticated.proxy 2>&1 | sed -E "s/(proxy-authorization:).*/\1: ***/i"`
* [Nessus](https://www.nessus.org/)
* [OWASP](https://www.owasp.org/)
* [SANS](https://www.sans.org)
* [Snort (IDS)](https://www.snort.org)


### ASP.Net
* [ASP.NET string.Format (Chinese)](aspnet-string-format.html)

### Miscellaneous
* [High Performance Browser Networking](https://hpbn.co/)
* [asciinema](https://asciinema.org)
* [Creating an Alpine Linux package](https://wiki.alpinelinux.org/wiki/Creating_an_Alpine_package)
* [Visual Studio Code Keyboard Shortcuts for Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)


## Frequently Used Commands
* Shutdown Windows immediately ```shutdown -r -t 0```, useful when you remote to a Windows PC
* Switch java version
{% codeblock %}export JAVA_HOME=`/usr/libexec/java_home -v 1.8`{% endcodeblock %}

### Git
* Undo (Not pushed) ```git reset --soft HEAD~```
* Deleting a remote branch ```git push [remote] --delete [branch]``` e.g., ```git push origin --delete feature/branch```
* Sync remote branch and delete remote non-existing local copy ```git fetch --prune```
* List the commit different between branches ```git rev-list [branch]...[another branch]```
* List the commit different between branches with arrow indicates which branch owns the commit ```git rev-list --left-right [branch]...[another branch]```
* List the commit of a branch is ahead/behind to a remote branch ```git rev-list [branch]...[remote]/[another branch]```
* Show the number of ahead of behind between branches ```git rev-list --left-right count [branch]...[another branch]```
* Update submodules with latest commit ```git submodule update --remote```

## Windows

### Remove XBox
* Remove XBox with Powershell ```Get-ProvisionedAppxPackage -Online | Where-Object { $_.PackageName -match "xbox" } | ForEach-Object { Remove-ProvisionedAppxPackage -Online -AllUsers -PackageName $_.PackageName }```
* Check if any Xbox application is left ```dism /Online /Get-ProvisionedAppxPackages | Select-String PackageName | Select-String xbox```

### Windows shortcuts
Only those that are frequently used and easily forgotten are listed.
| | |
| --- | --- |
| Move Window to another monitor | <kbd>Windows</kbd> + <kbd>Shift</kbd> + <kbd>←</kbd> / <kbd>→</kbd> |
| Switch to another desktop | <kbd>Windows</kbd> + <kbd>⌃ Control</kbd> + <kbd>←</kbd> / <kbd>→</kbd> |
| Task View | <kbd>Windows</kbd> + <kbd>Tab</kbd> |
| Open Action Center | <kbd>Windows</kbd> + <kbd>A</kbd> |
| Display/Hide Desktop | <kbd>Windows</kbd> + <kbd>D</kbd> |
| Open File Explorer | <kbd>Windows</kbd> + <kbd>E</kbd> |
| Quick Link Menu (System tools such as Event Viewer) | <kbd>Windows</kbd> + <kbd>X</kbd> |
| Lock | <kbd>Windows</kbd> + <kbd>L</kbd> |

### Editing
| | |
| --- | --- |
| Switch Voice Typing | <kbd>Windows</kbd> + <kbd>H</kbd> |
| Open Clipboard History | <kbd>Windows</kbd> + <kbd>⌃ Control</kbd> + <kbd>V</kbd> |
| Paste as plain text[^1] | <kbd>Windows</kbd> + <kbd>V</kbd>[^2] |
| Capture screen and then OCR to clipboard[^1] | <kbd>Windows</kbd> + <kbd>T</kbd>[^2] |
| Emoji | <kbd>Windows</kbd> + <kbd>.</kbd>[^2] |

[^1]:Requires PowerToys
[^2]:Customized shortcut

## Visual Studio Code shortcuts
Only those that are frequently used and easily forgotten are listed.

### Basic
| | |
| --- | --- |
| User Settings | <kbd>⌃ Control</kbd> + <kbd>,</kbd> |

### Navigation
| | |
| --- | --- |
| Go to Line... | <kbd>⌃ Control</kbd> + <kbd>G</kbd> |
| Go to File... | <kbd>⌃ Control</kbd> + <kbd>P</kbd> |
| Go to next error or warning | <kbd>F8</kbd> |

### Debug
| | |
| --- | --- |
| Go to Line... | <kbd>⌃ Control</kbd> + <kbd>G</kbd> |
| Go to File... | <kbd>⌃ Control</kbd> + <kbd>P</kbd> |
| Go to next error or warning | <kbd>F8</kbd> |

## Learning

* [CodeSchool](https://www.codeschool.com)
* [CodeFight](https://codefights.com/)
* [HackerRank](https://www.hackerrank.com)
* [CodeCombat](https://codecombat.com)
* [CodinGame](https://www.codingame.com)
* [Learn Git Branching](https://learngitbranching.js.org/)
* [Learn Kubernetes using Interactive Browser-Based Scenarios](https://www.katacoda.com/courses/kubernetes)
* [(ISC)2 International Information Systems Security Certification Consortium](https://www.isc2.org/)
* [UN Climate Change Learning](https://unccelearn.org/)

## Tech

### Mac
* [Change Java version on MacOS] http://www.guigarage.com/2013/02/change-java-version-on-mac-os/

## Notes
