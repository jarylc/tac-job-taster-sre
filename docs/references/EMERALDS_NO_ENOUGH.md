# EMERALDS_NO_ENOUGH

## Description

This usually means you are broke af according to the system.

Maybe a creeper blew your chest filled with emeralds up.

![Creeper Meme](assets/creeper-meme.jpg)

## Remediation steps

#### 1. Remotely access the system
```shell
$ docker exec -it $(docker ps | grep taster | cut -d' ' -f1) /bin/ash
```
#### 2. Add 45 emeralds to balance.txt
```shell
$ cd /root
$ echo $(($(cat balance.txt) + 45)) > balance.txt
```
