#Nathan broadbent
#9/17
# Allergy checker program

input_test= input("enter things eaten in the last 24 hours ").lower()
if  "milk" in input_test or "cheese" in input_test:
    dairy_check= True
else:
    dairy_check= False
print("is dairy in the list above", dairy_check)
print("are nuts in the list above","nuts" in input_test)
print("is seafood in the list above","seafood" in input_test)
print("is Chocolate in the list above","chocolate" in input_test)
