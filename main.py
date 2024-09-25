from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib

#functionality part

def clear():
    bathsopaEntry.delete(0,END)
    facecreamEntry.delete(0,END)
    facewashEntry.delete(0, END)
    hairsprayEntry.delete(0, END)
    hairgelEntry.delete(0, END)
    bodylotionEntry.delete(0, END)

    riceEntry.delete(0, END)
    daalEntry.delete(0, END)
    oilEntry.delete(0, END)
    sugarEntry.delete(0, END)
    teaEntry.delete(0, END)
    wheatEntry.delete(0, END)

    mumEntry.delete(0, END)
    pepsiEntry.delete(0, END)
    spriteEntry.delete(0, END)
    dewEntry.delete(0, END)
    cocacolaEntry.delete(0, END)
    maazaEntry.delete(0, END)

    bathsopaEntry.insert(0,0)
    facecreamEntry.insert(0,0)
    facewashEntry.insert(0,0)
    hairsprayEntry.insert(0,0)
    hairgelEntry.insert(0,0)
    bodylotionEntry.insert(0,0)

    riceEntry.insert(0,0)
    daalEntry.insert(0,0)
    oilEntry.insert(0,0)
    sugarEntry.insert(0,0)
    teaEntry.insert(0,0)
    wheatEntry.insert(0,0)

    mumEntry.insert(0,0)
    pepsiEntry.insert(0,0)
    spriteEntry.insert(0,0)
    dewEntry.insert(0,0)
    cocacolaEntry.insert(0,0)
    maazaEntry.insert(0,0)

    cosmeticpriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    drinkspriceEntry.delete(0,END)

    cosmetictaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    drinkstaxEntry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)

    textarea.delete(1.0,END)



