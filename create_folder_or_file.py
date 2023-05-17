'''
自动创建文件夹或文件 Automatically create folders or files.
'''
import os


def write_file(path, data):
    message = ''
    if '\\' in path:
        filename = path.rsplit('\\', 1)[1]
    elif '/' in path:
        filename = path.rsplit('/', 1)[1]
    else:
        print('write_file(path, data): path wrong. check it out')
    print(filename)
    if os.path.exists(path) and data != '':
        message = f'The file "{filename}" already exists and has been updated.'
        with open(path, 'w') as f:
            f.write(data)
    else:
        with open(path, 'w') as f:
            f.write(data)
        message =f'"{filename}" created successfully!'
    print(message)


class Create:
    def __init__(self):
        pass

    def mkdir(self, folder_name, subfolder_name=None):
        '''Check if the given file name exists.'''
        msg = ''
        # to only make mainfolder
        if not os.path.isdir(folder_name) and subfolder_name is None:
            os.makedirs(folder_name)
            msg = f"{folder_name} created successfully!"

        # to make mainfolder and subfolder
        elif os.path.isdir(folder_name) and subfolder_name is not None:
            # 子目录
            # print(os.path.join(os.getcwd(),folder_name, subfolder_name))
            try:
                os.makedirs(os.path.join(os.getcwd(), folder_name, subfolder_name))
                msg = f"{folder_name}/{subfolder_name} created successfully!"
            except FileExistsError:
                msg = f"{folder_name}/{subfolder_name} already exists."

        elif not os.path.isdir(folder_name) and subfolder_name is not None:
            os.makedirs(folder_name)
            os.makedirs(os.path.join(os.getcwd(), folder_name, subfolder_name))
            msg = f"{folder_name}/{subfolder_name} created successfully!"
        else:
            msg = f"{folder_name} already exists."
        return folder_name, subfolder_name, msg

    def mkfile(self, filename, folder='', content=''):
        # 当前路径+文件名
        # print(os.path.join(os.getcwd(),filename))
        # 当前路径+文件夹+文件名
        # print(os.path.join(os.getcwd(), folder, filename))

        path_without_folder = os.path.join(os.getcwd(), filename)
        path_with_folder = os.path.join(os.getcwd(), folder, filename)
        # print(path_with_folder)

        '''
            | 文件是否存在 | 提供文件夹名称 | 提供数据 |
         c1 |     否     |      没有    |   没有   |
         c2 |     否     |      没有    |     有   |
         c3 |     否     |       有    |    没有   |
         c4 |     否     |       有    |     有   |
         c5 |     是     |      没有    |   没有   |
         c6 |     是     |      没有    |    有   |
         c7 |     是     |       有    |    没有   |
         c8 |     是     |       有    |     有   |
         
        '''
        # Case 1：文件不存在 | 没有提供文件夹名称 | 没有提供数据
        if not os.path.exists(path_without_folder) and folder == '' and content == '':
            write_file(path=path_without_folder, data=content)
            # print('Case 1：文件不存在 | 没有提供文件夹名称 | 没有提供数据')

        # Case 2：文件不存在 | 没有提供文件夹名称 | 有提供数据
        elif not os.path.exists(path_without_folder) and folder == '' and content != '':
            write_file(path=path_without_folder, data=content)
            # print('Case 2：文件不存在 | 没有提供文件夹名称 | 有提供数据')


        # Case 3：文件不存在 | 有提供文件夹名称 | 没有提供数据
        elif not os.path.exists(path_with_folder) and folder != '' and content == '':
            # 反复尝试打开文件夹
            while True:
                try:
                    write_file(path=path_with_folder, data=content)
                    break
                except FileExistsError and FileNotFoundError:
                    # 创建文件夹
                    self.mkdir(folder_name=folder)
            # print(f"{folder}/{filename} created successfully!")
            # print('Case 3：文件不存在 | 有提供文件夹名称 | 没有提供数据')

        # Case 4：文件不存在 | 有提供文件夹名称 | 有提供数据
        elif not os.path.exists(path_with_folder) and folder != '' and content !='':
            # 反复尝试打开文件夹
            while True:
                try:
                    write_file(path=path_with_folder, data=content)
                    break
                except FileExistsError and FileNotFoundError:
                    # 创建文件夹
                    self.mkdir(folder_name=folder)
            # print('Case 4：文件不存在 | 有提供文件夹名称 | 有提供数据')

        # Case 5：文件存在 | 没有提供文件夹名称 | 没有提供数据
        elif os.path.exists(path_with_folder) and folder == '' and content == '':
            write_file(path_without_folder, data=content)
            # print('Case 5：文件存在 | 没有提供文件夹名称 | 没有提供数据')

        # Case 6：文件存在 | 没有提供文件夹名称 | 有提供数据
        elif os.path.exists(path_with_folder) and folder == '' and content != '':
            write_file(path=path_with_folder, data=content)
            # print('Case 6：文件存在 | 没有提供文件夹名称 | 有提供数据')

        # Case 7：文件存在 | 有提供文件夹名称 | 没有提供数据
        elif os.path.exists(path_with_folder) and folder != '' and content == '':
            write_file(path_with_folder,data=content)
            # print('Case 7：文件存在 | 有提供文件夹名称 | 没有提供数据')

        # Case 8: 文件存在 | 有提供文件夹名称 | 有提供数据
        elif os.path.exists(path_with_folder) and folder != '' and content != '':
            write_file(path_with_folder,data=content)
            # print('Case 8: 文件存在 | 有提供文件夹名称 | 有提供数据')
        else:
            pass

# 创建文件夹/子文件夹
# Create().mkdir(folder_name='download',subfolder_name='video')
tem_data = 'this is own module!!!'

# 创建文件
# Create().mkfile(filename='text.txt', content=tem_data)