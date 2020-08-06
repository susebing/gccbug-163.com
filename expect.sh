#!/bin/sh/expect
set timeout -1;
spawn telnet 127.0.0.71
expect "*username:"
send "root\r"
expect "*password:"
send "******\r"
expect "*name:"
send "china\r"
expect ">"
send "xxx.exe\r"
expect ">"
