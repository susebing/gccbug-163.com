# linux 远程调研 windows exe

```sh
#!/bin/sh/expect
set timeout -1;
spawn telnet 127.0.0.1
expect "*username:"
send "root\r"
expect "*password:"
send "123456\r"
expect "*name:"
send "china\r"
expect ">"
send "D:/xxx.exe\r"
expect ">"
```
