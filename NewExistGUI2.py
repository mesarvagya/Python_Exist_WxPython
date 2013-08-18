# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

######### IMPORTS ARE HERE ################################################
from matplotlib import axis
import wx
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from Tryone import TryExist
import os.path as pth
######### IMPORTS END HERE ################################################

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ExistGUI", pos = wx.DefaultPosition, size = wx.Size( 669,431 ), style = wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN, name = u"jh" )

        self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        bSizer2.SetMinSize( wx.Size( 610,30 ) )
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Open XML File", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.TOP|wx.BOTTOM|wx.LEFT|wx.ALIGN_RIGHT, 5 )

        self.fileChooser = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.xml", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        self.fileChooser.SetMinSize( wx.Size( 275,20 ) )

        bSizer2.Add( self.fileChooser, 0, wx.TOP|wx.RIGHT|wx.LEFT|wx.ALIGN_RIGHT, 5 )

        bSizer15 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Write Query", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer15.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.queryBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_MULTILINE )
        self.queryBox.SetMinSize( wx.Size( 275,-1 ) )

        bSizer15.Add( self.queryBox, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.queryButton = wx.Button( self, wx.ID_ANY, u"Execute Query", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.queryButton, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Result", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer15.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.resultBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_MULTILINE )
        self.resultBox.SetMinSize( wx.Size( 275,-1 ) )

        bSizer15.Add( self.resultBox, 1, wx.ALL|wx.ALIGN_RIGHT, 5 )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button13 = wx.Button( self, wx.ID_ANY, u"Plot Data", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button13, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"Plot Data", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

        bSizer15.Add( bSizer3, 1, wx.EXPAND, 5 )

        bSizer2.Add( bSizer15, 1, wx.EXPAND, 5 )

        self.SetSizer( bSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.fileChooser.Bind( wx.EVT_FILEPICKER_CHANGED, self.fileChoose )
        self.queryButton.Bind( wx.EVT_BUTTON, self.executeQuery )
        self.m_button13.Bind( wx.EVT_BUTTON, self.plotData )
        self.m_button3.Bind( wx.EVT_BUTTON, self.plotData2 )        #Panel ko
        self.a = p1(self)
        #EXIST DB
        self.existDB = TryExist()

    def __del__( self ):
        pass

    # Virtual event handlers, overide them in your derived class
    def fileChoose( self, event ):
        try:
            pat = str(self.fileChooser.GetPath())
            pat = pat.encode('utf-8')
            dir_name = pth.dirname(pat)
            file_name = pth.basename(pat)
            self.existDB.upload_file(dir_name,file_name)
            wx.MessageBox(str(file_name)+" "+'is uploaded to /db/tryone In Database', 'File Upload',wx.OK|wx.ICON_INFORMATION)
        except:
            wx.MessageBox('Something Went Wrong','Error',wx.OK|wx.ICON_ERROR)

    def executeQuery( self, event ):
        try:
            query = str(self.queryBox.GetValue())
            query = query.encode('UTF-8')
            resp = str(self.existDB.get_data(query))
            self.resultBox.SetValue(resp)
        except:
            wx.MessageBox('Something Went Wrong','Error',wx.OK|wx.ICON_ERROR)

    def plotData(self, event ):
        quer = '''
        let $x:=doc("/db/sample/books.xml")
        return $x/bookstore/book/price/text()'''
        resp = self.existDB.get_data(quer)
        self.a.Show()
        t = np.arange(len(resp))
        self.a.draw(t,resp)

    def plotData2(self,event):
        self.a.clearr()
        #self.a.Show()
        t = np.arange(6)
        s=[1,2,3,2,1,5]
        self.a.draw(t,s)


###########################################################################
## Class p1
###########################################################################

class p1 ( wx.Panel ):

    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 336,352 ), style = wx.TAB_TRAVERSAL )
        self.figure = Figure(figsize=(4.2,4.4),dpi=80)
        self.axes = self.figure.add_subplot(111)

    def __del__( self ):
        pass
    def draw(self,t,s):
        self.axes.plot(t,s,'b*')
        self.canvas=FigureCanvas(self,-1,self.figure)
    def clearr(self):
        self.axes.clear()
        self.canvas=FigureCanvas(self,-1,self.figure)


app = wx.App()
frame = MainFrame(None)
frame.Show()
app.MainLoop()