from Chef import Chef
from ChineseChef import ChineseChef

my_chef = Chef()
my_chef.make_special_dish()
print(my_chef.name)

my_chinese_chef = ChineseChef()
my_chinese_chef.make_special_dish()
my_chinese_chef.make_salad()
print(my_chinese_chef.name)
my_chinese_chef.print_name()
