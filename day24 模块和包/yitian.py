# 片头曲


main_person_man = "张无忌"
main_person_woman = "赵敏"

bad_person_one = "陈昆"
bad_person_two = "灭绝师太"

def fight_on_light__top():
    print(f"{main_person_man}粉碎了{bad_person_one}的阴谋")

def fight_on_shaolin():
    print(f"{main_person_man}粉碎了{bad_person_two}的阴谋")

def end():
    print(f"{main_person_man}和{main_person_woman}在一起了")

# print(__name__) # 如果作为子模块被其他导入，则显示模块名
                # 如果作为启动模块，则显示main

# 你要运行该文件时，才会执行的代码
if __name__ == "__main__":
    print("这里是片头曲")
    fight_on_light__top()
    fight_on_shaolin()
    end()
    print("这里是片尾曲")