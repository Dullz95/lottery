# main program
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random
from tkinter.font import Font

import Image
import requests
from tkinter import ttk
import PIL
from PIL import ImageTk

root = tk.Tk()
root.title("Play The LOTTO!!!")
root.geometry("800x1000")
root.configure(bg="black")

# image = Image.open('pngegg.png')
# test1 = ImageTk.PhotoImage(image)
# labelz=tkinter.Label(image=test1)
# labelz.image=test1
# labelz.place(x=0,y=0)
entry1 = []
entry2 = []
entry3 = []
randomlist = []
winnings1= []
winnings2=[]
winnings3=[]
earnings = [0, 0, 20, 100.50, 2384, 8584, 10000000]
total = ''
lbl_results= ''
banks = ["Nedbank","ABSA","FNB","Standard Bank"]
fonty = Font(family='Helvetica', size=40)


class main:
    def __init__(self,master):

        def adding(add):
            if len(entry1) < 6 and add not in entry1:
                entry1.append(add)
                self.ent1.config(text=entry1)
            elif len(entry1) == 6 and len(entry2) < 6 and add not in entry2:
                entry2.append(add)
                self.ent2.config(text=entry2)
            elif len(entry2) == 6 and len(entry3) < 6 and add not in entry3:
                entry3.append(add)
                self.ent3.config(text=entry3)

            else:
                if len(entry3) == 6:
                    messagebox.showerror("Error","Tries are full")
                else:
                    messagebox.showerror("Error","you can only select the same number once per entry")
        def play():
            global total
            if len(entry1) ==6 and len(entry2) ==6 and len(entry3) ==6:
                    while len(randomlist) < 6:
                        n = random.randint(1, 49)
                        if n not in randomlist:
                            randomlist.append(n)
                            randomlist.sort()
                            self.mainwin.config(text=randomlist)
                    for x in randomlist:
                        if x in entry1:
                            winnings1.append(x)
                            self.ent1_win.config(text=str(len(winnings1)) + "  R" + str(earnings[len(winnings1)]))
                    for x in randomlist:
                        if x in entry2:
                            winnings2.append(x)
                            self.ent2_win.config(text=str(len(winnings2)) + "   R" + str(earnings[len(winnings2)]))
                    for x in randomlist:
                        if x in entry3:
                            winnings3.append(x)
                            self.ent3_win.config(text=str(len(winnings3)) + "   R" + str(earnings[len(winnings3)]))
                    total ="  total winnings:  R" + str(earnings[len(winnings1)]+earnings[len(winnings2)]+earnings[len(winnings3)])
                    self.total.config(text=total)
                    text_file = open("PlayerID.txt", '+a')
                    text_file.write(
                        "\nEntry 1 : " + str(entry1) + "\nWinning in numbers entry1: "+str(winnings1)+
                        "\nEntry 2 : " + str(entry2) +"\nWinning numbers in entry2: "+str(winnings2) +"\nEntry 3 : " + str(entry3) +"\nWinning numbers in entry3: ")



                    text_file.close()
            else:
                messagebox.showerror("Error","Please fill entries")

        def convert_to_new_currency():
            global lbl_results
            if earnings[len(winnings1)] >=2 or earnings[len(winnings2)] >=2 or earnings[len(winnings3)] >= 2:
                convert_currency()
            else:
             messagebox.showerror("Error", "You do not have any winnings to convert")

        def convert_currency():
            global lbl_results
            root = Tk()

            # StringVar
            results = StringVar()

            # code to add widgets and style window will go here
            root.geometry("450x550")
            root.title("Currency Converter")
            root.config(bg='GREY')
            root.resizable(0, 0)

            information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/ZAR')
            information_json = information.json()

            conversion_rates = information_json['conversion_rates']
            currency = []

            for i in conversion_rates.keys():
                currency.append(i)

            currency_cb = ttk.Combobox(root)
            currency_cb['values'] = currency
            currency_cb['state'] = 'readonly'
            currency_cb.set('Select Currency')
            currency_cb.place(x=10, y=280)


            Label(root, text='Winnings: ', bg='gold').place(x=65, y=330)
            ent1 = Label(root, text=int(total[20:len(total)]),bg='white')
            ent1.place(x=200, y=330)
            ent1.focus()
            Label(root, text='Converted Amount:', bg='#00A868').place(x=65, y=380)
            lbl_results = Label(root, text='', bg='#00A868').place(x=200, y=380)

            def convert(to_currency, amount):

                amount = round(amount * conversion_rates[to_currency], 4)
                return amount

            def perform():
                try:
                    amount = ent1.cget('text')
                    to_curr = currency_cb.get()

                    converted_amount = convert(to_curr, amount)

                    lbl_results.config(text=converted_amount)
                except ValueError:
                    if ent1 != int and ent1 != float:
                        messagebox.showerror('invalid', 'Enter numbers only')

                except requests.exceptions.ConnectionError:
                    messagebox.showerror('Internet error', 'Poor connection')
                except KeyError:
                    messagebox.showerror('ERROR', 'Select Currency')
                # else:
                #     messagebox.showerror("error", "Somthing unknown  happened")

            # kill program
            def kill():
                return root.destroy()

            def clear():
                currency_cb.set('Select Currency')
                ent1.focus()
                results.set('')

            Button(root, text="CONVERT", borderwidth=3, bg='white', command=perform).place(x=180, y=430)
            Button(root, text="EXIT", borderwidth=3, bg='white', command=kill).place(x=281, y=480)
            Button(root, text="CLEAR", borderwidth=3, bg='white', command=clear).place(x=100, y=480)

            root.mainloop()  # continuously runs program in window

        def play_again():
            self.ent1.place(x=10, y=10)


        def destroy():
            messagebox.showinfo("warning", "closing game")
            master.destroy()

        def claim():
            if earnings[len(winnings1)] >=2 or earnings[len(winnings2)] >=2 or earnings[len(winnings3)] >= 2:
                bank_details()
                text_file = open("PlayerID.txt", '+a')
                text_file.write(
                    "\nEntry 1 winning numbers : " + str() + "\nEntry 2 winning numbers : " + str(entry2) + "\nEntry 3 winning numbers : " + str(entry3))
                text_file.close()
            else:
             messagebox.showerror("Error", "You do not have any winnings to claim")
        def bank_details():

            root = tk.Tk()
            root.title("Weather")
            root.geometry("800x400")
            root.configure(bg="black")

            # labels and entries
            us_name=Label(root,text="Account holder name")
            us_name.place(x=50,y=100)
            us_ent=Entry(root)
            us_ent.place(x=50,y=150)

            acc_no= Label(root, text="Account number")
            acc_no.place(x=50, y=200)
            acc_ent = Entry(root)
            acc_ent.place(x=50, y=250)

            currency_cb = ttk.Combobox(root)
            currency_cb['values'] = banks
            currency_cb['state'] = 'readonly'
            currency_cb.set('Select Bank')
            currency_cb.place(x=50, y=300)

            def submit():

                account_name= us_ent.get()
                account_no=acc_ent.get()

                if not account_name.isaplha():
                    messagebox.showerror("Error","name must be in alphabetical charectars")
                elif not account_no.isdigit():
                    messagebox.showerror("Error","Enter numeerical")

                import smtplib
                from email.mime.text import MIMEText
                from email.mime.multipart import MIMEMultipart
                s = smtplib.SMTP('smtp.gmail.com', 587)
                sender_email_id = 'abdullahtest585@gmail.com'
                f = open('PlayerID.txt', '+r')
                line = f.readlines()[2]
                reciever_email_id = line[6:len(line)]
                password = "testing0909"
                subject = "Hello All"
                msg = MIMEMultipart()
                msg['from'] = sender_email_id
                msg['To'] = reciever_email_id
                msg['Subject'] = subject
                body = "Hi guys how are you"
                body = body + "How was your task yesterday"

                msg.attach(MIMEText(body, 'plain'))
                text = msg.as_string()
                s.starttls()
                s.login(sender_email_id, password)

                s.sendmail(sender_email_id, reciever_email_id, text)
                s.quit()


            sub=Button(root,text="submit",command=submit)
            sub.place(x=50,y=350)


            root.mainloop()





        # frames within master
        self.frame = Frame(master, width=700, height=300, bg="", highlightbackground="gold", highlightthickness=15)
        self.frame.place(x=50, y=120)
        self.frame_two = Frame(master, width=330, height=250, bg="", highlightbackground="gold", highlightthickness=15)
        self.frame_two.place(x=50, y=445)
        self.frame_three = Frame(master, width=330, height=250, bg="", highlightbackground="gold",highlightthickness=15)
        self.frame_three.place(x=420, y=445)
        self.frame_four = Frame(master, width=700, height=180, bg="", highlightbackground="gold", highlightthickness=15)
        self.frame_four.place(x=50, y=720)
        self.lotto_head=Label(master, text="PLAY THE LOTTO",font=fonty,fg="gold",bg="black")
        self.lotto_head.place(x=200,y=40)


        # labels for frame 2
        self.draw=Label(self.frame_two, text="DRAW 1: ", fg="gold", bg="black")
        self.draw.place(x=40,y=30)
        self.ent1 = Label(self.frame_two, text="", fg="gold",bg="black")
        self.ent1.place(x=110,y=30)
        self.draw2 = Label(self.frame_two, text="DRAW 2: ", fg="gold", bg="black")
        self.draw2.place(x=40, y=100)
        self.ent2 = Label(self.frame_two,text="",fg="gold",bg="black", textvariable=entry2)
        self.ent2.place(x=110,y=100)
        self.draw3 = Label(self.frame_two, text="DRAW 3: ", fg="gold", bg="black")
        self.draw3.place(x=40, y=170)
        self.ent3=Label(self.frame_two,text="",fg="gold",bg="black", textvariable=entry3)
        self.ent3.place(x=110,y=170)

        # labels for frame 3
        self.winning_no=Label(self.frame_three,text="Winnning no's: ",fg="gold",bg="black")
        self.winning_no.place(x=10,y=30)
        self.mainwin=Label(self.frame_three,text=randomlist.sort(),bg="gold")
        self.mainwin.place(x=130,y=30)
        self.match=Label(self.frame_three,text="Draw 1 matches:",fg="gold",bg="black")
        self.match.place(x=10,y=70)
        self.ent1_win=Label(self.frame_three,text="",bg="gold")
        self.ent1_win.place(x=130,y=70)
        self.match2 = Label(self.frame_three, text="Draw 2 matches:", fg="gold", bg="black")
        self.match2.place(x=10, y=120)
        self.ent2_win = Label(self.frame_three, text="", bg="gold")
        self.ent2_win.place(x=130, y=120)
        self.match3 = Label(self.frame_three, text="Draw 3 matches:", fg="gold", bg="black")
        self.match3.place(x=10, y=180)
        self.ent3_win = Label(self.frame_three, text="", bg="gold")
        self.ent3_win.place(x=130, y=180)

        self.total=Label(self.frame_four,text="",bg="gold")
        self.total.place(x=50,y=20)
        #buttons

        self.one = Button(master, text="1", bg="gold", width=1, command=lambda: adding(1))
        self.one.place(x=100, y=200)
        self.two = Button(master, text="2", bg="gold", width=1, command=lambda: adding(2))
        self.two.place(x=140, y=200)
        self.three = Button(master, text="3", bg="gold", width=1, command=lambda: adding(3))
        self.three.place(x=180, y=200)
        self.four = Button(master, text="4", bg="gold", width=1, command=lambda: adding(4))
        self.four.place(x=220, y=200)
        self.five = Button(master, text="5", bg="gold", width=1, command=lambda: adding(5))
        self.five.place(x=260, y=200)
        self.six = Button(master, text="6", bg="gold", width=1, command=lambda: adding(6))
        self.six.place(x=300, y=200)
        self.seven = Button(master, text="7", bg="gold", width=1, command=lambda: adding(7))
        self.seven.place(x=340, y=200)
        self.eight = Button(master, text="8", bg="gold", width=1, command=lambda: adding(8))
        self.eight.place(x=380, y=200)
        self.nine = Button(master, text="9", bg="gold", width=1, command=lambda: adding(9))
        self.nine.place(x=420, y=200)
        self.ten = Button(master, text="10", bg="gold", width=1, command=lambda: adding(10))
        self.ten.place(x=460, y=200)
        self.eleven = Button(master, text="11", bg="gold", width=1, command=lambda: adding(11))
        self.eleven.place(x=500, y=200)
        self.twelve = Button(master, text="12", bg="gold", width=1, command=lambda: adding(12))
        self.twelve.place(x=540, y=200)
        self.thirteen = Button(master, text="13", bg="gold", width=1, command=lambda: adding(13))
        self.thirteen.place(x=580, y=200)
        self.fourteen = Button(master, text="14", bg="gold", width=1, command=lambda: adding(14))
        self.fourteen.place(x=620, y=200)
        self.fifteen= Button(master, text="15", bg="gold", width=1, command=lambda: adding(15))
        self.fifteen.place(x=660, y=200)
        self.sixteen = Button(master, text="16", bg="gold", width=1, command=lambda: adding(16))
        self.sixteen.place(x=140, y=230)
        self.seventeen = Button(master, text="17", bg="gold", width=1, command=lambda: adding(17))
        self.seventeen.place(x=180, y=230)
        self.eighteen = Button(master, text="18", bg="gold", width=1, command=lambda: adding(18))
        self.eighteen.place(x=220, y=230)
        self.nineteen = Button(master, text="19", bg="gold", width=1, command=lambda: adding(19))
        self.nineteen.place(x=260, y=230)
        self.twenty= Button(master, text="20", bg="gold", width=1, command=lambda: adding(20))
        self.twenty.place(x=300, y=230)
        self.twenty_one = Button(master, text="21", bg="gold", width=1, command=lambda: adding(21))
        self.twenty_one.place(x=340, y=230)
        self.twenty_two= Button(master, text="22", bg="gold", width=1, command=lambda: adding(22))
        self.twenty_two.place(x=380, y=230)
        self.twenty_three = Button(master, text="23", bg="gold", width=1, command=lambda: adding(23))
        self.twenty_three.place(x=420, y=230)
        self.twenty_four= Button(master, text="24", bg="gold", width=1, command=lambda: adding(24))
        self.twenty_four.place(x=460, y=230)
        self.twenty_five= Button(master, text="25", bg="gold", width=1, command=lambda: adding(25))
        self.twenty_five.place(x=500, y=230)
        self.twenty_six= Button(master, text="26", bg="gold", width=1, command=lambda: adding(26))
        self.twenty_six.place(x=540, y=230)
        self.twenty_seven = Button(master, text="27", bg="gold", width=1, command=lambda: adding(27))
        self.twenty_seven.place(x=580, y=230)
        self.twenty_eight= Button(master, text="28", bg="gold", width=1, command=lambda: adding(28))
        self.twenty_eight.place(x=620, y=230)
        self.twenty_nine = Button(master, text="29", bg="gold", width=1, command=lambda: adding(29))
        self.twenty_nine.place(x=180, y=260)
        self.thirty = Button(master, text="30", bg="gold", width=1, command=lambda: adding(30))
        self.thirty.place(x=220, y=260)
        self.thirty_one = Button(master, text="31", bg="gold", width=1, command=lambda: adding(31))
        self.thirty_one.place(x=260, y=260)
        self.thirty_two= Button(master, text="32", bg="gold", width=1, command=lambda: adding(32))
        self.thirty_two.place(x=300, y=260)
        self.thirty_three= Button(master, text="33", bg="gold", width=1, command=lambda: adding(33))
        self.thirty_three.place(x=340, y=260)
        self.thirty_four = Button(master, text="34", bg="gold", width=1, command=lambda: adding(34))
        self.thirty_four.place(x=380, y=260)
        self.thirty_five= Button(master, text="35", bg="gold", width=1, command=lambda: adding(35))
        self.thirty_five.place(x=420, y=260)
        self.thirty_six= Button(master, text="36", bg="gold", width=1, command=lambda: adding(36))
        self.thirty_six.place(x=460, y=260)
        self.thirty_seven= Button(master, text="37", bg="gold", width=1, command=lambda: adding(37))
        self.thirty_seven.place(x=500, y=260)
        self.thirty_eight= Button(master, text="38", bg="gold", width=1, command=lambda: adding(38))
        self.thirty_eight.place(x=540, y=260)
        self.thirty_nine= Button(master, text="39", bg="gold", width=1, command=lambda: adding(39))
        self.thirty_nine.place(x=580, y=260)
        self.forty = Button(master, text="40", bg="gold", width=1, command=lambda: adding(40))
        self.forty.place(x=220, y=290)
        self.forty_one = Button(master, text="41", bg="gold", width=1, command=lambda: adding(41))
        self.forty_one.place(x=260, y=290)
        self.forty_two = Button(master, text="42", bg="gold", width=1, command=lambda: adding(42))
        self.forty_two.place(x=300, y=290)
        self.forty_three= Button(master, text="43", bg="gold", width=1, command=lambda: adding(43))
        self.forty_three.place(x=340, y=290)
        self.forty_four= Button(master, text="44", bg="gold", width=1, command=lambda: adding(44))
        self.forty_four.place(x=380, y=290)
        self.forty_five = Button(master, text="45", bg="gold", width=1, command=lambda: adding(45))
        self.forty_five.place(x=420, y=290)
        self.forty_six = Button(master, text="46", bg="gold", width=1, command=lambda: adding(46))
        self.forty_six.place(x=460, y=290)
        self.forty_seven = Button(master, text="47", bg="gold", width=1, command=lambda: adding(47))
        self.forty_seven.place(x=500, y=290)
        self.forty_eight= Button(master, text="48", bg="gold", width=1, command=lambda: adding(48))
        self.forty_eight.place(x=540, y=290)
        self.forty_nine = Button(master, text="49", bg="gold", width=31, command=lambda: adding(49))
        self.forty_nine.place(x=260, y=322)

        #       function buttons

        self.play = Button(self.frame_two, text="PLAY", bg="gold", command=play)
        self.play.place(x=230, y=160)
        self.play_ag = Button(self.frame_four, text="PLAY AGAIN", bg="gold", command=play_again)
        self.play_ag.place(x=50, y=100)
        self.claim = Button(self.frame_four, text="convert", bg="gold", command=convert_to_new_currency)
        self.claim.place(x=500, y=100)
        self.exit = Button(self.frame_four, text="exit", bg="red", command=destroy)
        self.exit.place(x=600, y=100)
        self.claim = Button(self.frame_four, text="claim", bg="gold", command=claim)
        self.claim.place(x=400, y=100)




m = main(root)
root.mainloop()