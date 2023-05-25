import tkinter as tk                
from tkinter import OptionMenu, PhotoImage, StringVar, font  as tkfont
from tkinter.constants import ANCHOR 
from PIL import Image, ImageTk
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


match_data = pd.read_csv("D:/CS Project 21-22/IPL Dataset/Match dataset.csv")
ball_data = pd.read_csv("D:\CS Project 21-22\IPL Dataset\Ball_by_ball.csv")

list_batters = ball_data['batsman'].unique()

match_data['Season'] = pd.DatetimeIndex(match_data['date']).year

match_perseason = match_data.groupby(['Season'])['id'].count().reset_index().rename(columns={'id':'matches'})
season_data = match_data[['id','Season']].merge(ball_data, left_on = 'id', right_on = 'id', how = 'left').drop('id',axis = 1)
season_data.head()



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Proxima Nova', size=27, weight="bold")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Predictor, Analysis):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#0349a5')
        self.controller = controller

        self.controller.state('zoomed')
        self.controller.iconphoto(True,tk.PhotoImage(file="D:\CS Project 21-22\stump.png"))

        bg_frame = tk.Frame(self, bg='red')
        bg_frame.pack()
        analysis_frame = tk.Frame(self, bg='#030055')
        analysis_frame.pack(side='right', fill='y')
        predictor_frame = tk.Frame(self, bg='#030055')
        predictor_frame.pack(side='left', fill='y')

        pathtophoto = Image.open("D:\CS Project 21-22\\bg_ipl.jpg")
        pathtophoto = pathtophoto.resize((870, 700))
        image1 = ImageTk.PhotoImage(pathtophoto)
        panel1 = tk.Label(self, image=image1)
        panel1.image = image1 #keep a reference
        panel1.pack(side='bottom')

        
    
        label = tk.Label(bg_frame, text="Welcome to CAP", font=controller.title_font, bg='#0349a5')
        label.pack(side='top',fill="x")

        self.controller.title('CAP - Cricket Analysis and Predictor')


        button1 = tk.Button(predictor_frame, text="Predictor", relief='raised', activebackground='#ff751a', borderwidth=3, width=17, height=2, bg='#e6b800',
                             command=lambda: controller.show_frame("Predictor"))
        button2 = tk.Button(analysis_frame, text="Analysis", relief='raised', activebackground='#ff751a',  borderwidth=3, width=17, height=2, bg='#e6b800',
                            command=lambda: controller.show_frame("Analysis"))
        button1.pack(padx=70, pady= 7, side='left')
        button2.pack(side='right',padx=50, pady=7)
        




