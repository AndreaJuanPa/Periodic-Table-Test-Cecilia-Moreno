import tkinter as t
from tkinter import ttk
from tkinter import messagebox
import csv
import random

# PERIODIC TABLE OF THE ELEMENTS TEST PROJECT
# Creating function to store data
def store_data():
        fname=firstname_entry.get()
        lname=lastname_entry.get()
        grade=grade_entry.get()
        room=room_entry.get()
        score=score_result["text"]
        if fname and lname and grade and room:
            print("First name: ",fname,"    Last name: ", lname)
            print("Grade: ",grade,"    Room: ", room, "    ", score)

            with open("students.csv","a",newline="")as csv_append:
                csvwriter=csv.writer(csv_append)
                csvwriter.writerow([fname,lname,grade,room,score])
        else:
            t.messagebox.showwarning(title="Error",message="First name, last name, grade and room are required")


# CLASS and OBJECTS
class Elements():
  def __init__(self, name, symbol, family):
    self.name = name
    self.symbol = symbol
    self.family = family

# Creating list
list=[]

# APPENDING ALL THE OBJECTS to the list
list.append(Elements("Hydrogen", "H", "Nonmetal"))
list.append(Elements("Helium", "He", "Noble Gas"))
list.append(Elements("Lithium", "Li", "Alkali Metal"))
list.append(Elements("Beryllium", "Be", "Alkaline Earth"))
list.append(Elements("Boron", "B", "Semimetal"))
list.append(Elements("Carbon", "C", "Nonmetal"))
list.append(Elements("Nitrogen", "N", "Nonmetal"))
list.append(Elements("Oxygen", "O", "Nonmetal"))
list.append(Elements("Fluorine", "F", "Halogen"))
list.append(Elements("Neon", "Ne", "Noble Gas"))
list.append(Elements("Sodium", "Na", "Alkali Metal"))
list.append(Elements("Magnesium", "Mg", "Alkaline Earth"))
list.append(Elements("Aluminium", "Al", "Basic Metal"))
list.append(Elements("Silicon", "Si", "Semimetal"))
list.append(Elements("Phosphorus", "P", "Nonmetal"))
list.append(Elements("Sulfur", "S", "Nonmetal"))
list.append(Elements("Chlorine", "Cl", "Halogen"))
list.append(Elements("Argon", "Ar", "Noble Gas"))
list.append(Elements("Potassium", "K", "Alkali Metal"))
list.append(Elements("Calcium", "Ca", "Alkaline Earth"))
list.append(Elements("Scandium", "Sc", "Transition Metal"))
list.append(Elements("Titanium", "Ti", "Transition Metal"))
list.append(Elements("Vanadium", "V", "Transition Metal"))
list.append(Elements("Chromium", "Cr", "Transition Metal"))
list.append(Elements("Manganese", "Mn", "Transition Metal"))
list.append(Elements("Iron", "Fe", "Transition Metal"))
list.append(Elements("Cobalt", "Co", "Transition Metal"))
list.append(Elements("Nickel", "Ni", "Transition Metal"))
list.append(Elements("Zinc", "Zn", "Transition Metal"))
list.append(Elements("Gallium", "Ga", "Basic Metal"))
list.append(Elements("Germanium", "Ge", "Semimetal"))
list.append(Elements("Arsenic", "As", "Semimetal"))
list.append(Elements("Selenium", "Se", "Nonmetal"))
list.append(Elements("Bromine", "Br", "Halogen"))
list.append(Elements("Krypton", "Kr", "Noble Gas"))
list.append(Elements("Rubidium", "Rb", "Alkali Metal"))
list.append(Elements("Strontium", "Sr", "Alkaline Earth"))
list.append(Elements("Yttrium", "Y", "Transition Metal"))
list.append(Elements("Zirconium", "Zr", "Transition Metal"))
list.append(Elements("Niobium", "Nb", "Transition Metal"))
list.append(Elements("Molybdenum", "Mo", "Transition Metal"))
list.append(Elements("Technetium", "Tc", "Transition Metal"))
list.append(Elements("Ruthenium", "Ru", "Transition Metal"))
list.append(Elements("Rhodium", "Rh", "Transition Metal"))
list.append(Elements("Palladium", "Pd", "Transition Metal"))
list.append(Elements("Silver", "Ag", "Transition Metal"))
list.append(Elements("Cadmium", "Cd", "Transition Metal"))
list.append(Elements("Indium", "In", "Basic Metal"))
list.append(Elements("Tin", "Sn", "Basic Metal"))
list.append(Elements("Antimony", "Sb", "Semimetal"))
list.append(Elements("Tellurium", "Te", "Semimetal"))
list.append(Elements("Iodine", "I", "Halogen"))
list.append(Elements("Xenon", "Xe", "Noble Gas"))
list.append(Elements("Caesium", "Cs", "Alkali Metal"))
list.append(Elements("Barium", "Ba", "Alkaline Earth"))
list.append(Elements("Hafnium", "Hf", "Transition Metal"))
list.append(Elements("Tantalum", "Ta", "Transition Metal"))
list.append(Elements("Tungsten", "W", "Transition Metal"))
list.append(Elements("Rhenium", "Re", "Transition Metal"))
list.append(Elements("Osmium", "Os", "Transition Metal"))
list.append(Elements("Iridium", "Ir", "Transition Metal"))
list.append(Elements("Platinum", "Pt", "Transition Metal"))
list.append(Elements("Gold", "Au", "Transition Metal"))
list.append(Elements("Mercury", "Hg", "Transition Metal"))
list.append(Elements("Thallium", "Tl", "Basic Metal"))
list.append(Elements("Lead", "Pb", "Basic Metal"))
list.append(Elements("Bismuth", "Bi", "Basic Metal"))
list.append(Elements("Polonium", "Po", "Basic Metal"))
list.append(Elements("Astatine", "At", "Basic Metal"))
list.append(Elements("Radon", "Rn", "Noble Gas"))
list.append(Elements("Francium", "Fr", "Alkali Metal"))
list.append(Elements("Radium", "Ra", "Alkaline Earth"))
list.append(Elements("Rutherfordium", "Rf", "Transition Metal"))
list.append(Elements("Dubnium", "Db", "Transition Metal"))
list.append(Elements("Seaborgium", "Sg", "Transition Metal"))
list.append(Elements("Bohrium", "Bh", "Transition Metal"))
list.append(Elements("Hassium", "Hs", "Transition Metal"))
list.append(Elements("Meitnerium", "Mt", "Transition Metal"))
list.append(Elements("Darmstadtium", "Ds", "Transition Metal"))
list.append(Elements("Roentgenium", "Rg", "Transition Metal"))
list.append(Elements("Copernicium", "Cn", "Transition Metal"))
list.append(Elements("Nihonium", "Nh", "Basic Metal"))
list.append(Elements("Flerovium", "Fl", "Basic Metal"))
list.append(Elements("Moscovium", "Mc", "Basic Metal"))
list.append(Elements("Livermorium", "Lv", "Basic Metal"))
list.append(Elements("Tennessine", "Ts", "Halogen"))
list.append(Elements("Oganesson", "Og", "Noble Gas"))

