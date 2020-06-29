# rsync命令中的include参数顺序问题

目前我需要使用include参数和exclude参数配合使用把某些类型的文件同步到另一个位置,


后来把include提到exclude前面就可以了
```
rsync --inlude=*.文件后缀 --exclude=*.*   位置1 位置2 -r
```　　
 

如果是多种类型的文件使用多个include
```
rsync --inlude=*.文件后缀1 --inlude=*.文件后缀2 --exclude=*.*   位置1 位置2 -r
```
