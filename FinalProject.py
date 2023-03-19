import sys
import matplotlib.pyplot as plt
import numpy as py
import pandas as pd

#------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------------------------------
try:
	  from Tkinter import *
except ImportError:
	   from tkinter import *

try:
	  import ttk
	  py3 = False
except ImportError:
	   import tkinter.ttk as ttk
	   py3 = True


#-------------------------------------------------------------------------------------------------------------------------
import player_analysis_support
def player_ana():
	def vp_start_gui():
	    '''Starting point when module is the main routine.'''
	    global val, w, root
	    root = Tk()
	    top = New_Toplevel (root)
	    player_analysis_support.init(root, top)
	    root.mainloop()

	w = None
	def create_New_Toplevel(root, *args, **kwargs):
	    '''Starting point when module is imported by another program.'''
	    global w, w_win, rt
	    rt = root
	    w = Toplevel (root)
	    top = New_Toplevel (w)
	    player_analysis_support.init(w, top, *args, **kwargs)
	    return (w, top)

	def destroy_New_Toplevel():
	    global w
	    w.destroy()
	    w = None


	class New_Toplevel:
	    def __init__(self, top=None):
		'''This class configures and populates the toplevel window.
		   top is the toplevel containing window.'''
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85' 
		_ana2color = '#d9d9d9' # X11 color: 'gray85' 

		top.geometry("600x450+650+150")
		top.title("New Toplevel")



		self.Message1 = Message(top)
		self.Message1.place(relx=0.2, rely=0.156, relheight=0.078
		        , relwidth=0.128)
		self.Message1.configure(text='''Player 1''')
		self.Message1.configure(width=77)

		self.Message2 = Message(top)
		self.Message2.place(relx=0.2, rely=0.289, relheight=0.078
		        , relwidth=0.128)
		self.Message2.configure(text='''Player 2''')
		self.Message2.configure(width=77)

		self.Entry1 = Entry(top)
		self.Entry1.place(relx=0.367, rely=0.156,height=33, relwidth=0.277)
		self.Entry1.configure(background="white")
		self.Entry1.configure(font="TkFixedFont")
		self.Entry1.configure(width=166)

		self.Entry2 = Entry(top)
		self.Entry2.place(relx=0.367, rely=0.289,height=33, relwidth=0.277)
		self.Entry2.configure(background="white")
		self.Entry2.configure(font="TkFixedFont")
		self.Entry2.configure(width=166)

		p=pd.read_csv('CompleteDataset.csv')
		set = pd.DataFrame(p)
			
		def compare():

			x= set['Name']

			a=self.Entry1.get()
			b=self.Entry2.get()
			
			x= set['Name']
			y= set['Overall']

			z = []

			for i in range(len(x)):
				if x[i]==a:
					z.append(y[i])
					break

			for i in range(len(x)):
				if x[i]==b:
					z.append(y[i])
					break


			cmp_res = (a + " : " + str(z[0]) + "   " + b + " : " + str(z[1]))
			self.Label1 = Label(top)
			self.Label1.place(relx=0.10, rely=0.394, height=31, width=500)
			self.Label1.configure(text=cmp_res)
			self.Label1.configure(width=500)
			

			plt.bar([a,b],z,label="Comparison")
			plt.show()
	
			return


		self.Button1 = Button(top, command = compare)
		self.Button1.place(relx=0.717, rely=0.222, height=29, width=99)
		self.Button1.configure(activebackground="#d9d9d9")
		self.Button1.configure(text='''Compare''')
		self.Button1.configure(width=99)

		self.Message3 = Message(top)
		self.Message3.place(relx=0.3, rely=0.044, relheight=0.056, relwidth=0.27)

		self.Message3.configure(text='''Player Comparison''')
		self.Message3.configure(width=162)







	if __name__ == '__main__':
	    vp_start_gui()

	return

#player_ana()

#--------------------------------------------------------------------------------------------------------------------------


