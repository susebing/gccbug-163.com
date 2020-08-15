# 一 [BOM](https://www.cnblogs.com/findumars/p/3620078.html)

BOM 经常会导致乱码的出现，切无法正常解析，一般情况我们会使用 ignore 忽略不能正常 decode 的字符

```py
def get_decode_data_array(file_path):
    """
        二进制方式读取，获取字节数据，根据系统返回不同格式解码数据
    :param file_path:
    :return:
    """
    file_encode = get_encoding(file_path)
    if not file_encode:
        return None
    deco = 'utf-8'
    if 'utf-8' not in file_encode.lower():
        deco = 'gbk'
    with open(file_path, 'rb') as f:
        lines = f.readlines()
        data_arr = []
        for l in lines:
            data_arr.append(l.decode(deco, "ignore"))
        return data_arr
```

# 二 python 新生成的文件格式由什么决定？

## 1 window操作系统下文件大部分默认编码是ANSI，中文版是GBK编码

如果想要查看或者修改文件编码的话有两种方式

a：用记事本打开文件，另存为可以查看，和修改文件编码

b：另一种就是通过工具喽，notepad++

通过工具打开文件，默认选中的就是当前文件编码类型。
这里你可以修改文件的编码，基本上我会使用encode in UTF-8 without BOM

## 2 linux 系统默认是 ASCII 编码，也有 UTF-8 编码，GBK 在linux上并不友好

Linux上使用 file filename 可以查看文件的编码格式
