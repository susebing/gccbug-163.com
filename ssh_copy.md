
## Linux ssh copy

从远程linux 服务器拷贝大文件往往速度很慢, 需要ssh 登录远程服务器压缩需要拷贝的文件之后再拷贝，速度会大大提升。


### 可以先再服务器设置 ssh 免密登录

```

```

### 执行远程压缩

```
ssh root@10.123.111.110;
cd "/opt/test";
tar -zcf aaa.tar.gz --exclude=*.exe --exclude=ftp* --exclude=out* *;
exit;
```

### 本机执行 scp 拷贝

```
scp root@10.123.111.110:/opt/test/aaa.tar.gz /opt/testdata/;
cd /opt/testdata;
mkdir aaa;
tar -zxf aaa.tar.gz -C aaa;
rm -rf aaa.tar.gz;
```
