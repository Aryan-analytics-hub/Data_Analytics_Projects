#strip function

from ntpath import join


a = "        Aryan         "
print(a.strip())

#left strip

a = "        Aryan         "
print(a.lstrip())

#right strip function

a = "        Aryan         "
print(a.rstrip())


#upper case function

a = "Aryan"
print(a.upper())

#lowercase function
a = "Aryan"
print(a.lower())

#propercase function - title

a = "aryan"
print(a.title())

#strip function
a = "Aryan,kumar,Sharma"
print(a.strip(","))


#find function  = if found index- if not -1 
 
a = "Aryan kumar Sharma"
print(a.find("Aryan"))


#count function

a = "Aryan kumar Sharma"
print(a.count("r"))


#starts with function

a = "Aryan kumar Sharma"
print(a.startswith("Aryan"))

#ends with function

a = "Aryan kumar Sharma"
print(a.endswith("Sharma"))


#isdigit function


a = "34"
print(a.isdigit())





