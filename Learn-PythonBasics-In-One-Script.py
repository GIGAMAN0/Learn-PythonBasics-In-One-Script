
# Hi !!!! Every One This Is Eslam Abbas Network Security Engineer & Malware Analysit , Hope To Be Good !!  
# This Educational Script Is To Understand Python Basics ( Without OOP ) With Examples
# The Concept From The Script Is To Read The Syntax OF The Code , Then See The Explanition In The Comments And Finally Run The The Script To See The Output Of The Commends
# In This Script , There Are Many Main Topics I Will Explain To You And You WILL Find The Script Divided Into Many Parts ..
# Every Part Will Run Separately ...
# You Will Study Every Part Separately And Run The Script To See The Output Of The Commends 
# IN THE FUTURE , There Will Be Alot OF Updates In This Script To Development It And Explain More Topics In Python Like ( OOP , Some Libs , Erorr Handling , Regulaer Expressions And Alot Of Things More ..!)
# I Happy For Any Feedback , So Feel Free IN YOUR OPINOIN ..!!
# For Any Ques Or Any Feedback ...
# 
#
#
# And This MY Youtupe Channel .. (  )
# You Will Find In IT The Explaination For This Script In Video  On It ..! 
# Happy Learning !!! 




# This Is All Kinds Of Date In Python

print ("#" * 50 )

print(type(12))        # Int 
print(type("Eslam"))   # String
print(type(5+6j))      # Cmpination Number
print(type(12.34))     # Float
print(type([12,13,14,15,16]))   # List
print(type((12,13,14,15,16)))   # Table
print(type({"one": 1, "Two": 2}))  # Dictionary
print(type(True))

print ("#" * 50 )

# This Is All Shapes Of Variaples Name




Part1=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part1 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part1=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")



# 45Apas=Eslam      >>> Valid Because Its Starts With Nums Or Spesial Characters

apas="Eslam19"      # >>> Not Valid Because It Not Starts With Nums ,It Contains Nums

Apas="Eslam18"      # >>> Variable Name Is Case Sentisive And Can Start With Capital Character

testname="Eslam17"  # >>> This Name is camelcase name type

test_name="Eslam16"  # >>> This Name Is Snack_Case Name Type

test="Eslam15"      # >>> This Name Is Normam Name Type

print(help("keywords"))   # >>> This Output Is A Words Which You Can't Name Variable With


print ("#" * 50 )



Part2=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part2 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part2=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")


# Variable Input




a,b,c = 1,2,3         # >>> a=1  ,  b=2    c=2
a=4                   # Variablw a Has Now A Tow Values , Because Of Python ,This Variable Will Take The Sceond Value Only



print ("#" * 50 )



#Escape Characters




print ("Eslamm\bApas")       # " \b "   delete the perevious cahracter of it


print ("Eslamm\nApas")       # " \n" New Line To The Next Word Of It


print ("Eslam\
Apas")                      # " \" Delete The New line Of The Next Word Of It


print ("Eslam\\Apas")       # "\\" The Back Slach Escape What Is Next To It ,So Will Escpe The Other ' \'


print ("Eslam\tApas")       # " \t" Input A 'TAP Button' Between The Text


print ("Eslam \"Apas\"")     # " \" " Escape The Next Character

print ("Eslam\rApas")        # " \r"  Replace The Next Value Of It To The Perevious  Value To It ,Whrh The Same Nums Of Data Or Character


print ("Eslam\x4FApas")      # " \xhh " Type The Hex Value Of The Character Do You Want To Type ,Then Will Type The Character Not Hex Value



print ("#" * 50 )


Part3=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part3 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part3=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")


#Concatination


print (Apas + apas )     # You Can Add Or Concatinate Two String Data Or Two Variables With  "+"

# print ( Apas + 13 )    # You Can Only Concatinate String With String Or Variable With Valriable


print ("#" * 50 )

Part4=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part4 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part4=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")


#String Methods


print ("Eslam 'ApaS'")         # You Can Do EscaPe To '  With This Way

print ('Eslam "Apas"')         # you Can Do Escape To " With This Way

print ( """Eslam
Apas""")                      # You Can Print More Than Word And Each Of Then In New Line With  """   """

print ( '''Eslam
Apas''')                      # You Can Print More Than Word And Each Of Them In A Line  With  '''  '''




#IMPORTANT
#Python Deal With Date With Number Of Intex To Data Because It Is A Zero Index Language
#You Can Slice And Deal With Part Of Data in The Next Way





test="Eslam Apas"
test1="####### Eslam Apas #######"
test2="eslam 5a apas"
test3="1"
test4="ESLAM APAS"
test5="Eslam@Apas@Hmad"
test6="Eslam Apas Apas Hmad"
test7="""Eslam
Apas
Apas
Hmad"""
test8="eslam apas"

print (test[6:10])   # In This Example  You Will Print The Index 6 To Index 10 , But index 10 (The End ) isn't Included In The Printed Text  , The Index 6 Don't refear To  'p' because We Start Count index With zero not one


print (test[2::2])  # The Syntax Of Slicing Data in Python Is Like  [ Start Index Value : End Index Value : Steps ] , If Didn't Identify The Start Or End Or Steps ,Then Will Use Default Values >>> [ Start Of String : End Of String : 1 ]


print (test[-1])    # You Can Print Data From The Ebd Of String By Add A - To Index Number


print (len(test))  # Print The Lenth Of String Data And The Space Is A Normal Character In Counting

print (test1.strip("#"))  # strip() method used for delete any thing between the () from the string

print (test1.rstrip("#"))   # rstrip() method used for delet some thing from string from the right exactly

print (test1.lstrip("#"))   #lstrip() method used for delete some thing from string but from left side only

print (test2.title())       # title() method used for to make first character in each word capital and the character which locate after a nmuber

print (test2.capitalize())   # capitalize() method for make each character in the start of each word be capital

print (test3.zfill(3))       # zfill  method used for make the number with the battern which you add in zfil()

print (test.upper())        # upper() method used for make all character of the string capital

print (test4.lower())        # lower() method used for make all character of the string small

print (test.split())       # split() method used for reforn the string to list and the elements is defined with the separetor which you put im split()

print (test5.split("@", 1))   # with split() method you can define any character not only space , And you can define the max number of the output elemnts with 'maxsplit'

print (test5.rsplit("@", 1))    # split() method by def starts its jop from the left of the string ,but you can start from right with rsplit()

print (test.center( 12, "&"))   # center() method used for add any character to the string in left and right of string ,but center() need the total number of charcters in the output

print (test6.count("Apas"))    # count() method used for count any word which you define in the string

print (test6.count("Apas" , 5,10))   #  with count() method you can put the start index number and the end index number to make count the method count between them

print (test4.swapcase())            # swapcase() method used for reverse the state of the all characters in the string  ( if thay are capital , then will be small ) (if thay are small ,then will be cpital)