import international_analysis_support
def int_ana():
	
	def vp_start_gui():
	    '''Starting point when module is the main routine.'''
	    global val, w, root
	    root = Tk()
	    top = New_Toplevel (root)
	    international_analysis_support.init(root, top)
	    root.mainloop()

	w = None
	def create_New_Toplevel(root, *args, **kwargs):
	    '''Starting point when module is imported by another program.'''
	    global w, w_win, rt
	    rt = root
	    w = Toplevel (root)
	    top = New_Toplevel (w)
	    international_analysis_support.init(w, top, *args, **kwargs)
	    return (w, top)

	def destroy_New_Toplevel():
	    global w
	    w.destroy()
	    w = None


	class New_Toplevel:
	    def __init__(self, top=None):
		'''This class configures and populates the toplevel window.
		   top is the toplevel containing window.'''
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85' 
		_ana2color = '#d9d9d9' # X11 color: 'gray85' 

		top.geometry("600x450+650+150")
		top.title("New Toplevel")

		
	

		self.Label1 = Label(top)
		self.Label1.place(relx=0.317, rely=0.044, height=31, width=187)
		self.Label1.configure(text='''International Team Analysis''')
		self.Label1.configure(width=187)
		
		self.Label2 = Label(top)
		self.Label2.place(relx=0.117, rely=0.178, height=21, width=103)
		self.Label2.configure(text='''Home Team''')
		self.Label2.configure(width=103)

		self.Label3 = Label(top)
		self.Label3.place(relx=0.117, rely=0.267, height=21, width=103)
		self.Label3.configure(text='''Away Team''')
		self.Label3.configure(width=103)

		self.Entry1 = Entry(top)
		self.Entry1.place(relx=0.317, rely=0.156,height=33, relwidth=0.277)
		self.Entry1.configure(background="white")
		self.Entry1.configure(font="TkFixedFont")
		self.Entry1.configure(width=166)
		

		self.Entry2 = Entry(top)
		self.Entry2.place(relx=0.317, rely=0.244,height=33, relwidth=0.277)
		self.Entry2.configure(background="white")
		self.Entry2.configure(font="TkFixedFont")
		self.Entry2.configure(width=166)
		
		
		def compute():
			p=pd.read_csv('results.csv')
			result = pd.DataFrame(p)
			#opt = result.distinct(['home_team'])

			del result['date']
			del result['tournament']
			del result['city']
			del result['country']

			

			total_matches_home = 0
			total_matches_away = 0
			total_matches = 0

			h = result['home_team']
			a = result['away_team']
			home = self.Entry1.get()
			away = self.Entry2.get()
			print home,away
			for i in range(len(result)):
				if home == h[i] and away == a[i]:
					total_matches_home = total_matches_home + 1	
				elif home == a[i] and away == h[i]:
					total_matches_away = total_matches_away + 1


			for i in range(len(result)):
				if (home == h[i] and away == a[i]) or (home == a[i] and away == h[i]):
					total_matches = total_matches + 1	
				
			home_goals = 0
			away_goals = 0

			res_string_home = []
			res_string_away = []
			res_string = []
			for row in result.itertuples():
				if home == row[1] and away == row[2]:
					home_goals = home_goals + row[3]
					away_goals = away_goals + row[4]

			for row in result.itertuples():
				if (home == row[1] and away == row[2]):
					if row[3] > row[4]:
						res_string_home.append(home)
						res_string.append(home)
					elif row[3] < row[4]:
						res_string_home.append(away)
						res_string.append(away)
					else:
					 	res_string_home.append("Draw")
						res_string.append("Draw")

				elif (home == row[2] and away == row[1]):  
					if row[3] > row[4]:
						res_string_away.append(away)
						res_string.append(away)
					elif row[3] < row[4]:
						res_string_away.append(home)
						res_string.append(home)
					else:
					 	res_string_away.append("Draw")
						res_string.append("Draw")

			if total_matches_home==0:
					self.Labelx = Label(top)
					self.Labelx.place(relx=0.117, rely=0.444, height=31, width=500)
					self.Labelx.configure(text='Teams Have not played yet')
					self.Labelx.configure(width=500)
					return
	



			w = res_string_home.count(home)
			l = res_string_home.count(away)
			d = res_string_home.count("Draw")

			win_per = float((w*1.0000)/((w+l+d)*1.0000))*100
			loss_per = float((l*1.0000)/((w+l+d)*1.0000))*100
			draw_per = float((d*1.0000)/((w+l+d)*1.0000))*100
			
			total = ("Total Matches: " + str(total_matches) + " " + home +" : "+ str(res_string.count(home)) +" "+ away +" : " +str(res_string.count(away)) +" Draw : " + str(res_string.count("Draw")))
				
			
			self.Labelx = Label(top)
			self.Labelx.place(relx=0.117, rely=0.444, height=31, width=500)
			self.Labelx.configure(text=total)
			self.Labelx.configure(width=500)
	

			total_home = ("Total Matches in "+ home +" : " + str(total_matches_home) + " " + home +" : "+ str(res_string_home.count(home)) +" "+ away +" : "+ str(res_string_home.count(away)) +" Draw : " + str(res_string_home.count("Draw")))
				
			
			self.Labelh = Label(top)
			self.Labelh.place(relx=0.117, rely=0.544, height=31, width=500)
			self.Labelh.configure(text=total_home)
			self.Labelh.configure(width=500)


			self.Labelw = Label(top)
			self.Labelw.place(relx=0.117, rely=0.644, height=31, width=500)
			self.Labelw.configure(text='''Match Probability''')
			self.Labelw.configure(width=500)

			home_prob = ( home + " : " + str(win_per) + " %")
	
			self.Labelhp = Label(top)
			self.Labelhp.place(relx=0.117, rely=0.744, height=31, width=500)
			self.Labelhp.configure(text=home_prob)
			self.Labelhp.configure(width=500)

			away_prob = ( away + " : " + str(loss_per) + " %")

			self.Labelap = Label(top)
			self.Labelap.place(relx=0.117, rely=0.844, height=31, width=500)
			self.Labelap.configure(text=away_prob)
			self.Labelap.configure(width=500)

			draw_prob = ( "Draw" + " : " + str(draw_per) + " %")

			self.Labeldp = Label(top)
			self.Labeldp.place(relx=0.117, rely=0.944, height=31, width=500)
			self.Labeldp.configure(text=draw_prob)
			self.Labeldp.configure(width=500)



			plt.bar([home,away,"Draw"],[win_per,loss_per,draw_per],label="Match Prediction")
			plt.show()
			
			return
	
		self.Button1 = Button(top, command = compute)
		self.Button1.place(relx=0.683, rely=0.2, height=29, width=77)
		self.Button1.configure(activebackground="#d9d9d9")
		self.Button1.configure(text='''Next''')
		self.Button1.configure(width=77)






	if __name__ == '__main__':
	    vp_start_gui()

	return