# Creating function: Start Test Button.
# Print 10 Random elements from the list
def start_test_button():
  global name1
  name1 = random.choice(list)
  element1_name_label["text"] = f"1. NAME: {name1.name}"
  global name2
  name2 = random.choice(list)
  element2_name_label["text"] = f"2. NAME: {name2.name}"
  global name3
  name3 = random.choice(list)
  element3_name_label["text"] = f"3. NAME: {name3.name}"
  global name4
  name4 = random.choice(list)
  element4_name_label["text"] = f"4. NAME: {name4.name}"
  global name5
  name5 = random.choice(list)
  element5_name_label["text"] = f"5. NAME: {name5.name}"
  global name6
  name6 = random.choice(list)
  element6_name_label["text"] = f"6. NAME: {name6.name}"
  global name7
  name7 = random.choice(list)
  element7_name_label["text"] = f"7. NAME: {name7.name}"
  global name8
  name8 = random.choice(list)
  element8_name_label["text"] = f"8. NAME: {name8.name}"
  global name9
  name9 = random.choice(list)
  element9_name_label["text"] = f"9. NAME: {name9.name}"
  global name10
  name10 = random.choice(list)
  element10_name_label["text"] = f"10. NAME: {name10.name}"

def get_sum():
# Compare student entries to the list to calculate sum of total points.
  sum=0
  if element1_symbol_entry.get()==name1.symbol:
    sum+=1
  e1=element1_family_entry.get()
  if e1.title()==name1.family:
    sum+=1
  if element2_symbol_entry.get()==name2.symbol:
    sum+=1
  e2 = element2_family_entry.get()
  if e2.title()==name2.family:
    sum+=1
  if element3_symbol_entry.get()==name3.symbol:
    sum+=1
  e3 = element3_family_entry.get()
  if e3.title()==name3.family:
    sum+=1
  if element4_symbol_entry.get()==name4.symbol:
    sum+=1
  e4 = element4_family_entry.get()
  if e4.title()==name4.family:
    sum+=1
  if element5_symbol_entry.get()==name5.symbol:
    sum+=1
  e5 = element5_family_entry.get()
  if e5.title()==name5.family:
    sum+=1
  if element6_symbol_entry.get()==name6.symbol:
    sum+=1
  e6 = element6_family_entry.get()
  if e6.title()==name6.family:
    sum+=1
  if element7_symbol_entry.get()==name7.symbol:
    sum+=1
  e7 = element7_family_entry.get()
  if e7.title()==name7.family:
    sum+=1
  if element8_symbol_entry.get()==name8.symbol:
    sum+=1
  e8 = element8_family_entry.get()
  if e8.title()==name8.family:
    sum+=1
  if element9_symbol_entry.get()==name9.symbol:
    sum+=1
  e9 = element9_family_entry.get()
  if e9.title()==name9.family:
    sum+=1
  if element10_symbol_entry.get()==name10.symbol:
    sum+=1
  e10 = element10_family_entry.get()
  if e10.title()==name10.family:
    sum+=1
  return sum

