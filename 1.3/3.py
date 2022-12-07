"""Дано целое положительное число X, необходимо вывести вариант этого числа в римской системе счисления в формате строки. """

years = int(input("Enter year: "))
one = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
dozens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
hundreds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
thousands = ["","M","MM"]
    
thousands_rome = thousands[years // 1000]
hundreds_rome  = hundreds[years//100 % 10]
dozens_rome= dozens[years//10 % 10]
one_rome =  one[years%10]
print(thousands_rome + hundreds_rome + dozens_rome + one_rome)