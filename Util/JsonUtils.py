from Util.JsonToJava import JsonToJava
import json
import re


class JsonUtil():
    def __init__(self):
        self.statusArr = []
        self.statusArr.append([0, 0, 0, 0, 0, 3])
        self.statusArr.append([1, 2, 2, 0, 0, 0])
        self.statusArr.append([2, 0, 4, 0, 0, 0])
        self.statusArr.append([3, 1, 4, 0, 0, 0])
        self.statusArr.append([4, 0, 0, 0, 0, 3])
        self.NEW_LINE = "\r\n"
        self.util = JsonToJava()
        self.str = 'null'
        self.title = '@SerializedName("%s")'
        self.other = 'private %s '
        self.chushi = ''

    def format(self, str):
        json = str.replace("\n", "").replace("\r", "").replace("\t", "").replace("\\", "").replace(" ", "")

        prevStatus = 0  # 上一状态
        level = 0  # 缩进层级

        str = ""
        for c in json:
            oper = self.getOperation(prevStatus, c)

            if (oper == 1):
                str = str + self.NEW_LINE + self.getTab(level)
            elif (oper == 2):
                level = level + 1
                str = str + self.NEW_LINE + self.getTab(level)
            elif (oper == 3):
                level = level - 1
                str = str + self.NEW_LINE + self.getTab(level)
            elif (oper == 4):
                str = str + " "
            str = str + c
            prevStatus = self.getStatus(c)
        self.str = str
        return self.util.strToJson(json)

    def getOperation(self, status, c):
        return self.statusArr[status][self.getStatus(c) + 1]

    # 缩进
    def getTab(self, level):
        str = ''
        for i in range(level):
            str = str + "   "
        return str

    # 字符转化成对应的状态
    def getStatus(self, c):
        status = 0
        if (c == '{'):
            status = 1

        elif (c == '['):
            status = 1

        elif (c == ':'):
            status = 2

        elif (c == ','):
            status = 3

        elif (c == '}'):
            status = 4

        elif (c == ']'):
            status = 4

        return status

    def formatAndroid(self, str):
        if (str is None):
            return -1
        else:
            try:
                data = json.loads(str)
                # 定义一个函数，用来处理json，传入json1对象，层深初始为0，对其进行遍历
                self.chushi = ''
                self.hJson(data)
                return self.chushi
            except Exception as e:
                print(e)
                return -1

    def hJson(self, json1, i=0):

        # 判断传入的是否是json对象，不是json对象就返回异常
        if (isinstance(json1, dict)):
            # 遍历json1对象里边的每个元素
            for item in json1:
                # 如果item对应的value还是json对象，就调用这个函数进行递归，并且层深i加1，如果不是，直接z在else处进行打印
                if (isinstance(json1[item], dict)):
                    # 打印item和其对应的value
                    print("444" + "%s : %s" % (item, json1[item]))
                    # 调用函数进行递归，i加1
                    self.fanyi(item, json1[item])
                    self.hJson(json1[item], i=i + 1)

                else:
                    print(type(json1[item]))
                    if (isinstance(json1[item], list)):
                        print("222" + "%s : %s" % (item, json1[item][0]))
                        self.fanyi(item, json1[item])
                        self.hJson(dict(json1[item][0]), i=i + 1)
                    else:
                        self.fanyi(item, json1[item])

        # 程序入口，对adict进行处理，第二个参数可以不传
        else:
            print("json1  is not josn object!")

    def fanyi(self, data, mType):
        try:
            if (isinstance(mType, list)):
                mType = 'List<>'
            elif (isinstance(mType, int)):
                mType = 'int'
            elif (isinstance(mType, str)):
                mType = 'String'
            elif (isinstance(mType, dict)):
                return
            else:
                mType = 'String'
            for old in re.finditer('_', data):
                # 如果开头就是_ 跳过
                if old.span()[0] != 0:
                    num = old.span()[1]

                    s1 = list(data)  # 将字符串转换为列表

                    s1[num] = s1[num].upper()

                    data = ''.join(s1)  # 用空串将列表中的所有字符重新连接为字符串
            # 替换所有的 ‘—’
            data = data.replace('_', '')
            # 首字母小写
            data = data.replace(data[0], data[0].lower())
            self.chushi = self.chushi + self.title % data + "\n" + self.other % mType + data + '\n\n'
        except Exception as e:
            print(e)
