import tkinter as tk                
from tkinter import OptionMenu, PhotoImage, StringVar, font  as tkfont
from tkinter.constants import ANCHOR 
from PIL import Image, ImageTk
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


match_data = pd.read_csv("F:/CS Project 21-22/IPL Dataset/Match dataset.csv")
ball_data = pd.read_csv("F:/CS Project 21-22/IPL Dataset/Ball_by_ball.csv")

list_batters = ball_data['batsman'].unique()

match_data['Season'] = pd.DatetimeIndex(match_data['date']).year

match_perseason = match_data.groupby(['Season'])['id'].count().reset_index().rename(columns={'id':'matches'})
season_data = match_data[['id','Season']].merge(ball_data, left_on = 'id', right_on = 'id', how = 'left').drop('id',axis = 1)
season_data.head()



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=20, weight="bold")

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
        tk.Frame.__init__(self, parent, bg='#66d1c4')
        self.controller = controller

    
        label = tk.Label(self, text="Welcome to CAP", font=controller.title_font, bg='#66d1c4')
        label.pack(side="top", fill="x", pady=10)

        self.controller.title('CAP - Cricket Analysis and Predictor')


        button1 = tk.Button(self, text="Predictor", relief='raised', borderwidth=3, width=14, activebackground='#1870df',
                             command=lambda: controller.show_frame("Predictor"))
        button2 = tk.Button(self, text="Analysis", relief='raised', borderwidth=3, width=14, activebackground='#1870df',
                            command=lambda: controller.show_frame("Analysis"))
        button1.pack(padx=70, pady= 7, side='left')
        button2.pack(side='right',padx=50, pady=7)
        




class Predictor(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#66d1c4')
        self.controller = controller
        label = tk.Label(self, text="Predictor Page", bg='#66d1c4', font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        

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

            temp_array = temp_array + [overs, runs, wickets, runsprev5, wicketsprev5]
            #print(temp_array)

            filename = 'first-innings-score-lr-model.pkl'
            regressor = pickle.load(open(filename, 'rb'))

            data = np.array([temp_array])
            my_prediction = int(regressor.predict(data)[0])
            lower = str(my_prediction-5)
            upper = str(my_prediction+5)
            tk.Label(self, text='Predicted Score: '+lower+'-'+upper, bg='#66d1c4', font=('Helvetica',20, 'bold')).pack()
            #print(my_prediction-5,'-',my_prediction+5)


        

        tk.Label(self,
                text= "Select a Batting Team",
                fg = "black",
                font = "Helvetica", bg='#66d1c4').pack()
        options_list = ['Kolkata Knight Riders', 'Chennai Super Kings', 'Rajasthan Royals',
                            'Mumbai Indians', 'Kings XI Punjab', 'Royal Challengers Bangalore',
                            'Delhi Daredevils', 'Sunrisers Hyderabad']	
        value_inside1 = tk.StringVar(self)
        value_inside1.set("Select an Option")
        question_menu2 = tk.OptionMenu(self, value_inside1, *options_list)
        question_menu2.pack(pady=4)

        tk.Label(self,
                text= "Select a Bowling Team",
                fg = "black",
                font = "Helvetica", bg='#66d1c4').pack(pady=4)
        value_inside2 = tk.StringVar(self)
        value_inside2.set("Select an Option")
        question_menu2 = tk.OptionMenu(self, value_inside2, *options_list)
        question_menu2.pack()

        l1=tk.Label(self,text="Enter Overs Up", font="Helvetica", bg='#66d1c4')
        l1.pack(pady=4) 
        t1=tk.Entry(self)
        t1.pack()

        l2=tk.Label(self,text="Enter Runs Scored", font="Helvetica", bg='#66d1c4')
        l2.pack(pady=4)
        t2=tk.Entry(self)
        t2.pack()

        l3=tk.Label(self,text="Enter Wickets Fallen", font="Helvetica", bg='#66d1c4')
        l3.pack(pady=4)
        t3=tk.Entry(self)
        t3.pack()

        l4=tk.Label(self,text="Enter Runs Scored in Previous 5 Overs", font="Helvetica", bg='#66d1c4')
        l4.pack(pady=4)
        t4=tk.Entry(self)
        t4.pack()

        l5=tk.Label(self,text="Enter Wickets Fallen in Previous 5 Overs", font="Helvetica", bg='#66d1c4')
        l5.pack(pady=4)
        t5=tk.Entry(self)
        t5.pack()


        b=tk.Button(self, text="Submit", command = accept)
        b.pack(pady=10)

        button = tk.Button(self, text="Home Page", activebackground='#1870df',
                            command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=20)


class Analysis(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#66d1c4')
        self.controller = controller
        label = tk.Label(self, text="Analysis Page", background='#66d1c4', font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
    
        
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

        
        options = ['Total Macthes played in a season','Total Runs scored in a season','Toss Decisions each year', 'Top 10 run scorers of IPL', 'Most Man of the match winners']
        clicked = StringVar()
        clicked.set('Select an option')
        general_analysis_label = tk.Label(self, text='General Analysis', font=('Helvetica', 15), background='#66d1c4', foreground='blue').pack()
        dropdown = tk.OptionMenu(self, clicked, *options).pack(pady=10)
        display = tk.Button(self, text='Display', command=show).pack(pady=5)


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
            
            player = (ball_data['batsman'] == player_entry.get())
            df_player = ball_data[player]
            df_player['dismissal_kind'].value_counts().plot.pie(autopct = '%1.1f%%', shadow = True, radius = 1.2, rotatelabels = False)
            plt.title('Dismissal Kind of '+player_entry.get()+' in his entire IPL career', fontweight = 'bold', fontsize = 15)
            plt.show()

            def count(df_player, runs):
                return len(df_player[df_player['batsman_runs']== runs])*runs
            
            print('Runs scored from 1s: ',count(df_player,1))
            print('Runs scored from 2s: ',count(df_player,2))
            print('Runs scored from 3s: ',count(df_player,3))
            print('Runs scored from 4s: ',count(df_player,4))
            print('Runs scored from 6s: ',count(df_player,6))

        

        player_label = tk.Label(self, text='Player analysis', bg='#66d1c4', font=('Helvetica', 15), fg='Blue').pack(pady=10)
        
        #Player entry

        player_entry = tk.Entry(self, font=('Comic Sans', 10))
        player_entry.focus_set()
        player_entry.pack(pady=5)
        my_frame = tk.Frame(self )
        batter_scrollbar = tk.Scrollbar(my_frame, orient = 'vertical')
        player_listbox = tk.Listbox(my_frame, width=25, yscrollcommand=batter_scrollbar.set)
        player_listbox.pack(side='left',pady=3)
        batter_scrollbar.configure(command=player_listbox.yview)
        my_frame.pack()
        batter_scrollbar.pack(side='right',fill='y')
        

        update(list_batters)

        player_listbox.bind('<<ListboxSelect>>', fillout)

        player_entry.bind('<KeyRelease>', check)

        player_button = tk.Button(self, text='Select', command=batter).pack(pady=8)



        button_predictor = tk.Button(self, text = 'Predictor', activebackground='#1870df', command = lambda: controller.show_frame('Predictor'))
        button_predictor.place(x=300, y=490)
        button_back = tk.Button(self, text="Home Page", activebackground='#1870df',
                           command=lambda: controller.show_frame("StartPage"))
        button_back.place(x=100, y=490)
    



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()