print (test.startswith("E"))        # startwith() method used for print the true or false output ,and this depend of the character whitch the string start with

print (test.endswith("s"))         # endwith() method is like startwith() method but it form the end of the string  , but both of them are case sentesive characters

print (test.index("m", 0,10))        # index() method used for search for the index number of the spasific value which you input , but you must inpot the range of index numbers to search between them (vlaue which you want to now its index number , the start index number ,the end index number )

print (test.find("a" , 0,10))       # find() method do the same jop of index() ,but the differance between them that ,index() print error if your value isn't in the string ,but find() method in this case print "-1"

print (test.rjust(12 , "*" ))          # rjust() method do like center() method but in the spasific location (right or left)

print (test7.splitlines())           # splitlines() method do the same jop of split() but in string with more than line

print (len(test.expandtabs()))       # epandtabs() method add a taps like the escape chracter "\t"

print (test.istitle())               # istitle() method prints true and false and do its jop from its name

print (test4.isupper())               # isupper() method prints also true or false value and do its jop from its name

print (test8.islower())             # islower() method prints true and false like the previous methods

print (test.isidentifier())       # isidentifier() method prints true or false and like the rest of methods

print (test.isalpha())           # isalpha() method prints true or false and that if the string ordered or not  a-z

print (test2.isalnum())         # isalnum() method prints true or false if the string ordered like a_z , 0-9

print (test5.replace("@" , " " , 3))    # replace() method used for replace a oldvalue of string with the newvalue with the maxmum of the replacements ( replace (oldvalue,newvalue,the number of the replacements)


# String Method Is Done, You Can Read And Search About More String Methods In Pythn ....



print ("#" * 50)

Part5=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part5 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part5=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")


# String Formatting


name="Eslam Mohamed Apas"
age=19
country="Egypt"
School="Mansoura University"
comment="Stay High Witj Your Humility"
myrank=40.12
mymoney=123444667
name1,name2,name3="Eslam" , "Mohamed" , "Apas"

# Concatination In Python Can Only Concatinate Betwwen Two Strings And Can't Concatinate INT With STR
# There Are Some Ways To Do This Jop Called String Formatting , Read The Messages And The Code To UderStand 


print ( "My Name Is %s And My Age Is %d"  %(name,age))  # In This Code We Write The STR With INT With The OldWay Of String Formatting

print ( "My Name Is {:s} And My Age Is {:d}" .format(name,age))  # In This Code We Write The STR With The INT With The NewWay Of String Formatting

print (f"My Name Is {name} And My Age Is {age}")    # This Way Apply Only In Python3.6


# You Now See When I Want To Write A String with The String Formatting Write .., " %s , {:s} "  , And INT   " %d ,{:d} " And Floating Number  " %f ,{:f} "
# You Now Can Print A Str With Any Type Of Data
# You Can Do Some Jops With The String Formatting, Read The Code And The Explain To UderStand ..


print ("My Name Is %.5s And My Age Is %d ,This Script Done By %.3f " % ( name , age ,myrank))  # In This Code I Nake A String Sliceing With The String Formatting By "%.' the number of character to print '  

print ("My Name Is {:.5s} And My Age Is {:d} ,This Script Done By {:.3f}" .format(name,age,myrank))  # In This Code I Do The Same The Previous Jop But Whit The NewWay Of String Formatting

print ("My Money Now Is {:_d} And Will Be More In The Feture" .format(mymoney))   # In This Code I Devide The Number Of Money In Groups Each Group Has A 3 Numbers Only And Put The "_"To Be Between Eash Group ..

print ("My Name Is {:s} {:s} {:s} " .format(name2,name3,name1))   # Stay Foucs On The This Example And The Next One 

print ("My Name Is {1:s} {2:s} {0:s} " .format(name1,name2,name3))    # In This Code And The Previoues One I Rearanage The String With The Number Of The Index Of Date And Do This Jop With 2 Ways


# String Formatting Is Done ...
# You Can Read More About The String Formatting In The Next WebSite ...WWW.PYFORMAT.INFO...


print ("#" * 50 )

Part6=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part6 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$ \n")
 Part6=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")


# Numbers ( INT, Complex ) In Python

num1=122
num2=122+4j

print (type(num1))
print (type(num2))  # Numbers In Python Is Two Kinds INT,COMPLEX

print (num2.real)
print (num2.imag)  # You Can Print A real Or Imagine Part Of The Complex Number With This Way

# You Can Form The INT Data To Float Or Complex
# You Can Form The Float Data To INT Or Complex
# You Can't Form The Complex To Float Or INT

print (complex(122))
print (float(122))        # Form The INT To Complex And Float Data

print (complex(122.3))
print (int(122.3))       # Form The Float Number To INt And Complex

# This Is The Kinds Of The Numbers In Python ..

# Arithmetic Operators On Numbers

print (122+122)      # Addition

print (122-110)      # SubTraction

print (122*12)      # multipcation

print (121/11)      # Division

print (11**11)      # exponent

print (120%11)      # Modules

