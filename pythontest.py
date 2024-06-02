import re

str = "welcome to bangalore"


def capitalize_first_and_last_char(s):
    result_str = ""
    for word in s.split(" "):
        word_length = len(word)
        word_r =""
        for x in range(word_length):
            if x == 0 or x == word_length-1:
                txt = word[x].upper()
            else:
                txt = word[x]
            word_r += txt
        result_str+=word_r+" "
    return result_str


print(capitalize_first_and_last_char(str))


# find mirror image of string
# b,d d,b i,i o,o v,v w,w x,x

input_str = "gfg"
output_string = "voib"

def find_mirror_image(s):
    mirror_pair = {"b":"d", "d":"b", "i":"i", "o":"o", "v":"v", "w":"w", "x":"x"}
    result_str = ""
    for x in s:
        if x in mirror_pair:
            result_str += mirror_pair[x]
        else:
            result_str = "Not Possible"
            break
        
    return  result_str

print(find_mirror_image(input_str))




a = [12, 4, "c", 7, "a", "b"]
b = [1, 4, 33, "pooja"]

print(a + b)
c = zip(a, b)
print(c)


def compressed_string(s):
    current_char = s[0]
    count = 0
    result = ""
    for char in s:
        if char == current_char:
            count += 1
        else:
            result = result + current_char + str(count)
            current_char = char
            count = 1
    result = result + current_char + str(count)
    return result


#print(compressed_string("wwwkkgggwwr"))


def listofPunishedstudents(m, x, y, student, std_pun, punishment):
    punished_students = {}
    for entry in punishment:
        pid, description = entry
        if pid not in punished_students:
            punished_students[pid] = set()
        punished_students[pid].add(description)

    repeated_offences = []
    for stud_id, stud_name, _, _ in student:
        if stud_id in punished_students:
            student_offences = punished_students[stud_id]
            if len(student_offences) > 1:
                repeated_offences.append((stud_name, student_offences))

    result = ""
    for student, offences in repeated_offences:
        result += f"{student}-{'#'.join(offences)}#"

    return result[:-1]


# listofPunishedstudents()


def compress_string(s):
    if not s:
        return ""

    compressed_string = ""
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed_string += current_char + str(count)
            current_char = s[i]
            count = 1

    compressed_string += current_char + str(count)

    return compressed_string


print(compress_string("aaabbcaabb"))


def sort_any_list(input_list):
    str_list = []
    num_list = []
    for element in input_list:
        if bool(re.match("[a-zA-Z]", str(element))):
            str_list.append(element)
        else:
            num_list.append(element)
    str_list.sort()
    num_list.sort()
    result = str_list + num_list
    return result


print(sort_any_list(a))


def check_palindrome(input_data):
    return input_data[::-1] == input_data


print(check_palindrome("jhggu"))


def sq_list(input_list):
    result_list = []
    for i in input_list:
        result_list.append(i * i)
    return result_list


# print(sq_list([1,2,3,4]))

num_list = [1, 2, 3, 4]
resuu = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', num_list))
print(resuu)


# str1 = "Bhaskar is very good"
# str2 = "Bhaskar"
# str3 = "Priyanka"
#
# o/p -> "Priyanka is very good"

def replace_word(str1, str2, str3):
    result_str = ""
    for word in str1.split(" "):
        if word == str2:
            word = str3
        result_str += word + " "

    return result_str


print(replace_word("Bhaskar is very good", "Bhaskar", "Priyanka"))

str1 = "{[()]}"
