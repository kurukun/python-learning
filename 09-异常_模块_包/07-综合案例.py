from my_utlis.str_util import str_reverse
from my_utlis.str_util import substr
import my_utlis.file_util


my_str = "hello world"
print(str_reverse(my_str))
my_str = substr(my_str, 0, 5)
print(my_str)
my_utlis.file_util.print_file_info('D://abc.txt')
my_utlis.file_util.append_to_file('D://abc.txt', 'haha')