# # import os

# # if os.path.exists('lines.txt'):

# #     print('Файл існує')

# # else:

# #     print('Файл не існує')



# # import json
# # user={
# #     "name": 'John' , 
# #     'age': 30,
# #     'skills':['Python','Js','React']
# # }
# # with open('user.json','w',encoding='utf-8') as file:
# #     json.dump(user,file,ensure_ascii = False,indent=4)
# # with open('user.json','r', encoding = 'utf-8') as file:
# #     data=json.load(file)
# # #print(data)

# # print(name)

# students=[

#     {'name':'Alice', 'age':22, 'courses':['Math','Physics']},

#     {'name':'Bob', 'age':24, 'courses':['Biology','Chemistry']},

#     {'name':'Charlie', 'age':23, 'courses':['History','Literature']}

# ]
with open('notes.txt','w', encoding='utf-8') as file:

    json.dump(notes,file, ensure_ascii=False, indent=4)

    print('Hellow world!')
    print('Hellow world!')
    print('Hellow world!')