#int_ana()
#-------------------------------------------------------------------------------------------------------------------------------------

import stats_support
def player_stats():


#import stats_support

	def vp_start_gui():
	    '''Starting point when module is the main routine.'''
	    global val, w, root
	    root = Tk()
	    top = New_Toplevel (root)
	    stats_support.init(root, top)
	    root.mainloop()

	w = None
	def create_New_Toplevel(root, *args, **kwargs):
	    '''Starting point when module is imported by another program.'''
	    global w, w_win, rt
	    rt = root
	    w = Toplevel (root)
	    top = New_Toplevel (w)
	    stats_support.init(w, top, *args, **kwargs)
	    return (w, top)

	def destroy_New_Toplevel():
	    global w
	    w.destroy()
	    w = None


	class New_Toplevel:
	    def __init__(self, top=None):
		'''This class configures and populates the toplevel window.
		   top is the toplevel containing window.'''
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85' 
		_ana2color = '#d9d9d9' # X11 color: 'gray85' 

		top.geometry("600x450+650+150")
		top.title("New Toplevel")

		def player():
			p=pd.read_csv('CompleteDataset.csv')
			set = pd.DataFrame(p)
			p_name = self.Entry1.get()
			t_content = []
			print p_name
			for row in set.itertuples():
				if p_name == row[2]:
			
					self.text = Text(top)
					self.text.place(relx=0.25, rely=0.522)
					self.text.configure(font="TkFixedFont", width = 40, height = 10)
					self.text.insert(INSERT,''' Name: ''' + row[2] + '''\n''' +
								''' Nationality: ''' + str(row[4]) + '''\n''' +
								''' Age: ''' + str(row[3]) + '''\n''' +
								''' Club: ''' + row[7] + '''\n''' +
								''' Overall: ''' + str(row[5]) + '''\n''' +
								''' Potential: ''' + str(row[6]) + '''\n''' +
								''' Value: ''' + row[8] + '''\n''' +
								''' Wage: ''' + row[9] + '''\n'''
							)
					
			return


		self.Entry1 = Entry(top)
		self.Entry1.place(relx=0.35, rely=0.222,height=23, relwidth=0.277)
		self.Entry1.configure(background="white")
		self.Entry1.configure(font="TkFixedFont")

		self.Button1 = Button(top,command = player)
		self.Button1.place(relx=0.383, rely=0.311, height=29, width=129)
		self.Button1.configure(activebackground="#d9d9d9")
		self.Button1.configure(text='''Next''')
		self.Button1.configure(width=129)

		self.Label1 = Label(top)
		self.Label1.place(relx=0.35, rely=0.044, height=21, width=169)
		self.Label1.configure(text='''Player Statistics''')
		self.Label1.configure(width=169)

		self.Label2 = Label(top)
		self.Label2.place(relx=0.35, rely=0.133, height=21, width=169)
		self.Label2.configure(text='''Enter Player Name''')
		self.Label2.configure(width=169)

