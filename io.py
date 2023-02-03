# my_file = open('test.txt')

# # print(my_file.read())
# # my_file.seek(0)
# # print(my_file.read())
# # my_file.seek(0)
# # print(my_file.read())
# # my_file.seek(0) #move the cursor back to the start 
# # print(my_file.read()) # you can only read the file once

# # print(my_file.readline())
# print(my_file.readlines()) #no newline at the end of the file

# my_file.close()

try:
    with open('sad.txt', mode="w+") as my_file:
        text = my_file.write(':(')
        print(text) #no need to close here
except FileNotFoundError as err:
    print('file does nott exist')
    raise err
except IOError as err:
    print('file does not exist!!')
    raise err 

