#To Get name input and validate the input

# Changes made:
# Instead of using a seperate variable to for checking the validity of the name, 
# you can just use the while loop more efficiently
def name_or_not():
    name = input("Name :").lower()
    while not name.isalpha():
        print("Please enter only alphabets")
        name = input("Name Again:").lower()
    return name

#Input of name

# Changes made:
# Instead of using a list comprehension, you can make use of the list() function
name1 = list(name_or_not())
name2 = list(name_or_not())

#removing the repeated leaters in the names.
remov = []
for letter in name1:
    if letter in name2:
        name2.remove(letter)
        remov.append(letter)
    else:
        pass
for i in remov:
    name1.remove(i)

#Count od unique leters
final_count = len(name1+name2)

flames = 'F L A M E S'.split()

#Logic for Striking out the letters
while len(flames)>1:
    calcu = final_count % len(flames)
    remove_count = calcu -1
    #Spliting the list into two and joining it in a reverse oder
    if remove_count >= 0:
        right_list = flames[remove_count + 1:]
        left_list = flames[:remove_count]
        flames = right_list + left_list
    else:
        flames = flames[:len(flames)-1]

#Dictionary to display the output
out_dict = {
    'F' : 'Friends',
    'L' : 'Love',
    'A' : 'Affection',
    'M' : 'Marriage',
    'E' : 'Enemy',
    'S' : 'Sister'
}
print(out_dict[flames[0]])
