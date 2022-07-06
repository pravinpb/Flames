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

while len(flames)>1:
    calcu = final_count % len(flames)
    remove_count = calcu -1
    #print(remove_count)
    if remove_count >= 0:
        right_list = flames[remove_count + 1:]
        left_list = flames[:remove_count]
        flames = left_list + right_list
        #print(flames)
    else:
        flames = flames[:len(flames)-1]
        #print(flames)

out_dict = {
    'F' : 'Friends',
    'L' : 'Love',
    'A' : 'Affection',
    'M' : 'Marriage',
    'E' : 'Enemy',
    'S' : 'Sister'
}
print(out_dict[flames[0]])