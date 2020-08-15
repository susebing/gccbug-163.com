# [BOM](https://www.cnblogs.com/findumars/p/3620078.html)

# python 新生成的文件格式由什么决定？

## window操作系统下文件大部分默认编码是ANSI，中文版是GBK编码

如果想要查看或者修改文件编码的话有两种方式

一：用记事本打开文件，另存为可以查看，和修改文件编码

二：另一种就是通过工具喽，notepad++

通过工具打开文件，默认选中的就是当前文件编码类型。
这里你可以修改文件的编码，基本上我会使用encode in UTF-8 without BOM

## linux 系统默认是 ASCII 编码，也有 UTF-8 编码，GBK 在linux上并不友好

Linux上使用 file filename 可以查看文件的编码格式
