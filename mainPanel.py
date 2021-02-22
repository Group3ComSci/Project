import wx
import wx.adv
import g1
from ObjectListView import ObjectListView, ColumnDefn
import sqlite3
conn = sqlite3.connect('studydb.db')
cursor = conn.cursor()

data=cursor.fetchone()


class BankHoliday(object):
    def __init__(self, name,start,end,overtimeWork,Emergency):
        self.Name=name
        self.startDate=start
        self.endDate=end
        self.overTimeWork=overtimeWork
        self.emergencyContect=Emergency
    def __repr__(self):
        return"<BankHoliday:[Name]>".format(Name=self.Name)
    

class Page1(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        lc=wx.ListCtrl(self,-1,pos=(10,10),size=(300,300),style=wx.LC_REPORT)
        lc.InsertColumn(0,'Name',width=140)
        lc.InsertColumn(1,'Start Date',width=130)
        lc.InsertColumn(2,'End Date',width=130)
        lc.InsertColumn(3,'Authority of overtime work',width=140)
        lc.InsertColumn(4,'Emergency Contect',wx.LIST_FORMAT_RIGHT, 90)
        hbox.Add(lc,1,wx.EXPAND)
        self.SetSizer(hbox)
        self.Center
        
  
        #self.current_selection=None
        #self.dataOlv = ObjectListView(self, wx.ID_ANY,style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        #self.setBooks()
        #self.dataOlv.cellEditMode = ObjectListView.CELLEDIT_SINGLECLICK
        
        #LB=wx.ListBox(self,-1,pos=(10,10),size=(300,300))
        #LB.Append("hello")
    #def setBooks(self):
          #self.dataOlv.SetColumns([
               #ColumnDefn("Title", "left", 220, "title"),
               #ColumnDefn("Author", "left", 200, "author"),
               #ColumnDefn("ISBN", "right", 100, "isbn"),
               #ColumnDefn("Mfg", "left", 180, "mfg")
          #])
          #self.dataOlv.SetObjects(self.products)
        
class Page2(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)
        calender=wx.adv.CalendarCtrl(self,-1,pos=(10,10))
        apply=wx.Button(self,label="Apply",pos=(250,10))

class Page3(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)
        LB2=wx.ListBox(self,-1,pos=(10,10),size=(300,300))
        agree=wx.Button(self,label="agree",pos=(350,10),size=(100,100))
        refuse=wx.Button(self,label="refuse",pos=(350,120),size=(100,100))
 
def Open():
    app = wx.App(False)
    frame = wx.Frame(None, title="Leave management",size=(500,400))
    nb = wx.Notebook(frame)
    if(g1.get_value('user')=="12345"):
        nb.AddPage(Page1(nb),"Bank Holiday")
        nb.AddPage(Page2(nb),"APPLICATION")
        nb.AddPage(Page3(nb),"Management")
    else:
        nb.AddPage(Page1(nb),"Bank Holiday")
        nb.AddPage(Page2(nb),"APPLICATION")
    frame.Show()
    app.MainLoop()
