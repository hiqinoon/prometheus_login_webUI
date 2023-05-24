from werkzeug.security import generate_password_hash

def add_user():
    # 输入用户名和密码
    username = input("请输入用户名：")
    password = input("请输入密码：")

    # 将密码转换为哈希值
    hashed_password = generate_password_hash(password)

    # 将用户名和哈希值写入文件
    with open("profiles.json", "r+") as f:
        lines = f.readlines()
        # 检查用户名是否已存在
        for line in lines:
            if f'"{username}"' in line:
                print(f"用户名 '{username}' 已存在")
                break
        else:
            # 如果用户名不存在，则将新的用户名和哈希值添加到文件中
            lines.insert(1, f'\t"{username}": ["{hashed_password}"],\n')
            f.seek(0)
            f.writelines(lines)
            print(f"用户:'{username}' 添加成功\n")

def change_password():
    # 输入用户名和新密码
    username = input("请输入要修改密码的用户名：")
    new_password = input("请输入新密码：")

    # 将新密码转换为哈希值
    new_hashed_password = generate_password_hash(new_password)

    # 在文件中查找指定用户并替换密码
    with open("profiles.json", "r+") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if f'"{username}"' in line:
                lines[i] = f'\t"{username}":["{new_hashed_password}"],\n'
                f.seek(0)
                f.writelines(lines)
                print(f"用户:'{username}' 的密码已修改")
                break
        else:
            print(f"找不到用户 '{username}'\n")
            
# 显示菜单并根据用户选择执行相应操作
while True:
    print("请选择操作：")
    print("1. 新增用户")
    print("2. 修改密码")
    print("0. 退出")
    choice = input("请输入选项：")
    if choice == "1":
        add_user()
    elif choice == "2":
        change_password()
    elif choice == "0":
        break
    else:
        print("无效选项，请重试\n")
