from customtkinter import *
from Global_Config import *
from PIL import Image, ImageTk
from random import *


root = CTk()

centreScreen(root, root,1000,550)
root.title("Animal Taxonomy")
root.maxsize(width = 1000, height = 550)
#root.iconbitmap(r"E:\Dhejus\PythonPractice\XII_Project\Animal_Taxonomy_CTK\icon\favicon6.ico")
#root.minsize(width = 1000, height = 550)
set_appearance_mode("Dark")

colour_list = [
    "#1E90FF" , "#2E2E2E", "#D3D3D3", #1
    "#007ACC", "#1A1A1A", "#F5F5F5", #2
    "#0A84FF", "#3A3A3A", "#C0C0C0", #3
    "#4682B4", "#2F2F2F", "#DCDCDC", #4
    "#6495ED", "#121212", "#E5E4E2", #5
    "#4169E1", "#353535", "#F8F8FF", #6
    "#00BFFF", "#2B2B2B", "#B0C4DE", #7
    "#5F9EAD", "#2D2D2D", "#E6E6FA", #8
    "#4682B4", "#191970", "#F0F8FF", #9
    "#00CED1", "#414A4C", "#E0FFFF" #10
    
]
trial = []

def refesh():
    trial.clear()
    for i in range(3):
        trial.append(choice(colour_list))
    #print()
    global glb_color_1, glb_color_2, glb_color_3
    print(trial) 
    
    glb_color_1 = trial[0]#"darkorchid2"# #FFC125 #FFCC70
    glb_color_2 = trial[1]#"dodgerblue3"
    glb_color_3 = trial[2]#"#308014"# darkorchid2, #308014 #c850c0

    # for i in f.winfo_children:
    #     i.destroy()
    f1.configure(border_color = glb_color_1)
    f2.configure(border_color = glb_color_2)
    f3.configure(border_color = glb_color_3)
    



glb_color_1 = ""# #FFC125 #FFCC70 #darkorchid2
glb_color_2 = "" #dodgerblue3
glb_color_3 = ""# darkorchid2, #308014 #c850c0

# global f
# f = CTkFrame(root, width=1000, height= 550, corner_radius=5, border_color="transparent", border_width=3)
# f.place(x = 0, y = 0)

f1 = CTkFrame(root, width=1000, height= 550, corner_radius=5, border_color=glb_color_1, border_width=3)

ref_btn = CTkButton(f1, text = "Refresh", command = lambda: refesh())
ref_btn.place(x = 850, y = 50)

f1.place(x = 1, y = 1)

f2 = CTkFrame(root, width=800, height= 350, corner_radius=5, border_color=glb_color_2, border_width=3)
f2.place(x = 100, y = 100)

f3 = CTkFrame(root, width=600, height= 150, corner_radius=5, border_color=glb_color_3, border_width=3)
bg_img = Image.open(r"images\Bg_with_overlapping_luxury_shapes.PNG")
bg_photo = ImageTk.PhotoImage(bg_img)
canvas = CTkCanvas(f1, width = 1000, height = 550)
canvas.pack(fill="both", expand= True)
canvas.create_image(2,2, anchor = "nw", image = bg_photo)

f3.place(x = 200, y = 200)


refesh()

root.mainloop()
