import wx
import wx.adv
import g1
from ObjectListView import ObjectListView, ColumnDefn
import sqlite3


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
        conn = sqlite3.connect('sqlite3.db')
        cursor = conn.cursor()
        cursor.execute("SELECT BankHolidayName,StartDate from BankHoliday")
        wx.Panel.__init__(self, parent)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        lc=wx.ListCtrl(self,-1,pos=(10,10),size=(300,300),style=wx.LC_REPORT)
        lc.InsertColumn(0,'Name',width=250)
        lc.InsertColumn(1,'Start Date',width=170)
        #add data
        for row in cursor:
            total=lc.GetItemCount()
            indexItem=lc.InsertItem(total,str(total+1))
            lc.SetItem(indexItem,0,row[0])
            lc.SetItem(indexItem,1,row[1])
        #add data end
        hbox.Add(lc,1,wx.EXPAND)
        self.SetSizer(hbox)
        self.Center
        conn.close()

        
class DatePicker( wx.adv.DatePickerCtrl):
    def __init__(self,parent,dt,style=wx.adv.DP_DEFAULT):
        super(DatePicker,self).__init__(parent,dt=dt,style=style)
        self.SetInitialSize((120,-1))
class Page2(wx.Panel):
    def __init__(self,parent):
        super(Page2,self).__init__(parent)
        self.labelStartDate=wx.StaticText(self,label="Start Date:",pos=(25,30))
        self.startDate = wx.adv.DatePickerCtrl(self, id = -1,size=(90,20),pos=(90,30),style=wx.adv.DP_DROPDOWN|wx.adv.DP_SHOWCENTURY)
        self.startDateFormat=wx.TextCtrl(self,pos=(200,30),size=(120, -1))
        self.endDate = wx.adv.DatePickerCtrl(self, id = -1,size=(90,20),pos=(90,60),style=wx.adv.DP_DROPDOWN|wx.adv.DP_SHOWCENTURY)
        self.labelEndDate=wx.StaticText(self,label="End Date:",pos=(25,60))
        self.endDateFormat=wx.TextCtrl(self,pos=(200,60),size=(120, -1))
        self.labelReason=wx.StaticText(self,label="Reason",pos=(25,90))
        self.textReason=wx.TextCtrl(self,pos=(90,90),size=(235,200),style=wx.TE_LEFT)
        self.buttonSubmit=wx.Button(self,label="submit",pos=(325,30))
        self.buttonSubmit.Bind(wx.EVT_BUTTON,self.OnclickSubmit)
        self.startDate.Bind(wx.adv.EVT_DATE_CHANGED,self.startDateChange)
        self.endDate.Bind(wx.adv.EVT_DATE_CHANGED,self.endDateChange)
    def startDateChange(self,evt):
        cal=evt.GetEventObject()
        datestr=cal.GetValue()
        year=str(datestr.year)
        month = str(int(datestr.month)+1)
        day=str(datestr.day)
        total=year+"/"+month+"/"+day
        self.startDateFormat.SetValue(total)
    def endDateChange(self,evt):
        cal=evt.GetEventObject()
        datestr=cal.GetValue()
        year=str(datestr.year)
        month = str(int(datestr.month)+1)
        day=str(datestr.day)
        total=year+"/"+month+"/"+day
        self.endDateFormat.SetValue(total)
    def OnclickSubmit(self,event):
        conn = sqlite3.connect('sqlite3.db')
        cursor = conn.cursor()
        Id=g1.get_value('user')
        name=""
        startDateSubmit=self.startDateFormat.GetValue()
        endDateSubmit=self.endDateFormat.GetValue()
        TextReasonSubmit=self.textReason.GetValue()
        cursor.execute("SELECT Name,ID FROM LOGIN")
        for row in cursor:
            if row[1]==Id:
                name=row[0]
        if startDateSubmit=="" or endDateSubmit=="" or TextReasonSubmit=="":
            message="error"
        else:
            try:
                cursor.execute("INSERT INTO PersonalVacation(ID,name,StartDate,EndDate,promise,reason) VALUES('%s','%s','%s','%s','%s','%s');"%(Id,name,startDateSubmit,endDateSubmit,"wait",TextReasonSubmit))
            except:
                message="Database insert error"
            else:
                conn.commit()
                cursor.close()
                conn.close()
                message = "successful"
        wx.MessageBox(message)

class Page3(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)
        LB2=wx.ListBox(self,-1,pos=(10,10),size=(300,300),style=wx.LB_SINGLE)
        agree=wx.Button(self,label="agree",pos=(350,10),size=(100,100))
        refuse=wx.Button(self,label="refuse",pos=(350,120),size=(100,100))
        conn = sqlite3.connect('sqlite3.db')  # connect database(this database i created in localhost in future can build a server to manage the database)
        cursor = conn.cursor()  # Create a cursor, the cursor is a Class and have some function to contral the database
        cursor.execute("SELECT Name,StartDate,EndDate,reason FROM PersonalVacation")
        reason=wx.Button(self,label="reason",pos=(350,230),size=(100,100))
        for row in cursor:
            message="name:"+row[0]+" start:"+row[1]+" end:"+row[2]
            LB2.Append(message)
        conn.close()

 
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
