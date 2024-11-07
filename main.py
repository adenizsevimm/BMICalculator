from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=250,height=250)

#kg label kısmı
label1 = Label(text="Enter Your Weight kg")
label1.config(padx=10,pady=10)
label1.pack()
#kg veri alma kısmı
entry1 = Entry(width=20)
entry1.pack()
#cm label kısmı
label2 = Label(text ="Enter Your Height cm")
label2.config(padx=20,pady=20)
label2.pack()
#cm veri alma kısmı
entry2 = Entry(width=20)
entry2.pack()
# Sonucu göstermek için yeni bir label
result_label = Label(text="")
result_label.pack()


def button_clicked():
    # Kullanıcının girdiği verileri al ve sayıya çevir
    kg = float(entry1.get())
    cm = float(entry2.get())

    # BMI hesaplama
    bmi = kg / ((cm / 100) ** 2)

    # BMI kategorisini belirleme
    if bmi <= 16:
        category = "Severe Thinness"
    elif 16 < bmi <= 17:
        category = "Mild Thinness"
    elif 17 < bmi <= 18.5:
        category = "Moderate Thinness"
    elif 18.5 < bmi <= 25:
        category = "Normal"
    elif 25 < bmi <= 30:
        category = "Overweight"
    elif 30 <= bmi <= 35:
        category = "Obese Class I"
    elif 35 <= bmi <= 40:
        category = "Obese Class II"
    else:
        category = "Obese Class III"

    # Sonucu göster
    result_label.config(text=f"Your BMI is: {bmi:.2f}\nCategory: {category}")


# Buton kısmı
button = Button(text="Calculate", command=button_clicked)
button.config(padx=4, pady=4)
button.pack()

window.mainloop()