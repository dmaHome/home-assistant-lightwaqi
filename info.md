[![GitHub Release][img-release]][link-release]
[![Maintainer][img-maintainer]][link-maintainer]
[![All Contributors][img-contributors]][link-contributors]
[![PRs Welcome][img-contribute]][link-contribute]
[![Open issues][img-issues]][link-issues]
[![Stargazers][img-stars]][link-stars]

## Description :mag:

This project is a light implementation of the WAQI component that allows to specify a specific 
station using its identifier. It has mainly be tested with stations located in France. It publishes
information from the [World Air Quality Index](http://aqicn.org/).

This project is based on the official [WAQI component](https://www.home-assistant.io/components/waqi/) 
of [home assistant](https://www.home-assistant.io).

## Configuration :gear:

```yaml
# Example configuration.yaml entry
sensor:
  - platform: lightwaqi
    scan_interval: 300
```

- **icon** _(string) (optional)_  
  [Material Design Icon](https://materialdesignicons.com) that illustrates the sensor. (default = [`mdi:air-purifier`](https://materialdesignicons.com/icon/air-purifier))
- **name** _(string) (optional)_  
  Custom name of sensor. (default = `WAQI`)
- **scan_interval** _(number) (optional)_  
  Number of seconds between polls.

## Contributing :sparkles:

This project follows the [all-contributors](https://allcontributors.org) specification ([emoji key available here](https://allcontributors.org/docs/en/emoji-key)). 
Found a bug, want to suggest an idea or share some improvements? [Contributions of any kind are welcome!](./CONTRIBUTING.md) 😃

[img-contributors]:https://img.shields.io/github/contributors/dmaHome/home-assistant-lightwaqi.svg?style=for-the-badge&logo=github
[img-contribute]:https://img.shields.io/badge/pull_requests-welcome-brightgreen.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48IURPQ1RZUEUgc3ZnIFBVQkxJQyAiLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4iICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTYsM0EzLDMgMCAwLDEgOSw2QzksNy4zMSA4LjE3LDguNDIgNyw4LjgzVjE1LjE3QzguMTcsMTUuNTggOSwxNi42OSA5LDE4QTMsMyAwIDAsMSA2LDIxQTMsMyAwIDAsMSAzLDE4QzMsMTYuNjkgMy44MywxNS41OCA1LDE1LjE3VjguODNDMy44Myw4LjQyIDMsNy4zMSAzLDZBMywzIDAgMCwxIDYsM002LDVBMSwxIDAgMCwwIDUsNkExLDEgMCAwLDAgNiw3QTEsMSAwIDAsMCA3LDZBMSwxIDAgMCwwIDYsNU02LDE3QTEsMSAwIDAsMCA1LDE4QTEsMSAwIDAsMCA2LDE5QTEsMSAwIDAsMCA3LDE4QTEsMSAwIDAsMCA2LDE3TTIxLDE4QTMsMyAwIDAsMSAxOCwyMUEzLDMgMCAwLDEgMTUsMThDMTUsMTYuNjkgMTUuODMsMTUuNTggMTcsMTUuMTdWN0gxNVYxMC4yNUwxMC43NSw2TDE1LDEuNzVWNUgxN0EyLDIgMCAwLDEgMTksN1YxNS4xN0MyMC4xNywxNS41OCAyMSwxNi42OSAyMSwxOE0xOCwxN0ExLDEgMCAwLDAgMTcsMThBMSwxIDAgMCwwIDE4LDE5QTEsMSAwIDAsMCAxOSwxOEExLDEgMCAwLDAgMTgsMTdaIiBmaWxsPSIjZmZmZmZmIiAvPjwvc3ZnPgo=&style=for-the-badge
[img-maintainer]:https://img.shields.io/badge/maintainer-dma_Home-blue.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiICB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+CiAgIDxwYXRoIGZpbGw9IiNmZmZmZmYiIGQ9Ik0xMiwyQTEwLDEwIDAgMCwwIDIsMTJBMTAsMTAgMCAwLDAgMTIsMjJBMTAsMTAgMCAwLDAgMjIsMTJBMTAsMTAgMCAwLDAgMTIsMk0xMSwxNC40MVYxOS45M0M5LjU4LDE5Ljc1IDguMjMsMTkuMTkgNy4xLDE4LjMxTDExLDE0LjQxTTEzLDE0LjQxTDE2LjksMTguMzFDMTUuNzcsMTkuMTkgMTQuNDIsMTkuNzUgMTMsMTkuOTNWMTQuNDFNNCwxMkM0LDcuOTcgNyw0LjU3IDExLDQuMDdWMTEuNTlMNS42OSwxNi45QzQuNTksMTUuNSA0LDEzLjc4IDQsMTJNMTguMzEsMTYuOUwxMywxMS41OVY0LjA3QzE3LDQuNTcgMjAsNy45NyAyMCwxMkMyMCwxMy43OCAxOS40MSwxNS41IDE4LjMxLDE2LjlaIiAvPgo8L3N2Zz4=&style=for-the-badge
[img-issues]:https://img.shields.io/github/issues/dmaHome/home-assistant-lightwaqi.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiICB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCI+CiAgIDxwYXRoIGZpbGw9IiNmZmZmZmYiIGQ9Ik0xMSwxNUgxM1YxN0gxMVYxNU0xMSw3SDEzVjEzSDExVjdNMTIsMkM2LjQ3LDIgMiw2LjUgMiwxMkExMCwxMCAwIDAsMCAxMiwyMkExMCwxMCAwIDAsMCAyMiwxMkExMCwxMCAwIDAsMCAxMiwyTTEyLDIwQTgsOCAwIDAsMSA0LDEyQTgsOCAwIDAsMSAxMiw0QTgsOCAwIDAsMSAyMCwxMkE4LDggMCAwLDEgMTIsMjBaIiAvPgo8L3N2Zz4=&style=for-the-badge&color=orange
[img-release]:https://img.shields.io/github/release-pre/dmaHome/home-assistant-lightwaqi.svg?logo=git&logoColor=white&style=for-the-badge&color=yellow
[img-stars]:https://img.shields.io/github/stars/dmaHome/home-assistant-lightwaqi.svg?label=Stargazers&logo=github&style=for-the-badge&color=ff69b4

[link-contribute]:https://github.com/dmaHome/home-assistant-lightwaqi/blob/master/CONTRIBUTING.md
[link-contributors]:https://github.com/dmaHome/home-assistant-lightwaqi/graphs/contributors
[link-issues]:https://github.com/dmaHome/home-assistant-lightwaqi/issues
[link-maintainer]:https://github.com/dmaHome/
[link-release]:https://github.com/dmaHome/home-assistant-lightwaqi/releases
[link-stars]:https://github.com/dmaHome/home-assistant-lightwaqi/stargazers
