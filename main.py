import wx, sqlite3
from backend import *
import wx.lib.agw.shapedbutton as SB 	# Shaped Button (Circular)
import wx.lib.mixins.inspection			# DEBUGGER FOR WIDGETS

class MainWindow(wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'Dummy Here', size=(650,480))
		self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)					# Bind the close event, if they hit the X
		self.dataValues = dataValues()
		self.MakeMenuBar()
		self.MakeSplitter()
		self.MakeItemTree(self.panelSelection)
		self.MakeSizer()

		self.SetSizeWH(900,400)

	def OnCloseWindow(self,event):
		self.Destroy()

	def CreateImageButton(self, parent, function, filename="Defenseup", size=(100,100), pos=(0,0)):
		path = "assets\\{}.png".format(filename)
		bmp = wx.Image(path, wx.BITMAP_TYPE_PNG).Scale(size[0],size[1])
		bmp = bmp.ConvertToBitmap()
		button = SB.SBitmapButton(parent, -1, bmp, pos)
		button.SetButtonColour(wx.Colour(0,0,0,0))
		self.Bind(wx.EVT_BUTTON, function, button)
		return button

	def CreateImage(self, parent, filename, size=(100,100), pos=(50,50)):
		path = "assets\\{}.png".format(filename)
		img = wx.Image(path).Scale(size[0], size[1])
		

	def DoNothing(self):
		pass

	def MakeMenuBar(self):
		pass

	def MakeItemTree(self, panel):

		def querybulkSQL(table, searchterm):
			path = "assets\\data.db"
			with sqlite3.connect(path) as connection:
				c = connection.cursor()
				c.execute("SELECT name FROM "+table+" WHERE type = (?)", (searchterm,))
				return c.fetchall()

		self.tree = wx.TreeCtrl(panel, size=(198,360))
		self.branches = {"Weapons": None, "Hat": None, "Shirt": None, "Shoes": None}
		weaponSubbranches = ("Shooters", "Chargers", "Rollers", "Sloshers", "Splatings")
		self.root = self.tree.AddRoot("Gear")

		for itemtype in self.branches:
			if itemtype == "Weapon":
				pass
			else:
				self.branches[itemtype] = self.tree.AppendItem(self.root, itemtype)
				for item in querybulkSQL('armor', itemtype.lower()):
					self.tree.AppendItem(self.branches[itemtype], item[0])



	def MakeSizer(self):
		self.mainhbox = wx.BoxSizer(wx.HORIZONTAL)
		self.mainvbox = wx.BoxSizer(wx.VERTICAL)	# Seperates Icons and Status
		self.hbox1 = wx.BoxSizer(wx.HORIZONTAL)		# First Row (First Choices)
		self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)		# Second Row (Second Choices)
		self.hbox3 = wx.BoxSizer(wx.VERTICAL)		# Third Row (Stats)

		self.CreateWeaponSizer(self.hbox1)
		self.hbox1.Add((72,50),1)
		self.CreateArmorSizer(self.hbox1)
		self.mainvbox.Add(self.hbox1)
		self.mainhbox.Add(self.mainvbox)

		self.mainvbox.Add((450,55), 0)

		self.CreateArmorSizer(self.hbox2, "shirt")
		self.hbox2.Add((71,50),1)
		self.CreateArmorSizer(self.hbox2, "shoes")
		self.mainvbox.Add(self.hbox2)

		self.CreateStatsSizer(self.hbox3)
		self.mainhbox.Add(self.hbox3, 2, wx.ALL, 10)

		self.panelDisplay.SetSizer(self.mainhbox)
		self.mainhbox.Fit(self)

	def CreateWeaponSizer(self, sizer):
		vbox = wx.BoxSizer(wx.VERTICAL)
		for i in range(0,2):
			vbox.Add(self.CreateImageButton(self.panelDisplay, self.DoNothing(), "Defenseup", (45,45)), 0, wx.ALL, 0)
		sizer.Add(vbox, 1, wx.ALL, 0)
		sizer.Add(self.CreateImageButton(self.panelDisplay, self.DoNothing(), 'weapon'), 2, wx.ALL, 0)

	def CreateArmorSizer(self, sizer, name="helmet"):
		sizer.Add(self.CreateImageButton(self.panelDisplay, self.DoNothing(), name), 2, wx.ALL, 2)
		vbox = wx.BoxSizer(wx.VERTICAL)
		vbox.Add(self.CreateImageButton(self.panelDisplay, self.DoNothing(), "Defenseup", (35,35)), 1, wx.ALL, 0)
		for i in range(0,3):
			vbox.Add(self.CreateImageButton(self.panelDisplay, self.DoNothing(), "Defenseup", (15,15)), 0, wx.ALIGN_CENTER, 0)
		sizer.Add(vbox, 1, wx.ALL, 5)

	def CreateStatsSizer(self, sizer):
		i = 0
		names =	("Attack", "Defense", "Ink Recovery", "Tank Capacity", "Run", "Swim", "Jump", "Respawn", "Charge Rate", "Loss Rate", "Duration")
		for section in ("Attack", "Speed", "Special"):
			sbox = wx.StaticBox(self.panelDisplay, -1, section)
			hbox = wx.StaticBoxSizer(sbox, wx.VERTICAL)
			gbox = wx.GridSizer(cols=2, hgap=15, vgap=5)
			for k in range(0,4):
				if(k+(4*i) < 11):
					index = names[k+(4*i)]
					fillerGap = ""
					for l in range(0,(14-len(index))):
						fillerGap += " "
					gbox.Add(wx.StaticText(self.panelDisplay, -1, index+fillerGap), 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL)
					gbox.Add(wx.StaticText(self.panelDisplay, -1, str(self.dataValues.data[index])), 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
				else:
					gbox.Add(wx.StaticText(self.panelDisplay, -1, ""), 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
					gbox.Add(wx.StaticText(self.panelDisplay, -1, ""), 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
			i += 1
			hbox.Add(gbox)
			sizer.Add(hbox, 0, wx.ALL, 5)


	def MakeSplitter(self):
		self.splitter = wx.SplitterWindow(self)
		self.panelSelection = wx.Panel(self.splitter, style=wx.SUNKEN_BORDER, name="Selection")
		self.panelDisplay = wx.Panel(self.splitter, style=wx.SUNKEN_BORDER, name="Display")
		self.panelSelection.SetBackgroundColour(wx.Colour(250,250,250,0))
		self.panelDisplay.SetBackgroundColour(wx.Colour(215,215,215,0))
		self.splitter.SetMinimumPaneSize(20)
		self.splitter.SplitVertically(self.panelSelection, self.panelDisplay, 200)

if __name__ == '__main__':
	app = wx.PySimpleApp()	
	frame = MainWindow(parent=None, id=-1)
	frame.Show()
	wx.lib.inspection.InspectionTool().Show()		# Debugger
	app.MainLoop()