#		self.Labelframe1 = LabelFrame(top)
#		self.Labelframe1.place(relx=0.067, rely=0.4, relheight=0.567
#		        , relwidth=0.9)
#		self.Labelframe1.configure(relief=GROOVE)
#		self.Labelframe1.configure(text='''Statistics''')
#		self.Labelframe1.configure(width=540)






	if __name__ == '__main__':
	    vp_start_gui()


	return

def team_stats():


	p=pd.read_csv('results.csv')
	result = pd.DataFrame(p)
	del result['date']
	del result['tournament']
	del result['city']
	del result['country']


	def vp_start_gui():
	    '''Starting point when module is the main routine.'''
	    global val, w, root
	    root = Tk()
	    top = New_Toplevel (root)
	    stats_support.init(root, top)
	    root.mainloop()

	w = None
	def create_New_Toplevel(root, *args, **kwargs):
	    '''Starting point when module is imported by another program.'''
	    global w, w_win, rt
	    rt = root
	    w = Toplevel (root)
	    top = New_Toplevel (w)
	    stats_support.init(w, top, *args, **kwargs)
	    return (w, top)

	def destroy_New_Toplevel():
	    global w
	    w.destroy()
	    w = None


	class New_Toplevel:
	    def __init__(self, top=None):
		'''This class configures and populates the toplevel window.
		   top is the toplevel containing window.'''
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85' 
		_ana2color = '#d9d9d9' # X11 color: 'gray85' 

		top.geometry("600x450+650+150")
		top.title("New Toplevel")

		def team():
			tot_matches = 0
			home_matches = 0
			home_win = 0
			home_loss = 0
			home_draw =0
			away_matches = 0
			away_win = 0
			away_loss = 0
			away_draw =0
	
			p_name = self.Entry1.get()
			for row in result.itertuples():
				if(p_name == row[1]):
					home_matches = home_matches + 1
					if(row[3]>row[4]):
						home_win = home_win + 1
					elif(row[4]>row[3]):
						home_loss = home_loss + 1
					else:
						home_draw = home_draw + 1

				if(p_name == row[2]):
					away_matches = away_matches + 1
					if(row[4]>row[3]):
						away_win = away_win + 1
					elif(row[3]>row[4]):
						away_loss = away_loss + 1
					else:
						away_draw = away_draw + 1

			tot_matches = home_matches + away_matches
			self.text = Text(top)
			self.text.place(relx=0.25, rely=0.4)
			self.text.configure(font="TkFixedFont", width = 40, height = 15)
			self.text.insert(INSERT,''' Team: ''' + p_name + '''\n''' +
							''' Total Matches: ''' + str(tot_matches) + '''\n''' +
							''' 	Win: ''' + str((home_win+away_win)) + '''\n''' +
							''' 	Loss: ''' + str((home_loss+away_loss)) + '''\n''' +
							''' 	Draw: ''' + str((home_draw+away_draw)) + '''\n\n''' +
							''' Home Matches: ''' + str(home_matches) + '''\n''' +
							''' 	Win: ''' + str(home_win) + '''\n''' +
							''' 	Loss: ''' + str(home_loss) + '''\n''' +
							''' 	Draw: ''' + str(home_draw) + '''\n\n''' +
							''' Away Matches: ''' + str(away_matches) + '''\n''' +
							'''	 Win: ''' + str(away_win) + '''\n''' +
							'''  	 Loss: ''' + str(away_loss) + '''\n''' +
							'''	 Draw: ''' + str(away_draw) + '''\n''' 
							
							)
			return


		self.Entry1 = Entry(top)
		self.Entry1.place(relx=0.35, rely=0.222,height=23, relwidth=0.277)
		self.Entry1.configure(background="white")
		self.Entry1.configure(font="TkFixedFont")

		self.Button1 = Button(top,command = team)
		self.Button1.place(relx=0.383, rely=0.311, height=29, width=129)
		self.Button1.configure(activebackground="#d9d9d9")
		self.Button1.configure(text='''Next''')
		self.Button1.configure(width=129)

		self.Label1 = Label(top)
		self.Label1.place(relx=0.35, rely=0.044, height=21, width=169)
		self.Label1.configure(text='''Team Statistics''')
		self.Label1.configure(width=169)

		self.Label2 = Label(top)
		self.Label2.place(relx=0.35, rely=0.133, height=21, width=169)
		self.Label2.configure(text='''Enter Team Name''')
		self.Label2.configure(width=169)