def send_email():
    def send_gmail():
        try:
           ob=smtplib.SMTP('smtp.gmail.com',587)
           ob.starttls()
           ob.login(senderEntry.get(),passwordEntry.get())
           message=email_textarea.get(1.0,END)
           ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
           ob.quit()
           messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
           root1.destroy()
        except:
            messagebox.showerror('Error','Something went wrong, please try again',parent=root1)
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('Send Gmail')
        root1.config(bg='green2')
        root1.resizable(0,0)

        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='green2',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderLabel=Label(senderFrame,text="Sender's Email:",font=('arial',14,'bold'),bg='green2',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)
        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)


        passwordLabel = Label(senderFrame, text="Password:", font=('arial', 14, 'bold'), bg='green2', fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)
        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE,show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='green2', fg='white')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        recieverLabel = Label(recipientFrame, text="Email Address:", font=('arial', 14, 'bold'), bg='green2', fg='white')
        recieverLabel.grid(row=0, column=0, padx=10, pady=8)
        recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipientFrame, text="Message", font=('arial', 14, 'bold'), bg='green2', fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)
        email_textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        sendButton=Button(root1,text='SEND',font=('arial',16,'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)





        root1.mainloop()


def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberEntry.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')




if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill number {billnumber}is saved successfully')
        billnumber = random.randint(500, 1000)

billnumber=random.randint(500,1000)

def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details Are Required')
    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and drinkspriceEntry.get()=='':
        messagebox.showerror('Error', 'No Products are selected')
    elif cosmeticpriceEntry.get()=='0 Tk' and grocerypriceEntry.get()=='0 Tk' and drinkspriceEntry.get()=='0 Tk':
        messagebox.showerror('Error','No Products are selected')
        textarea.delete(1.0,END)
    else:
        textarea.insert(END,'\t\t**Welcome Customer**\n')
        textarea.insert(END,f'\nBill Number: {billnumber}')
        textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}')
        textarea.insert(END,f'\nCustomer Phone Number: {phoneEntry.get()}')
        textarea.insert(END,'\n==================================================')
        textarea.insert(END,'\nProducts\t\tQuantity\t\t\tPrice')
        textarea.insert(END,'\n==================================================')
        if bathsopaEntry.get()!='0':
            textarea.insert(END,f'\nBath Soap\t\t{bathsopaEntry.get()}\t\t\t{sopaprice}Tk')
        if facecreamEntry.get() != '0':
            textarea.insert(END, f'\nFace Cream\t\t{facecreamEntry.get()}\t\t\t{creamprice}Tk')
        if facewashEntry.get() != '0':
            textarea.insert(END, f'\nFace Wash\t\t{facewashEntry.get()}\t\t\t{facewashprice}Tk')
        if hairsprayEntry.get()!='0':
            textarea.insert(END,f'\nHear Spray\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice}Tk')
        if hairgelEntry.get()!='0':
            textarea.insert(END,f'\nHear Gel\t\t{hairgelEntry.get()}\t\t\t{hairgelprice}Tk')
        if bodylotionEntry.get()!='0':
            textarea.insert(END,f'\nBody Lotion\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice}Tk')
        if riceEntry.get()!='0':
            textarea.insert(END,f'\nRice\t\t{riceEntry.get()}\t\t\t{ riceprice}Tk')
        if oilEntry.get()!='0':
            textarea.insert(END,f'\nOil\t\t{oilEntry.get()}\t\t\t{ oilprice}Tk')
        if daalEntry.get()!='0':
            textarea.insert(END,f'\nDaal\t\t{daalEntry.get()}\t\t\t{daalprice}Tk')
        if sugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar\t\t{sugarEntry.get()}\t\t\t{ sugarprice}Tk')
        if teaEntry.get()!='0':
            textarea.insert(END,f'\nTea\t\t{teaEntry.get()}\t\t\t{ teaprice}Tk')
        if wheatEntry.get()!='0':
            textarea.insert(END,f'\nWheat\t\t{wheatEntry.get()}\t\t\t{ wheatprice}Tk')
        if mumEntry.get()!='0':
            textarea.insert(END,f'\nMum\t\t{mumEntry.get()}\t\t\t{mumprice}Tk')
        if maazaEntry.get()!='0':
            textarea.insert(END,f'\nMaaza\t\t{maazaEntry.get()}\t\t\t{maazaprice}Tk')
        if spriteEntry.get()!='0':
            textarea.insert(END,f'\nSprite\t\t{spriteEntry.get()}\t\t\t{ spriteprice}Tk')
        if pepsiEntry.get()!='0':
            textarea.insert(END,f'\nPepsi\t\t{pepsiEntry.get()}\t\t\t{ pepsiprice}Tk')
        if dewEntry.get()!='0':
            textarea.insert(END,f'\nDew\t\t{dewEntry.get()}\t\t\t{dewprice}Tk')
        if cocacolaEntry.get()!='0':
            textarea.insert(END,f'\nCoca Cola\t\t{cocacolaEntry.get()}\t\t\t{cocacolaprice}Tk')
        textarea.insert(END, '\n\n--------------------------------------------------')

        if cosmetictaxEntry.get()!='0.0 Tk':
            textarea.insert(END,f'\n Cosmetic Tax\t\t{cosmetictaxEntry.get()}')
        if grocerytaxEntry.get()!='0.0 Tk':
            textarea.insert(END,f'\n Grocery Tax\t\t{grocerytaxEntry.get()}')
        if drinkstaxEntry.get()!='0.0 Tk':
            textarea.insert(END,f'\n Drinks Tax\t\t{drinkstaxEntry.get()}')
        textarea.insert(END,f'\n\n Total Bill\t\t\t\t\t{totalbill}')
        textarea.insert(END, '\n\n-------------------------------------------------')
        save_bill()








def total():
    global sopaprice,hairsprayprice,creamprice,facewashprice,hairgelprice,bodylotionprice
    global riceprice,oilprice,daalprice,sugarprice,teaprice,wheatprice
    global mumprice,maazaprice,spriteprice,pepsiprice,dewprice,cocacolaprice
    global totalbill

    #cosmetic price list

    sopaprice=int(bathsopaEntry.get())*130
    creamprice=int(facecreamEntry.get())*150
    facewashprice=int(facewashEntry.get())*250
    hairsprayprice=int(hairsprayEntry.get())*170
    hairgelprice=int(hairgelEntry.get())*100
    bodylotionprice=int(bodylotionEntry.get())*100

    totalcosmeticprice=sopaprice+creamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'{totalcosmeticprice}Tk')
    cosmetictax=totalcosmeticprice*0.06
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,str(cosmetictax)+'Tk')

    #Grocery price list

    riceprice=int(riceEntry.get())*60
    oilprice=int(oilEntry.get())*100
    daalprice=int(daalEntry.get())*70
    sugarprice=int(sugarEntry.get())*80
    teaprice=int(teaEntry.get())*50
    wheatprice=int(wheatEntry.get())*40

    totalgroceryprice=riceprice+oilprice+daalprice+sugarprice+teaprice+wheatprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'{totalgroceryprice}Tk')
    grocerytax = totalgroceryprice * 0.05
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, str(grocerytax) + 'Tk')

    #drinks price list

    mumprice=int(mumEntry.get())*25
    maazaprice=int(maazaEntry.get())*30
    spriteprice=int(spriteEntry.get())*30
    pepsiprice=int(pepsiEntry.get())*30
    dewprice=int(dewEntry.get())*30
    cocacolaprice=int(cocacolaEntry.get())*30

    totaldrinksprice=mumprice+maazaprice+spriteprice+pepsiprice+dewprice+cocacolaprice
    drinkspriceEntry.delete(0,END)
    drinkspriceEntry.insert(0,f'{totaldrinksprice}Tk')
    drinkstax = totaldrinksprice * 0.08
    drinkstaxEntry.delete(0, END)
    drinkstaxEntry.insert(0, str(drinkstax) + 'Tk')


    totalbill=totalcosmeticprice+totalgroceryprice+totaldrinksprice+grocerytax+cosmetictax+drinkstax







