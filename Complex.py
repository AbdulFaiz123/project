lst = []
def add(ele):
    lst.append(ele)
    
def pop():
    if len(lst) == 0
       print("eleement is empty")
    else:
        ele = lst.pop()
        print("ele is {ele}is removed")
def search(elel):
     if len(lst) == 0
       print("eleement is empty")
    else:
         if ele in lst:
              index = lst.index(ele)
              print(f"elemet {ele} is found at {index}")
        else:
            print(f"given {ele} is not found")
def dispaly():
    pass

while True:
    print("1.add 2<del 3>search  4.dispaly 5.exit\******")
    ch = int(input("enter ur choice"))
    if ch == 1:
        ele = int(input("eneter the element tom add:"))
        add(ele)
    elif ch == 2:
         pop()
    elif ch == 3:
          ele == int(input("enter the element to search"))
          search(ele)
    elif ch == 4
          dispaly()
    else 
    print("thanmk u")
          



    