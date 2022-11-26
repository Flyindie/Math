import tkinter as tk

def plus():
    try:
        number1 = int(num_input1.get())
        number2 = int(num_input2.get())
        output = str(number1) + "+" + str(number2) + "=" + str(number1+number2)
        output_label.configure(text=output)
    except:
        output_label.configure(text="โปรดใส่ตัวเลข")

def deleat():
    try:
        number1 = int(num_input1.get())
        number2 = int(num_input2.get())
        output = str(number1) + "-" + str(number2) + "=" + str(number1 - number2)
        output_label.configure(text=output)
    except:
        output_label.configure(text="โปรดใส่ตัวเลข")

def multiplys():
    try:
        number = int(num_input1.get())
        output = ''
        for i in range(1, 26):
           output += str(number) + 'x' + str(i)
           output += '=' + str(number * i) + '\n'
           output_label.configure(text=output)
    except:
        output_label.configure(text="โปรดใส่ตัวเลข(เฉพาะด้านบน)ด้วย")

def divide():
    try:
        number1 = int(num_input1.get())
        number2 = int(num_input2.get())
        output = str(number1) + "/" + str(number2) + "=" + str(number1 / number2)
        output_label.configure(text=output)
    except:
        output_label.configure(text="โปรดใส่ตัวเลข")

def circumference():
    try:
        number1 = int(num_input1.get())
        output = ''
        output += 'เส้นรอบวงเท่ากับ ' + str(number1*(22/7))
        output_label.configure(text=output)
    except:
        output_label.configure(text="โปรดใส่ตัวเลข(เฉพาะด้านบน)ด้วย")

def close():
    window.destroy()

window=tk.Tk()                   #เปิดwindow
window.title('num loop')
window.minsize(500, 500)

label = tk.Label(master=window, text='num loop')
label.pack(pady=5)

num_input1 = tk.Entry(master=window, bg='#F6F6F6')
num_input2 = tk.Entry(master=window, bg='#F6F6F6')
num_input1.pack(pady=5)
num_input2.pack(pady=5)

new_button = tk.Button(master=window, text='บวก \n (ใส่ทั้ง2ช่อง)', comman=plus)
new_button2 = tk.Button(master=window, text='ลบ \n (ใส่ทั้ง2ช่อง)', comman=deleat)
new_button3 = tk.Button(master=window, text='สูตรคูณ \n (ใส่ตัวเลขที่ช่องด้านบนสุด)', comman=multiplys)
new_button4 = tk.Button(master=window, text='หาร \n (ใส่ทั้ง2ช่อง)', comman=divide)
new_button5 = tk.Button(master=window, text='หาเส้นรอบวง \n (ใส่เส้นผ่าศูนย์กลางที่ช่องด้านบนสุด)', comman=circumference)
outbutton = tk.Button(master=window, text='ปิดโปรแกรม', comman=close)


new_button.pack(pady=5)
new_button2.pack(pady=5)
new_button4.pack(pady=5)
new_button3.pack(pady=5)
new_button5.pack(pady=5)
outbutton.pack(pady=5)

output_label = tk.Label(master=window)
output_label.pack()

window.mainloop()