class Predictor(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#0349a5')
        self.controller = controller
        label1 = tk.Label(self, text="Prediction", bg='#0349a5', font=controller.title_font)
        label1.pack(side="top", fill="x", pady=10)
        label2 = tk.Label(self, text="Find out how your favourite team would fare against other teams", bg='#0349a5', font=('Helvetica',15, 'italic'))
        label2.pack(side="top", fill="x", pady=3)

        input_frame = tk.Frame(self, bg='#030055')
        input_frame.pack(side='left', fill='both', expand='true')

        display_frame = tk.Frame(self, bg='#030055')
        display_frame.pack(padx=10, side='right', fill='both', expand='true')

        
        

        def accept():

            temp_array = []

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

            flag1 = False

            if batting_team == bowling_team:
                flag1 = True
                tk.messagebox.showerror("Error","Batting team and Bowling team cannot be same")
            if overs>20.0:
                flag1 = True
                tk.messagebox.showerror("Error","Please check values for the number of overs up")
            if wickets>10:
                flag1 = True
                tk.messagebox.showerror("Error","Please check values for the number of wickets fallen")
            if runs<0 or runs>350:
                flag1 = True
                tk.messagebox.showerror("Error","Please check values for the number of runs scored")
            if runsprev5>150:
                flag1 = True
                tk.messagebox.showerror("Error","Please check values for the number of runs scored in last 5 overs")
            if wicketsprev5>10:
                flag1 = True
                tk.messagebox.showerror("Error","Please check values for the number of wickets fallen in last 5 overs")
            if flag1 == False:
                temp_array = temp_array + [overs, runs, wickets, runsprev5, wicketsprev5]
                #print(temp_array)

                filename = 'first-innings-score-lr-model.pkl'
                regressor = pickle.load(open(filename, 'rb'))

                data = np.array([temp_array])
                my_prediction = int(regressor.predict(data)[0])
                lower = str(my_prediction-5)
                upper = str(my_prediction+5)
                tk.Label(display_frame, text='Predicted Score:\n '+lower+'-'+upper, fg='white', bg='#030055', font=('Helvetica',30, 'bold')).place(x=200, y=250)
           


        tk.Label(input_frame,
                text= "Select a Batting Team",
                fg = "white",
                font = "Helvetica", bg='#030055').place(x=50, y=30)
        options_list = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
                            'Mumbai Indians', 'Kings XI Punjab', 'Royal Challengers Bangalore',
                            'Delhi Daredevils', 'Sunrisers Hyderabad']	
        value_inside1 = tk.StringVar(input_frame)
        value_inside1.set("Choose a Batting Team")
        question_menu2 = tk.OptionMenu(input_frame, value_inside1, *options_list)
        question_menu2.configure(activebackground='#ff751a')
        question_menu2.place(x=500, y=30)

        tk.Label(input_frame,
                text= "Select a Bowling Team",
                fg = "white",
                font = "Helvetica", bg='#030055').place(x=50, y=90)
        value_inside2 = tk.StringVar(input_frame)
        value_inside2.set("Choose a Bowling Team")
        question_menu2 = tk.OptionMenu(input_frame, value_inside2, *options_list)
        question_menu2.configure(activebackground='#ff751a')
        question_menu2.place(x=500, y=90)

        l1=tk.Label(input_frame,text="Enter Overs Up", fg = "white", font="Helvetica", bg='#030055')
        l1.place(x=50, y=160) 
        t1=tk.Entry(input_frame, font=('Helvetica', 10))
        t1.place(x=500, y=160)

        l2=tk.Label(input_frame,text="Enter Runs Scored", fg = "white", font="Helvetica", bg='#030055')
        l2.place(x=50, y=230)
        t2=tk.Entry(input_frame, font=('Helvetica', 10))
        t2.place(x=500, y=230)

        l3=tk.Label(input_frame,text="Enter Wickets Fallen", fg = "white", font="Helvetica", bg='#030055')
        l3.place(x=50, y=300)
        t3=tk.Entry(input_frame, font=('Helvetica', 10))
        t3.place(x=500, y=300)

        l4=tk.Label(input_frame,text="Enter Runs Scored in Previous 5 Overs", fg = "white", font="Helvetica", bg='#030055')
        l4.place(x=50, y=370)
        t4=tk.Entry(input_frame, font=('Helvetica', 10))
        t4.place(x=500, y=370)

        l5=tk.Label(input_frame,text="Enter Wickets Fallen in Previous 5 Overs", fg = "white", font="Helvetica", bg='#030055')
        l5.place(x=50, y=440)
        t5=tk.Entry(input_frame, font=('Helvetica', 10))
        t5.place(x=500, y=440)

        def clear_text():
            value_inside1.set("Choose a Batting Team")
            value_inside2.set("Choose a Bowling Team")
            t1.delete(0,'end')
            t2.delete(0,'end')
            t3.delete(0,'end')
            t4.delete(0,'end')
            t5.delete(0,'end')

        b=tk.Button(input_frame, text="Submit", command = accept)
        b.configure(width=10, bg='#e6b800', activebackground='#ff751a')
        b.place(x=230, y=480)

        b1=tk.Button(input_frame, text="Clear Entries", command = clear_text)
        b1.configure(width=10, bg='#e6b800', activebackground='#ff751a')
        b1.place(x=350, y=480)


        button1 = tk.Button(input_frame, text="Analysis", bg='#e6b800', height=2, activebackground='#ff751a', 
                            command=lambda: controller.show_frame("Analysis"))
        button1.place(x=550, y=530)

        button2 = tk.Button(input_frame, text="Home Page", bg='#e6b800', height=2, activebackground='#ff751a', 
                            command=lambda: controller.show_frame("StartPage"))
        button2.place(x=20, y=530)


