driving = input('請問你有沒有開過車?')
if driving != 'yes' and driving != 'no':
    print('工三小')
    raise SystemExit
age = input('請問你的年齡?')
age = int(age)
if driving == 'yes':
    if age >= 18:
        print('你通過測驗')
    else:
        print('你怎麼會開過車?')	
elif driving == 'no':
    if age >= 18:
        print('去考')
    else:
        print('以後再去考') 
