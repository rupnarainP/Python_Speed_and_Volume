import json
import re
import dirtyjson
import time

global json_string

class Speed_test:

    def read_File(self):
        json_string = ''
        with open('../Inputs/input.txt') as file:
            for lines in file.readlines():
                json_string += lines

        return json_string

    def translate_JSONArray(self, jsonString):
        passthrough = False
        s = ''
        lines = jsonString.split('\n')

        for j in range(len(lines)):
            elements = lines[j].split(":")

            for i in range(len(elements)):
                'Skips lines that have brackets'
                if not elements[0] in "[" and not elements[0] in "]" and not elements[0] in "{" and not elements[0] in "}" and not elements[0] in "'\t},'":

                    'Find that initial country name line and replace it with a bracket'
                    if elements[0] in "\"" or elements[1] in ' {':
                       lines[j] = "{"

                    else:
                        if (elements[0] in "\t\tfvc" or elements[0] in "\t\tmvc") and not passthrough:
                            elements[1] = elements[1].replace(".", "0.")

                            # print(elements[1])
                            passthrough = True

                        elif elements[0] in "\t\tfsc" or elements[0] in "\t\tfj" or elements[0] in "\t\tmsc" or elements[0] in "\t\tfu" or elements[0] in "\t\tfl":
                            lines[j] = ""

                        else:
                            first = "\t\t" + '"' + elements[0][elements[0].index("\t") + 2 : len(elements[0])] + '"'
                            lines[j] = first + ": " + elements[1]
                        'find the volume arrays and convert the volumes to a JSON format'

            passthrough = False

        for line in lines:
            s += line

        return s

    def convert_String_To_Json(self, json1):
        print('Convert to JSON')

        json_Object = json.loads(json1)

        # to_file = json.dumps(json_Object, indent=4)

        with open('Inputs/input.txt', 'w') as file:
            file.writelines(json1)

        return json_Object

    def translate_JSONArray2(self, jsonString):
        print('Transforming data', end=' ')
        t1 = time.perf_counter()

        new = list(jsonString)

        for letter in range(len(new)):
            if new[letter] == '{':
                new[letter] = '{\n'

            if letter > 0:
                if new[letter] == ',' and new[letter - 1] == '}':
                    new[letter - 1] = '\n}'
                    new[letter] = ',\n'
            # print(words[count])

        new[len(new) - 1] = '\n}'
        words = ''.join(new)
        # print(words)

        temp = []
        json_s = ''
        temp.append('[')

        for line in words.splitlines():
            if line.__contains__(',') and not line.__contains__('}'):
                # temp.append('{\n' + re.sub(r"(\w+):", r'"\1":', line) + '\n},\n')
                json_s = dirtyjson.loads('{\n' + re.sub(r"(\w+):", r'"\1":', line) + '\n},\n')

                e = '{\n'
                li = ''

                for dj in json_s:
                    if dj == 'fj':
                        continue

                    elif dj == 'n':
                        e += '\t"{}"'.format(dj) + ': ' + '"{}"'.format(str(json_s[dj])) + ',\n'

                    elif dj == 'ml':
                        e += '\t"{}"'.format(dj) + ': ' + str(json_s[dj]) + '\n'

                    else:
                        if str(json_s[dj]).__contains__("'"):
                            li = str(json_s[dj]).replace("'", '"')
                            e += '\t"{}"'.format(dj) + ': ' + li + ',\n'

                        else:
                            e += '\t"{}"'.format(dj) + ': ' + str(json_s[dj]) + ',\n'

                e += '},\n'
                temp.append(e)
                e = ''

        d = temp[len(temp) - 1]
        temp[len(temp) - 1] = d[0:len(d) - 2]
        temp.append(']')

        temp = ''.join(temp)

        t2 = time.perf_counter()
        print('Time taken to transform data: {:.2f}'.format(t2 - t1))

        return temp

    @staticmethod
    def remote_data_to_json(remote):
        jq = json.dumps(remote, indent=4)

        with open('Inputs/remote_input.txt', 'w') as file:
            file.writelines(jq)

        answer = json.loads(jq)

        return answer
