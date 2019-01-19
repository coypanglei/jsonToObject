import json


class JsonToJava():

    def strToJson(self, str):
        try:
            list =json.loads(str)
            # for key in list:
            #     print(key + ':' + list[key])
            return 1
        except json.JSONDecodeError as e:
            print(e)
            return 0