#Gui part
root=Tk()
root.title('Retail Billing System')
root.geometry('1270x690')
root.iconbitmap('')
headingLabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold')
                   ,bg='green2',fg='blue',bd=15,relief=GROOVE)
headingLabel.pack(fill=X,pady=7)


customer_details_frame=LabelFrame(root,text="Customer Details",font=('times new roman',15,'bold')
                                  ,fg='blue',bd=8,relief=GROOVE,bg='green2')
customer_details_frame.pack(fill=X)
nameLabel=Label(customer_details_frame,text='Name:',font=('times new roman',15,'bold'),fg='black',bg='green2')
nameLabel.grid(row=0,column=0,padx=20)
nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number:',font=('times new roman',15,'bold'),fg='black',bg='green2')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)
phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number:',font=('times new roman',15,'bold'),fg='black',bg='green2')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)
billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=6)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),
                    bd=6,width=8,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=6)

productsFrame=Frame(root)
productsFrame.pack(fill=X,pady=7)

cosmeticFrame=LabelFrame(productsFrame,text='Cosmetic',font=('times new roman',15,'bold')
                                  ,fg='blue',bd=8,relief=GROOVE,bg='green2')
cosmeticFrame.grid(row=0,column=0,padx=10)

bathsopaLabel=Label(cosmeticFrame,text='Bath Sopa:',font=('times new roman',15,'bold'),fg='black',bg='green2')
bathsopaLabel.grid(row=0,column=1,padx=10,sticky='w')
bathsopaEntry=Entry(cosmeticFrame,font=('arial',15),bd=5,width=8)
bathsopaEntry.grid(row=0,column=2,padx=10)
bathsopaEntry.insert(0,0)

facecreamLabel=Label(cosmeticFrame,text='Face Cream:',font=('times new roman',15,'bold'),fg='black',bg='green2')
facecreamLabel.grid(row=1,column=1,padx=10,sticky='w')
facecreamEntry=Entry(cosmeticFrame,font=('arial',15),bd=5,width=8)
facecreamEntry.grid(row=1,column=2,padx=10)
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmeticFrame,text='Face Wash:',font=('times new roman',15,'bold'),fg='black',bg='green2')
facewashLabel.grid(row=2,column=1,padx=10,sticky='w')
facewashEntry=Entry(cosmeticFrame,font=('arial',15),bd=5,width=8)
facewashEntry.grid(row=2,column=2,padx=10)
facewashEntry.insert(0,0)

hairsprayLabel=Label(cosmeticFrame,text='Hair Spray:',font=('times new roman',15,'bold'),fg='black',bg='green2')
hairsprayLabel.grid(row=3,column=1,padx=10,sticky='w')
hairsprayEntry=Entry(cosmeticFrame,font=('arial',15),bd=5,width=8)
hairsprayEntry.grid(row=3,column=2,padx=10)
hairsprayEntry.insert(0,0)

hairgelLabel=Label(cosmeticFrame,text='Hair Gel:',font=('times new roman',15,'bold'),fg='black',bg='green2')
hairgelLabel.grid(row=4,column=1,padx=10,sticky='w')
hairgelEntry=Entry(cosmeticFrame,font=('arial',15),bd=5,width=8)
hairgelEntry.grid(row=4,column=2,padx=10)
hairgelEntry.insert(0,0)

