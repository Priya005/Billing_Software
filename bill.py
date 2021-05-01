from tkinter import*
import math,random,os
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #=======================Variabls=================================

        #================================Cosmetics==============================

        self.soap=IntVar()
        self.Face_cream=IntVar()
        self.face_wash=IntVar()
        self.Spray=IntVar()
        self.gel=IntVar()
        self.loshan=IntVar()

        #=========================Grocery====================

        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.Sugar=IntVar()
        self.tea=IntVar()

        #======================Cold drinks=================

        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbs_up=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()


        #===================Total Product price and Tax Variable
        self.Cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()
        

        self.Cosmetic_price_tax=StringVar()
        self.grocery_price_tax=StringVar()
        self.cold_drink_price_tax=StringVar()
        

        #====================Customer==================

        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()




#===============================================Customer Frame=====================================================================================

        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Details",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15, textvariable=self.c_name  ,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_lbl=Label(F1,text=" Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        cbill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_button=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)


#==============================++++++++++++++=============Cosmetics Frame=====================++++++++++++==============================================
        
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics ",bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
        F2.place(x=5,y=185,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new romen",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky='w')
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl=Label(F2,text="Face Cream",font=("times new romen",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky='w')
        Face_Cream_txt=Entry(F2,width=10,textvariable=self.Face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Face_W_lbl=Label(F2,text="Face Wash",font=("times new romen",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky='w')
        Face_W_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)


        Hair_s_lbl=Label(F2,text="Hair Spray",font=("times new romen",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky='w')
        Hair_s_txt=Entry(F2,width=10,textvariable=self.Spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)


        Hair_g_lbl=Label(F2,text="Hair Gel",font=("times new romen",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky='w')
        Hair_g_txt=Entry(F2,width=10,textvariable=self.gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Body_l_lbl=Label(F2,text="Body loshan",font=("times new romen",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky='w')
        Body_l_txt=Entry(F2,width=10,textvariable=self.loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


#=========================================Grocery Product===========================================================================

        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery Product ",bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
        F3.place(x=340,y=185,width=325,height=380)

        rice_lbl=Label(F3,text="Rice",font=("times new romen",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky='w')
        bath_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        food_oil_lbl=Label(F3,text="Food oil",font=("times new romen",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky='w')
        Food_oil_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Daal_lbl=Label(F3,text="Daal",font=("times new romen",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky='w')
        daal_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)


        wheat_lbl=Label(F3,text="wheat",font=("times new romen",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky='w')
        wheat_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)


        sugar_lbl=Label(F3,text="Sugar",font=("times new romen",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky='w')
        sugar_txt=Entry(F3,width=10,textvariable=self.Sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        tead_lbl=Label(F3,text="Tea",font=("times new romen",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky='w')
        tea_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

#====================================================================================

        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks ",bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
        F4.place(x=670,y=185,width=325,height=380)

        maza_lbl=Label(F4,text="Maza",font=("times new romen",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky='w')
        maza_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        cock_lbl=Label(F4,text="Cock",font=("times new romen",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky='w')
        cock_Cream_txt=Entry(F4,width=10,textvariable=self.cock,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Frooti_lbl=Label(F4,text="Frooti",font=("times new romen",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky='w')
        Frooti_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)


        thumbs_up_lbl=Label(F4,text="Thumbs Up",font=("times new romen",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky='w')
        thumbs_up_txt=Entry(F4,width=10,textvariable=self.thumbs_up,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)


        Limca_lbl=Label(F4,text="Limca",font=("times new romen",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky='w')
        Limca_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        sprite_lbl=Label(F4,text="Sprite",font=("times new romen",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky='w')
        sprite_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #===================================================Bill Area=======================================
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=185,width=350,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

       # ============================Button Frame=================

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu ",bg=bg_color,fg="gold",font=("times new roman",15,"bold"))
        F6.place(x=0,y=560,relwidth=1,height=140)
        m1_lbl=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0)
        m1_txt=Entry(F6,width=18,textvariable=self.Cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1,sticky="w")
        
        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0)
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1,sticky="w")

        m3_lbl=Label(F6,text="Total Cold Drink Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0)
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1,sticky="w")

       
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
        c1_lbl=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2)
        c1_txt=Entry(F6,width=18,textvariable=self.Cosmetic_price_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1,sticky="w")
        
        c2_lbl=Label(F6,text=" Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2)
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_price_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1,sticky="w")

        c3_lbl=Label(F6,text=" Cold Drink Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2)
        c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1,sticky="w")


        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=750,width=580,height=105)

        total_btn=Button(btn_f,command=self.total,text="Total",bg="cadetblue",fg="white",bd=2,pady=15,width=12,font="arial 12 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_f,text="Genrate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=12,font="arial 12 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_f,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=2,pady=15,width=12,font="arial 12 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_f,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",bd=2,pady=15,width=12,font="arial 12 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
    #---------------------------------------------------------

    def total(self):
        self.c_S_p=self.soap.get()*40
        self.c_fc_p=self.Face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_sp_p=self.Spray.get()*180
        self.c_g_p=self.gel.get()*140
        self.c_bl_p=self.loshan.get()*180

        self.total_cosmetic_price=float(
                                        self.c_S_p+
                                        self.c_fc_p+
                                        self.c_fw_p+
                                        self.c_sp_p+
                                        self.c_g_p+
                                        self.c_bl_p

                                        )
        self.Cosmetic_price.set("Rs."+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.01),2)
        self.Cosmetic_price_tax.set("Rs."+str(self.c_tax))
        

        self.g_r_p=self.rice.get()*80
        self.g_f_p=self.food_oil.get()*180
        self.g_d_p=self.daal.get()*60
        self.g_w_p=self.wheat.get()*240
        self.g_s_p=self.Sugar.get()*45
        self.g_t_p=self.tea.get()*150
        
        self.total_grocery_price=float(
                                          
                                        self.g_r_p+
                                        self.g_f_p+
                                        self.g_d_p+
                                        self.g_w_p+
                                        self.g_s_p+
                                        self.g_t_p
                                  )
        self.grocery_price.set("Rs."+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.05),2)
        self.grocery_price_tax.set("Rs."+str(self.g_tax))

        self.d_m_P=self.maza.get()*60
        self.d_c_P=self.cock.get()*60
        self.d_f_P=self.frooti.get()*50
        self.d_t_P=self.thumbs_up.get()*45
        self.d_l_P=self.limca.get()*40
        self.d_s_P=self.sprite.get()*60

        self.total_drinks_price=float(
                                        self.d_m_P+
                                        self.d_c_P+
                                        self.d_f_P+
                                        self.d_t_P+
                                        self.d_l_P+
                                        self.d_s_P
                                  )
        self.cold_drink_price.set("Rs."+str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price*0.05),2)
        self.cold_drink_price_tax.set("Rs."+str(self.d_tax))


        self.Total_bill=float(self.total_cosmetic_price+
                              self.total_grocery_price+
                              self.total_drinks_price+
                              self.c_tax+
                              self.g_tax+
                              self.d_tax
                              )
    def welcome_bill(self):
         self.txtarea.delete('1.0',END)
         self.txtarea.insert(END,f"\t Welcome Webcipher Retail ")
         self.txtarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
         self.txtarea.insert(END,f"\n Customer Name:{self.c_name.get()} ")
         self.txtarea.insert(END,f"\n Phone No: {self.c_phone.get()}")

         self.txtarea.insert(END,f"\n======================================")

         self.txtarea.insert(END,f"\n Product\t\tQTY\t\tPrice")

         self.txtarea.insert(END,f"\n======================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
                 messagebox.showerror("Error","Customer details are must")

        elif self.Cosmetic_price.get()=="Rs.0.0" and self.grocery_price.get()=="Rs. 0.0" and self.drinks_price.get()=="Rs. 0.0":
                 messagebox.showerror("Error","No product selected")
        else:
                self.welcome_bill()
        #==========Cosmetics==========
                if self.soap.get()!=0:
                        self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_S_p}")
                if self.Face_cream.get()!=0:
                        self.txtarea.insert(END,f"\n Face Cream\t\t{self.Face_cream.get()}\t\t{self.c_fc_p}")
                if self.face_wash.get()!=0:
                        self.txtarea.insert(END,f"\n Face wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
                if self.Spray.get()!=0:
                        self.txtarea.insert(END,f"\n Spray\t\t{self.Spray.get()}\t\t{self.c_sp_p}")
                if self.gel.get()!=0:
                        self.txtarea.insert(END,f"\n Gell\t\t{self.gel.get()}\t\t{self.c_g_p}")
                if self.loshan.get()!=0:
                        self.txtarea.insert(END,f"\n Loshan\t\t{self.loshan.get()}\t\t{self.c_bl_p}")
        
        #==========Grocery==========

                if self.rice.get()!=0:
                        self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
                if self.food_oil.get()!=0:
                        self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
                if self.daal.get()!=0:
                        self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
                if self.wheat.get()!=0:
                        self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
                if self.Sugar.get()!=0:
                        self.txtarea.insert(END,f"\n Sugar\t\t{self.Sugar.get()}\t\t{self.g_s_p}")
                if self.tea.get()!=0:
                        self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")

        #===========Cold drinks==========

                if self.maza.get()!=0:
                        self.txtarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t\t{self.d_m_P}")
                if self.cock.get()!=0:
                        self.txtarea.insert(END,f"\n Cock\t\t{self.cock.get()}\t\t{self.d_c_P}")
                if self.frooti.get()!=0:
                        self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_P}")
                if self.thumbs_up.get()!=0:
                        self.txtarea.insert(END,f"\n Thumbs Up\t\t{self.thumbs_up.get()}\t\t{self.d_t_P}")
                if self.limca.get()!=0:
                        self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_P}")
                if self.sprite.get()!=0:
                        self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_P}")


                self.txtarea.insert(END,f"\n--------------------------------------")
       
                if self.Cosmetic_price_tax.get()!="Rs. 0.0":
                        self.txtarea.insert(END,f"\n Cosmetic Tax :\t\t\t{self.Cosmetic_price_tax.get()}")
                if self.grocery_price_tax.get()!="Rs. 0.0":
                        self.txtarea.insert(END,f"\n Grocery Tax :\t\t\t{self.grocery_price_tax.get()}")
                if self.cold_drink_price_tax.get()!="Rs. 0.0":
                        self.txtarea.insert(END,f"\n Cold drink Tax :\t\t\t{self.cold_drink_price_tax.get()}")
        
                self.txtarea.insert(END,f"\n Total Bill :\t\t\t{self.Total_bill}")

                self.txtarea.insert(END,f"\n--------------------------------------")
                self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("Save bill","Do you want to save the bill?")
        if op>0:
                self.bill_data=self.txtarea.get('1.0',END)
                f1=open("bills/"+str(self.bill_no.get())+".txt","w")
                f1.write(self.bill_data)
                f1.close()
                messagebox.showinfo("Saved",f"Bill no:{self.bill_no.get()} saved Succesfully")
        else:
                return
    def find_bill(self):
            present="no"
            for i in os.listdir("bills/"):
                if i.split('.')[0]==self.search_bill.get():
                    f1=open(f"bills/{i}","r") 
                    self.txtarea.delete('1.0',END) 
                    for d in f1: 
                        self.txtarea.insert(END,d) 
                    f1.close() 
                    present="yes"
            if present=="no":
                    messagebox.showerror("Error","Invalid Bill No.")

    def clear_data(self):
        
        op=messagebox.askyesno("Clear","Do you really want to Clear data?")
        if op>0:
                self.soap.set(0)
                self.Face_cream.set(0)
                self.face_wash.set(0)
                self.Spray.set(0)
                self.gel.set(0)
                self.loshan.set(0)

        #=========================Grocery====================

                self.rice.set(0)
                self.food_oil.set(0)
                self.daal.set(0)
                self.wheat.set(0)
                self.Sugar.set(0)
                self.tea.set(0)

        #======================Cold drinks=================

                self.maza.set(0)
                self.cock.set(0)
                self.frooti.set(0)
                self.thumbs_up.set(0)
                self.limca.set(0)
                self.sprite.set(0)


                #===================Total Product price and Tax Variable
                self.Cosmetic_price.set("")
                self.grocery_price.set("")
                self.cold_drink_price.set("")
                

                self.Cosmetic_price_tax.set("")
                self.grocery_price_tax.set("")
                self.cold_drink_price_tax.set("")
                

                #====================Customer==================

                self.c_name.set("")
                self.c_phone.set("")
                self.bill_no.set("")
                x=random.randint(1000,9999)
                self.bill_no.set(str(x))
                self.search_bill.set("")
                self.welcome_bill()
        
    def Exit_app(self):
            op=messagebox.askyesno("Exit","Do you really want to exit?")
            if op>0:
                    self.root.destroy()

root=Tk()
obj = Bill_App(root)
root.mainloop()