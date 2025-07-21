import tkinter as tk
from tkinter import messagebox

def valid_roman(s):
    return all(char in "IVXLCDM" for char in s.upper())

def roman_to_int(numeral):
    final_ans = 0
    if "CM" in numeral:
        final_ans+=900
        numeral=numeral.replace("CM" , "")
    if "CD" in numeral:
        final_ans += 400
        numeral = numeral.replace("CD", "")
    if "XC" in numeral:
        final_ans += 90
        numeral = numeral.replace("XC", "")
    if "XL" in numeral:
        final_ans += 40
        numeral = numeral.replace("XL", "")
    if "IX" in numeral:
        final_ans += 9
        numeral = numeral.replace("IX", "")
    if "IV" in numeral:
        final_ans += 4
        numeral = numeral.replace("IV", "")
    for i in numeral:
        if i =="M":
            final_ans+=1000
        elif i =="D":
            final_ans+=500
        elif i =="C":
            final_ans+=100
        elif i =="L":
            final_ans+=50
        elif i =="X":
            final_ans+=10
        elif i =="V":
            final_ans+=5
        elif i =="I":
            final_ans+=1
    return final_ans

def convert():
    roman=entry.get().upper()
    if roman=="":
        messagebox.showwarning("Input Error","Please enter a Roman Numeral.")
        return
    if not valid_roman(roman):
        messagebox.showerror("Invalid Input","Enter only valid Roman Numeral")
        return
    result=roman_to_int(roman)
    result_label.config(text=f"Integer : {result}")


window=tk.Tk()
window.title("Roman to Integer Convertor")
window.geometry("800x500")

entry = tk.Entry(window,font=("Arial",14),width=20)
entry.pack(pady=10)

convert_button= tk.Button(window,
                          text= "CONVERT",command=convert,
                          font=("Arial",12,"bold"))
convert_button.pack(pady=5)

x=tk.Label(window,text="Please enter Roman No.\nthen press Convert",font=("Arial",12))
x.pack(pady=10)
result_label= tk.Label(window, text="",
                       font=("Arial",14))
result_label.pack(pady=10)

window.mainloop()
