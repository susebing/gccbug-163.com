# linux 远程调研 windows exe

windows10: 安装 telnetserver

linux: yum install -y expect

create test.sh

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

# 直接执行
sh test.sh

# 后台挂载执行
nohub xxx.sh>2>&1 &