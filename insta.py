from tkinter import*
from PIL import  Image,ImageTk
root=Tk()
root.title("Login.Instagram",)


x=Label(root,text="Instagram",fg="black",font=("Brush Script MT",70))
x.place(x=700,y=30)
x1=Label(root,text="username",font=("Arial",10),fg="black")
x1.place(x=750,y=150)
e1=Entry(root,fg="black",bg="white",bd=1,borderwidth=3)
e1.place(x=750,y=170)
x2=Label(root,text="password",fg="black",font=("Arial",10))
x2.place(x=750,y=200)
e2=Entry(root,fg="black",bg="white",bd=1,borderwidth=3)
e2.place(x=750,y=220)
def loginbtn():
    print("Log in Sucessfully")
btn=Button(root,text="Log in ",fg="white",bg="Deep Sky Blue",command=loginbtn)
btn.place(x=790,y=280)    
x3=Label(root,text="_______________________ OR _______________________",fg="black",font=("Arial",8))
x3.place(x=690,y=330)
path = Image.open("C:/Users/HP/OneDrive/Desktop/python1/f.png")
image = path.resize((20,20))  
photo = ImageTk.PhotoImage(image)



label_image = Label(root, image=photo)
label_image.place(x=750,y=390)
label_image.image = photo
x4=Label(root,text="Log in with Facebook",fg="Deep sky blue",font=("Arial",8))
x4.place(x=780,y=390)
x5=Label(root,text="Forget Password ?",fg="black",font=("Arial",8))
x5.place(x=760,y=430)
x6=Label(root,text="Don't have an Account?",fg="black",font=("Arial",8))
x6.place(x=730,y=460)
x7=Label(root,text="Sign up",fg="white",bg="deep sky blue",font=("Arial",8))
x7.place(x=850,y=460)
path = Image.open("C:/Users/HP/OneDrive/Desktop/python1/in2.png")
image = path.resize((500,600))  
photo = ImageTk.PhotoImage(image)



label_image = Label(root, image=photo)
label_image.place(x=100,y=50)
label_image.image = photo
x8=Label(root,text="Get the app",fg="black",font=("Arial",8))
x8.place(x=780,y=500)

path = Image.open("C:/Users/HP/OneDrive/Desktop/python1/google.png")
image = path.resize((100,50))  
photo = ImageTk.PhotoImage(image)



label_image = Label(root, image=photo)
label_image.place(x=700,y=550)
label_image.image = photo

path = Image.open("C:/Users/HP/OneDrive/Desktop/python1/m1.png")
image = path.resize((100,50))  
photo = ImageTk.PhotoImage(image)



label_image = Label(root, image=photo)
label_image.place(x=850,y=550)
label_image.image = photo
x9=Label(root,text="Meta        About        Blog       Help       API       Privacy        Terms        Location         Instagram Lite         Threads           Contact Uploading & Non-Users           Meta Verified",fg="Black",font=("Arial",12))
x9.place(x=200,y=680)
x10=Label(root,text="English  ^    @ 2025 Instagram from Meta",fg="Black",font=("Arial",10))
x10.place(x=600,y=720)



root.geometry("2000x2000")
root.mainloop()