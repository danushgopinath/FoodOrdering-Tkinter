import pyodbc
from tkinter import *
import tkinter.messagebox as messagebox


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-SMC51SMG;'
                      'Database=food_ordering_management_system;'
                      'Trusted_Connection=yes;')


def restaurants():
    print("Avialable Restaurants")


def new_login():
    def cancelled():
        messagebox.showinfo("User Registration", "User Registered Cancelled!!")
        root2.destroy()

    def print_details_new():
        first = first_name_var.get()
        last = last_name_var.get()
        number = number_int.get()
        customer_id = customer_id_var.get()
        password = password_var.get()
        cur2_1 = conn.cursor()
        ins2 = "select * from customer_details where cust_id = '%s' " %customer_id
        cur2_1.execute(ins2)
        count=0
        for i in cur2_1:
            count+=1
        if count>0:
            messagebox.showinfo("Unsuccesfull", "Customer Id already exists! Try again")
            root2.destroy()
            return
        else:
            cur2=conn.cursor()
            ins1= "insert into customer_details values('%s','%s','%s',%d,'%s')"%(customer_id,first,last,number,password)
            cur2.execute(ins1)
            conn.commit()
            first_name_var.set("")
            last_name_var.set("")
            number_int.set("")
            customer_id_var.set("")
            password_var.set("")
        messagebox.showinfo("User Registration", "    User Registered!!\nExit and Login Again!!    ")

    root2 = Tk()
    root2.geometry('500x300')
    root2.title("NEW USER LOGIN")
    new_label = Label(root2, text="NEW USER LOGIN").place(x=200, y=30)
    first_name_var = StringVar(root2)
    last_name_var = StringVar(root2)
    number_int = IntVar(root2)
    customer_id_var = StringVar(root2)
    password_var = StringVar(root2)
    L_1 = Label(root2, text="FIRST NAME").place(x=25, y=90)
    E_1 = Entry(root2, textvariable=first_name_var).place(x=120, y=90)
    L_2 = Label(root2, text="LAST NAME").place(x=250, y=90)
    E_2 = Entry(root2, text=last_name_var).place(x=325, y=90)
    L_3 = Label(root2, text="NUMBER").place(x=25, y=140)
    E_3 = Entry(root2, textvariable=number_int).place(x=120, y=140)
    L_4 = Label(root2, text="CUSTOMER ID").place(x=25, y=180)
    E_4 = Entry(root2, textvariable=customer_id_var).place(x=120, y=180)
    L_5 = Label(root2, text="PASSWORD").place(x=250, y=180)
    E_5 = Entry(root2, textvariable=password_var, show='*').place(x=325, y=180)
    B_sub = Button(root2, text="SUBMIT", borderwidth=5, command=print_details_new).place(x=150, y=260)
    B_can = Button(root2, text="CANCEL", borderwidth=5, command=cancelled).place(x=250, y=260)