print (122//11)     # Floor Division


# Numbers Is Done ..



print ("#" * 50 )


Part7=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part7 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part7=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")




# Lists In Python ..



# Lists In Python Is Mutable ,You Can edit Its Data And Remove And Add Data to It
# Lists In Python Is like Array In The rest Languages


List1=[1,2,3,4,5,"Eslam" ,"Apas"]          # lists in Python Typed Between [] And Contain Any Type Of Data


print (List1[3])              # You can Print Or do Any Thind In a Element In The List
print (List1[0:3])             # You Can Slice The Data With Type The Start And The End Index Of Data
List1[6] = []                  # You can Replace An Item From The List By This Way ,And You Can Remove An Item If You Don't Write Any Thing In The []
List1[0:2] = ["one" ,"two","three"]   # Will edit The First Three Elemnts In The List And Replce Them With The Value Which You Add




print ("#" * 50 )

Part8=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part8 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part8=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")



# Lists Methods In Python

List2 = [6,7,8,9,10,"Apas" , "Hmad" ]
List3 = [ 1,2,10,12,17,-1,100]
List4 = [ 1,1,1,5,6,7,8]
List5= ["Eslam", "Mohamed", "Apas"]
List6 = ["Eslam", "Apas", "Apas", "Hmad"]

print (List1.append(11))            # Append() Method Used For Add An Element To The List ' Any Type Of Date '

print (List1.append(List2))         # You Can Use A List To Be Added With Append() But The Added List Will Be A One Elemnt In The List1

print (List1.extend(List2))       # Extend() Method do The Prev Jop But The Differance Between It And Append() Is The List2 Will Be More Than One Element In The List1

print (List1.remove("Eslam"))    # Remove() Method Used To Remove An Item From The List ,But If Thia Item Is Repeated More Than One Element ,Remove() Method Will Remove The First Item Of Repeated Items only

print (List3.sort())             # Sort() Method Is to Sort The Elements  In The Order ,Sort() Method Often used With Numbers To Order Them ,And By Def It Order Them Ascending ,And Sort Only Used For Strings Only Or Ints Only And Can't Mix  thme In One List

print (List3.sort(reverse=True))   # N This Case Sort() Will Order The Numbers Descending

print (List3.sort(reverse=False))    # In Thia Case Sort() Will Order The Numbers Ascending

print (List3.reverse())           # Reverse() Method Only Make The First Element The The Last, And The Last Element Be The First , And Can Work With Mixed List Between Str And Int

print (List6.clear())            # Clear() Method Used For Clear All Items From The List

print (List4.count(1))          # Count() Method Used To Count A Spacific Value In The List

print (List5.index("Eslam"))      # Index() Method Used To Show The Index Number Of The Input Value , If There Are Two Values In The Same List ,The Index Will Work With The First Value Only

print (List2.insert(5,"Eslam"))     # Insert() Method Do The Smae Jop Of Append() But Append() Add The Element In The End Of The List ,But Insert() You Input The index Which Insert() Will Add The Value To The Previous Index You Inputed

print (List5.pop(2))                   # Pop() Method Require A Index Number To Show You The Element Which refear To This Index



# Some Of Prev Codea Print The "None" Value Because There Is No Thing To Print ,In This Part Foucs On The Code And The Explanition Only Not on The Output



# Nasted Lists ...

List7= [1,2,3,4,5,[6,7,8,9]]     # Nasted List Is A List Has A list Inside It

print (List7[5][2])              # To Print Or Do Any Thing In The Inside List You Can Do This Way , First [] Is to Set The index of the inside list ,The Second [] To Set The Element From The Inside List


print ("#" * 50 )

Part9=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part9 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part9=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")




# Tuples In Python ..




# Tuples Is Like The Lists but The Tuple typed between () not []

# Typles Is a Immutable data ,You Cna't Edit any Data inside The Tuple

# You Can Repeat The Element In The Tuple ,And You Can Use Any Type Of data In It

# You Can reash To Any Element In The Tuple By Its index Number

# If You Had A Tuple With 1 Element Inside It ,The Type Here Will Be "str" Not "Tuple" , To Make It "Tuple" You Must Type ',' After The Element ..

# You Can Do Concatination Like Strings by "+" in The Tuples

# You can Repeat The Tuple Like String By Typing "*"



print ("#" * 50 )


# Tuples Methods...



tuple1= (1,2,3)
tuple2= ("Eslam", "Mohamed", "Apas", "Apas", "Hmad")



print (tuple2.count("Apas"))     # Count() Method Count The Element Which You Input

print (tuple1.index(3))        # Index() Method Print To You The Index Number Of The Value

example1, example2, example3, example4, example5 = tuple2    # You can Make A Tuple Destruct by Distribute Its elements To Variables

print (example1 + example2 + example3 + example4 + example5)

# tuple1 = example6, example7         # If The number Of Variables Doesn't Equal The Elements of The Tuple ,It Will Make An Error

example6, _, example7 = tuple1       # By Adding A "_" To An Element To Discard It ,The Error Will Solve ..

print (example6 + example7)




print ("#" * 50 )

Part10=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part10 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part10=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")



# Sets In Python ...




# Sets Is Like Tuple Or Lists But Typed Between {}

# Sets Elements In Every Output is With An Order differ From The Prev One

# Because That You Can't Reach To Any element With Its Index Number

# You Can't Do Sliceing To The Set

# Seta Is Immutable Like Tuple

# Sets Approve Only The Immutable Data In It Like ( String,Numbers,Tuples) And Don't Approve (Dicts,Lists)

# Sets' elements Is uniqe And Can't Repeat Any Of Them And If We Typed A repeated Elemwnts ,When We Run The code, The Repeated Elwmwnts Will Br Deleted



print ("#" * 50 )



# Sets Methods ...


set1 = {1,2,3,4,5,6}
set2 = {"Eslam", "Mohamed", "Apas", "Apas", "Hmad"}
set3 = {1,2,3,2,1}
set4 = {100,10,20,30,40,50}
set5 = {10,60,70,80,90,100}
set6 = {11,22,33,44,55}
set7 = {11,22,77,88,99}

set3.clear()        # Clear() Method Used To Clear The Set From Its Elements

print (set1.union(set2))    # Union() Method Used To Add A Set To Another One , And You Can Do This Jop Like This Code " set1|set2 "

print (set1.add(7))      # Add() Method Used To Add A Only One Element To The Set

print (set1.remove(1))   # Remove() Method Used To Remove A Element From The Set, But If You Input A Element Doesn't In The Set Then Remove() Method Will Print To You An Error

print (set1.discard(2))   # Discard() Method Do The Same Jop Of Remove() But Without Error

print (set2.pop())        # Pop() Method Print To You A Random Element From The Set

print (set3.update(set4))  # Update() Method Do The Same Jop Of Union() But You Can With Update() Add A List To Set

print (set5.update([1,2,3,4]))    # Updating With List

print (set4.difference(set5))    # Differance() Method Used to Show You The Differance Between The Two Sets ,By Printing The Elements In The First Set Don't Exist In The Second Se

print (set4.difference_update(set2))   # Difference_update() Method used To Add The Different Elemnsts To The Main Set "Set4 In This Example"

print (set4-set5)        # By This Code You Can Do The Same Jop Of Difference() Method

print (set4.intersection(set5))  # Intersection() Method Print The Mutual Elements Between The Two Sets

print (set4&set5)        # Do The Same Jop Of Intersection() Method

print (set4.intersection_update(set5))   # The Mothod Of Intersection_update() Update The Main Set With The Mutual Elements Between The Two Sets

print (set6.symmetric_difference(set7))   #Symmtric_Difference() Method Print The All UnMutual Elements Between The Two Sets

print (set6^set7)              # Another Code To Do The Same Prev Jop

print (set6.issuperset(set3))    # IsSuperSet() Prints Thats True If The First Method Exists Completely In The Second Set And Prints False If Not

# Hint ..This Is The Shape Of The Code In The Sets Method  (" The Main set .MethodName(The Second Set ))

print (set3.issubset(set5))    # IsSubSet() Tell You If The Elemensts Of The Second Set Exist Completely In The First Set Or Not

print (set2.isdisjoint(set7))  # IsDisJoint() Tell You If The Elements Of The Tow Sets Completly Different Or Not ( There Isn't Any Mutual Element Between The Two Sets)




print ("#" * 50 )

Part11=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part11 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part11=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")



# Dict In Python ...



# Dict Data Is A Type Of Data in Ptyhon Typed Between {} Like This Shape {1:one, 2:Two} >>> {key:value, key:value}
# Key In The Dict Must Be Immutable Like String Or Int Or Tuple
# Value Can Be Any Type Of Data
# Key Must Be Uniqe In The Dict , And If There Are Two Keys Then The Second Key Will Be The Only Key And Will Discard The First One
# In Dict You Can't Reach To Any Element By The Index Number ,But You Can Do That By The Key

dict1 = {1:"one", 2:"two", 3:"three"}

print (dict1[1])
print (dict1.get(2))         # By Those Two Examples ,You can Reash To Any Element In The Dict By Its Key Name 

# You Can Print All Dict Kays Or Print All Dict Values

print (dict1.keys())
print (dict1.values())        # Printing Keys And Values By Those Codes

#"Nasted Dict" = "Two DimenSional Dictionary" >>> Like Nasted List ,You Can Write A Dic Inside The Dic

dict2 = {1:{"PentrationTesting":"80%", "BugHunting":"50%"}, 2:"Two"}

print (dict2[1]["BugHunting"])       # You Must Follow This Syntax ... "print (Maim DictName[The Key Of The Indide Dict ][ The Key Of The Wanted Value From The Inside Dict]
print (len(dict2))        # Printing The Lenth Of The Dict , The Key:Value Is A One Element Inside The Dict

dict3 = {1:dict1, 2:dict2}
print (dict3)            # You Can Make A Dict From The Variables which Its Values Are Dicts, By Make The Variable In The Value Place

print ("#" * 50 )



# Dict Method



dict4 = {4:"four", 5:"Five", 6:"Six"}
dict5 = {8:"Eight"}
dict6 = {9:"Nine", 10:"Ten"}
dict7 = {11:"eleven", 12:"twelve"}


dict5.clear()       # Clear() Method Used For Clear All Elements From The Dict

copy1 = dict4.copy()
print (copy1)          # Copy() Take A shallow Copy From The Dict To A Variable

dict4.update({"Python":"50%"})
dict4["Html"] = "40%"       # Update() Method Can Add From It An Element To The Dict , And This Is The Second Way To Do The Jop
print (dict4)

print (dict6.keys())       # Keys() Method To Print All Keys Of Dict
print (dict6.values())     # Values() Method To Print All Values From The Dict

print (dict6.setdefault(9, "Nine"))   # SetDefault() Method Used For That You Add A Key And Value Then It go To Dict And Search For The Key You Added And Print Its Value From Dic ,And If Doesn't Find The Ky Then It Will Add The Key With The Value You Added
print (dict6.setdefault(50, "fivety"))  # The Key Isn't Found In The Dic ,Then SetDefault() Will Add (50:"Fivety") to The Dic

print (dict6.popitem())           # PopItem() Method Can Print To You The Last Item Which Been Added To Dict By User

print (dict6.items())       # Items() Method Used For Change The Format Of Data To The Dict ,To Make It A Big List Contain A Small Tuples ( Keys And Valaus )

Tuple10 = (1,2,3,4)
Tuple11 = ("one", "two", "three", "four")
print (dict7.fromkeys(Tuple10,Tuple11))   # FromKeys() Method Can Make A Dict From Two Tuples One Of Them Will Be The Keys And The Other Will Be The Values



print ("#" * 50 )

Part12=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part12 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part12=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")



# Booleans In Python ...



# Boolean Is The Logic And Its Values Are True And False
# There Is A Built In Fun In Python Do The Same Jop "bool()"
print (bool(1))
print (bool(3))
print (bool("Eslam"))       # Print True If The Added Value Is 1 Or UnEmpty Data
print (bool([]))
print (bool({}))            # Print False If The Added Value Is 0 Or Empty Data
print (bool(0))

# Boolean Operators ..

# (And)

name1= "Eslam"
age1= 19

print (name1 == "Eslam")
print (age > 20)
print (age > 10 and name1 == "Eslam")
print (age > 20 and name1 == "Eslam")     # And Operator Is Used To Check All Codes In The Statment ,If Its Boolean Value Is True Then Print True ,If One Value From Boolean Values Is False Then Print False


# (Or)

name2= "Mohamed"
age2= 45

print (name2 == "Mohamed")
print (age2 == 44)
print (name2 == "Mohamed" or age > 30)
print (name2 == "Mohamed" or age > 50)
print (name2 == "Eslam" or age > 90)             # Or Operator Is Used To Check All Codes , If All Booleans Values Are True Then Print True , If All Boolean Values Are False Then Print False ,If One Boolean Value Is False And There Is A True Value In the Same Statment ,The Print True


# (Not)

name3= "Apas"
age3= 70

print (not name3 =="Apas")
print (not age > 90)                        # Not Operator Is Used To Reverse The Statment , If The Value Is True Then Print False ,And If The Valaue Id False Then Print True



print ("#" * 50 )


Part13=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part13 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part13=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")




# Assignments Operators In Python ....


# Assign Operator Is The Character Which Assign A Value To A Variable
# The Assign Operator In Python Is " = "

Var1 = 40
Var2 = 50
Var4 = 60


Var3 = Var1 + Var2           # This Example Explain The Assign Operator , The Next Examples Will Do Some Operation On The Assignment Character

Var4 = Var4 + Var1           # This Case The Var4 + Var1 = The Var4 Again And The Final Value Will Be Assigens To The Var4

Var4 += Var2                 # " += " By This Operator You Can Do The Prev Jop By It
print (Var4)

Var4 -= Var2                 # " -= " By This Operator You Can Do This" Var4 = Var4-Vae2 "
print (Var4)

Var4 *= Var2                 # " *= " By This Operator You Can Do This " Var4 = Var4*Var2 "
print (Var4)

Var4 %= Var2                 # " %= " By This Operator You Can Do This " Var4 = Var4%Var2 "
print (Var4)

Var4 /= Var2                 # " /= " By This Operator You Can Do This " Var4 = Var4/Var2 "
print (Var4)

Var4 //= Var2                # " //= " By This Operator You Can Do This " Var4 = Var4//Var2 "
print (Var4)

Var4 **= Var2                # " **= " By This Operator You Can Do Thia " Var4 = Var4**Var2 "
print (Var4)


print ("#" * 50 )

Part14=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part14 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part14=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")



# Comparison Operators In Python ...

# ( == )     >>> Equal
# ( != )     >>> Not Equal
# ( < )      >>> Less Than
# ( > )      >>> Greater Than
# ( >= )     >>> Greater Than Or Equal
# ( <= )     >>> Less Than Or Equal


Var5 = 50
Var6 = 44

print (Var5 == Var6)

print (Var5 != Var6)

print (Var5 < Var6)

print (Var5 > Var6)

print (Var5 <= Var6)

print (Var5 >= Var6)




print ("#" * 50 )

Part15=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part15 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part15=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")




# Type Conversion In Python ....


# In Pyhton You Can Convert The Data To Another Type By This Part
# Every Built In Fun Will Help You To Convert Your Data
# You Can't Convert The Int Or Complex Data To Another Type
# When You Want To Convert The Dict To Another Data The Keys Only Will Be Converted Not Values
# When You Convert The Set To Another Data Type , The Elementa Won't Be In The Order
# The String Can't Be Converted To The Dict Type
# When You Wan't To Convert Any Data Type To Dict , The Data Must Be Nasted To Be Able To Convert To Dict
# Set Can't Be Converted To Dict


Test11 = ("Eslam", "Apas")
Test12 = 12
Test13 = {"Eslam", "Apas"}
Test14 = ["Eslam", "Aaps"]
Test15 = {"Eslam":1, "Apas":2}
Test16 = "Eslam Apas"
Test17 = (("Eslam",1), ("Apas",2))



print (type(str(Test11)))     # Str() Convert The Data To The String Type


print (type(tuple(Test14)))    # Tuple() Convert Data To The Tupke Type


print (type(list(Test13)))     # List() Convert The Data To The List Type


print (type(set(Test11)))      # Set() Convert The Data To The Set Type


print (type(dict(Test17)))     # Dict() Convert The Nasted Data To The Dict Type




print ("#" * 50 )

Part16=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part16 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part16=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")





# UssrInput In Python ..


# By This Method In Python You Make The user Input Data to The Script ..
# You Can Make A Variable With The Value Which User Input ,And You Can use The Methods With Input Fun Normaly
# You Can Make More Than One Method In The One Line Or Variable And This Way Called Chane Methods
# The OutPut Data Type Is String From Input Fun , If You Want To Convert It , Use The Last Lesson Of Type Convert


nametest1 = input ( "What Is Your Name Please ..!? ").title()  # By This Syntax You Will Write Your Name And Save It In the Variable " nametest1 "
print (f"Welcome {nametest1}..!")


# There Ara Alot Of Projects Online To Practice On This Part , I Will Make One For Example And You Must Do One To Be Good In This Part



# Slicing Email Account ...
# In This Small Project You Want Slice The Input Account To The Name And The Domain Name And Let The User Now Voth Of Them



emailtest1 = input (" Please Type Your Email ...! ").title().strip()
emailname1 = emailtest1[:emailtest1.index("@")]
emaildomain1 = emailtest1[emailtest1.index("@")+1:]

print (f"Welcome {emailname1}...!  \n Your Account Is {emailtest1} \n Your Name Is {emailname1} \n Your Domain Name Is {emaildomain1}")


print ("#" * 50 )

Part17=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part17 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part17=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")





# Control Flow In Python ... ( If ,Else ,Elif )





# ( If ,Elif, Else ) Are The Part Of Taking Orders In The Script

nametest2 = input("Please Type Your Name..").title().strip()
country = input("Please Type Your Country .. ").title().strip()
agetest1 = int(input("Please Type Your Age.. "))

if nametest2 == "Eslam Apas":
 print (f"Welcome Admin {nametest2}")
else :
 print (f"Hello {nametest2} You Aren't Admin" )



# ( You Can Use The Logical Operators With If Condition "And , Or , Not ")


if agetest1 == 19 and country == "Egypt" :
 print (f"{nametest1} Will Use All Advantages Of This Script..!")
else :
 print (f" {nametest1} Won't Use All Advantages Of This Script..!")


# You Can Make Nested If ..
if nametest1 == "Eslam Apas" :
 if agetest1 == 19 and country == "Egypt":
   print ("Welcome Eslam Apas , We Script Will Wait You To Edit It ")
 else:
   print (" You Aren't The Dev , You Only Had Name Like Him..!")
else:
 print (f"Welcome {nametest1} , You Are A Normal User In The Script")


# You Can Type A Short If Condithon ( Ternary If ) Like This ..

if  agetest1 == 19: print ( " Your Age Is 19, Good You Will Have Some Good Advantages in This Script ")
else: print (f" Your Age Is {agetest1}, You Won't Have All Advantages in This Script")

# Another Shape For Ternary If

print ("Your Age Is 19, Good You Will Have Some Good Advantages in This Script") if agetest1 == 19 else print ("f Your Age Is {agetest1}, You Won't Have All Advantages in This Script")


# MemberShip Operators In Python ..( In - Not In )

tupleTest1 = ( "Egypt", "KSA" , "USA" "UK" )
if country in tupleTest1:
 print (" Your Country Has Discount 90% Dor This Script")
else:
 print (" Your Country Don't Have Any Discount Offer " )



print ("#" * 50 )

Part18=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part18 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part18=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")



# Loop ( While) In Python ...



# The Loop Is The Repeating Thing To Make It Easy
# There Are Alot Of Kinds Of Loop Like ( While - For )
# While Loop Apply When The Condition Is True Only
# While Syntax Like ...
#  While + Condition True: else: Condition False



numtest1 = 10

while numtest1 <= 20:      # While Condition Is True The Loop Will Be Done , When It Be False Will Do The Else Condition
 print (numtest1)
 numtest1 += 1
else:
 print ( "The Loop Is Done....!" )


# Loop ( For ) In Python ...



# The For Loop Isn't Like While Loop , Done Without Condition
# For Syntax Must Have An Iterable Data To Take The Value From It
# For Syntax Like ...( " For ' Any_Variable_name' in 'iterable_name' : Block Of Code To Be Done On Every Element In The Iterable Object.." )
# When You Make For Loop With Dicts , The Block Of Code Of For Loop Apply Only On Kwys


tupletest20 = ( 10,20,30,40,50,60)

for num_in_tuple1 in tupletest20:
 print  (num_in_tuple1 + 10)



print ("#" * 50 )

Part19=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part19 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part19=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")


# I Will Explain Some Examples For This Part And You Must Practise In This Part Well ..


print ("#" * 50 )

# While Loop Examples ..
# 1- First Example In The Explaination Is Simple Loop Prints What In A List

MyNewList = [ "Eslam", "Mohamed", "Apas", "Apas", "Apas", "Hmad" ]
numtest10 = 0

while numtest10 < len(MyNewList):       # I Make A Variable And I Will Add In IT 1 In Every Time The Loop Apply In And While Condition Is TrueThe Code Will Apply
 print (MyNewList[numtest10])       # I Use Len(MyNewList) To Make Sure The Loop Will Off When The Number Of The Variable Is lower Than The Num Of Elements 
 numtest10 += 1
else:
 print (" The Loop Is DONE ")


print ("#" * 50 )

# 2- Second Example In The Explanition Is Simple BookMark Manger

BookMark = []
MaxBookMark = 3

while MaxBookMark > 0:
 bookmark = input ( "Please Input Your Web Site ..! ").strip().title()
 BookMark.append(bookmark)
 BookMark.sort()
 print (f" The BookMark Which Add Is {bookmark}")
 print (f"Your BookMark Now Is {BookMark}")
 MaxBookMark -= 1

else:
 print (f"You Can't Add Any Book Mark To Your List .. , Your Bookmark Is {BookMark}")


print ("#" * 50 )


# 3- Third Example In The Explanition is Simple Passwod Guess


MyPass = " EslamApas"
Tries = 3
TheInputedPass = input (" Please Type Your Pass ..")

while TheInputedPass != "EslamApas":
 Tries -= 1
 print (f"Wrong Pass ,{'Last' if Tries == 0 else Tries} Chanse Left ..!")
 TheInputedPass = input (" Please Type Your Pass ..")
 if Tries == 0:
  break
else:
 print (" True Pass Typed ")
print ( "Loop Is DONE")



print ("#" * 50 )

Part20=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part20 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part20=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")


# For Loop Examples ..

# 1- First Example Is A Simple Loop On The Dict With Printing Its Keys And Values

MyLang = { "Php":"50%", "Html":"50%", "Python":"80%", "MySql":"40%"}

for lang in MyLang:
 print (f"Your Lang Is {lang} And Your Progress In It Is {MyLang[lang]}...!")



print ("#" * 50 )



# 2- Second Example Is A Second Way To Apply The Prev Example

print (" This Is Another Way For The Prev Example ..!*")
for lang_Key,lang_Value in MyLang.items():     # By This Method You Print Nasted List With A Multi Tuples In it And The Two Variables Will Take Divide This Data ,One Take Keys And One Take The Values
 print (f" Your Lang Is {lang_Key} And Your Progress In It Is {lang_Value}..!")


print ("#" * 50 )

# 3- Third Example Is Advanced Example In For Loop On Nested Dict (Nested For Loop)

peoples = {"Eslam":{"Html":"40%","Php":"20%"},"Apas":{"Css":"10%", "MySql":"30%"}, "Mohamed":{"Js":"25%", "Python":"80%"}}

for people in peoples:
 print (f" Hello {people} , Your Skills Is : ")
 for skill in peoples[people]:
  print (f"{skill} >>> {peoples[people][skill]}")



print ("#" * 50 )

Part21=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part21 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part21=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")



# Break , Continue , Pass


# (Break)
# Stop The Loop On The Custom Value

TestTuple1 = ( 1,2,3,4,5,6,7,8,9,10 )

for num in TestTuple1:
 print (num)
 if num == 6:
  break
print (" You Breaked The Loop..")

# (Pass)
# Ignori Any Thing And Continue Normaly

for num1 in TestTuple1:
 print (f"The {num1} Is In {TestTuple1} ...")
 if num1 == "Eslam":
  pass
print ( " You Ignored The Error ..")

# (Continue)
# Do An Expction Of An Element From The Iterable Object

for num2 in TestTuple1:
 if num2 == 3:
  continue
 print (num2)

print (" You Make The Element '3' Ignored From The Loop ")


print ("#" * 50 )

Part22=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part22 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part22=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")



# Functions And Return Statement In Python ...!

# All Funcs Which We Use In All Prev Exaples Are Built In Funcs In Python
# Func Is A Object Has A Block Of Code To Done
# You Can Create A Func And Type In It A Block Of Code To Done By "def"
# Func Wanted From You Parameters To Do The Block Of Code On Them
# The Value Of The Parameters Called Arguments , You Typed The Arguments When You Call The Func
# You Must Type The Right Numb Of The Parameters And Be Equal To The Arguments Numb
# If You Want To Save The Data In The Fun To Handle It By Your Self Type " Return"
# When You Typed Return Then You Must Make A Variable With The Data Of The Fanc To Do Any Thing On The Data
# The Aim Of Func Is To Apply The DRY (Don't Repeat Yourself) principle
# The Argument Be Put In The Place Which Parameter In And The Jop Done On Them Instead



def Say_Hello(name,age):
 print (f" Hi {name} Your Age Is {age}...")
Say_Hello("Eslam Apas",19)


def Say_HowAreYou(name1):
 return f" How Are You , {name1} ?"
HowAreYou = Say_HowAreYou("Eslam Apas")
print (HowAreYou)


print ("#" * 50 )

Part23=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part23 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part23=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")



# Packing And UnPacking Data In Python...!



# When You Make A List And Print It , The OutPut Is The All Elements , Abd If You Wnat Print Each Element Alone , Type "*" Before The List Name
TheTestList = [10,11,12,13,14,15,16]
print (*TheTestList, end="  ")
print ( "Okk..")

print ("#" * 50 )

# The Same Thing Is In The Func , When You Make Func , You Input A Number Of Parameters And You Don't Know The Number Of Arguments Because The User Who Input It
# If The Parameters != Arguments , Then It Will Be An Error In Your Code
# You Can Make The Same Thing Which We Do With The List With The Paraneters To Make Any Number Of Argument Without Error Because You Make UnPacking To The Parameter
# You Can Make UnPacking To A Parameter And Don't To Another One
# When You Do UnPacking To The Parameter Then You Must Make A For Loop To The Paraneter To Make The Block Of Code On Any Number Arguments


def Example(*name10):
 for name in name10:
  print (f" Hello {name} ,You Learn Now Python3 ..!")
Example("Eslam","Mustafa","Yousef","Hmad")

print ("#" * 50 )

# You Can Make A Default Value To The Parametere Because User May Not Type The Argument For This Parameter
# If There Are More Than One Parameter And You Typed To Each One Of Them A Default Value And User Typed An Arguments To Those Parameters , Then The User's Value Will Be Written Not The Default


def Example2(name="Eslam",age=19):
 print (f"Hi {name} Wow...! Your Age Is {age} Good ..!")
Example2("Apas")

print ("#" * 50 )

# Each Argument Data Type Is Tuple , Because That We Can Say That The Parameter Is A Tuple Data Type
# If We Want To Make It A Dict Type , Then We Will Type "**" Before The Parameter and Argument Name , And Make A For Loop On The Dict Items To Make The Block Of Code On Them


dict20 = {"Php":"Good..68%", "Html":"VeryGood...90%", "Python":"Perfect..99%"}
def Example3(**Skills):
 for Skill ,Statue in Skills.items():
  print (f" Hi Your Skill Is {Skill} And Your Statue In It Is {Statue}....! !")
Example3(**dict20)

print ("#" * 50 )

# You Can Read And Practice In This Part And Now I Will Make A Completely Example For This Part To More UderStanding

dict30 = {"Php":"Good..68%", "Html":"VeryGood...90%", "Python":"Perfect..99%"}
Tuple30 = ("Js", "Mysql", "Css", "Go")

def Example4(name="UnKnowen",*Tuple,**Dict):
 print (f" Hi {name} , Your Future Skills Is : .." , end= " >>> ")
 for Skill1 in Tuple:
  print (Skill1 , end=" & ")
 print (f"Now {name} We Will Show You The Skills Which You Started ..")
 for Skill2_Key, Skill2_Value in Dict.items():
  print (f" Your Skill Is ..{Skill2_Key} And Your Level Is >>> {Skill2_Value}..!")
Example4("Eslam Apas",*Tuple30,**dict30)

print ("#" * 50 )

Part24=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part24 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part24=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")



# Func Scope In Python ...!

# Variables In Python Divided To Two Kinds The First Is Global Variable And Tbe Second Is Local Variable
# Global Variable You Can Call It From Any Place From The Code
# Local Variable Is Made Inside The Func And You Can Only Call It Inside The Func
# If The Variable Which In The Func Call OutSide The Func , Will Happen An Error
# If The Global Variable Called From The Func , Will Not Happen Any Error
# If You Call Any Variable Inside The Func And This Variable Isn't Defiend In The Func Then The Func Search For This Variable Globaly
# You Can Make The Local Variable >> Global Variable By Type " global + var_name " Inside The Func
# The Local Variable Which You Make It Global Won't Be Global Until You Call The Func Which Inside It The Variable



ff = "Eslam"

def say_hello(name):
 print (f" Hi {name} ...! , This Is The Global Variable ..")
say_hello(ff)               # I Call The Variable Inside The Func Because It Is A Global One


print ("#" * 50 )


def say_hello10():
 name20 = "Eslam"
 print (f" Hi {name20} .....! , This Is The Local Variable ..")
say_hello10()                # I Call The Local Variable Which Locate Inside It And I Can't Call It Outside The Func ..

# print (name20)            # An Error , The Variable Is Not Defined Because "name20" Is A Local Variable Inside A Func

print ("#" * 50 )

def say_hello20():
 global name30
 name30 = "Eslam Apas"
 print (f" '{name30}' , The Local Variable Which Will Be Global ...")
say_hello20()

print ("#" * 50 )

print (f"'{name30}' Hii , I Have Been A Global Variable ....!")

print ("#" * 50 )

Part25=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part25 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part25=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")



# Func Recursion In Python ....! 

# To Understand The Recursion Func You Must Uderstand The Recursion First ...
# Recursion Like A While Loob , But With Func , In Recursion You But Func Inside Another Func And Make The Return Statment With This Func ..
# And Make The Loop , But In Every Time In The Loop Your Value Will Be Changed To Anthor Value (A Small Edit ) 
# To Understand The Recursion Very Well , Read The follwing Code ...

def clean_word(word):
  if len(word) ==1:
    return word 
  if word[0] == word[1]:
    return clean_word(word[1:])
  else:
    return word[0] + clean_word(word[1:])

print (clean_word("eeeeeeesssssslllllllaaaaaaaammmmmmmm"))


# From The Previous COde You Will Understand The Recursion Very Well ...


print ("#" * 50 )

Part26=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part26 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part26=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")




# Lambda Func iN Python ..

# The Lambda Func Is A Func Without Name , And You Can Use It The Return Statment Of ANthor Func ..
# And You Can Use It Without Define ..
# Its Content Is Alone Code , Can't Used With BlockOfCode ..
# See The Next Example To Understand The Lambda Func .. 
# Note ||\|\| You Must Type All Func In One Line Like This ..

Hello1 = lambda name11 , age11: f"Hello {name11} , Your Age Is {age11}" 


print (Hello1("Eslam",18))


# By This Example You Will UnderSTAND The Lambda Func Very Will ..


print ("#" * 50 )

Part27=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part27 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part27=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")



# File Hnandling In Python ..



# In This Part We Will Learn How Python WOrk With Files And Put AN Files In Our Script ..
# We Will Use "Open()" Built In Func To Handle Working With Files In Python ..
# In Open() , IT Require Two Things , First Of Them Is The Path OF The File , And The Second The Mode Of Handling With File ( W = Wirte  , R = Read  , A = Abbend , C = Create )
# In Every Mode There IS Some Things Must Be Noticed ..
# (W = Write )       In This Case You Will Write The File And If The File iSN'T Exist , Will Create One Withe The Name Which You Give To IT Without AN Error  ..
# (A = Abbend )     In This Case You Will Abbend A Value In The File , And If The File Isn't Exist , Will Create One Without An Error ..
# ( C = Create )    In This Case Will Create A fILE And If There Is A file With The Same Name , Then An Error Will Occer ..
# (R = Read  )      In This Case Will Read The File Only Withot And Modifide On It , And If The File Isn't Exist , Then An Error Will Occur .. (The Default Argument )
#  When You Type The Pth Of The File , There Are Two TYPES of PATH..!
# First Kind IS Called ( Apsolute Path )   Which Open() Wored With ,, And THis Path Must Be The Path From The Root Dir..
# Second Kind Of Path Is ( Reletive Path ) 
# Doesn't Good Becase It Realy On The Current Working Dir ..
# You Can Now What IS Your Current Working Dir By This Moudle {OS Moudle} , By This Commend (print (os.getcwd()))
# I Can't Use Any Path From MY Device Because If I Do That , In Your Device AN Error Will Be Occur Because My Path Isn't In Your Device ..
# When You Type Your Absolute Path , You Will Face A Problem In The Name Which Start With An Escape Charactar .. , To Solve This Probllem , Type "r" Before The Path , Sush Like "f" Which You Type In Formating
# When You Use Open() , You Use With It A variable , But If You Type This Variable In The ( print() ) You Will Get Only Some Info About This File , Not The Content Of IT ..
# If You Want To Handle The File With Some Options Like Write Or Read , You Must Type The Option In The Open() And Type ( Print(Var_Name.Option) ) , Like ... { print(file.read()) }
# And So On ..
# There Is An Iportant Note With [ write() ] , When Input Any Data Between .. () , Then All Data Of File Will Be Replaced With The Value You Input ..
# To Solve This Problem .., You Must Use [ Abbend() ] To Add A Value To A File ..
# You Can Type [ Var_Name.close() ] When You Finch Working With The File ..
# When You Use Abbend() OR Write() , The Value Which Between () Will Be Add IN The Position Which The Cursier OF The Mouse ON .. , aND tO Know Where Is The Cursier Of The Mouse , Use [ Tell() ] With The Name Of The Variable Of The File ..
# The Output From This Func Will Be The Index OF The Character Which The Cursier IS ..
# There Are Alot Of Methodes To Handle FileS With Python .., Search For The Methodes To Be Good With Handling Files In Python ..


print (" File Handling In Python , I Can't Apply On It With Example Because The File Path Will Make An Error On Your Device ..!")

print ("#" * 50 )

Part28=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part28 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part28=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")



# Built In Func In Ptython ..! 



# We Know How To Define Any Func To Do Any Jop We Want , There Are Alot Of Functions In Python Pre-Defiend (Built In Function) ,We Will Explain Some Of Them With Explanition.. 
# You Can Type The Function Name And Stand On It wITH tHE Mouce To See Its Options And Arguments ..


Testtt1 = "Eslam Mohamed Abbas"
Tupleee1 = ("Eslam" , " Mohamed" ,"Abbas")
Listt1 = [1,2,3,4,5,6,7,8,9]
Listt2 = [0,0,0,0,1]
Dictt1 = {"Eslam" : 18 , "Ahmed" : 19 , "Muustafa" : 22 }


if all(Listt1) :
  print("All Values In Ths List Is True ...")           # all() Function IS A Function That Cheak All Values In The Iterable Opject And If All Values == True , Then Condition Will Applied  ..

if any(Listt2):
  print("There Is An Element == True Value In The List")     # any() Function Is A Function That If There At Least One Value == True To Apply Condition ..

print(bin(12345))     # bin() Is A Function Which Return To You A Binary Number To Your Inputed Number ...

print(id(Testtt1))    # id() Is A Function Which Return To You The Id Process Of The Variable In The RAM ..

print(sum(Listt1 , 10))   # sum() Is A Function Which Sum All Values In The List , And Add To The Output The Given Number (10 In Our Example)

print(round(12344.4567676 , 3 ))   # round() Is A Function Return The Given Number To The Nearst Number , And You Can Type The Number Which You Want To Be After The ( . ) 

print(list(range(1,11)))       # range() Is A Function That Take A Range From User To Do Any Operation On It .. , You Can Give To IT  The Start And The End And The Steps .. , And Be Noticed That That Given End Won't Be Included In The Operation ..

print("Hello" , end = " ")
print("Eslam")                  # print() Is A Function Which Printing The Given Values , And You Can Use (end = ..) To Define The End Of Print Stetment .. , Be Noticed That The Default Value Of "end" Is [/n] 

print(abs(-1113))    # abs() Is A Function Which Return The Positive Value OF The Given Number ..

print(pow(10 , 10 ))     # pow() Is A Function That Return The Number Power The Exp ..

print(min(Listt1))    # min() Is A Function That Return The Minemum Value Either Int Or String ..

print(max(Listt1))    # max() Do The Same Jop OF Min() But With The Greatest Value ..

Slice1 = "EEEEEEslamMMMMM"
print (Slice1[slice(5 ,10 )])       # slice() Function Do The Same Jop Of Slicing Syntax ..

def Testttt1(*Name):
  for Namee in Name:
   print(f" HI {Namee} ")

for Nameee in  map(Testttt1 , Tupleee1 ):
  print (Nameee)        # map() Is A Function Do A Jop Of A Defined Function ON A Spacific Element (Iterable Element) , If The Function (lambda) Then Only Type Its Code IN The Place Of Function Name .. 

for Output in filter(Testttt1,Tupleee1):
  print (Output)           # filter() Function Do The Same Jop Of map() But Must The Outpot == True Or Any Value Exept (0) ... , And You Can Type It In A Return Stetment

from functools import reduce       # This Part Will Be Explained Later Don't Worry ..
# The Previous Commend Is Important To Use [reduce() Function]

def Summ(Num1 , Num2):
  return Num1 + Num2

Num3 = reduce(Summ , Listt1)
print (Num3)             # reduce() Function Do That , Take From You Func And Iterable Opject And Do The Function On The First Tow Elements In The Iterable And Take The Result With The Thierd Element And Apply The Function On Them..
   
# print(help())    # help() Is A Function Do Help Document To You , And I Make It In A Comment TO Doesn't Stop The Workflow Of The Script  ..




print ("#" * 50 )

Part29=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part29 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part29=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")


# Modules In Python ..! 

# Modules In Python Are Like Folders , Inside It Alot Of Functions Which Used In The Language , To USE One Of Them You Must Import The Module  ..
# You Can Create Your Own Moudle In Your Script Normaly..! 
# Python Has ALot Of Modules And You Can Find Your Target Functions In Some Of This Modules , You Can Search About Your Func And ITS Moudule To Import It ..
# To Import Any Module Use The KeyWord (import) And The Moudule Name .. , Like .. " import os "  , " import socket " etc..
# You Can Import Only One Function From The Module By " from functools import reduce "  This To Import [reduce()] From Functools Module ..!
# You Can See All Functions In A module By " print (dir('module_name')) " 
# You Can Import All Function From A Module By " from 'module_name' import * "
# You Can Search About All Modules Which Built In Python Or See "lib" Folder Inside Python Folder In Your Computer ..! 
# ANd You Can Make Your Own Module bY create Pyhon File With All Functions Which You Want , And Then PUT It In The Modules Folder And Import It Normaly ..! 
# And Another Way To Import Your Module , BY [ import sys += sys.path.append("your_absolute_path_for_your_module") += import " Your_Module_Name " ] ..!
# You Can Change The Moudule Name In Your Script To BE Like AN Alies To IT BY [ import "module_name" as " the_new_name " ] , The New Name Of The Imported Module Will Only Used In The Script ..!
# " Package " Is A collection OF Modules .. And You Can Install Any Package In Python By "Pip" The Packge Manger IN Python ..!
# There Are Some Of Useful Links Which Will Benefit In This Part ..
# https://docs.python.org/3/py-modindex.html     # For All Built Modules In Python 
# https://pypi-org/        # For All Pakages In Python 
# https://pip.pypa.io/en/stable/reference/pip-install/     # For More Further Information About Pip 

print (" Be Good In This Part Because OF Its Importance And Read About It More ..! ")



print ("#" * 50 )

Part30=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part30 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part30=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")



# Date And Time In Python ..!

# Date And Time Is A Module In Python Work With Data And Time Only 
# You Can Import It BY ..!

import datetime

print (datetime.datetime.now())       # To Print The Current DATE And Time , And You Can Type " .time " or " .year , .month  , .day  "  To Print The Day Or The Wanted Info ..!
print (datetime.datetime.time())
print (datetime.datetime.day())     # And Those Are Some Commends In This Module ..! 
# print (datetime.datetime.now().strftime())      # You Can Edit The Date & Time Format By The Method (" strftime() ")  , And Use The " Directives " , And You Can Read MORE About It In  # https://strftime.org/


print ("#" * 50 )

Part31=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
while Part31 != "Done":
 print ("$$$$$$ You Must Complete This Part First $$$$$$ \n")
 Part31=input("If This Part Be Done , Please Type Done ... ").capitalize().strip()
else:
 print (" Good Jop ...! \n")
 
 print ("#" * 50 )

print(" Now You Have Been Understand The Basics Concept In Python Without OOP , Stay Tuned For The Update For Any Enhancemnet Or Any Addition , GOOD BYE (  mRrOBOT ) " )

# Form This Point You Will Be Able To Read And Write Python Scripts ( Without OOP ) 
# Hope To Be A Good Script And Make You Understand The Basic Concepts In Python ..
# Stay Tuned For The Update !!!!  (  MrROBOT  )