# Creating function: "Get your Score" button.
def get_your_score():
  x=get_sum()
  score = x / 20 * 100
  score_result["text"]=f"YOUR SCORE IS:  {x}/20= {score} %"

# Main Frame
window=t.Tk()
window.title("PERIODIC TABLE OF THE ELEMENTS TEST")
window.geometry("850x750")

# Main frame inside the window
frame=t.Frame(window)
frame.pack()
frame_userInfo=t.LabelFrame(frame,text="STUDENT INFORMATION",padx=20,pady=10)
frame_userInfo.grid(row=0,column=0)

# First name label
firstname_label=t.Label(frame_userInfo,text="FIRST NAME: ",padx=5,pady=5)
firstname_label.grid(row=0,column=0)
# Firstname entry box
firstname_entry=t.Entry(frame_userInfo)
firstname_entry.grid(row=0,column=1)
# Lastname label
lastname_label=t.Label(frame_userInfo,text="LAST NAME: ",padx=5,pady=5)
lastname_label.grid(row=0,column=2)
# Lastname entry box
lastname_entry=t.Entry(frame_userInfo)
lastname_entry.grid(row=0,column=3)

# GRADE label
grade_label=t.Label(frame_userInfo,text="GRADE: ",padx=5,pady=5)
grade_label.grid(row=1,column=0)
# GRADE entry box
grade_entry=t.Entry(frame_userInfo)
grade_entry.grid(row=1,column=1)

# ROOM label
room_label=t.Label(frame_userInfo,text="ROOM: ",padx=5,pady=5)
room_label.grid(row=1,column=2)
# ROOM entry box
room_entry=t.Entry(frame_userInfo)
room_entry.grid(row=1,column=3)

# START TEST Button
start_button=t.Button(frame,text="PRESS THIS BUTTON TO START YOUR TEST",command=start_test_button)
start_button.grid(row=2,column=0,sticky="news",pady=10)

# TEST frame inside the window
frame_Test=t.LabelFrame(frame,text="ELEMENTS TEST:\n\n Instructions:     1. Family Options are:   Alkali Metal, Alkaline Earth, Transition Metal, Basic Metal, Semimetal, \n\t           Nonmetal, Halogen, Noble Gas. Be very careful to spell them correctly, exactly as shown here.\n\n\t 2. Remember that all symbols must start with a capital letter followed by lower case. \nFill all the blanks and try your best. \tGOOD LUCK !!!",padx=20,pady=10)
frame_Test.grid(row=3,column=0)

