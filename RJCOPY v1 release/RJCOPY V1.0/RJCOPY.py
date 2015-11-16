
from Tkinter import *
import ttk

import subprocess
import time,os.path
import uuid
import threading
import tkFileDialog as fd
import tkMessageBox as messagebox



class RajaProj(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent=parent
        
        self.resizable(width=True,height=True)
        
   

        self.initialize()
        
    def initialize(self):

        self.dest="..\\"
         
        main_frame=ttk.Frame(self)
        self.minsize(width=750,height=175)
        
        
        
        
        main_frame.grid(columnspan=5,sticky='ewns')
        main_frame.rowconfigure(5,weight=1)
        main_frame.columnconfigure(0,weight=100)
     
        main_frame.info_button=ttk.Button(main_frame,text=u"Gather Informations about Files",width=110,command=self.gatherinfo)
        
    
        main_frame.info_button.grid(column=0,row=0,columnspan=2,sticky='we',padx=3)
        main_frame.about_button=ttk.Button(main_frame,text=u"About RJCOPY..",command=self.about_fn)
        main_frame.about_button.grid(column=3,row=0,sticky='we',ipadx=10)
        main_frame.open_button=ttk.Button(main_frame,text=u"View Log",command=self.onClickOpen)
      
        main_frame.open_button.grid(column=2,row=0,padx=3)
        self.entryVariable = StringVar()
        
       
        main_frame.searchEntry=ttk.Entry(main_frame,textvariable=self.entryVariable,width=100)
        
        main_frame.searchEntry.grid(column=0,row=1,sticky='EW',columnspan=3,ipady=5,pady=3)
        main_frame.searchEntry.bind("<Return>", self.onPressEnter)
        
        
        self.entryVariable.set(u"Enter file/folder name here.")
        main_frame.searchEntry.focus_set()
        main_frame.searchEntry.selection_range(0,END)
        
      
        main_frame.copy_button=ttk.Button(main_frame,text=u"Search",command=self.onClickCopy)
        main_frame.copy_button.grid(column=3,row=1,ipady=5,sticky='EW',pady=3)
        

        self.labelVariable = StringVar()
        main_frame.status_label=ttk.Label(main_frame,textvariable=self.labelVariable,relief=RIDGE,padding=10,anchor=CENTER)

        main_frame.status_label.grid(columnspan=4,row=3,sticky='EW')
        try:
            mac=uuid.getnode()
            mac=str(mac)

            mf=open("mac_file.txt","r+")
            for line in mf:
                last_line=line
            mac_ipt=last_line.rstrip()


            if mac==mac_ipt:
                inp_file=open("info_file_2.txt","r")

                mod_time="%s" % time.ctime(os.path.getmtime("info_file_2.txt"))

                self.labelVariable.set(u"Info_File updated at "+mod_time)
         
                
              
              
                inp_file.close()
            else:
                mf.write('\n'+mac)
                mf.close()
                os.system(r"del info_file_2.txt & exit")
                self.labelVariable.set(u"Gather information about Files")
            
         


            
        except IOError:
            self.labelVariable.set(u"Gather information about Files")
            
        self.labelVariable2 = StringVar()
        main_frame.status_copy=ttk.Label(main_frame,textvariable=self.labelVariable2,relief=RIDGE,padding=10,anchor=CENTER)
        self.labelVariable2.set(u"Developed By Raja Syed Abuthahir .J")
        main_frame.status_copy.grid(columnspan=5,row=4,sticky='EW')
        
    def about_fn(self):
     
                
                
                root=Toplevel()
                root.resizable(width='False',height='False')
                root.title("About RJCOPY")
                frame=Frame(root)
                frame.grid()
                import webbrowser
                def OpenUrl():
                    webbrowser.open_new("www.facebook.com/rajasyedabu")
                label1=ttk.Label(frame,text="RJCOPY V1.0",relief=GROOVE,anchor=CENTER)
                label1.grid(column=0,row=0,columnspan=2,ipady=15,sticky='EW')
                desc_label=ttk.Label(frame,text="The Fastest File Copy System \n     Developed using Python",relief=GROOVE,anchor=CENTER)
                desc_label.grid(column=0,row=1,columnspan=2,ipady=5,sticky='EW')
                label_dev=ttk.Label(frame,text="About Developer",relief=FLAT,anchor=CENTER)
                label_dev.grid(column=0,row=2,columnspan=2,ipady=15,sticky='EW')
                label2=ttk.Label(frame,text="Name",relief=GROOVE,anchor=CENTER)
                label2.grid(column=0,row=3,ipady=5,sticky='EW',ipadx=10)
                label3=ttk.Label(frame,text="Raja Syed Abuthahir .J   BE(CSE)",relief=GROOVE,anchor=CENTER)
                label3.grid(column=1,row=3,ipady=5,sticky='EW',ipadx=10)
                label4=ttk.Label(frame,text="Phone No",relief=GROOVE,anchor=CENTER)
                label4.grid(column=0,row=4,ipady=5,sticky='EW',ipadx=10)
                label5=ttk.Label(frame,text="+918344447814",relief=GROOVE,anchor=CENTER)
                label5.grid(column=1,row=4,ipady=5,sticky='EW',ipadx=10)
                label6=ttk.Label(frame,text="Mail ID",relief=GROOVE,anchor=CENTER)
                label6.grid(column=0,row=5,ipady=5,sticky='EW',ipadx=10)
                label7=ttk.Label(frame,text="rajasyedab@gmail.com",relief=GROOVE,anchor=CENTER)
                label7.grid(column=1,row=5,ipady=5,sticky='EW',ipadx=10)
                label8=ttk.Label(frame,text="Facebook ID",relief=GROOVE,anchor=CENTER)
                label8.grid(column=0,row=6,ipady=5,sticky='EW',ipadx=10)
                
                clk_butt=ttk.Button(frame,text="Click Here",command=OpenUrl)
                clk_butt.grid(column=1,row=6,sticky='EW')
              
                
                
                
                
 
     
    def autogatherinfo(self):
     
      try:  
        self.update_info_var = StringVar()
        update_label=Label(self,textvariable=self.update_info_var,pady=5,relief=GROOVE,fg="gray20",bg='gray99',justify=LEFT)
        update_label.config(anchor='w')
        update_label.grid(columnspan=5,row=20,sticky='EW')
        self.update_info_var.set(u"updating info file...")
       
        os.system(r"MOUNTVOL > vol.txt")
        part=open("vol.txt","r")
        parti=open("partit.txt","w")
        partitionlist=open("partlist.txt","w")
        flag=0
        for line in part:
            if line.startswith("Possible"):
                flag=1
            if flag==1:
                
                parti.write(line)
        
        parti.close()
        inter_parti=open("partit.txt","r")
        for line in inter_parti:
            if (line.strip()).startswith("\\"):
                    
                    pv=inter_parti.next()
                    
                    
                    partitionlist.write(pv.strip())
		    partitionlist.write('\n')
                    #partitionlist.write((inter_parti.readline()).strip()+'\n')
       
        partitionlist.close()
        plist=open("partlist.txt","r")
        info=[]
        
        
        for line in plist:
        
            info.append("dir "+line.strip()+" /s /b /a & ")
            
      
        
        in1=''.join(info)
        in1_lst=[]
        in1_lst=in1.rsplit("&",1)
        info_f="cmd /k "+"("+in1_lst[0]+")"+" > info_file_auto.txt & exit"     
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        pipeObj=subprocess.Popen(info_f.strip(),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr= subprocess.PIPE,startupinfo=startupinfo).wait()

        auto_info=open("info_file_auto.txt","r")
        main_info=open("info_file_2.txt","w")
        content=auto_info.read()
        main_info.write(content)
        main_info.close()
        mod_time="%s" % time.ctime(os.path.getmtime("info_file_2.txt"))
      
        update_label.config(anchor='w')
        self.update_info_var.set("info updated at "+mod_time)
        self.labelVariable.set("info updated at "+mod_time)
        obj.update_idletasks()
       
        auto_info.close()
        #main_info.close()
      except:
          
           
          self.update_info_var.set(u"Done.")
         

    def gatherinfo(self):
     
      def thread_gather_fn():
         
         self.labelVariable.set(u"Gathering....") 
         obj.update_idletasks()  
         os.system(r"MOUNTVOL > vol.txt")
         part=open("vol.txt","r")
         parti=open("partit.txt","w")
         partitionlist=open("partlist.txt","w")
         flag=0
         for line in part:
            if line.startswith("Possible"):
                flag=1
            if flag==1:
                
                parti.write(line)
        
         parti.close()
         inter_parti=open("partit.txt","r")
         for line in inter_parti:
            if (line.strip()).startswith("\\"):
        
                    
                    pv=inter_parti.next()
                    
                    
                    partitionlist.write(pv.strip())
		    partitionlist.write('\n')
        
         partitionlist.close()
         plist=open("partlist.txt","r")
         info=[]
        
        
         for line in plist:
        
            info.append("dir "+line.strip()+" /s /b /a & ")
       
        
         in1=''.join(info)
         in1_lst=[]
         in1_lst=in1.rsplit("&",1)
         info_f="cmd /k "+"("+in1_lst[0]+")"+" > info_file_1.txt & exit"  

         startupinfo = subprocess.STARTUPINFO()
         startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
         pipeObj=subprocess.Popen(info_f.strip(),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr= subprocess.PIPE,startupinfo=startupinfo).wait()
         auto_info1=open("info_file_1.txt","r")
         main_info1=open("info_file_2.txt","w")
         content1=auto_info1.read()
         main_info1.write(content1)
         main_info1.close()
         mod_time="%s" % time.ctime(os.path.getmtime("info_file_2.txt"))

         self.labelVariable.set(u"Info_File updated at "+mod_time)
         obj.update_idletasks()
      gather_thread=threading.Thread(target=thread_gather_fn)
      gather_thread.deamon=True
      gather_thread.start()
      
    def onClickOpen(self):
      def open_info_thread():
        try:
            
            inp_file=open("info_file_2.txt","r")
            self.labelVariable.set(u"File Informations are gathered")
            os.system(r"notepad info_file_2.txt & exit")  
            inp_file.close()
        except IOError:
            self.labelVariable.set(u"Try to Open after Gathering information about files")
      opthread=threading.Thread(target=open_info_thread)
      opthread.start()
        
    def onPressEnter(self,event):

        try:
              present=0
              filename="info_file_2.txt"
              file=open(filename,"r")
              
              
              temp=open('temp.txt','w')
              key=self.entryVariable.get()

              filepos=key.lower()
              
              for line in file:
                 keylist=line.rsplit("\\",1)
                 
                 
               
                 key1=keylist[1]
                 
                 key2=key1.lower()
                 
                 
                
                     
                 
                 if filepos in key2:
                      
                      temp.write(line)
                      present=1
                    
                      
              temp.close()
              read_temp=open("temp.txt","r")
              
              mlb_header = ['Name','File/Folder','Path','Size']
              self.tree = ttk.Treeview(self,columns=mlb_header, show="headings")
              self.tree.grid(row=6,sticky='nsew',columnspan=4)
              if present==1:
                        self.minsize(width=810,height=500)
                        self.labelVariable.set(u"File Found")  
                        self.labelVariable2.set(u"select any from the below Location(s)")
                        obj.update_idletasks()
                        

                       
                        vsb = ttk.Scrollbar(self,orient="vertical",
                        command=self.tree.yview)
                        hsb = ttk.Scrollbar(self,orient="horizontal",
                        command=self.tree.xview)
                        self.tree.configure(yscrollcommand=vsb.set,
                        xscrollcommand=hsb.set)
                        self.tree.grid(row=6,sticky='nsew',columnspan=4)
                        vsb.grid(column=4, row=6, sticky='ns')
                        hsb.grid(column=0, row=15, sticky='ew',columnspan=5)


                        self.brws_entry_var=StringVar()
                        brws_entry=Entry(self,textvariable=self.brws_entry_var,width=100)
                        
                        
                        d_set=0
                        self.brws_entry_var.set(u"../")
                        
                        


                        
                        def brows():
                                dest_retrn=fd.askdirectory(parent=self)
                                self.dest ='"'+str(dest_retrn)+'"'
                                
                                d_set=1
                                
                                self.brws_entry_var.set(u"%s"%dest_retrn)
                           
                                obj.update_idletasks()
                        
                                
                        button1=ttk.Button(self,text="Browse..",command=brows)
                        button1.grid(column=3,row=18,sticky='w',padx=10)

                        
                           
                        obj.update_idletasks()
                        brws_entry.grid(columnspan=3,column=0,row=18,sticky='ew')
                        brws_label=ttk.Label(self,text="Choose Destination Path : ")
                        brws_label.grid(column=0,row=17,sticky='w')
                        def onselect():

                            item=self.tree.selection()[0]

                            src_details=self.tree.item(item,"values")
                            print (src_details)
                            
                            src_path='"'+src_details[2]+'"'
                            src_fn=src_details[0]
                            src_fname='"'+src_fn.rstrip()+'"'
                           
                            
                 
                            

                            
                            self.labelVariable.set(u"Wait..")  
                            self.labelVariable2.set(u"Copying...")
                            obj.update_idletasks()
                            title="title PRESS 'ENTER' TO COPY & "
                          
                            if src_details[1].strip()=='File':
                                self.dest='"'+self.brws_entry_var.get()+'"'
                                comm="robocopy "+src_path+" "+self.dest+" "+src_fname+" /eta"+" /A-:SH"+" & exit"
                            elif src_details[1].strip()=='Folder':

                                self.dest=self.brws_entry_var.get()
                                comm="robocopy "+'"'+src_details[2]+"\\"+src_fn.rstrip()+'"'+" "+'"'+self.dest+"\\"+src_fn.rstrip()+'"'+" /E /A-:SH"+" & exit"
                                
                    
                           
                            
                            def enkey_thread():
                                 os.system(r"%s%s"%(title,comm))

                                 obj.update_idletasks()
                                 self.labelVariable.set(src_fname+" Copied Successfully")
                                 self.labelVariable2.set(u"Done")
                                 obj.update_idletasks()
                            en_cp_th=threading.Thread(target=enkey_thread)
                            en_cp_th.start()
                       
        

                        
                        
                        butt=ttk.Button(self,text="COPY",command=onselect)

                        
                        
                        butt.grid(row=17,column=3,ipady=10,rowspan=2,sticky='E',ipadx=10)
                        mlb_list=[]
                        for line in read_temp:
                            line=line.replace("\\","\\\\")
                            size=""
                            fof=1
                            import os.path
                            fof_flag=os.path.isdir(line.rstrip())
                            if fof_flag:
                                
                             import os.path
                             fof=0
                             try:
                               
                               source=line.rstrip()
                               def _total_size(source):
                               	 total_size = os.path.getsize(source)
   			       	 for item in os.listdir(source):
       					 itempath = os.path.join(source, item)
        				 if os.path.isfile(itempath):
            					total_size += os.path.getsize(itempath)
        				 elif os.path.isdir(itempath):
           				        total_size +=_total_size(itempath)
                                 return total_size
                               #except:
                               sz=_total_size(source)
                             except:
                                    
                                 continue
                             sz_mb=round(sz/(1024*1024),2)
                             sz_kb=round(sz/1024,2)
                             sz_gb=round(sz/(1024*1024*1024),2)
                             if sz_mb>1024:
                                      size=('\t '+str(sz_gb)+"GB")
                             elif sz_mb<1:
                                      if sz_kb<1:
                                           size=("\t "+"1KB")
                                      else:    
                                           size=("\t "+str(sz_kb)+"KB")
                             else:   
                                      size= ("\t "+str(sz_mb)+"MB")
                            else:
                                 
                                    import os.path
                                    try:
                                    
                                     sz=os.path.getsize(line.rstrip())
                                    except:
                                      continue
                                    sz_mb=round(sz/(1024*1024),2)
                                    sz_kb=round(sz/1024,2)
                                    sz_gb=round(sz/(1024*1024*1024),2)
                                    if sz_mb>1024:
                                        size=('\t '+str(sz_gb)+"GB")
                                    elif sz_mb<1:
                                        if sz_kb<1:
                                             size=("\t "+"1KB")
                                        else:    
                                             size=("\t "+str(sz_kb)+"KB")
                                    else:   
                                        size= ("\t "+str(sz_mb)+"MB")
                                    
                            srcp_srcf=line.rsplit("\\\\",1)
                            src_path=srcp_srcf[0].strip()
                            src_fn=srcp_srcf[1]
                            src_fname='"'+src_fn.rstrip()+'"'
                            if fof==0:
                                fof_status="\t Folder"
                                
                            else:
                                fof_status="\t File"
                            mlb_list.append((src_fn,fof_status,src_path,size))
        
                        def _build_tree():
                                for col in mlb_header:
                                    self.tree.heading(col,text=col.title(),
                                    command=lambda c=col: sortby(self.tree, c, 0))
 
                                    

                                for item in mlb_list:
                                    self.tree.insert('', 'end', values=item)

        
                        _build_tree()
                        def sortby(tree, col, descending):
                                """sort tree contents when a column header is clicked on"""
            
                                data = [(tree.set(child, col), child) \
                                for child in tree.get_children('')]
            
            
            
                                data.sort(reverse=descending)
                                for ix, item in enumerate(data):
                                    tree.move(item[1], '', ix)
            
                                tree.heading(col,command=lambda col=col: sortby(tree, col, \
                                                                             int(not descending)))
        
        
        
                        
                       
                        
                        
        
        
        
                       
                       

             
                
                
              obj.update_idletasks()
                
              if present==0:
                self.labelVariable.set(u"File not Found")
                self.labelVariable2.set(u"Give Correct File Name")
               

                
        except IOError:
               
             self.labelVariable2.set(u"Info_File not Found")
             obj.update_idletasks()

            
    def onClickCopy(self):
          
        try:
              present=0
              filename="info_file_2.txt"
              file=open(filename,"r")
              
              
              temp=open('temp.txt','w')
              key=self.entryVariable.get()

              filepos=key.lower()
              
              for line in file:
                 keylist=line.rsplit("\\",1)
                 
                 
               
                 key1=keylist[1]
                 
                 key11=key1.lower()
                 
                 
                
                     
                 
                 if filepos in key11:
                      
                      temp.write(line)
                      present=1
                    
                      
              temp.close()
              read_temp=open("temp.txt","r")
              mlb_header = ['Name','File/Folder','Path','Size']
              self.tree = ttk.Treeview(self,columns=mlb_header, show="headings")
              self.tree.grid(row=6,sticky='nsew',columnspan=4)
              if present==1:
                        self.minsize(width=810,height=500)
                        self.labelVariable.set(u"File Found")  
                        self.labelVariable2.set(u"select any from the below Location(s)")
                        obj.update_idletasks()
                        

                
                        
                        vsb = ttk.Scrollbar(self,orient="vertical",
                        command=self.tree.yview)
                        hsb = ttk.Scrollbar(self,orient="horizontal",
                        command=self.tree.xview)
                        self.tree.configure(yscrollcommand=vsb.set,
                        xscrollcommand=hsb.set)
                        
                        vsb.grid(column=4, row=6, sticky='ns')
                        hsb.grid(column=0, row=15, sticky='ew',columnspan=5)


                        self.brws_entry_var=StringVar()
                        brws_entry=Entry(self,textvariable=self.brws_entry_var,width=100)
                        self.dest="..\\"
                        
                        d_set=0
                        self.brws_entry_var.set(u"../")
                        
                        


                        
                        def brows():
                                dest_retrn=fd.askdirectory(parent=self)
                                self.dest ='"'+str(dest_retrn)+'"'
                                
                                d_set=1
                                
                                self.brws_entry_var.set(u"%s"%dest_retrn)
                           
                                obj.update_idletasks()
                        
                                
                        button1=ttk.Button(self,text="Browse..",command=brows)
                        button1.grid(column=3,row=18,sticky='w',padx=10)

                        
                           
                        obj.update_idletasks()
                        brws_entry.grid(columnspan=3,column=0,row=18,sticky='ew')
                        brws_label=ttk.Label(self,text="Choose Destination Path : ")
                        brws_label.grid(column=0,row=17,sticky='w')
                        def onselect():

                            item=self.tree.selection()[0]

                            src_details=self.tree.item(item,"values")
                            print (src_details)
                            
                            src_path='"'+src_details[2]+'"'
                            src_fn=src_details[0]
                            src_fname='"'+src_fn.rstrip()+'"'
                           
                            
                 
                            

                            
                            self.labelVariable.set(u"Wait..")  
                            self.labelVariable2.set(u"Copying...")
                            obj.update_idletasks()
                            title="title PRESS 'ENTER' TO COPY & "
                          
                            if src_details[1].strip()=='File':
                                self.dest='"'+self.brws_entry_var.get()+'"'
                                comm="robocopy "+src_path+" "+self.dest+" "+src_fname+" /eta"+" /A-:SH"+" & exit"
                            elif src_details[1].strip()=='Folder':

                                self.dest=self.brws_entry_var.get()
                                comm="robocopy "+'"'+src_details[2]+"\\"+src_fn.rstrip()+'"'+" "+'"'+self.dest+"\\"+src_fn.rstrip()+'"'+" /E /A-:SH"+" & exit"
                                
                    
                            print (comm)
                            
                            def enkey_thread():
                                 os.system(r"%s%s"%(title,comm))

                                 obj.update_idletasks()
                                 self.labelVariable.set(src_fname+" Copied Successfully")
                                 self.labelVariable2.set(u"Done")
                                 obj.update_idletasks()
                            en_cp_th=threading.Thread(target=enkey_thread)
                            en_cp_th.start()
                       
        

                        
                        
                        butt=ttk.Button(self,text="COPY",command=onselect)

                        
                        
                        butt.grid(row=17,column=3,ipady=10,rowspan=2,sticky='E',ipadx=10)
                        mlb_list=[]
                        for line in read_temp:
                           line=line.replace("\\","\\\\")
                           size=""
                           fof=1
                           import os.path
                           fof_flag=os.path.isdir(line.rstrip())
                           if fof_flag:
                               
                            import os.path
                            fof=0
                            try:
                               
                               source=line.rstrip()
                               def _total_size(source):
                               	 total_size = os.path.getsize(source)
   			       	 for item in os.listdir(source):
       					 itempath = os.path.join(source, item)
        				 if os.path.isfile(itempath):
            					total_size += os.path.getsize(itempath)
        				 elif os.path.isdir(itempath):
           				        total_size +=_total_size(itempath)
                                 return total_size
                               #except:
                               sz=_total_size(source)
                            except:
                                 continue
                            sz_mb=round(sz/(1024*1024),2)
                            sz_kb=round(sz/1024,2)
                            sz_gb=round(sz/(1024*1024*1024),2)
                            if sz_mb>1024:
                                     size=('\t '+str(sz_gb)+"GB")
                            elif sz_mb<1:
                                     if sz_kb<1:
                                          size=("\t "+"1KB")
                                     else:    
                                          size=("\t "+str(sz_kb)+"KB")
                            else:   
                                     size= ("\t "+str(sz_mb)+"MB")
                           else:
                                 
                                    import os.path
                                    try:
                                    
                                     sz=os.path.getsize(line.rstrip())
                                    except:
                                      continue
                                    sz_mb=round(sz/(1024*1024),2)
                                    sz_kb=round(sz/1024,2)
                                    sz_gb=round(sz/(1024*1024*1024),2)
                                    if sz_mb>1024:
                                        size=('\t '+str(sz_gb)+"GB")
                                    elif sz_mb<1:
                                        if sz_kb<1:
                                             size=("\t "+"1KB")
                                        else:    
                                             size=("\t "+str(sz_kb)+"KB")
                                    else:   
                                        size= ("\t "+str(sz_mb)+"MB")
                           srcp_srcf=line.rsplit("\\\\",1)
                           src_path=srcp_srcf[0].strip()
                           src_fn=srcp_srcf[1]
                           src_fname='"'+src_fn.rstrip()+'"'
                           if fof==0:
                               fof_status="\t Folder"
                               
                           else:
                               fof_status="\t File"
                           mlb_list.append((src_fn,fof_status,src_path,size))
        
                        def _build_tree():
                                for col in mlb_header:
                                    self.tree.heading(col,text=col.title(),
                                    command=lambda c=col: sortby(self.tree, c, 0))
 
                                    

                                for item in mlb_list:
                                    self.tree.insert('', 'end', values=item)

        
                        _build_tree()
                        def sortby(tree, col, descending):
                                """sort tree contents when a column header is clicked on"""
            
                                data = [(tree.set(child, col), child) \
                                for child in tree.get_children('')]
            
            
            
                                data.sort(reverse=descending)
                                for ix, item in enumerate(data):
                                    tree.move(item[1], '', ix)
            
                                tree.heading(col,command=lambda col=col: sortby(tree, col, \
                                                                             int(not descending)))
        
        
        
                        
                       
                        
                        
        
        
        
                       
                       

             
                
                
              obj.update_idletasks()
                
              if present==0:
                self.labelVariable.set(u"File not Found")
                self.labelVariable2.set(u"Give Correct File Name")
               

                
        except IOError:
               
             self.labelVariable2.set(u"Info_File not Found")
             obj.update_idletasks()

      
           
           
       
            
            
if __name__ == "__main__":  

  obj=RajaProj(None)
  obj.title("RJ COPY")
  
  obj.rowconfigure(6, weight=15) 
  obj.columnconfigure(3,weight=10)
#   obj.rowconfigure(18, weight=5) 
  thread1=threading.Thread(target=obj.autogatherinfo)
  thread1.start()
  
  


  
  
  os.system(r"del partit.txt & exit")
  os.system(r"del partlist.txt & exit")
  os.system(r"del vol.txt & exit")
  
  obj.mainloop()
  os.system(r"del temp.txt & exit")
  os.system(r"del info_file_1.txt & exit")
  os.system(r"del info_file_auto.txt & exit")
  


    