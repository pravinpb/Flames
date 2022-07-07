#To Get name input and validate the input
def name_or_not():
    name = input("Name :").lower()
    NameAlph = False
    while NameAlph == False:
        if name.isalpha():
            NameAlph = True
        else:
            print("PLease enter only Alphabets")
            name = input("Name Again:").lower()
    return name

#Input of name
name1 = [i for i in name_or_not()]
name2 = [i for i in name_or_not()]

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