class Analysis(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#0349a5')
        self.controller = controller
        label = tk.Label(self, text="Analysis", background='#0349a5', font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label2 = tk.Label(self, text="Analyse your favourite IPL teams and batsmen over the years", background='#0349a5', font=('Helvetica',15,'italic'))
        label2.pack(side="top", fill="x", pady=3)

        main_frame = tk.Frame(self, bg='#030055')
        main_frame.pack(side='left', fill='both', expand='true')

        batter_frame = tk.Frame(self, bg='#030055')
        batter_frame.pack(padx=10, side='right', fill='both', expand='true')

    
        
        def show():

            def total_matches():
                sns.countplot(match_data['Season'])
                plt.xticks(rotation = 30, fontsize = 10)
                plt.yticks(fontsize = 10)
                plt.xlabel(xlabel='Season', fontsize = 10)
                plt.ylabel(ylabel='No. of matches', fontsize =10)
                plt.title('Total matches played in a season from 2008-2020', fontsize = 20, fontweight = 'bold')
                plt.show()
            
            def total_runs():
                season = season_data.groupby(['Season'])['total_runs'].sum().reset_index()
                p = season.set_index('Season')
                ax = plt.axes()
                ax.set(facecolor = 'black')
                sns.lineplot(data = p, palette = 'magma')
                plt.title('Total runs scored each year by all the teams', fontsize = 15, fontweight = 'bold')
                plt.show()
            
            def toss_decision():
                ax = plt.axes()
                ax.set(facecolor = 'grey')
                sns.countplot(x = 'Season', hue = 'toss_decision', data = match_data, palette = 'magma')
                plt.xticks(rotation = 40, fontsize = 10)
                plt.yticks(fontsize = 10)
                plt.xlabel('Season', fontsize = 15)
                plt.ylabel('Count', fontsize = 15)
                plt.title('Toss decisions by  teams from 2008-2020', fontsize = 20, fontweight = 'bold')
                plt.show()
            
            def most_runs():
                runs = ball_data.groupby(['batsman'])['batsman_runs'].sum().reset_index()
                runs.columns = ['Batsman', 'runs']
                y = runs.sort_values(by = 'runs', ascending = False).head(10).reset_index().drop('index', axis = 1)

                ax = plt.axes()
                ax.set(facecolor = 'grey')
                sns.barplot(x=y['Batsman'], y=y['runs'], palette = 'rocket', saturation = 1)
                plt.xticks(rotation = 75, fontsize = 8)
                plt.yticks(fontsize = 10)
                plt.xlabel('\nPlayer', fontsize = 10)
                plt.ylabel('Runs scored', fontsize = 10)
                plt.title('Top Run scorers of IPL from 2008-2020', fontsize = 15, fontweight = 'bold')
                plt.show()
            
            def m_o_m():
                ax = plt.axes()
                ax.set(facecolor = 'black')
                match_data.player_of_match.value_counts()[:10].plot(kind = 'bar')
                plt.xticks(rotation = 70)
                plt.xlabel('Players')
                plt.ylabel('No. of MOM awards')
                plt.title('Top Man Of The Match awards from 2008-2020', fontsize = 15, fontweight = 'bold')
                plt.show()

            if clicked.get() == options[0]:
                total_matches()
            elif clicked.get() == options[1]:
                total_runs() 
            elif clicked.get() == options[2]:
                toss_decision()
            elif clicked.get() == options[3]:
                most_runs()
            elif clicked.get() == options[4]:
                m_o_m()

        
        options = ['Total Matches played in a season','Total Runs scored in a season','Toss Decisions each year', 'Top 10 run scorers of IPL', 'Most Man of the match winners']
        clicked = StringVar()
        clicked.set('Select an option')
        general_analysis_label = tk.Label(main_frame, text='GENERAL ANALYSIS', font=('Helvetica', 20), background='#030055', foreground='white').pack(pady=5)
        dropdown = tk.OptionMenu(main_frame, clicked, *options)
        dropdown.configure(activebackground='#ff751a')
        dropdown.pack(pady=10)
        display = tk.Button(main_frame, text='Display', command=show)
        display.configure(border=2, fg='black', bg='#e6b800', activebackground='#ff751a', repeatdelay=10)
        display.pack(pady=7)

        tk.Label(main_frame, text='', bg='#0349a5', height=1).pack(fill='x')


        batter_heading = tk.Label(batter_frame, bg='#030055')
        batter_detail = tk.Label(batter_frame, bg='#030055')
        dismissal_button = tk.Button(batter_frame, bg='#030055', relief='flat')

        batter_heading.pack()
        batter_detail.pack()
        dismissal_button.pack()

        def check(e):
            typed = player_entry.get()

            if typed == '':
                data = list_batters
            else:
                data = []
                for item in list_batters:
                    if typed.lower() in item.lower():
                        data.append(item)
            update(data)
        
        def fillout(e):
            player_entry.delete(0, tk.END)

            #Add clicked item to EntryBox
            player_entry.insert(0, player_listbox.get(ANCHOR))

        def update(list_batters1):
            player_listbox.delete(0, tk.END)

            #Add players to listbox
            for batter in list_batters1:
                player_listbox.insert(tk.END, batter)
        
        def batter():
            
            nonlocal batter_detail, batter_heading, dismissal_button

            batter_heading.destroy()
            batter_detail.destroy()
            dismissal_button.destroy()
            
            player = (ball_data['batsman'] == player_entry.get())
            df_player = ball_data[player]

            def dismissal():
                df_player['dismissal_kind'].value_counts().plot.pie(autopct = '%1.1f%%', shadow = True, radius = 1.2, rotatelabels = False)
                plt.title('Dismissal Kind of '+player_entry.get()+' in his entire IPL career', fontweight = 'bold', fontsize = 15)
                plt.show()

            def count(df_player, runs):
                return len(df_player[df_player['batsman_runs']== runs])*runs
            
            ones = count(df_player,1)
            twos = count(df_player,2)
            threes = count(df_player,3)
            fours = count(df_player,4)
            sixes = count(df_player,6)
            total = ones+twos+threes+fours+sixes


            batter_heading = tk.Label(batter_frame, text='IPL career stats of '+str(player_entry.get()), bg='#030055', fg='white', font=('Helvetica', 20, 'bold'))
            batter_heading.pack(pady=100)
            batter_detail = tk.Label(batter_frame, text='Runs scored from 1s:   '+str(ones)+'\nRuns scored from 2s:   '+str(twos)+'\nRuns scored from 3s:   '+str(threes)+'\nRuns scored from 4s:   '+str(fours)+'\nRuns scored from 6s:   '+str(sixes)+'\n\n\nTotal runs scored:   '+str(total), bg='#030055', fg='white', font=('Helvetica',15))
            batter_detail.pack(pady=0)

            dismissal_button = tk.Button(batter_frame, text='Dismissal kind', command=dismissal)
            dismissal_button.configure(bg='#e6b800', activebackground='#ff751a', height=2)
            dismissal_button.pack(pady=16)
            

        player_label = tk.Label(main_frame, text='PLAYER ANALYSIS', bg='#030055', font=('Helvetica', 20), fg='white').pack(pady=3)
        
        #Player entry
        player_entry = tk.Entry(main_frame, font=('Lucida Sans Unicode', 14), width=22)
        player_entry.focus_set()
        player_entry.pack(pady=5)
        my_frame = tk.Frame(main_frame )
        batter_scrollbar = tk.Scrollbar(my_frame, orient = 'vertical')
        player_listbox = tk.Listbox(my_frame, height=12, width=27, bg='#0349a5', fg='white', font=('Lucida Sans Unicode',12), yscrollcommand=batter_scrollbar.set)
        player_listbox.pack(side='left',pady=5)
        batter_scrollbar.configure(command=player_listbox.yview)
        my_frame.pack()
        batter_scrollbar.pack(side='right',fill='y')
        

        update(list_batters)

        player_listbox.bind('<<ListboxSelect>>', fillout)

        player_entry.bind('<KeyRelease>', check)

        player_button = tk.Button(main_frame, text='Select', command=batter)
        player_button.configure(bg='#e6b800', activebackground='#ff751a', width=15)
        player_button.pack(pady=8)

        button_predictor = tk.Button(main_frame, text = 'Home Page', activebackground='#193366', command = lambda: controller.show_frame('StartPage'))
        button_predictor.configure(bg='#e6b800',  activebackground='#ff751a', height=2)
        button_predictor.pack(side='left', pady=8, padx=8)
        button_back = tk.Button(main_frame, text="Predictor", activebackground='#193366',
                           command=lambda: controller.show_frame("Predictor"))
        button_back.configure(bg='#e6b800', activebackground='#ff751a', height=2)
        button_back.pack(side='right', pady=8, padx=11)
    


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