def old_login():
    def cancelled():
        messagebox.showinfo("User Registration", "User Registered Cancelled!!")
        root3.destroy()

    def restaurants():
        a=customer_id_var.get()
        b=password_var.get()
        currest1=conn.cursor()
        ins1="select * from customer_details where cust_id='%s' and c_password='%s'"%(a,b)
        currest1.execute(ins1)
        count=0
        for i in currest1:
            count+=1
        if count==1:
            def KFC():
                def kfc_total():
                    root10 = Tk()
                    root10.geometry('450x400')
                    root10.title("TOTAL BILL")
                    bill_kfc = Label(root10, text = "BILL FOR YOUR ORDER").place(x= 148, y = 30)
                    qty1 = quantity1.get()
                    qty2 = quantity2.get()
                    qty3 = quantity3.get()
                    qty4 = quantity4.get()
                    qty5 = quantity5.get()
                    cust_kfc = Cust_Id.get()
                    Lkfc = Label(root10, text = "CUSTOMER ID" + " = " + str(cust_kfc)).place(x = 143, y = 50)
                    curkfc = conn.cursor()
                    inskfc = "select * from food_items where rest_id = 'R01'"
                    curkfc.execute(inskfc)
                    n = []
                    for i in curkfc:
                        n.append(list(i))
                    l1 = Label(root10, text = n[0][2] + "\t\t" + str(X) + str(qty1) + "\t\t" + str(n[0][3] * qty1)).place(x = 75, y = 80)
                    l2 = Label(root10, text = n[1][2] + "\t\t" + str(X) + str(qty2) + "\t\t" + str(n[1][3] * qty2)).place(x = 75, y = 120)
                    l3 = Label(root10, text = n[2][2] + "\t\t\t" + str(X) + str(qty3) + "\t\t" + str(n[2][3] * qty3)).place(x = 75, y = 160)
                    l4 = Label(root10, text = n[3][2] + "\t" + str(X) + str(qty4) + "\t\t" + str(n[3][3] * qty4)).place(x = 75, y = 200)
                    l5 = Label(root10, text = n[4][2] + "\t\t\t" + str(X) + str(qty5) + "\t\t" + str(n[4][3] * qty5)).place(x = 75, y = 240)

                    total = (n[0][3] * qty1) + (n[1][3] * qty2) + (n[2][3] * qty3) + (n[3][3] * qty4) + (n[4][3] * qty5)

                    lt = Label(root10, text = "\t  Total Price" + "\t   " + str(total)).place(x = 160, y = 270)

                root5 = Tk()
                root5.geometry('500x400')
                root5.title("ITEMS AVAILABLE AT KFC")
                kfc_label = Label(root5, text="CHOOSE FROM THE BELOW ITEMS !!!").place(x=120, y=30)

                curkfc = conn.cursor()
                inskfc = "select * from food_items where rest_id = 'R01'"
                curkfc.execute(inskfc)
                n = []
                for i in curkfc:
                    n.append(list(i))
                print(n)
                l0_kfc = Label(root5, text = n[0][0] + "\t" + n[0][1] + "\t" + n[0][2] + "\t\t" + str(n[0][3])).place(x = 25, y = 60)
                l1_kfc = Label(root5, text = n[1][0] + "\t" + n[1][1] + "\t" + n[1][2] + "\t\t" + str(n[1][3])).place(x = 25, y = 100)
                l2_kfc = Label(root5, text = n[2][0] + "\t" + n[2][1] + "\t" + n[2][2] + "\t\t\t" + str(n[2][3])).place(x = 25, y = 140)
                l3_kfc = Label(root5, text = n[3][0] + "\t" + n[3][1] + "\t" + n[3][2] + "\t" + str(n[3][3])).place(x = 25, y = 180)
                l4_kfc = Label(root5, text = n[4][0] + "\t" + n[4][1] + "\t" + n[4][2] + "\t\t\t" + str(n[4][3])).place(x = 25, y = 220)
                l_cus_kfc = Label(root5, text = "ENTER CUSTOMER ID").place(x = 110, y = 320)

                quantity1 = IntVar(root5)
                quantity2 = IntVar(root5)
                quantity3 = IntVar(root5)
                quantity4 = IntVar(root5)
                quantity5 = IntVar(root5)
                Cust_Id = StringVar(root5)

                e1_kfc = Entry(root5, textvariable = quantity1).place(x = 315, y = 60)
                e2_kfc = Entry(root5, textvariable = quantity2).place(x = 315, y = 100)
                e3_kfc = Entry(root5, textvariable = quantity3).place(x = 315, y = 140)
                e4_kfc = Entry(root5, textvariable = quantity4).place(x = 315, y = 180)
                e5_kfc = Entry(root5, textvariable = quantity5).place(x = 315, y = 220)
                custkfc = Entry(root5, textvariable = Cust_Id).place(x = 230, y = 320)

                b_kfc = Button(root5, text = "PROCEED TO CHECKOUT", borderwidth = 5, command = kfc_total).place(x = 170, y = 360)
                    

            def McD():
                def mcd_total():
                    root11 = Tk()
                    root11.geometry('450x400')
                    root11.title("TOTAL BILL")
                    bill_mcd = Label(root11, text = "BILL FOR YOUR ORDER").place(x= 148, y = 30)
                    qty1 = quantity1.get()
                    qty2 = quantity2.get()
                    qty3 = quantity3.get()
                    qty4 = quantity4.get()
                    qty5 = quantity5.get()
                    cust_mcd = Cust_Id.get()
                    Lmcd = Label(root11, text = "CUSTOMER ID" + " = " + str(cust_mcd)).place(x = 143, y = 50)
                    curmcd = conn.cursor()
                    insmcd = "select * from food_items where rest_id = 'R02'"
                    curmcd.execute(insmcd)
                    n = []
                    for i in curmcd:
                        n.append(list(i))
                    l1 = Label(root11, text = n[0][2] + "\t\t" + str(X) + str(qty1) + "\t\t" + str(n[0][3] * qty1)).place(x = 75, y = 80)
                    l2 = Label(root11, text = n[1][2] + "\t\t" + str(X) + str(qty2) + "\t\t" + str(n[1][3] * qty2)).place(x = 75, y = 120)
                    l3 = Label(root11, text = n[2][2] + "\t\t" + str(X) + str(qty3) + "\t\t" + str(n[2][3] * qty3)).place(x = 75, y = 160)
                    l4 = Label(root11, text = n[3][2] + "\t\t\t" + str(X) + str(qty4) + "\t\t" + str(n[3][3] * qty4)).place(x = 75, y = 200)
                    l5 = Label(root11, text = n[4][2] + "\t\t\t" + str(X) + str(qty5) + "\t\t" + str(n[4][3] * qty5)).place(x = 75, y = 240)

                    total = (n[0][3] * qty1) + (n[1][3] * qty2) + (n[2][3] * qty3) + (n[3][3] * qty4) + (n[4][3] * qty5)

                    lt = Label(root11, text = "\t  Total Price" + "\t   " + str(total)).place(x = 160, y = 270)

                root6 = Tk()
                root6.geometry('500x400')
                root6.title("ITEMS AVAILABLE AT McD")
                mcd_label = Label(root6, text="CHOOSE FROM THE BELOW ITEMS !!!").place(x=120, y=30)

                curmcd = conn.cursor()
                insmcd = "select * from food_items where rest_id = 'R02'"
                curmcd.execute(insmcd)
                n = []
                for i in curmcd:
                    n.append(list(i))
                print(n)
                l0_mcd = Label(root6, text = n[0][0] + "\t" + n[0][1] + "\t" + n[0][2] + "\t\t" + str(n[0][3])).place(x = 25, y = 60)
                l1_mcd = Label(root6, text = n[1][0] + "\t" + n[1][1] + "\t" + n[1][2] + "\t\t" + str(n[1][3])).place(x = 25, y = 100)
                l2_mcd = Label(root6, text = n[2][0] + "\t" + n[2][1] + "\t" + n[2][2] + "\t\t" + str(n[2][3])).place(x = 25, y = 140)
                l3_mcd = Label(root6, text = n[3][0] + "\t" + n[3][1] + "\t" + n[3][2] + "\t\t\t" + str(n[3][3])).place(x = 25, y = 180)
                l4_mcd = Label(root6, text = n[4][0] + "\t" + n[4][1] + "\t" + n[4][2] + "\t\t\t" + str(n[4][3])).place(x = 25, y = 220)
                l_cus_mcd = Label(root6, text = "ENTER CUSTOMER ID").place(x = 110, y = 320)

                quantity1 = IntVar(root6)
                quantity2 = IntVar(root6)
                quantity3 = IntVar(root6)
                quantity4 = IntVar(root6)
                quantity5 = IntVar(root6)
                Cust_Id = StringVar(root6)

                e1_mcd = Entry(root6, textvariable = quantity1).place(x = 315, y = 60)
                e2_mcd = Entry(root6, textvariable = quantity2).place(x = 315, y = 100)
                e3_mcd = Entry(root6, textvariable = quantity3).place(x = 315, y = 140)
                e4_mcd = Entry(root6, textvariable = quantity4).place(x = 315, y = 180)
                e5_mcd = Entry(root6, textvariable = quantity5).place(x = 315, y = 220)
                custmcd = Entry(root6, textvariable = Cust_Id).place(x = 230, y = 320)

                b_mcd = Button(root6, text = "PROCEED TO CHECKOUT", borderwidth = 5, command = mcd_total).place(x = 170, y = 360)

            def HAVMOR():
                def hav_total():
                    root12 = Tk()
                    root12.geometry('450x400')
                    root12.title("TOTAL BILL")
                    bill_hav =  Label(root12, text = "BILL FOR YOUR ORDER").place(x= 148, y = 30)
                    qty1 = quantity1.get()
                    qty2 = quantity2.get()
                    qty3 = quantity3.get()
                    qty4 = quantity4.get()
                    qty5 = quantity5.get()
                    cust_hav = Cust_Id.get()
                    Lhav = Label(root12, text = "CUSTOMER ID" + " = " + str(cust_hav)).place(x = 143, y = 50)
                    curhav = conn.cursor()
                    inshav = "select * from food_items where rest_id = 'R03'"
                    curhav.execute(inshav)
                    n = []
                    for i in curhav:
                        n.append(list(i))
                    l1 = Label(root12, text = n[0][2] + "\t\t" + str(X) + str(qty1) + "\t\t" + str(n[0][3] * qty1)).place(x = 75, y = 80)
                    l2 = Label(root12, text = n[1][2] + "\t\t\t" + str(X) + str(qty2) + "\t\t" + str(n[1][3] * qty2)).place(x = 75, y = 120)
                    l3 = Label(root12, text = n[2][2] + "\t\t" + str(X) + str(qty3) + "\t\t" + str(n[2][3] * qty3)).place(x = 75, y = 160)
                    l4 = Label(root12, text = n[3][2] + "\t\t\t" + str(X) + str(qty4) + "\t\t" + str(n[3][3] * qty4)).place(x = 75, y = 200)
                    l5 = Label(root12, text = n[4][2] + "\t\t\t" + str(X) + str(qty5) + "\t\t" + str(n[4][3] * qty5)).place(x = 75, y = 240)

                    total = (n[0][3] * qty1) + (n[1][3] * qty2) + (n[2][3] * qty3) + (n[3][3] * qty4) + (n[4][3] * qty5)

                    lt = Label(root12, text = "\t  Total Price" + "\t   " + str(total)).place(x = 160, y = 270)

                root7 = Tk()
                root7.geometry('500x400')
                root7.title("ITEMS AVAILABLE AT HAVMOR")
                kfc_label = Label(root7, text="CHOOSE FROM THE BELOW ITEMS !!!").place(x=120, y=30)

                curhav = conn.cursor()
                inshav = "select * from food_items where rest_id = 'R03'"
                curhav.execute(inshav)
                n = []
                for i in curhav:
                    n.append(list(i))
                print(n)
                l0_hav = Label(root7, text = n[0][0] + "\t" + n[0][1] + "\t" + n[0][2] + "\t\t" + str(n[0][3])).place(x = 25, y = 60)
                l1_hav = Label(root7, text = n[1][0] + "\t" + n[1][1] + "\t" + n[1][2] + "\t\t\t" + str(n[1][3])).place(x = 25, y = 100)
                l2_hav = Label(root7, text = n[2][0] + "\t" + n[2][1] + "\t" + n[2][2] + "\t\t" + str(n[2][3])).place(x = 25, y = 140)
                l3_hav = Label(root7, text = n[3][0] + "\t" + n[3][1] + "\t" + n[3][2] + "\t\t\t" + str(n[3][3])).place(x = 25, y = 180)
                l4_hav = Label(root7, text = n[4][0] + "\t" + n[4][1] + "\t" + n[4][2] + "\t\t\t" + str(n[4][3])).place(x = 25, y = 220)
                l_cus_hav = Label(root7, text = "ENTER CUSTOMER ID").place(x = 110, y = 320)

                quantity1 = IntVar(root7)
                quantity2 = IntVar(root7)
                quantity3 = IntVar(root7)
                quantity4 = IntVar(root7)
                quantity5 = IntVar(root7)
                Cust_Id = StringVar(root7)

                e1_hav = Entry(root7, textvariable = quantity1).place(x = 315, y = 60)
                e2_hav = Entry(root7, textvariable = quantity2).place(x = 315, y = 100)
                e3_hav = Entry(root7, textvariable = quantity3).place(x = 315, y = 140)
                e4_hav = Entry(root7, textvariable = quantity4).place(x = 315, y = 180)
                e5_hav = Entry(root7, textvariable = quantity5).place(x = 315, y = 220)
                custhav = Entry(root7, textvariable = Cust_Id).place(x = 230, y = 320)

                b_hav = Button(root7, text = "PROCEED TO CHECKOUT", borderwidth = 5, command = hav_total).place(x = 170, y = 360)

            def MOD():
                def mod_total():
                    root13 = Tk()
                    root13.geometry('450x400')
                    root13.title("TOTAL BILL")
                    bill_mod = Label(root13, text = "BILL FOR YOUR ORDER").place(x= 148, y = 30)
                    qty1 = quantity1.get()
                    qty2 = quantity2.get()
                    qty3 = quantity3.get()
                    qty4 = quantity4.get()
                    qty5 = quantity5.get()
                    cust_mod = Cust_Id.get()
                    Lhav = Label(root13, text = "CUSTOMER ID" + " = " + str(cust_mod)).place(x = 143, y = 50)
                    curhav = conn.cursor()
                    inshav = "select * from food_items where rest_id = 'R04'"
                    curhav.execute(inshav)
                    n = []
                    for i in curhav:
                        n.append(list(i))
                    l1 = Label(root13, text = n[0][2] + "\t\t" + str(X) + str(qty1) + "\t\t" + str(n[0][3] * qty1)).place(x = 75, y = 80)
                    l2 = Label(root13, text = n[1][2] + "\t\t" + str(X) + str(qty2) + "\t\t" + str(n[1][3] * qty2)).place(x = 75, y = 120)
                    l3 = Label(root13, text = n[2][2] + "\t\t\t" + str(X) + str(qty3) + "\t\t" + str(n[2][3] * qty3)).place(x = 75, y = 160)
                    l4 = Label(root13, text = n[3][2] + "\t\t\t" + str(X) + str(qty4) + "\t\t" + str(n[3][3] * qty4)).place(x = 75, y = 200)
                    l5 = Label(root13, text = n[4][2] + "\t\t" + str(X) + str(qty5) + "\t\t" + str(n[4][3] * qty5)).place(x = 75, y = 240)

                    total = (n[0][3] * qty1) + (n[1][3] * qty2) + (n[2][3] * qty3) + (n[3][3] * qty4) + (n[4][3] * qty5)

                    lt = Label(root13, text = "\t  Total Price" + "\t    " + str(total)).place(x = 160, y = 270)

                root8 = Tk()
                root8.geometry('500x400')
                root8.title("ITEMS AVAILABLE AT MOD")
                hav_label = Label(root8, text="CHOOSE FROM THE BELOW ITEMS !!!").place(x=120, y=30)

                curhav = conn.cursor()
                inskfc = "select * from food_items where rest_id = 'R04'"
                curhav.execute(inskfc)
                n = []
                for i in curhav:
                    n.append(list(i))
                print(n)
                l0_mod = Label(root8, text = n[0][0] + "\t" + n[0][1] + "\t" + n[0][2] + "\t\t" + str(n[0][3])).place(x = 25, y = 60)
                l1_mod = Label(root8, text = n[1][0] + "\t" + n[1][1] + "\t" + n[1][2] + "\t\t" + str(n[1][3])).place(x = 25, y = 100)
                l2_mod = Label(root8, text = n[2][0] + "\t" + n[2][1] + "\t" + n[2][2] + "\t\t\t" + str(n[2][3])).place(x = 25, y = 140)
                l3_mod = Label(root8, text = n[3][0] + "\t" + n[3][1] + "\t" + n[3][2] + "\t\t\t" + str(n[3][3])).place(x = 25, y = 180)
                l4_mod = Label(root8, text = n[4][0] + "\t" + n[4][1] + "\t" + n[4][2] + "\t\t" + str(n[4][3])).place(x = 25, y = 220)
                l_cus_mod = Label(root8, text = "ENTER CUSTOMER ID").place(x = 110, y = 320)

                quantity1 = IntVar(root8)
                quantity2 = IntVar(root8)
                quantity3 = IntVar(root8)
                quantity4 = IntVar(root8)
                quantity5 = IntVar(root8)
                Cust_Id = StringVar(root8)

                e1_mod = Entry(root8, textvariable = quantity1).place(x = 315, y = 60)
                e2_mod = Entry(root8, textvariable = quantity2).place(x = 315, y = 100)
                e3_mod = Entry(root8, textvariable = quantity3).place(x = 315, y = 140)
                e4_mod = Entry(root8, textvariable = quantity4).place(x = 315, y = 180)
                e5_mod = Entry(root8, textvariable = quantity5).place(x = 315, y = 220)
                custmod = Entry(root8, textvariable = Cust_Id).place(x = 230, y = 320)

                b_mod = Button(root8, text = "PROCEED TO CHECKOUT", borderwidth = 5, command = mod_total).place(x = 170, y = 360)

            def BARISTA():
                def bar_total():
                    root14 = Tk()
                    root14.geometry('450x400')
                    root14.title("TOTAL BILL")
                    bill_bar = Label(root14, text = "BILL FOR YOUR ORDER").place(x= 148, y = 30)
                    qty1 = quantity1.get()
                    qty2 = quantity2.get()
                    qty3 = quantity3.get()
                    qty4 = quantity4.get()
                    qty5 = quantity5.get()
                    cust_bar = Cust_Id.get()
                    Lbar = Label(root14, text = "CUSTOMER ID" + " = " + str(cust_bar)).place(x = 143, y = 50)
                    curbar = conn.cursor()
                    insbar = "select * from food_items where rest_id = 'R05'"
                    curbar.execute(insbar)
                    n = []
                    for i in curbar:
                        n.append(list(i))
                    l1 = Label(root14, text = n[0][2] + "\t\t" + str(X) + str(qty1) + "\t\t" + str(n[0][3] * qty1)).place(x = 75, y = 80)
                    l2 = Label(root14, text = n[1][2] + "\t\t" + str(X) + str(qty2) + "\t\t" + str(n[1][3] * qty2)).place(x = 75, y = 120)
                    l3 = Label(root14, text = n[2][2] + "\t\t" + str(X) + str(qty3) + "\t\t" + str(n[2][3] * qty3)).place(x = 75, y = 160)
                    l4 = Label(root14, text = n[3][2] + "\t\t\t" + str(X) + str(qty4) + "\t\t" + str(n[3][3] * qty4)).place(x = 75, y = 200)
                    l5 = Label(root14, text = n[4][2] + "\t\t" + str(X) + str(qty5) + "\t\t" + str(n[4][3] * qty5)).place(x = 75, y = 240)

                    total = (n[0][3] * qty1) + (n[1][3] * qty2) + (n[2][3] * qty3) + (n[3][3] * qty4) + (n[4][3] * qty5)

                    lt = Label(root14, text = "\t  Total Price" + "\t   " + str(total)).place(x = 160, y = 270)

                root9 = Tk()
                root9.geometry('500x400')
                root9.title("ITEMS AVAILABLE AT KFC")
                bar_label = Label(root9, text="CHOOSE FROM THE BELOW ITEMS !!!").place(x=120, y=30)

                curbar = conn.cursor()
                insbar = "select * from food_items where rest_id = 'R01'"
                curbar.execute(insbar)
                n = []
                for i in curbar:
                    n.append(list(i))
                print(n)
                l0_bar = Label(root9, text = n[0][0] + "\t" + n[0][1] + "\t" + n[0][2] + "\t\t" + str(n[0][3])).place(x = 25, y = 60)
                l1_bar = Label(root9, text = n[1][0] + "\t" + n[1][1] + "\t" + n[1][2] + "\t\t" + str(n[1][3])).place(x = 25, y = 100)
                l2_bar = Label(root9, text = n[2][0] + "\t" + n[2][1] + "\t" + n[2][2] + "\t\t\t" + str(n[2][3])).place(x = 25, y = 140)
                l3_bar = Label(root9, text = n[3][0] + "\t" + n[3][1] + "\t" + n[3][2] + "\t" + str(n[3][3])).place(x = 25, y = 180)
                l4_bar = Label(root9, text = n[4][0] + "\t" + n[4][1] + "\t" + n[4][2] + "\t\t\t" + str(n[4][3])).place(x = 25, y = 220)
                l_cus_bar = Label(root9, text = "ENTER CUSTOMER ID").place(x = 110, y = 320)

                quantity1 = IntVar(root9)
                quantity2 = IntVar(root9)
                quantity3 = IntVar(root9)
                quantity4 = IntVar(root9)
                quantity5 = IntVar(root9)
                Cust_Id = StringVar(root9)

                e1_bar = Entry(root9, textvariable = quantity1).place(x = 315, y = 60)
                e2_bar = Entry(root9, textvariable = quantity2).place(x = 315, y = 100)
                e3_bar = Entry(root9, textvariable = quantity3).place(x = 315, y = 140)
                e4_bar = Entry(root9, textvariable = quantity4).place(x = 315, y = 180)
                e5_bar = Entry(root9, textvariable = quantity5).place(x = 315, y = 220)
                custbar = Entry(root9, textvariable = Cust_Id).place(x = 230, y = 320)

                b_bar = Button(root9, text = "PROCEED TO CHECKOUT", borderwidth = 5, command = bar_total).place(x = 170, y = 360)
 
            root4 = Tk()
            root4.geometry('300x350')
            root4.title("RESTAURANTS")
            rest_label = Label(root4, text="CHOOSE FROM THE BELOW RESTAURANTS !!!").place(x=30, y=30)
            B_rest_1 = Button(root4, text="   KFC   ", borderwidth=5, command=KFC).place(x=120, y=80)
            B_rest_2 = Button(root4, text="   McD   ", borderwidth=5, command=McD).place(x=120, y=130)
            B_rest_3 = Button(root4, text=" HAVMOR  ", borderwidth=5, command=HAVMOR).place(x=110, y=180)
            B_rest_4 = Button(root4, text="   MOD   ", borderwidth=5, command=MOD).place(x=118, y=230)
            B_rest_5 = Button(root4, text=" BARISTA ", borderwidth=5, command=BARISTA).place(x=116, y=280)

        else:
            messagebox.showinfo("INVALID LOGIN", "Invalid Username and Password!!")

    root3 = Tk()
    root3.geometry('400x300')
    root3.title("EXISTING USER LOGIN")
    old_label = Label(root3, text="EXISTING USER LOGIN").place(x=140, y=30)
    customer_id_var = StringVar(root3)
    password_var = StringVar(root3)
    L_1 = Label(root3, text="CUSTOMER ID").place(x=25, y=90)
    E_1 = Entry(root3, textvariable=customer_id_var).place(x=120, y=90)
    L_2 = Label(root3, text="PASSWORD").place(x=25, y=150)
    E_2 = Entry(root3, textvariable=password_var, show='*').place(x=120, y=150)
    B_sub = Button(root3, text="SUBMIT", borderwidth=5, command=restaurants).place(x=130, y=260)
    B_can = Button(root3, text="CANCEL", borderwidth=5, command=cancelled).place(x=230, y=260)


root1 = Tk()
root1.title("FOOD BOX")
root1.geometry('400x300')

user_label = Label(root1, text="ONLINE FOOD ORDERING SYSYTEM").place(x=100, y=50)
B1 = Button(root1, text="NEW USER", borderwidth=6, command=new_login)
B1.place(x=75, y=100)
B2 = Button(root1, text="EXISTING USER", borderwidth=6, command=old_login)
B2.place(x=230, y=100)
