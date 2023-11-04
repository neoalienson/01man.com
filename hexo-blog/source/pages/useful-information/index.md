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
* [Vulnerability Database](https://www.cybersecurity-help.cz/vdb/)

#### Passkey support
Passkey is a type of authentication method used to secure access to various online services and accounts. It is a unique key pair consisting of a public key and a private key that is generated specifically for an individual user. The passkey serves as a secure and convenient way to authenticate and encrypt data, providing an additional layer of protection for user accounts.

Services that support Passkey:
* [Bitwarden](https://bitwarden.com/)
* Windows (Windows Hello)
* iOS
* Andorid

Websites that support Passkey:
* [Google Account](https://myaccount.google.com)
* [GitHub](https://github.com)

Websites that do not yet support Passkey but support Multi-Factor Authentication (MFA):
* [Gitlab](https://gitlab.com)
* [Atlassian](https://atlassian.com) and its product family such as [Bitbucket](https://bitbucket.com)

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
| Move Window to another monitor | <kbd>&#x229E; Windows</kbd> + <kbd>&#x21E7; Shift</kbd> + <kbd>←</kbd> / <kbd>→</kbd> |
| Switch to another desktop | <kbd>&#x229E; Windows</kbd> + <kbd>⌃ Control</kbd> + <kbd>←</kbd> / <kbd>→</kbd> |
| Task View | <kbd>&#x229E; Windows</kbd> + <kbd>Tab</kbd> |
| Open Action Center | <kbd>&#x229E; Windows</kbd> + <kbd>A</kbd> |
| Display/Hide Desktop | <kbd>&#x229E; Windows</kbd> + <kbd>D</kbd> |
| Open File Explorer | <kbd>&#x229E; Windows</kbd> + <kbd>E</kbd> |
| Quick Link Menu (System tools such as Event Viewer) | <kbd>&#x229E; Windows</kbd> + <kbd>X</kbd> |
| Lock | <kbd>&#x229E; Windows</kbd> + <kbd>L</kbd> |

### Editing
| | |
| --- | --- |
| Switch Voice Typing | <kbd>&#x229E; Windows</kbd> + <kbd>H</kbd> |
| Open Clipboard History | <kbd>&#x229E; Windows</kbd> + <kbd>⌃ Control</kbd> + <kbd>V</kbd> |
| Paste as plain text[^1] | <kbd>&#x229E; Windows</kbd> + <kbd>V</kbd>[^2] |
| Capture screen and then OCR to clipboard[^1] | <kbd>&#x229E; Windows</kbd> + <kbd>T</kbd>[^2] |
| Emoji | <kbd>&#x229E; Windows</kbd> + <kbd>.</kbd>[^2] |

[^1]:Requires PowerToys
[^2]:Customized shortcut

## Visual Studio Code shortcuts
Only those that are frequently used and easily forgotten are listed. Refernce from https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf

### Basic
| | |
| --- | --- |
| User Settings | <kbd>⌃ Control</kbd> + <kbd>,</kbd> |
| Select all occurences of Find match |  <kbd>Alt</kbd> + <kbd>Enter</kbd> |
| Quick Fix |  <kbd>⌃ Control<</kbd> + <kbd>.</kbd> |
| Ctrl+K Ctrl+X |  <kbd>⌃ Control<</kbd> + <kbd>K</kbd> <kbd>⌃ Control<</kbd> + <kbd>X</kbd> |

### Navigation
| | |
| --- | --- |
| Go to Line... | <kbd>⌃ Control</kbd> + <kbd>G</kbd> |
| Go to File... | <kbd>⌃ Control</kbd> + <kbd>P</kbd> |
| Go to next error or warning | <kbd>F8</kbd> |
| Focus into 1st, 2nd or 3rd... editor group |  <kbd>⌃ Control</kbd> + <kbd>1</kbd>/<kbd>2</kbd>/<kbd>3</kbd>... |
| Spit editor |  <kbd>⌃ Control</kbd> + <kbd>\</kbd> |
| Show integrated termina | <kbd>⌃ Control</kbd> + <kbd>`</kbd> |
| Create new terminal | <kbd>⌃ Control</kbd> + <kbd>&#x21E7; Shift</kbd> + <kbd>`</kbd> |
| Show Explorer / Toggle focus | <kbd>⌃ Control</kbd> + <kbd>&#x21E7; Shift</kbd> + <kbd>E</kbd> |
| Show Search | <kbd>⌃ Control</kbd> + <kbd>&#x21E7; Shift</kbd> + <kbd>S</kbd> |
| Show Source Control | <kbd>⌃ Control</kbd> + <kbd>&#x21E7; Shift</kbd> + <kbd>G</kbd> |
| Show Debug | <kbd>⌃ Control</kbd> + <kbd>&#x21E7; Shift</kbd> + <kbd>D</kbd> |
| Show Extension | <kbd>⌃ Control</kbd> + <kbd>&#x21E7; Shift</kbd> + <kbd>X</kbd> |
| Replace in files | <kbd>⌃ Control</kbd> + <kbd>&#x21E7; Shift</kbd> + <kbd>H</kbd> |
| Show Output panel | <kbd>⌃ Control</kbd> + <kbd>&#x21E7; Shift</kbd> + <kbd>U</kbd> |
| Open Markdown preview to the side | <kbd>⌃ Control</kbd> + <kbd>K</kbd> <kbd>V</kbd> |

### Debug
| | |
| --- | --- |
| Toggle breakpoin | <kbd>F9</kbd> |
| Start/Continue | <kbd>F5</kbd> |
| Step over | <kbd>F10</kbd> |
| Step into | <kbd>F11</kbd> |
| Step out | <kbd>&#x21E7; Shift</kbd> + <kbd>F11</kbd> |

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
