vikrant = { #creating dictionary
    "Trainee-1" : "Vikrant",
    "Mob no." : "9211420420",
    "Year" : "2022",
    "Gender" : "Male" ,
    "Education" : "B.tech",
    "DOB" : "1947-01-05",
    "hublulu" : "blla bllaa"
}
mob= vikrant["Mob no."] #
vikrant.update ({"Gender" : "Not Defined"})
print(vikrant)
#updating dictionary

x= vikrant.keys()
print(vikrant)


print(len(vikrant))

print(mob)

print(x)

b= vikrant.items()

print(b)

vikrant ["Mob no."] = 4204209211

print(vikrant)


vikrant.pop("hublulu")

print(vikrant)

vikrant.popitem() 

print(vikrant)

#removes last inserted item


brands = {"1": "Nike",

"2" : "Adidas",

"3": "Puma",

"4": "Lotto"

}

sizes = {"08":0, "09" : 0, "12":0, "09":0

}

eksath = {}

eksath.update(brands)

eksath.update(sizes)

print(eksath)

#combining two dictionary

brands["Red_cheif"]=brands.pop("2")

print(sorted(brands))


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 
print(myfamily)
