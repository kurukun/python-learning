"""
字符串相关工具
"""


def str_reverse(s):
    """
    反转字符串
    :param s: 待反转的字符串
    :return: 结果
    """
    return s[::-1]


if __name__ == '__main__':
    print(str_reverse('hello'))  # 测试功能用


def substr(s, x, y):
    """
    按照下标x和y对字符串进行切片
    :param s:字符串
    :param x:开始位置
    :param y:结束位置（不包含）
    :return:结果
    """
    return s[x:y]
