```sh
linux-ros:/usr/sbin # whereis nginx
nginx: /usr/sbin/nginx /usr/local/nginx
linux-ros:/usr/sbin # which nginx
/usr/sbin/nginx
linux-ros:/usr/sbin # ps -ef|grep nginx
root      57597      1  0 09:43 ?        00:00:00 nginx: master process ./nginx
root      58780  57597  0 09:54 ?        00:00:00 nginx: worker process
root      58802  57430  0 09:55 pts/3    00:00:00 grep --color=auto nginx
linux-ros:/usr/sbin #

```
