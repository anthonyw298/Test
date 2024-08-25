# HW1

#Office hours
#Comments are good? Do I need to comment the input and output?Do i need to comment the function and what its doing?

def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #
    out_list=[]
    while num != 1:         
        out_list.append(num)        
        if num%2==1:            #if num odd, num becomes 3 times old num plus 1
            num=(3*num+1)//1
        else:                   # if num even,divide by 2
            num=num//2
    out_list.append(num)     #adds 1 on to the output list
    return out_list

#
def to_decimal(oct_num):
    """
        >>> to_decimal(237) 
        159
        >>> to_decimal(35) 
        29
        >>> to_decimal(600) 
        384
        >>> to_decimal(420) 
        272
    """
    digit=0             #number repesented in the decimal system
    num=0                 
    while (oct_num)>0:
        num+=(oct_num%10)*(8**digit)    #converts the last digit on oct_num from octal to decimal and adds it to num value
        oct_num//=10                    #next digit
        digit+=1                        
    return num


#
def has_hoagie(num):            
    """
        >>> has_hoagie(737) 
        True
        >>> has_hoagie(35) 
        False
        >>> has_hoagie(-6060) 
        True
        >>> has_hoagie(-111) 
        True
        >>> has_hoagie(6945) 
        False
    """
    if num<0:                       #changes number to positive
        num=-num
    else:
        pass
    num2=num//10                    #new number for even place values
    while num>0 and num//100>0:     # iterates through odd place values to find a sandwich
        if num%10==(num//100)%10:
            return True
        else: 
            num=num//100
    while num2>0 and num2//100>0:           #iterates through even place values to find a sandwich
        if num2%10==(num2//100)%10:
            return True
        else:
            num2=num2//100
    return False

#
def is_identical(num_1, num_2):
    """
        >>> is_identical(51111315, 51315)
        True
        >>> is_identical(7006600, 7706000)
        True
        >>> is_identical(135, 765) 
        False
        >>> is_identical(2023, 20) 
        False
    """
    place_value=1
    new_num_1=0
    new_num_2=0
    while num_1>0:                      #removes the sequence of repeated digit of num_1
        if num_1%10!=(num_1//10)%10:                #takes the lowest digit,compares it with the second lowest digit
            new_num_1+=(num_1%10)*(place_value)      #adds to new_num_1 if its not equal or goes to the next place value
            num_1//=10                              
            place_value*=10 
        else:
            num_1//=10
    place_value=1
    while num_2>0:                      #removes the sequence of repeated digit of num_2
        if num_2%10!=(num_2//10)%10:
            new_num_2+=(num_2%10)*(place_value)
            num_2//=10
            place_value*=10
        else:
            num_2//=10
    if new_num_1==new_num_2:            #compares the two new values
        return True
    else:
        return False
    
#
def frequency(txt):
    '''
        >>> frequency('mama')
        {'m': 2, 'a': 2}
        >>> answer = frequency('We ARE Penn State!!!')
        >>> answer
        {'w': 1, 'e': 4, 'a': 2, 'r': 1, 'p': 1, 'n': 2, 's': 1, 't': 2}
        >>> frequency('One who IS being Trained')
        {'o': 2, 'n': 3, 'e': 3, 'w': 1, 'h': 1, 'i': 3, 's': 1, 'b': 1, 'g': 1, 't': 1, 'r': 1, 'a': 1, 'd': 1}
    '''
    d={}
    new_txt=''
    for i in txt:           #stores string of all lowercase letters and eliminates non-alphabetical into new_txt
        if i.isalpha()==True:
            new_txt+=i.lower()

    for i in new_txt:       #iterates through new_txt,stores each letter in dictionary or adds 1 to key
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d


def invert(d):              
    """
        >>> invert({'one':1, 'two':2,  'three':3, 'four':4})
        {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        >>> invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3})
        {3: 'three'}
        >>> invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'}) 
        {'Sara': '123-456-78', 'sara': '258715'}
    """
    lst=[]
    lst2=[]
    invert_d = {}
    for key in d:
        if d[key] not in invert_d:          #iterates through d and adds the inverted key,value pair into invert_d if it isnt yet
            val = d[key]
            invert_d[val] = key 
        else:
            lst.append(d[key])           #if key is in invert_d, it adds the duplicates into a list
    for i in lst:
        if i not in lst2:      #puts all the numbers without any of its duplicates into a new list
            lst2.append(i)
    for i in lst2:                  #runs through the list to eliminate any of that value from the invert_d
        del invert_d[i]
    return invert_d




def employee_update(d, bonus, year):        
    """
        >>> records = {2020:{"John":["Managing Director","Full-time",65000],"Sally":["HR Director","Full-time",60000],"Max":["Sales Associate","Part-time",20000]}, 2021:{"John":["Managing Director","Full-time",70000],"Sally":["HR Director","Full-time",65000],"Max":["Sales Associate","Part-time",25000]}}
        >>> employee_update(records,7500,2022)
        {2020: {'John': ['Managing Director', 'Full-time', 65000], 'Sally': ['HR Director', 'Full-time', 60000], 'Max': ['Sales Associate', 'Part-time', 20000]}, 2021: {'John': ['Managing Director', 'Full-time', 70000], 'Sally': ['HR Director', 'Full-time', 65000], 'Max': ['Sales Associate', 'Part-time', 25000]}, 2022: {'John': ['Managing Director', 'Full-time', 77500], 'Sally': ['HR Director', 'Full-time', 72500], 'Max': ['Sales Associate', 'Part-time', 32500]}}
    """
  
    new_d={}
    for keys in d:
        if keys==(year-1):          #iterates the year in the dictionary which is 1 less than the year we are implementing
            employee_lst=d[keys]       #takes value and sets it to a variable(employee_lst)
    for keys in employee_lst:
        new_d[keys]=employee_lst[keys].copy()     #the values in employee_lst which are lists are iterated,copied,and added into new_d
        new_d[keys][2]+=bonus                       # their salary is added and saved into new_d
    d[year]=new_d                           #new_d key,value pair is added into d
    return d
        

def overloaded_add(d, key, value):
    """
        Adds the key value pair to the dictionary. If the key is already in the dictionary, the value is made a list and the new value is appended to it.
        >>> d = {"Alice": "Engineer"}
        >>> overloaded_add(d, "Bob", "Manager")
        >>> overloaded_add(d, "Alice", "Sales")
        >>> d == {"Alice": ["Engineer", "Sales"], "Bob": "Manager"}
        True
    """
    if key in d: 
        if isinstance(d[key],list):         #checks to see if the value already contains a list
            d[key]+=[value]                 # if so it adds the value into the list
        else:
            d[key]=[d[key],value]              #if not, it adds it to the key and multiple values in dictionary as a list
    else:
        d[key]=value                        #adds input into the value of dictionary
    

            


def by_department(d):
    """
        >>> employees = {
        ...    1: {'name': 'John Doe', 'position': 'Manager', 'department': 'Sales'},
        ...    2: {'position': 'Budget Advisor', 'name': 'Sara Miller', 'department': 'Finance'},
        ...    3: {'name': 'Jane Smith', 'position': 'Engineer', 'department': 'Engineering'},
        ...    4: {'name': 'Bob Johnson', 'department': 'Finance', 'position': 'Analyst'},
        ...    5: {'position': 'Senior Developer', 'department': 'Engineering', 'name': 'Clark Wayne'}
        ...    }

        >>> by_department(employees)
        {'Sales': [{'emp_id': 1, 'name': 'John Doe', 'position': 'Manager'}], 'Finance': [{'emp_id': 2, 'name': 'Sara Miller', 'position': 'Budget Advisor'}, {'emp_id': 4, 'name': 'Bob Johnson', 'position': 'Analyst'}], 'Engineering': [{'emp_id': 3, 'name': 'Jane Smith', 'position': 'Engineer'}, {'emp_id': 5, 'name': 'Clark Wayne', 'position': 'Senior Developer'}]}
    """
    new_d={}
    for key in d:
        departments=d[key]['department']                            #creates variable for name,position, and department
        name=d[key]['name']
        position=d[key]['position']
        format={'emp_id':key,'name':name, 'position':position}          #creates a new format
        if departments not in new_d:                                #changes the key of new_d to departments and check to see if it is unique
            new_d[departments]=[format]                 #if its unique, it adds the format
        else:
            new_d[departments].append(format)           #if not, it appends it to the list of information of that key
    return new_d

def successors(file_name):
    """
        >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
        >>> returnedDict = successors('items.txt')
        >>> expected == returnedDict
        True
        >>> returnedDict['.']
        ['We', 'Maybe']
        >>> returnedDict['to']
        ['learn', 'have', 'make']
        >>> returnedDict['fun']
        ['.']
        >>> returnedDict[',']
        ['eat']
    """
    lst=[]
    fptr=open(file_name,'r')      #opens file, splits and stores each value except spacies and punction into lst and closes file   
    line=fptr.read()
    lst+=line.split()
    fptr.close()
    var=''
    empty = ['.'] 
    d={}
    for i in lst:               #iterates through the list and appends it to empty if the element is completely alphanumeric
        if i.isalnum():
            empty.append(i)
        else:                   #if it is not, it iterates through each character of the nonalphanumeric element 
            for d in i:
                if d.isalnum() == False:   #once reaches a character that is nonalphanumeric, previous letters that were added to var is added to empty as an element
                    empty.append(var)      #along with the nonalphanumeric character itself is added back to empty as an element and var is set back to none
                    empty.append(d)
                    var=''
                else:                   #iterating through alphanumeric characters, each letter gets added to var
                    var+=d  
            empty.append(var)           #end of the loop, the final var is added to empty and var is set back to none
            var=''


    for i in empty:                 #iterates empty and removes excess elements that contain nothing
        if i=='':
            empty.remove(i)
  

    
    for i in range(len(empty) - 1):     #creates a dictionary with its first key (period) setting it equal to the first string
        if i==0:
            d={empty[i]:[empty[i+1]]}
        elif empty[i] not in d:            #iterates through empty and sets each key to the elements with its value being unique successor to key 
            d[empty[i]] = [empty[i + 1]]
        elif empty[i] in d:                             #if it is not unique, it adds it into the list of values in that key
            if empty[i+1] not in d[empty[i]]:
                d[empty[i]]+=[empty[i+1]]
    return d




def addToTrie(trie, word):
    """
        The following dictionary represents the trie of the words "A", "I", "Apple":
            {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}}}
       
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> addToTrie(trie_dict, 'art')
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}}
        >>> addToTrie(trie_dict, 'moon') 
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}, 'm': {'o': {'o': {'n': {'word': True}}}}}
    """
    new_d=trie
    for char in word:
        if char not in new_d:           #if the character is not in new_d, a new key value pair is added into new_d at the end to represent that character
            new_d[char]={}
        new_d=new_d[char]               #new_d is shortened to the dictionary of that value
    new_d['word']=True                  #at the end of all the characters, it creates the last value of word true.



def createDictionaryTrie(file_name):
    """        
        >>> trie = createDictionaryTrie("words.txt")
        >>> trie == {'b': {'a': {'l': {'l': {'word': True}}, 't': {'s': {'word': True}}}, 'i': {'r': {'d': {'word': True}},\
                     'n': {'word': True}}, 'o': {'y': {'word': True}}}, 't': {'o': {'y': {'s': {'word': True}}},\
                     'r': {'e': {'a': {'t': {'word': True}}, 'e': {'word': True}}}}}
        True
    """
    lst=[]
    lower=[]
    var=''
    trie={}
    fptr=open(file_name,'r')        #opens the file and stores all the word into a list
    line=fptr.read()
    lower+=line.split()
    fptr.close()


    for i in lower:             #converts all the elements of the list in lowercase
        for d in i:
            d=d.lower()  
            var+=d
        lst.append(var)
        var=''

    for i in lst:               #calls addToTrie to store it into dictionary making a trie representation
        addToTrie(trie,i)
    return trie
def wordExists(trie, word):
    """
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> wordExists(trie_dict, 'armor')
        False
        >>> wordExists(trie_dict, 'apple')
        True
        >>> wordExists(trie_dict, 'apples')
        False
        >>> wordExists(trie_dict, 'a')
        True
        >>> wordExists(trie_dict, 'as')
        False
        >>> wordExists(trie_dict, 'tt')
        False
    """
    new_d=trie
    for i in range(len(word)):      #runs through each character and and if its in the key, new_d is shortened to the dictionary of the value and it goes to the next character and repeats
        if word[i] in new_d:
          new_d=new_d[word[i]]
    if new_d == {'word': True}:         #in the end, if there is only one dictionary left which is the end, then it would mean the whole word was in the trie
        return True
    else:
        return False                    










def run_tests():
    import doctest
    # Run start tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run start tests per function - Uncomment the next line to run doctest by function. Replace rectangle with the name of the function you want to test
    doctest.run_docstring_examples(wordExists, globals(), name='HW1',verbose=True)   
    #successors('items.txt')
if __name__ == "__main__":
    run_tests()