letter = "Hey my name is {0} and i am form {1}"
name = "Shreyas"
country = "INDIA"
print(letter.format(name,country))
print(f"Hey name is {name } and i am form {country}")
print("Hey name is {{name}} and i am form {{country}}")


price = 49.989
txt = "The price is {:.2f} dollars"
print(txt.format(price))