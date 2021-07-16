#The soltuion class to the data.py questions, by Jonathan Na

from data import WEBSITES

'''
From the looks of it, the list seems to be filled with dictionaries, so my first order of business is to figure out a way to access the keys inside
the dictionaries which are inside a list. 

1) Find and return a new list of data where each item's value key is equal to or greater than four.
In other words we need to create a method to return a new list of data where only items with an equal or greater value of four are allowed.
This seems easy enough by iterating through the entire list and using an if statement to check the value number
'''
class Task1:
    #Create ane empty constructor 
    def __init__(self):
        pass

    #Name: method1, parameter: list of dictionaries, return a new list of dictionaries 
    #Find and return a new list of data where each item's value key is equal to or greater than four.
    def method1(self, inputlist):
        newList = []
        for i in inputlist:
            if i['value'] >= 4:
                newList.append(i)
        return(newList)

CallTask1 = Task1()
print(CallTask1.method1(WEBSITES))

'''
2) Amend the list so each domain key value is prepended with the string www.
We need to get the value of the domain and append the string "www" to the beginning of each domain
'''
class Task2:
    #Create ane empty constructor 
    def __init__(self):
        pass
    
    #Name: method2, parameter: list of dictionaries, return the same list of dictionaries 
    #Amend the list so each domain key value is prepended with the string www.
    def method2(self, inputlist):
        str = "www."
        for i in inputlist:
            i['domain'] = str + i['domain']
        return(inputlist)

CallTask2 = Task2()
print(CallTask2.method2(WEBSITES))

'''
3) Some of the data is inaccurate, the secure key is set to False when the url key contains a URL beginning with https://. The opposite is also true in some cases. 
The list should be cleansed and returned so the secure keys are accurate.
I'll admit the wording on this was a little confusing due to the lack of info from the example. However it just means that if the url contains the "https://" then 
the secure value should be true otherwise it should be false. 
However! we know that we're only looking for the 's' in the "https" so in reality we just need to find the 4th index in the string to see if it contains an 's' or not
'''
class Task3:
    #Create ane empty constructor 
    def __init__(self):
        pass

    #Name: method3, parameter: list of dictionaries, return the same list of dictionaries 
    #Make sure the url contains an 's' in the 4th index to change the boolean value of secure
    def method3(self, inputlist):
        for i in inputlist:
            if i['url'][4] == 's':
                i['secure'] = True
            else:
                i['secure'] = False
        return(inputlist)


CallTask3 = Task3()
print(CallTask3.method3(WEBSITES))

'''
4) Add up all the value keys in the list and return an integer.
We need to add up all the vaules from the list, so create a method that adds all the values and returns an integer.
'''
class Task4:
    #Create ane empty constructor 
    def __init__(self):
        pass

    #Name: method4, parameter: list of dictionaries, return an integer
    #Add up all the value keys in the list and return an integer.
    def method4(self, inputlist):
        num = 0
        for i in inputlist:
            num += i['value']
        return(num)

CallTask4 = Task4()
print(CallTask4.method4(WEBSITES))