#		self.Labelframe1 = LabelFrame(top)
#		self.Labelframe1.place(relx=0.067, rely=0.4, relheight=0.567
#		        , relwidth=0.9)
#		self.Labelframe1.configure(relief=GROOVE)
#		self.Labelframe1.configure(text='''Statistics''')
#		self.Labelframe1.configure(width=540)






	if __name__ == '__main__':
	    vp_start_gui()


	return



import unknown_support
def main():


	def vp_start_gui():
	    '''Starting point when module is the main routine.'''
	    global val, w, root
	    root = Tk()
	    top = New_Toplevel (root)
	    unknown_support.init(root, top)
	    root.mainloop()

	w = None
	def create_New_Toplevel(root, *args, **kwargs):
	    '''Starting point when module is imported by another program.'''
	    global w, w_win, rt
	    rt = root
	    w = Toplevel (root)
	    top = New_Toplevel (w)
	    unknown_support.init(w, top, *args, **kwargs)
	    return (w, top)

	def destroy_New_Toplevel():
	    global w
	    w.destroy()
	    w = None


	class New_Toplevel:
	    def __init__(self, top=None):
		'''This class configures and populates the toplevel window.
		   top is the toplevel containing window.'''
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85' 
		_ana2color = '#d9d9d9' # X11 color: 'gray85' 

		top.geometry("600x450+650+150")
		top.title("New Toplevel")
		top.configure(highlightcolor="black")



		self.Message1 = Message(top)
		self.Message1.place(relx=0.333, rely=0.2, relheight=0.089, relwidth=0.32)

		self.Message1.configure(text='''FIFA Analysis Application''')
		self.Message1.configure(width=192)

		self.Button1 = Button(top,command = player_ana)
		self.Button1.place(relx=0.367, rely=0.4, height=29, width=159)
		self.Button1.configure(activebackground="#d9d9d9")
		self.Button1.configure(text='''Player Analysis''')

		self.Button2 = Button(top, command = int_ana)
		self.Button2.place(relx=0.367, rely=0.5, height=29, width=159)
		self.Button2.configure(activebackground="#d9d9d9")
		self.Button2.configure(text='''Team Analysis''')

		self.Button3 = Button(top, command = player_stats)
		self.Button3.place(relx=0.367, rely=0.6, height=29, width=159)
		self.Button3.configure(activebackground="#d9d9d9")
		self.Button3.configure(text='''Player Statistics''')

		self.Button4 = Button(top, command = team_stats)
		self.Button4.place(relx=0.367, rely=0.7, height=29, width=159)
		self.Button4.configure(activebackground="#d9d9d9")
		self.Button4.configure(text='''Team Statistics''')





	if __name__ == '__main__':
	    vp_start_gui()


	return

main()
