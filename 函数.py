def info_print():
    print("请选择功能--------------")
    print("1.txt、添加学员")
    print("2、删除学员")
    print("3、修改学员")
    print("4、查询学员")
    print("5、显示所有学员")
    print("6、退出系统")
    print("-"*20)
info = []
def add_info():
    """添加学员系统"""
    new_id = input("请输入学员的学号：")
    new_name = input("请输入学员的姓名：")
    new_tel = input("请输入学员的手机号：")
    global info
    for i in info:
        if new_name == i["name"]:
            print("已添加此学员")
            return
    info_dict = {}
    info_dict["id"] = new_id
    info_dict["name"] = new_name
    info_dict["tel"] = new_tel
    info.append(info_dict)
    print(info)
def del_info():
    """删除学员系统"""
    del_id = input("请输入学员的学号：")
    del_name = input("请输入学员的姓名：")
    del_tel = input("请输入学员的手机号：")
    global info
    for i in info:
        if del_name == i["name"]:
            info.remove(i)
            break
    else:
            print("该学员不存在")
    print(info)
def modify_info():
    """修改学员系统"""
    modify_name = input("请输入学员的姓名：")
    global info
    for i in info:
        if modify_name == i["name"]:
            i["tel"] = input("请输入修改的手机号：")
            break
    else:
        print("该学员不存在")
    print(info)
def search_info():
    """查询学员系统"""
    search_info = input("请输入学员的姓名：")
    global info
    for i in info:
        if search_info == i["name"]:
            print(i)
            break
    else:
        print("该学员不存在")
def print_all():
    """显示所有学员信息"""
    print("学号\t姓名\t手机号")
    for i in info:
        print(f"{i["id"]}\t{i["name"]}\t{i["tel"]}")
while True:
    info_print()
    user_num = int(input("请输入功能序号："))
    if user_num == 1:
        # print("请输入添加学员的信息:")
        add_info()
    elif user_num == 2:
        # print("请输入删除学员的信息:")
        del_info()
    elif user_num == 3:
        # print("请输入修改学员的信息:")
        modify_info()
    elif user_num == 4:
        # print("请输入查询学员的信息:")
        search_info()
    elif user_num == 5:
        # print("显示所有学员的信息")
        print_all()
    elif user_num == 6:
        # print("退出系统")
        exit_flag = input("确定要退出吗？yes or no")
        if exit_flag == "yes":
            break
    else:
        print("输入有误")