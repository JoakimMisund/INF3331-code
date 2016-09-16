import pickle, matplotlib.pyplot as plt

#1 Class definition and mathods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_me(self):
        print("My name is %s, and I am %d years old" % (self.name, self.age))

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name


def plot_ages(persons):
    #5 Plot using matplotlib's plyplot
    fig, ax = plt.subplots()

    for i,p in enumerate(persons):
        ax.bar(i, p.get_age(), width=0.5,  label=p.get_name())

    #Set lables of x and y axis
    ax.set_ylabel('Age')
    #6 List comprehension. Do something with every element in a list and
    # put the result in a new list
    ax.set_xticklabels([p.get_name() for p in persons])

    #Adjust x axis labels to match the bars
    x_len = len(persons)+1
    ax.set_xticks([i+0.25 for i in range(0,x_len)])
    plt.axis([0,x_len,0,100])

    plt.show()


save_filename = "persons.dump"
persons = []

#2 Try to load saved data if exists
try:
    persons = pickle.load(open(save_filename, "rb"))
except:
    print("Did not find any savefile")


while(1):
    #3 Getting user input (Should add error checking! Omitted for simplicity)
    name = input("Please enter a name (q: quit, l: list, p: plot): ").strip()
    
    if name == "q":
        break;
    elif name == "l":
        for p in persons:
            p.print_me()
    elif name == "p":
        plot_ages(persons)
    elif len(name) < 1:
        continue
    else:
        age = int(input("Please enter %s's age: " % name))
        #4 Add new elemnt to end of list
        persons.append(Person(name, age))

#2 Save the persons to a savefile for later processing
pickle.dump(persons, open(save_filename, "wb"))


