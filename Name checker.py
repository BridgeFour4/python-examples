#Nathan Broadbent
#9/18

# get a users name
##def get_name():
##    
###step 1 ask for a name
##    name= input("What is your name")
### step 2 display Name to User
##    print("the name you entered was", name)
###step 3  verify the name
##    verify= input("is this correct yes or no")
##
##print("this is our function")    
##get_name()



#calculate the area of a circle
#radius squared*pi


#step 1 get the radius
#step 2 calculate the area
#step three display area

def circle_area():
    pi=3.141592653
    radius= input("what is the radius ")
    radius= float(radius)

    area= radius*radius*pi
    print("the area of your circle is ", area)
    
circle_area();