bodylotionLabel=Label(cosmeticFrame,text='Body Lotion:',font=('times new roman',15,'bold'),fg='black',bg='green2')
bodylotionLabel.grid(row=5,column=1,padx=10,sticky='w')
bodylotionEntry=Entry(cosmeticFrame,font=('arial',15),bd=5,width=8)
bodylotionEntry.grid(row=5,column=2,padx=10)
bodylotionEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold')
                                  ,fg='blue',bd=8,relief=GROOVE,bg='green2')
groceryFrame.grid(row=0,column=1,padx=10)

riceLabel=Label(groceryFrame,text='Rice:',font=('times new roman',15,'bold'),fg='black',bg='green2')
riceLabel.grid(row=1,column=1,padx=10,sticky='w')
riceEntry=Entry(groceryFrame,font=('arial',15),bd=5,width=8)
riceEntry.grid(row=1,column=2,padx=10)
riceEntry.insert(0,0)

oilLabel=Label(groceryFrame,text='Oil:',font=('times new roman',15,'bold'),fg='black',bg='green2')
oilLabel.grid(row=2,column=1,padx=10,sticky='w')
oilEntry=Entry(groceryFrame,font=('arial',15),bd=5,width=8)
oilEntry.grid(row=2,column=2,padx=10)
oilEntry.insert(0,0)
daalLabel=Label(groceryFrame,text='Daal:',font=('times new roman',15,'bold'),fg='black',bg='green2')
daalLabel.grid(row=3,column=1,padx=10,sticky='w')
daalEntry=Entry(groceryFrame,font=('arial',15),bd=5,width=8)
daalEntry.grid(row=3,column=2,padx=10)
daalEntry.insert(0,0)

wheatLabel=Label(groceryFrame,text='Wheat:',font=('times new roman',15,'bold'),fg='black',bg='green2')
wheatLabel.grid(row=4,column=1,padx=10,sticky='w')
wheatEntry=Entry(groceryFrame,font=('arial',15),bd=5,width=8)
wheatEntry.grid(row=4,column=2,padx=10)
wheatEntry.insert(0,0)

sugarLabel=Label(groceryFrame,text='Sugar:',font=('times new roman',15,'bold'),fg='black',bg='green2')
sugarLabel.grid(row=5,column=1,padx=10,sticky='w')
sugarEntry=Entry(groceryFrame,font=('arial',15),bd=5,width=8)
sugarEntry.grid(row=5,column=2,padx=10)
sugarEntry.insert(0,0)

teaLabel=Label(groceryFrame,text='Tea:',font=('times new roman',15,'bold'),fg='black',bg='green2')
teaLabel.grid(row=6,column=1,padx=10,sticky='w')
teaEntry=Entry(groceryFrame,font=('arial',15),bd=5,width=8)
teaEntry.grid(row=6,column=2,padx=10)
teaEntry.insert(0,0)

drinksFrame=LabelFrame(productsFrame,text='Drinks',font=('times new roman',15,'bold')
                                  ,fg='blue',bd=8,relief=GROOVE,bg='green2')
drinksFrame.grid(row=0,column=2,padx=10)

mumLabel=Label(drinksFrame,text='Mum:',font=('times new roman',15,'bold'),fg='black',bg='green2')
mumLabel.grid(row=1,column=1,padx=10,sticky='w')
mumEntry=Entry(drinksFrame,font=('arial',15),bd=5,width=8)
mumEntry.grid(row=1,column=2,padx=10)
mumEntry.insert(0,0)

maazaLabel=Label(drinksFrame,text='Maaza:',font=('times new roman',15,'bold'),fg='black',bg='green2')
maazaLabel.grid(row=2,column=1,padx=10,sticky='w')
maazaEntry=Entry(drinksFrame,font=('arial',15),bd=5,width=8)
maazaEntry.grid(row=2,column=2,padx=10)
maazaEntry.insert(0,0)

spriteLabel=Label(drinksFrame,text='Sprite:',font=('times new roman',15,'bold'),fg='black',bg='green2')
spriteLabel.grid(row=3,column=1,padx=10,sticky='w')
spriteEntry=Entry(drinksFrame,font=('arial',15),bd=5,width=8)
spriteEntry.grid(row=3,column=2,padx=10)
spriteEntry.insert(0,0)

