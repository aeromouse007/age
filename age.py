driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有':
    print('只能回答有/沒有')
    raise SystemExit

age = input('請問你的年齡?')
age = int(age)
if driving == '有':
    if age >= 18:
        print('你通過測驗')
    else:
        print('你怎麼會開過車?')	
elif driving == '沒有':
    if age >= 18:
        print('快去考駕照')
    else:
        print('乖孩子')   