# 10 RANDOM ELEMENTS
# NAME label for element 1.
element1_name_label=t.Label(frame_Test,text="1. NAME: ",padx=5,pady=5)
element1_name_label.grid(row=0,column=0)
# SYMBOL label for element 1.
element1_symbol_label=t.Label(frame_Test,text="SYMBOL: ",padx=5,pady=5)
element1_symbol_label.grid(row=0,column=1)
# SYMBOL 1 entry box
element1_symbol_entry=t.Entry(frame_Test)
element1_symbol_entry.grid(row=0,column=2)
# FAMILY label for element 1.
element1_family_label=t.Label(frame_Test,text="FAMILY: ",padx=5,pady=5)
element1_family_label.grid(row=0,column=3)
# FAMILY 1 entry box
element1_family_entry=t.Entry(frame_Test)
element1_family_entry.grid(row=0,column=4)

# NAME label for element 2.
element2_name_label=t.Label(frame_Test,text="2. NAME: ",padx=5,pady=5)
element2_name_label.grid(row=1,column=0)
# SYMBOL label for element 2.
element2_symbol_label=t.Label(frame_Test,text="SYMBOL: ",padx=5,pady=5)
element2_symbol_label.grid(row=1,column=1)
# SYMBOL 2 entry box
element2_symbol_entry=t.Entry(frame_Test)
element2_symbol_entry.grid(row=1,column=2)
# FAMILY label for element 2.
element2_family_label=t.Label(frame_Test,text="FAMILY: ",padx=5,pady=5)
element2_family_label.grid(row=1,column=3)
# FAMILY 2 entry box
element2_family_entry=t.Entry(frame_Test)
element2_family_entry.grid(row=1,column=4)

# NAME label for element 3.
element3_name_label=t.Label(frame_Test,text="3. NAME: ",padx=5,pady=5)
element3_name_label.grid(row=2,column=0)
# SYMBOL label for element 3.
element3_symbol_label=t.Label(frame_Test,text="SYMBOL: ",padx=5,pady=5)
element3_symbol_label.grid(row=2,column=1)
# SYMBOL 3 entry box
element3_symbol_entry=t.Entry(frame_Test)
element3_symbol_entry.grid(row=2,column=2)
# FAMILY label for element 3.
element3_family_label=t.Label(frame_Test,text="FAMILY: ",padx=5,pady=5)
element3_family_label.grid(row=2,column=3)
# FAMILY 3 entry box
element3_family_entry=t.Entry(frame_Test)
element3_family_entry.grid(row=2,column=4)

# NAME label for element 4.
element4_name_label=t.Label(frame_Test,text="4. NAME: ",padx=5,pady=5)
element4_name_label.grid(row=3,column=0)
# SYMBOL label for element 4.
element4_symbol_label=t.Label(frame_Test,text="SYMBOL: ",padx=5,pady=5)
element4_symbol_label.grid(row=3,column=1)
# SYMBOL 4 entry box
element4_symbol_entry=t.Entry(frame_Test)
element4_symbol_entry.grid(row=3,column=2)
# FAMILY label for element 4.
element4_family_label=t.Label(frame_Test,text="FAMILY: ",padx=5,pady=5)
element4_family_label.grid(row=3,column=3)
# FAMILY 4 entry box
element4_family_entry=t.Entry(frame_Test)
element4_family_entry.grid(row=3,column=4)

# NAME label for element 5.
element5_name_label=t.Label(frame_Test,text="5. NAME: ",padx=5,pady=5)
element5_name_label.grid(row=4,column=0)
# SYMBOL label for element 5.
element5_symbol_label=t.Label(frame_Test,text="SYMBOL: ",padx=5,pady=5)
element5_symbol_label.grid(row=4,column=1)
# SYMBOL 5 entry box
element5_symbol_entry=t.Entry(frame_Test)
element5_symbol_entry.grid(row=4,column=2)
# FAMILY label for element 5.
element5_family_label=t.Label(frame_Test,text="FAMILY: ",padx=5,pady=5)
element5_family_label.grid(row=4,column=3)
# FAMILY 5 entry box
element5_family_entry=t.Entry(frame_Test)
element5_family_entry.grid(row=4,column=4)

# NAME label for element 6.
element6_name_label=t.Label(frame_Test,text="6. NAME: ",padx=5,pady=5)
element6_name_label.grid(row=5,column=0)
# SYMBOL label for element 6.
element6_symbol_label=t.Label(frame_Test,text="SYMBOL: ",padx=5,pady=5)
element6_symbol_label.grid(row=5,column=1)
# SYMBOL 6 entry box
element6_symbol_entry=t.Entry(frame_Test)
element6_symbol_entry.grid(row=5,column=2)
# FAMILY label for element 6.
element6_family_label=t.Label(frame_Test,text="FAMILY: ",padx=5,pady=5)
element6_family_label.grid(row=5,column=3)
# FAMILY 6 entry box
element6_family_entry=t.Entry(frame_Test)
element6_family_entry.grid(row=5,column=4)

