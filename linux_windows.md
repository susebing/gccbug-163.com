# linux 远程调用 windows exe

1. windows10: 安装 telnetserver

2. linux: yum install -y expect

3. create test.sh

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
