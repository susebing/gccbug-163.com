# encoding: utf-8
# @Author: zhengbing
# @Date: 2020/3/25
# @Desc: 文件操作


import chardet


# 获取文件编码类型
def get_encoding(file_path):
    """
        二进制方式读取，获取字节数据，检测类型
    :param file_path:
    :return:
    """
    with open(file_path, 'rb') as f:
        data = f.read()
        if len(data)>0:
            return chardet.detect(data)['encoding']

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

def get_first_line_number_by_kwords(file_path, kwords):
    """
        返回第一次遇到关键字的行号
    :param file_path:
    :param kwords:
    :return:
    """
    txts = get_decode_data_array(file_path)
    for i,txt in enumerate(txts):
        for kw in kwords:
            if kw in txt:
                return i

def get_first_line_number_by_kword(keyword, file_path):
    """
        读取文件指定行内容
    :param keyword: 关键字
    :param file_path: 文件路径
    :return: 文件最后一次出现的行号，从 1 开始计数
    """
    with open(file_path) as f:
        for l, v in enumerate(f):
            if keyword in v:
                return l

def get_last_line_number_by_kword(keyword, file_path):
    """
        读取文件指定行内容
    :param keyword: 关键字
    :param file_path: 文件路径
    :return: 文件最后一次出现的行号，从 1 开始计数
    """
    last_line = 0
    with open(file_path) as f:
        for l, v in enumerate(f):
            if keyword in v:
                last_line = l
    return last_line

def get_line_numbers(keyword, file_path):
    """
        读取文件指定行内容
    :param keyword: 关键字
    :param file_path: 文件路径
    :return: 返回所有包含关键字的行号
    """
    line_numbers = []
    with open(file_path) as f:
        for l, v in enumerate(f):
            if keyword.lower() in v.lower():
                line_numbers.append(l)
    return line_numbers

def read_txts(file_path):
    return get_decode_data_array(file_path)

def read_line_numbers_by_kword():
    pass

def read_txts_by_kword():
    pass

def write_line():
    pass

def write_line_append(file_path, txt):
    with open(file_path, 'a') as f:
        f.write(txt)
        f.write('\n')

def write_lines(file_path, txts):
    with open(file_path, 'w') as f:
        for txt in txts:
            txt = txt.replace('\r\n','\n')
            f.write(str(txt))

def write_lines_append(file_path, txts):
    with open(file_path, 'a') as f:
        for txt in txts:
            f.write(txt)
            f.write('\n')

def write_line_before_first_kword(keyword, txt, file_path):
    line_number = get_first_line_number_by_kword(keyword, file_path)
    line_content = get_decode_data_array(file_path)
    if line_number:
        line_content.insert(line_number - 1, txt)
        with open(file_path, 'w') as f:
            for line_txt in line_content:
                f.write('{}\n'.format(line_txt))

def write_line_after_first_kword(keyword, txt, file_path):
    """
        在指定文本后面插入数据
    :param keyword:
    :param txt:
    :param file_path:
    :return:
    """
    line_number = get_first_line_number_by_kword(keyword, file_path)
    line_content = get_decode_data_array(file_path)
    if not line_number is None:
        line_content.insert(line_number + 1, txt)
        with open(file_path, 'w') as f:
            for line_txt in line_content:
                f.write('{}\n'.format(line_txt))


def write_line_after_last_kword(keyword, txt, file_path):
        """
            在指定文本后面插入数据
        :param keyword:
        :param txt:
        :param file_path:
        :return:
        """
        last_line_number = get_last_line_number_by_kword(keyword, file_path)
        line_content = get_decode_data_array(file_path)
        if last_line_number:
            line_content.insert(last_line_number + 1, txt)

            with open(file_path, 'w') as f:
                for line_txt in line_content:
                    f.write('{}\n'.format(line_txt))

def write_lines_after_kword():
    pass



