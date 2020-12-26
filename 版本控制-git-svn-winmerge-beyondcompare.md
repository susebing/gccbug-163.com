# svn


# git 

## 1、给项目添加.gitignore

```
.gitignore可以忽略你不想上传的文件，比如doc,target,classes等等
只需要在.git同目录下新增.gitignore文件，然后添加不需要上次的目录即可，比如

/doc/
/target/
/.idea/
/offer.iml
```

## 2、清除已经上传的多余文件

```
如果你添加.gitignore的时候，git里面已经上传了很多不需要的文件，则使用下面两个命令干掉他们
如果是文件夹：git rm -r --cached 文件夹名
如果是文件：git rm --cached 文件名
```

## gitignore生效
```
清除全局缓存，再添加所有文件，让.gitignore生效。这里的所谓的清除全局缓存好像对项目也没有多大影响。

git rm -r --cached .
git add .
git commit -m "update .gitignore "
```

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
$ git config --global user.email "yourmail@163.com"
```

# 检查配置
可以使用如下命令检查配置是否正确：
```
$ git config --list
```
设置完了全局用户名和邮箱即可在本地使用Git了，但要使用远程仓库功能，还要进一步进行「配置SSH Key」。

# git 出现 SSL certificate problem: unable to get local issuer certificate

在Windows下的git窗口里使用命令直接去掉ssl的验证：

```
git config --global http.sslVerify false 
```

### 配置 SSH

```
运行 Git Bash, 在弹出的终端中输入下面提示的代码
cd ~/.ssh
ssh-keygen -t rsa -C "xxx@xxx.com"
clip < ~/.ssh/id_rsa.pub
```


### 配置Git全局用户名和用户邮箱

```
git config --global user.name "your username"
git config --global user.email "your Email"
```


### 在本地克隆仓库并推送新建的README文件

```
git clone ssh://git@xxx.github.com:2222/susebing/test.git
cd test
echo "# test" > README.md
git add README.md
git commit -m "add README"
git push -u origin master
```


### 关联已有代码目录到仓库

```
cd <Your directory path>
mv README.md README-backup.md
git init
git remote add origin ssh://git@xxx.github.com:2222/susebing/test.git
git pull origin master
git add --all
git commit -m "Initial commit"
git push -u origin master
```


### 关联已有代码目录到仓库

```
cd <Your directory path>
git init
git remote add origin ssh://git@xxx.github.com:2222/susebing/test.git
git add --all
git commit -m "Initial commit"
git push -u origin master
```


### 关联已有的Git仓库

```
cd <Your Git repository path>
git remote remove origin > /dev/null 2>&1
git remote add origin ssh://git@xxx.github.com:2222/susebing/test.git
git push -u origin --all -f
git push -u origin --tags -f
```




