def famous_per(fname, lname, title, clan_tit, stu_tit):
    name = f"The name full name: {stu_tit} {fname} {lname} {title} {clan_tit}"
    return name

text = famous_per(fname='Md', title='bishase', lname='Al Amin', clan_tit='Mondol', stu_tit='Enginner')
print(text)


def kargsExam(fname, lname, **kargs):
    for key, value in kargs.items():
        print(key, value)
    return f"{fname} {lname}"

text2 = kargsExam(fname='Md', lname="Al Amin", title= 'Bishase', stu_tit= 'Enginner')
print(text2)

# return multiple value from in functions 

def ret_all_res(num1, num2):
    add = num1 + num2
    mul = num1 * num2
    div = num1 // num2
    minas = abs(num1 - num2)

    return add, mul, div, minas

all_result = ret_all_res(40, 34)
# print(all_result)

for value in all_result:
    print(value)
