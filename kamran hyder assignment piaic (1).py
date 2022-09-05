#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Assign a message to a variable and then print that message
x = "Hello world!"
print(x)


# In[7]:


#Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something 
#like the following, including the quotation marks:

name="Oscar Wilde, said,"
quote="Experience is merely the name men gave to their mistakes."
print(name," ",quote,' ') 


# In[11]:


#Calculate Area of a Circle: Write a Python program which accepts the radius of a circle from the user and compute the area.
Radius = float(input(" Enter radius of the circle: "))

print(" Input Radius:",Radius)
print ("Area of Circle with Radius " + str(Radius) + " is : " + str(3.141 * Radius**2))


# In[14]:


#Check Number either positive, negative or zero:: Write a Python program to check if a number is positive,
num = float(input("Enter a number: "))
if num > 0:
    print("Positive Number")
elif num == 0:
    print("Zero Entered")
else:
    print("Negative number")


# In[29]:


#Vowel Tester Write a Python program to test whether a passed letter is a vowel or not
Vowel = input(" Enter a character:")
if Vowel == 'A' or Vowel == "a" or Vowel == 'E' or Vowel == 'e' or Vowel == 'I' or Vowel == 'i' or Vowel == 'O' or Vowel == 'o' or Vowel == 'U' or Vowel == 'u':
    print('Letter',Vowel,"is Vowel")
else:
    print("Letter",Vowel,"is not Vowel")


# In[30]:


#BMI Calculator Write a Python program to calculate body mass index Program
Height = float(input("Enter Height in Cm: "))
Weight = float(input("Enter Weight in Kg:: "))
Height_m = Height / 100
print("Your body mass is: ", Weight / (Height_m * Height_m) )


# In[31]:


#Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the 
#list, one at a time
name = ['Kamran' , 'Rahul' ,  'Ali' , 'Raheel' , 'Anees' , 'Irshad']
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])


# In[33]:


#Start with the list you used in Question 4, but instead of just printing each person’s name, print a message to them. 
#The text of each message should be the same, but each message should be personalized with the person’s name.
for friend in name:
    print(friend,"is a nice guy")


# In[35]:


#Make a python program that conatains your nine favourite dishes in a list called foods. Print the message, 
#The first three items in the list are:
foods = ['Pizza','burger','pizza','mommos','macroni','spheghetti','corn','nuggets','pasta']
print('The first three items in the list are',foods[0:3])
print('Three items from the middle of the list are',foods[3:6])
print('The last three items in the list are',foods[6:])


# In[38]:


#Start with your program from your last Question8. Make a copy of the list of foods, and call it friend_foods. Then, 
#do the following
#Add a new dish to the original list.
#Add a different dish to the list friend_foods.
#Prove that you have two separate lists
friends_food = foods[0:9]
foods.append("chicken roll")
friends_food.append("chapotla")
print(foods)
print(friends_food)


#Print the message, My favorite pizzas are: and then use a for loop to print the first list.
#Print the message
print("My favorite pizza are : ")
for items in foods:
    print(items)


# In[8]:


def variable_charges (monthly_units):
    if monthly_units > 1 and monthly_units < 1:
        v_charges = monthly_units * 9.43
    if monthly_units > 101 and monthly_units < 200:
        v_charges = monthly_units * 17.9566
    if monthly_units > 201 and monthly_units < 300:
        v_charges = monthly_units * 18.84
    if monthly_units > 301 and monthly_units < 400:
        v_charges = monthly_units * 19.76
    return int(v_charges)

def uniform_adj (June_uni_units):
    result = June_uni_units * 0.5715
    return int(result)

def fuel_adj_a(May):
    m = May * 6.8858
    return int(m)

def fuel_adj_b(Jun):
    j = Jun * 3.0114
    return int(j)
    

def ke_charges (c1, c2, c3, c4):
    result = c1 + c2 + c3 + c4
    return result

def duty (ke_charges):
    result = ke_charges * 0.015
    return int(result)

def sales_tax (ke_charges, duty):
    result = (ke_charges + duty) * 0.17
    return int(result)

def govt_charges (a, b):
    result = a + b
    return int(result)
def total_dues (a, b):
    result = a + b
    return int(result)

Aug_user_input = int(input ("enter Units of Aug: "))
Jun_user_input = int(input ("enter Units of Jun: "))
Jun_uni_user_input = int(input ("enter Units of Jun Uni: "))
May_user_input = int(input ("enter Units of May: "))


def main_calc(Aug, June, Jun_uni, May):
    display_a = variable_charges(Aug)
    print ("\nvariable Charges is: ", display_a)
    
    display_b = uniform_adj(Jun_uni_user_input)
    print ("\nuniform Adjustment is: ", display_b)
    
    display_c = fuel_adj_a(May_user_input)
    print ("\nFuel Adj of May-22 is : ", display_c)
    
    display_d = fuel_adj_b(Jun_user_input)
    print ("\nFuel Adj of June-22 is : ", display_d)
    
    display_e = ke_charges(display_a, display_b, display_c, display_d)
    print ("\nTotal KE charges are: ", display_e)
    
    display_f = duty(display_e)
    print ("\nElectricity duty: ", display_f)
    
    display_g = sales_tax(display_e, display_f)
    print ("\nSales tax: ", display_g)

    display_h = govt_charges(display_f, display_g)
    print ("\nTotal Government charges are: ", display_h)
    
    display_e = total_dues(display_e, display_h)
    print ("\nYour Electricity charges for the period: ", display_e)

main_calc(Aug_user_input, Jun_user_input, Jun_uni_user_input, May_user_input)


# In[ ]:




