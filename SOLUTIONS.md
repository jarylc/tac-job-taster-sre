# Possible solutions
### 1. Follow the alert reference
### 2. Cronjob to add $100 to balance.txt every minute
[crontab.guru (*/1 * * * *)](https://crontab.guru/#*/1_*_*_*_*)
```shell
$ echo "*/1 * * * * echo $(($(cat /root/balance.txt) + 100)) > /root/balance.txt" | crontab -
```
### 3. Read the codes and realized expense.txt and income.txt is being used and change the values remotely
```shell
$ echo 0 > expense.txt
$ echo 30 > income.txt
```
### 4. Change the code entirely to not even read or change balance.txt
