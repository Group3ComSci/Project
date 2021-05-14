import wx #wx is a library which you need use Anaconda to do download it but i think it is a good GUI library
import sqlite3 #it is used to link with the sqlite3 database,which we have already builded
import mainPanel 

class TandCpanel1(wx.Frame):
   def __init__(self, parent, id, title="Term and Conditions", pos=(100, 100), size=(100, 100)):
      frame = wx.Frame.__init__(self, parent, id, title="Term and Conditions1", pos=(500, 250), size=(600,600))
      panel = wx.Panel(self)
  
      text2 = wx.TextCtrl(panel, pos=(50,50), size=(500,500), style=wx.TE_CENTER|wx.TE_READONLY|wx.TE_MULTILINE)
      text2.AppendText(data)

data = """ 
Terms and conditions – Leave time management software
BrainVire LTD 

What is contained in this document
These terms and conditions are for all users of this software. All users must agree before continuing. Please make sure you read this carefully as these are the terms set out by our company. By agreeing to these terms you will have access to use our software.

Failure to agree to these terms means you are unable to use this software and therefore unable to book off any holiday leave time via this system.

The following document is in regard to the leave time management software created for BrainVire LTD and is strictly licenced for current BrainVire employees only.

Your personal information and how we use it
1.This software will need to use your personal data in order to be useable. Details on what personal data specifically we will use can be found below in the “What personal data will we use?” Section.

2.As defined in the Data Protection act we will use your information :
  2a. Fairly, Lawfully and transparently
  2b. For specified, explicit purposes
  2c. Accurately and kept up to date.

3.Data collected by us for use in the leave management software will not be kept for longer than is necessary. If you do not wish us to store this information any longer we will remove it by the request of the user however in this case the user will no longer be able to use our software.

4.As Data will be stored with us we will also be in line with the general data protection regulations (GDPR) to ensure that the data is kept secure. We will do our upmost to keep your data saved with us secure.
5.Data stored by us for the purpose of this software will NOT be shared to any other companies and/or parties unless requested to by a lawful order.

What Personal data will we use?
1.The system that is being used will be for booking leave time. In order to do this accurately and correctly the following information may be required. All users will be employees of BrainVire LTD and therefore will be subject to providing the following information.

2.If the information is not provided then the employee is unable to use this booking system due to us needing the correct information to implement leave time.


3.It is up to you as the employee to ensure that all personal data gathered about yourself is up to date and accurate. If this is not the case please contact your administrator in order to alter these details before you decide to book leave.

4.To use this software efficiently we will need the following personal information:
  -Full name
  -Company ID
  -Email Address
  -Age 
  -Job role
  This information will be used to accurately and correctly to book off your holiday leave.

Using and altering our software
1.In order to use this software you will have to complete your registration. During the registration you will be asked for your personal information. Details on this can be found in the “What personal data will we use?” Section.

2.By using our software you agree to not try and manipulate, change or use this software for malicious purposes. You also agree to not attempt to reverse engineer or reproduce the leave management system.


3.We also do not allow you to copy and redistribute our software under any circumstances.

4.We own all rights to the software and its distribution and therefore will take legal action against those re distributing or using without prior permission.


5.The only copied version of this program which are permitted will be copies made for back up purposes. Any other copy or imitation to this software will be in breach of this agreement and you will be prosecuted.

Changes to this agreement
1.On occasion this terms and conditions document will be revised to adjust for updates to the software or for new features which will need further agreement.
  We reserve all right to change and alter the software as needed. Software may be changed due to but not limited to:

  -Bugs or errors in the program

  -Additional features or requirements 

  -Update security 

  -Change of law

2.In the event this document is revised you will be asked to read them again and resign.


3.If you do not agree to these terms and believe something is wrong then please contact us on terms@brainvire.co.uk to seek advice.
"""  
def open():
    app = wx.App()
    t = TandCpanel1(parent=None, id=34)
    t.Show()
    app.MainLoop()
