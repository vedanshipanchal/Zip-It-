# zipped list from two lists
s1 = {1,2,3}
s2 = ['Tasheen',  'Vedanshi',  'Chiamalite']
res = list(zip(s1,s2))
print(res)

#elements of two lists zipped together,
#but 2nd list in reverse order 
list1 = [1,2,3,4,5]
list2 = [10,20,30,40,50]
for i,j in zip(list1,list2[::-1]):
  print(i,j)

#elements of two lists zipped into a dictionary
food =['noodles','ramen','sphagetti','Dosa']
prices = [100, 170,230,80]
newdict = {food:prices for food, prices in zip(food,prices)}
print(newdict)