# svn


# git 

# Git global setup
```
git config --global user.name "gccbug"
git config --global user.email "gccbug@163.com"
```
# Create a new repository
```
git clone https://github.com/gccbug/ttt.git
cd ttt
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master
```
# Existing folder
```
cd existing_folder
git init
git remote add origin https://github.com/gccbug/ttt.git
git add .
git commit
git push -u origin master
```
# Existing Git repository
```
cd existing_repo
git remote add origin https://github.com/gccbug//ttt.git
git push -u origin --all
git push -u origin --tags
```

# Git 用户名、邮箱配置
配置全局用户名及邮箱
```
$ git config --global user.name "yourname"
$ git config --global user.email "yourmail@huawei.com"
```
注：请确保该邮箱地址为正确的用户华为邮箱地址，否则会影响代码量统计！！！

yourname：用户名是你的域账号名，如h00131288
youremail：邮箱为你的外部邮箱，如huzhiyong@huawei.com

Tips：必须要设置用户名及邮箱后才能使用Git，Git通过检测用户名和邮箱来跟踪进行commit的用户,在每次提交代码时这些信息将会附加在提交信息当中。

# 检查配置
可以使用如下命令检查配置是否正确：
```
$ git config --list
```
设置完了全局用户名和邮箱即可在本地使用Git了，但要使用CodeClub的远程仓库功能，还要进一步进行「配置SSH Key」。

# git 出现 SSL certificate problem: unable to get local issuer certificate

在Windows下的git窗口里使用命令直接去掉ssl的验证：

```
git config --global http.sslVerify false 
```