# NAME label for element 7.
element7_name_label=t.Label(frame_Test,text="7. NAME: ",padx=5,pady=5)
element7_name_label.grid(row=6,column=0)
# SYMBOL label for element 7.
element7_symbol_label=t.Label(frame_Test,text="SYMBOL: ",padx=5,pady=5)
element7_symbol_label.grid(row=6,column=1)
# SYMBOL 7 entry box
element7_symbol_entry=t.Entry(frame_Test)
element7_symbol_entry.grid(row=6,column=2)
# FAMILY label for element 7.
element7_family_label=t.Label(frame_Test,text="FAMILY: ",padx=5,pady=5)
element7_family_label.grid(row=6,column=3)
# FAMILY 7 entry box
element7_family_entry=t.Entry(frame_Test)
element7_family_entry.grid(row=6,column=4)

# NAME label for element 8.
element8_name_label=t.Label(frame_Test,text="8. NAME: ",padx=5,pady=5)
element8_name_label.grid(row=7,column=0)
# SYMBOL label for element 8.
element8_symbol_label=t.Label(frame_Test,text="SYMBOL: ",padx=5,pady=5)
element8_symbol_label.grid(row=7,column=1)
# SYMBOL 8 entry box
element8_symbol_entry=t.Entry(frame_Test)
element8_symbol_entry.grid(row=7,column=2)
# FAMILY label for element 8.
element8_family_label=t.Label(frame_Test,text="FAMILY: ",padx=5,pady=5)
element8_family_label.grid(row=7,column=3)
# FAMILY 8 entry box
element8_family_entry=t.Entry(frame_Test)
element8_family_entry.grid(row=7,column=4)

# NAME label for element 9.
element9_name_label=t.Label(frame_Test,text="9. NAME: ",padx=5,pady=5)
element9_name_label.grid(row=8,column=0)
# SYMBOL label for element 9.
element9_symbol_label=t.Label(frame_Test,text="SYMBOL: ",padx=5,pady=5)
element9_symbol_label.grid(row=8,column=1)
# SYMBOL 9 entry box
element9_symbol_entry=t.Entry(frame_Test)
element9_symbol_entry.grid(row=8,column=2)
# FAMILY label for element 9.
element9_family_label=t.Label(frame_Test,text="FAMILY: ",padx=5,pady=5)
element9_family_label.grid(row=8,column=3)
# FAMILY 9 entry box
element9_family_entry=t.Entry(frame_Test)
element9_family_entry.grid(row=8,column=4)

# NAME label for element 10.
element10_name_label=t.Label(frame_Test,text="10. NAME: ",padx=5,pady=5)
element10_name_label.grid(row=9,column=0)
# SYMBOL label for element 10.
element10_symbol_label=t.Label(frame_Test,text="SYMBOL: ",padx=5,pady=5)
element10_symbol_label.grid(row=9,column=1)
# SYMBOL 10 entry box
element10_symbol_entry=t.Entry(frame_Test)
element10_symbol_entry.grid(row=9,column=2)
# FAMILY label for element 10.
element10_family_label=t.Label(frame_Test,text="FAMILY: ",padx=5,pady=5)
element10_family_label.grid(row=9,column=3)
# FAMILY 10 entry box
element10_family_entry=t.Entry(frame_Test)
element10_family_entry.grid(row=9,column=4)

# GET YOUR SCORE Button
score_button=t.Button(frame,text="PRESS THIS BUTTON TO GET YOUR SCORE",command=get_your_score)
score_button.grid(row=10,column=0,sticky="news",pady=10)

# SCORE Result
score_result=t.Label(frame,text="YOUR SCORE IS: ",padx=5,pady=5)
score_result.grid(row=11,column=0, sticky="news")

# SAVE DATA Button
save_button=t.Button(frame,text="PRESS THIS BUTTON TO SAVE YOUR DATA",command=store_data)
save_button.grid(row=12,column=0,sticky="news",pady=10)

window.mainloop()
