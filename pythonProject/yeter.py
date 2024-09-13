# Получаем числа от пользователя
salary = float(input("Введите зарплату за месяц : "))
credit_payment = float(input("Введите сумма платежа по кредит : "))
utilities_debt = float(input("Введите задолженность за коммуналку : "))

# Вычисляем остаток
remaining_money = salary - credit_payment - utilities_debt

# Выводим результат на экран
print("Остаток :", remaining_money)