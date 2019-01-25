#Highlight - Overlay Application for Notes
from tkinter import *
import time, os

class App:
	#3 tools: Highlighter, Line, Rectangle
	tool = 'Highlighter'
	color = '#FF0'
	wdth = 18
	b1 = 'up'
	x_pos, y_pos = None, None
	x1_pt, y1_pt, x2_pt, y2_pt = None, None, None, None

	#constructor
	def __init__(self, root):
		root.title('Highlight')
		self.createWidgets()

	def createWidgets(self):
		mainMenu = Frame(root, bg='#CCC')

		Label(mainMenu, text='Color: ').pack(side='left')
		setColorY = Button(mainMenu, width=5, command=self.setColorY, borderwidth=0, bg='#FF0').pack(side='left')
		setColorR = Button(mainMenu, width=5, command=self.setColorR, borderwidth=0, bg='#F00').pack(side='left')
		setColorG = Button(mainMenu, width=5, command=self.setColorG, borderwidth=0, bg='#0F0').pack(side='left')

		Label(mainMenu, text=' ', padx=root.winfo_screenwidth()/6).pack(side='left')

		Label(mainMenu, text='Tool: ').pack(side='left')
		setToolHL = Button(mainMenu, text='Highlighter', command=self.setToolHL, bg='#000', fg='#fff', borderwidth=0, relief='groove').pack(side='left')
		setToolLine = Button(mainMenu, text='Line', command=self.setToolL, bg='#000', fg='#fff', borderwidth=0, relief='raised').pack(side='left')
		setToolLine = Button(mainMenu, text='Rectangle', command=self.setToolR, bg='#000', fg='#fff', borderwidth=0, relief='raised').pack(side='left')

		cap = Button(mainMenu, text='Capture', command=self.capture, bg='#000', fg='#fff', borderwidth=0, relief='raised').pack(side='right')

		mainMenu.pack(fill='x')

		drawing_area = Canvas(root, bg='#888', width=root.winfo_screenwidth(), height=root.winfo_screenheight())
		drawing_area.pack()
		drawing_area.bind("<Motion>", self.motion)
		drawing_area.bind("<ButtonPress-1>", self.b1down)
		drawing_area.bind("<ButtonRelease-1>", self.b1up)

	#Color setters
	def setColorY(self):
		self.color = '#FF0'
	def setColorR(self):
		self.color = '#F00'
	def setColorG(self):
		self.color = '#0F0'

	#Tool setters
	def setToolHL(self):
		self.tool = 'Highlighter'
	def setToolL(self):
		self.tool = 'Line'
	def setToolR(self):
		self.tool = 'Rectangle'

	#capture screenshot
	def capture(self):
		os.system('import -window root shot1.png') #linux only

	#LMB pressed
	def b1down(self, event=None):
		self.b1 = 'down'
		self.x1_pt, self.y1_pt = event.x, event.y

	#LMB released
	def b1up(self, event=None):
		self.b1 = 'up'
		self.x_pos, self.y_pos = None, None
		self.x2_pt, self.y2_pt = event.x, event.y
		if (self.tool == 'Line'):
			self.line(event)
		elif (self.tool == 'Rectangle'):
			self.rectangle(event)

	#track mouse movement
	def motion(self, event=None):
		if (self.b1 == 'down'):
			if (self.tool == 'Highlighter'):
				self.highlight(event)

	def highlight(self, event):
		if(self.x_pos is not None and self.y_pos is not None):
			#multiple for smoothness
			event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth=TRUE, fill=self.color, width=self.wdth)
			time.sleep(0.015)
			event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth=TRUE, fill=self.color, width=self.wdth)
			time.sleep(0.015)
			event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, fill=self.color, width=self.wdth)
		self.x_pos = event.x
		self.y_pos = event.y

	def line(self, event):
		if (None not in (self.x1_pt, self.y1_pt, self.x2_pt, self.y2_pt)):
			event.widget.create_line(self.x1_pt, self.y1_pt, self.x2_pt, self.y2_pt, smooth=TRUE, fill=self.color, width=self.wdth)

	def rectangle(self, event):
		if(None not in (self.x1_pt, self.y1_pt, self.x2_pt, self.y2_pt)):
			event.widget.create_rectangle(self.x1_pt, self.y1_pt, self.x2_pt, self.y2_pt, outline=self.color, fill=self.color, width=self.wdth)

#main
if(__name__ == '__main__'):
	root = Tk()
	highlight = App(root)
	#root.overrideredirect(True) #fullscreen
	#keeps always as topmost window
	root.wm_attributes('-topmost', True)
	#root.wm_attributes('-disabled', True)
	#root.wm_attributes('-transparent', True)
	root.wait_visibility(root)
	root.wm_attributes('-alpha',0.4)
	root.mainloop()