pepsiLabel=Label(drinksFrame,text='Pepsi:',font=('times new roman',15,'bold'),fg='black',bg='green2')
pepsiLabel.grid(row=4,column=1,padx=10,sticky='w')
pepsiEntry=Entry(drinksFrame,font=('arial',15),bd=5,width=8)
pepsiEntry.grid(row=4,column=2,padx=10)
pepsiEntry.insert(0,0)

dewLabel=Label(drinksFrame,text='Dew:',font=('times new roman',15,'bold'),fg='black',bg='green2')
dewLabel.grid(row=5,column=1,padx=10,sticky='w')
dewEntry=Entry(drinksFrame,font=('arial',15),bd=5,width=8)
dewEntry.grid(row=5,column=2,padx=10)
dewEntry.insert(0,0)

cocacolaLabel=Label(drinksFrame,text='Coca Cola:',font=('times new roman',15,'bold'),fg='black',bg='green2')
cocacolaLabel.grid(row=6,column=1,padx=10,sticky='w')
cocacolaEntry=Entry(drinksFrame,font=('arial',15),bd=5,width=8)
cocacolaEntry.grid(row=6,column=2,padx=10,)
cocacolaEntry.insert(0,0)


  #bill fream


billareaFrame=Frame(productsFrame,bd=8,relief=GROOVE)
billareaFrame.grid(row=0,column=3,padx=10)

billareaLable=Label(billareaFrame,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLable.pack(fill=X)

scrollbar=Scrollbar(billareaFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billareaFrame,height=15,width=50,yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)

#/////////////////////////////////

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold')
                                  ,fg='blue',bd=8,relief=GROOVE,bg='green2')
billmenuFrame.pack(fill=X)

cosmeticpriceLabel=Label(billmenuFrame,text='Cosmetic Price:',font=('times new roman',15,'bold'),fg='black',bg='green2')
cosmeticpriceLabel.grid(row=0,column=1,padx=10,sticky='w')
cosmeticpriceEntry=Entry(billmenuFrame,font=('arial',15),bd=5,width=8)
cosmeticpriceEntry.grid(row=0,column=2,padx=10,)
grocerypriceLabel=Label(billmenuFrame,text='Grocery Price:',font=('times new roman',15,'bold'),fg='black',bg='green2')
grocerypriceLabel.grid(row=1,column=1,padx=10,sticky='w')
grocerypriceEntry=Entry(billmenuFrame,font=('arial',15),bd=5,width=8)
grocerypriceEntry.grid(row=1,column=2,padx=10)

drinkspriceLabel=Label(billmenuFrame,text='Drink Price:',font=('times new roman',15,'bold'),fg='black',bg='green2')
drinkspriceLabel.grid(row=2,column=1,padx=10,sticky='w')
drinkspriceEntry=Entry(billmenuFrame,font=('arial',15),bd=5,width=8)
drinkspriceEntry.grid(row=2,column=2,padx=10)


cosmetictaxLabel=Label(billmenuFrame,text='Cosmetic Tax:',font=('times new roman',15,'bold'),fg='black',bg='green2')
cosmetictaxLabel.grid(row=0,column=3,padx=10,sticky='w')
cosmetictaxEntry=Entry(billmenuFrame,font=('arial',15),bd=5,width=8)
cosmetictaxEntry.grid(row=0,column=4,padx=10,)

grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax:',font=('times new roman',15,'bold'),fg='black',bg='green2')
grocerytaxLabel.grid(row=1,column=3,padx=10,sticky='w')
grocerytaxEntry=Entry(billmenuFrame,font=('arial',15),bd=5,width=8)
grocerytaxEntry.grid(row=1,column=4,padx=10)

drinkstaxLabel=Label(billmenuFrame,text='Drink Tax:',font=('times new roman',15,'bold'),fg='black',bg='green2')
drinkstaxLabel.grid(row=2,column=3,padx=10,sticky='w')
drinkstaxEntry=Entry(billmenuFrame,font=('arial',15),bd=5,width=8)
drinkstaxEntry.grid(row=2,column=4,padx=10)

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=5,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',15,'bold'),
                   fg='black',bg='green2',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text='Bill',font=('arial',15,'bold'),
                  fg='black',bg='green2',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',font=('arial',15,'bold'),fg='black',bg='green2',
                   bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=0,column=3,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',15,'bold'),fg='black',bg='green2',
                   bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=4,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',15,'bold'),fg='black',bg='green2',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=5,pady=20,padx=5)






root.mainloop()