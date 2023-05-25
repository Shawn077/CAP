import pickle
import numpy as np
temp_array=list()  
import tkinter as tk
root = tk.Tk()
root.title("Cricket Innings Score Predictor")
root.geometry('700x500')
root.configure(background='light blue')
tk.Label(root, 
		 text="Cricket Innings Score Predictor",
		 fg = "blue",
		 font = "Verdana 25 bold").pack()
def accept():
    global temp_array
    batting_team=value_inside1.get()
    if batting_team == 'Chennai Super Kings':
        temp_array = temp_array + [1,0,0,0,0,0,0,0]
    elif batting_team == 'Delhi Daredevils':
        temp_array = temp_array + [0,1,0,0,0,0,0,0]
    elif batting_team == 'Kings XI Punjab':
        temp_array = temp_array + [0,0,1,0,0,0,0,0]
    elif batting_team == 'Kolkata Knight Riders':
        temp_array = temp_array + [0,0,0,1,0,0,0,0]
    elif batting_team == 'Mumbai Indians':
        temp_array = temp_array + [0,0,0,0,1,0,0,0]
    elif batting_team == 'Rajasthan Royals':
        temp_array = temp_array + [0,0,0,0,0,1,0,0]
    elif batting_team == 'Royal Challengers Bangalore':
        temp_array = temp_array + [0,0,0,0,0,0,1,0]
    elif batting_team == 'Sunrisers Hyderabad':
        temp_array = temp_array + [0,0,0,0,0,0,0,1]

    bowling_team=value_inside2.get()
    if bowling_team == 'Chennai Super Kings':
        temp_array = temp_array + [1,0,0,0,0,0,0,0]
    elif bowling_team == 'Delhi Daredevils':
        temp_array = temp_array + [0,1,0,0,0,0,0,0]
    elif bowling_team == 'Kings XI Punjab':
        temp_array = temp_array + [0,0,1,0,0,0,0,0]
    elif bowling_team == 'Kolkata Knight Riders':
        temp_array = temp_array + [0,0,0,1,0,0,0,0]
    elif bowling_team == 'Mumbai Indians':
        temp_array = temp_array + [0,0,0,0,1,0,0,0]
    elif bowling_team == 'Rajasthan Royals':
        temp_array = temp_array + [0,0,0,0,0,1,0,0]
    elif bowling_team == 'Royal Challengers Bangalore':
        temp_array = temp_array + [0,0,0,0,0,0,1,0]
    elif bowling_team == 'Sunrisers Hyderabad':
        temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
    overs=float(eval(t1.get()))
    runs=int(eval(t2.get()))
    wickets=int(eval(t3.get()))
    runsprev5=int(eval(t4.get()))
    wicketsprev5=int(eval(t5.get()))

    temp_array = temp_array + [overs, runs, wickets, runsprev5, wicketsprev5]
    print(temp_array)

    filename = 'first-innings-score-lr-model.pkl'
    regressor = pickle.load(open(filename, 'rb'))

    data = np.array([temp_array])
    my_prediction = int(regressor.predict(data)[0])
    print(my_prediction-5,my_prediction+5)



tk.Label(root,
         text= "Select a Batting Team",
         fg = "black",
         font = "Times 15 bold").pack()
options_list = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
                    'Mumbai Indians', 'Kings XI Punjab', 'Royal Challengers Bangalore',
                    'Delhi Daredevils', 'Sunrisers Hyderabad']	
value_inside1 = tk.StringVar(root)
value_inside1.set("Select an Option")
question_menu2 = tk.OptionMenu(root, value_inside1, *options_list)
question_menu2.pack()
tk.Label(root,
         text= "Select a Bowling Team",
         fg = "black",
         font = "Times 15 bold").pack()
value_inside2 = tk.StringVar(root)
value_inside2.set("Select an Option")
question_menu2 = tk.OptionMenu(root, value_inside2, *options_list)
question_menu2.pack()

l1=tk.Label(root,text="Enter Overs Up", font="Times 15 bold")
l1.pack() 
t1=tk.Entry(root)
t1.pack()

l2=tk.Label(root,text="Enter Runs Scored", font="Times 15 bold")
l2.pack()
t2=tk.Entry(root)
t2.pack()

l3=tk.Label(root,text="Enter Wickets Fallen", font="Times 15 bold")
l3.pack()
t3=tk.Entry(root)
t3.pack()

l4=tk.Label(root,text="Enter Runs Scored in Previous 5 Overs", font="Times 15 bold")
l4.pack()
t4=tk.Entry(root)
t4.pack()

l5=tk.Label(root,text="Enter Wickets Fallen in Previous 5 Overs", font="Times 15 bold")
l5.pack()
t5=tk.Entry(root)
t5.pack()

b=tk.Button(root, text="Submit", command = accept)
b.pack()

root.mainloop()












