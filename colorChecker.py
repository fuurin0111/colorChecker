import tkinter as tk

app = tk.Tk()
app.title("カラーチェッカー")
app.geometry("500x650")

canvas = tk.Canvas(
    app,
    width = 500,  # 水平サイズ
    height = 500,  # 垂直サイズ
    bg = "white",  # Appの背景色
)
canvas.pack()  # 配置

start_x, start_y = 0, 0
end_x, end_y = 500, 500
name = "name"

rectangle = canvas.create_rectangle(
    start_x, start_y, # 四角の左上
    end_x, end_y,  # 四角の右下
    outline = "gray",  # 枠の色
    fill = "#000",  # 中身の色
)

var_scale = tk.DoubleVar()
scale = tk.Scale(app,  orient="horizontal", from_=0, to=255, resolution=1, variable=var_scale,length = 500)
scale.pack()

var_scale2 = tk.DoubleVar()
scale2 = tk.Scale(app, orient="horizontal", from_=0, to=255, resolution=1, variable=var_scale2, length = 500)
scale2.pack()

var_scale3 = tk.DoubleVar()
scale3 = tk.Scale(app, orient="horizontal", from_=0, to=255, resolution=1, variable=var_scale3, length = 500)
scale3.pack()

label4 = tk.Label(app, text="#000000")
label4.pack()

def rgb(color1:int,color2:int,color3:int):
    color1 = hex(color1)[2:]
    if len(color1) == 1:
        color1 = "0"+color1
    color2 = hex(color2)[2:]
    if len(color2) == 1:
        color2 = "0"+color2
    color3 = hex(color3)[2:]
    if len(color3) == 1:
        color3 = "0"+color3
    return_rgb = "#"+ color1 + color2 + color3
    return return_rgb

def slider_scroll(event=None):
    global canvas,rectangle
    canvas.delete(rectangle)
    rectangle = canvas.create_rectangle(
        start_x, start_y, # 四角の左上
        end_x, end_y,  # 四角の右下
        outline = "gray",  # 枠の色
        fill = rgb(int(scale.get()),int(scale2.get()),int(scale3.get())),  # 中身の色
    )
    label4["text"] = rgb(int(scale.get()),int(scale2.get()),int(scale3.get()))
    app.after(5,slider_scroll)
    
app.after(5,slider_scroll)
app.mainloop()