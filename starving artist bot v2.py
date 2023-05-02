from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from threading import *
import os
from PIL import Image
import time
import keyboard
import decimal
from decimal import Decimal
import pyautogui
import pydirectinput
import win32api
import win32con
import win32gui
file_path=''
image = ''
white_block=0
def rgb_to_hex(rgb):
    global hexa, wait_hexa
    hexa = str('%02x%02x%02x' % rgb)
    wait_hexa=0
def get_colors():
    global hexa, colors, wait_colors, wait_hexa, rgb,calcul_ETA, white_block
    global r, g, b
    for i3 in range(32):
        for i4 in range(32):
            x=i4
            y=i3
            (r, g, b) = image.getpixel((x, y))
            rgb_to_hex((r,g,b))
            if not (hexa in colors) and not (hexa in ['ffffff','fefefe']):
                colors.append(hexa)
                calcul_ETA+=1
            elif (hexa in ['ffffff','fefefe']):
                white_block = white_block+1
    wait_colors=0
def drawn():
    global x, y, colors, draw, delay, hexa, image, calcul_ETA, white_block
    delay = 0
    draw = 1
    x=0
    y=0
    if platform == 1:
        calcul_ETA=calcul_ETA+int((0.25*(1024-white_block)))
    elif platform ==2:
        calcul_ETA=calcul_ETA+int((0.125*(1024-white_block)))
    x= 0
    y= 0
    i=0
    i2=0
    counter=0
    mouseX=0
    mouseY=0
    l5.config(text = 'Click on your Roblox tab and let it draw (you can press "F" key to quit the app)')
    app.update()
    time.sleep(5)
    l5.config(text = 'We draw your pixel art')
    app.update()
    for i5 in range(len(colors)):
        if keyboard.is_pressed("f"):
            disable_event()
        if keyboard.is_pressed("p"):
            l5.config(text = 'Paused')
            app.update()
            keyboard.wait('v')
            l5.config(text = 'We draw your pixel art')
            app.update()
        hexa2=colors[i5]
        time.sleep(delay)
        if platform ==1:
            pydirectinput.moveTo(int(((1083-window_rect[0]) / 1928) * window_width+window_rect[0]), int(((828-window_rect[1]) / 1048) * window_height+window_rect[1]))
        if platform ==2:
            win32api.SetCursorPos((int(((1085-window_rect[0]) / 1928) * window_width+window_rect[0]), int(((825-window_rect[1]) / 1017) * window_height+window_rect[1])))
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 1, 0, 0)
        pyautogui.click()
        time.sleep(delay)
        if keyboard.is_pressed("f"):
            disable_event()
        if keyboard.is_pressed("p"):
            l5.config(text = 'Paused')
            app.update()
            keyboard.wait('v')
            l5.config(text = 'We draw your pixel art')
            app.update()
        if platform ==1:
            pydirectinput.moveTo(int(((1080-window_rect[0]) / 1928) * window_width+window_rect[0]), int(((745-window_rect[1]) / 1048) * window_height+window_rect[1]))
        elif platform==2:
            win32api.SetCursorPos((int(((1085-window_rect[0]) / 1928) * window_width+window_rect[0]), int(((745-window_rect[1]) / 1017) * window_height+window_rect[1])))
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 1, 0, 0)
        pyautogui.click()
        time.sleep(delay*2)
        pyautogui.typewrite(hexa2)
        time.sleep(delay*2)
        pydirectinput.press('enter')
        time.sleep(delay*2)
        if keyboard.is_pressed("f"):
            disable_event()
        if keyboard.is_pressed("p"):
            l5.config(text = 'Paused')
            app.update()
            keyboard.wait('v')
            l5.config(text = 'We draw your pixel art')
            app.update()
        time.sleep(delay)
        if platform == 1:
            pydirectinput.moveTo(int(((1083-window_rect[0]) / 1928) * window_width+window_rect[0]), int(((828-window_rect[1]) / 1048) * window_height+window_rect[1]))
        elif platform ==2:
            win32api.SetCursorPos((int(((1085-window_rect[0]) / 1928) * window_width+window_rect[0]), int(((825-window_rect[1]) / 1017) * window_height+window_rect[1])))
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 1, 0, 0)
        pyautogui.click()
        time.sleep(delay)
        calcul_ETA=calcul_ETA-1
        heures, reste = divmod(calcul_ETA, 3600)
        minutes, secondes = divmod(reste, 60)
        heures=int(heures)
        minutes=int(minutes)
        secondes=int(secondes)
        l6.config(text=str(float(Decimal(((counter/(1024-white_block))*100)).quantize(Decimal('1.00'))))+' % | ETA : '+f"{heures:02}:{minutes:02}:{secondes:02}")
        app.update()
        if keyboard.is_pressed("f"):
                    disable_event()
        if keyboard.is_pressed("p"):
            l5.config(text = 'Paused')
            app.update()
            keyboard.wait('v')
            l5.config(text = 'We draw your pixel art')
            app.update()
        for i in range(0,32):
            for i2 in range(0,32):
                if keyboard.is_pressed("f"):
                    disable_event()
                if keyboard.is_pressed("p"):
                    l5.config(text = 'Paused')
                    app.update()
                    keyboard.wait('v')
                    l5.config(text = 'We draw your pixel art')
                    app.update()
                x=i2
                y=i
                (r, g, b) = image.getpixel((x, y))
                rgb_to_hex((r, g, b))
                if hexa == hexa2:
                    if platform ==1:
                        mouseX=int(((int((666+(18.9*i2))//1)-window_rect[0]) / 1928) * window_width+window_rect[0])
                        mouseY=int(((int((180+(18.9*i))//1)-window_rect[1]) / 1048) * window_height+window_rect[1])
                        pydirectinput.moveTo(mouseX, mouseY)
                    elif platform ==2:
                        mouseX=int(((int((665+(19*i2))//1)-window_rect[0]) / 1928) * window_width+window_rect[0])
                        mouseY=int(((int((175+(19*i))//1)-window_rect[1]) / 1017) * window_height+window_rect[1])
                        win32api.SetCursorPos((mouseX, mouseY))
                        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1, 1, 0, 0)
                    pyautogui.click()
                    if platform ==1:
                        calcul_ETA=calcul_ETA-0.25
                    elif platform ==2:
                        calcul_ETA=calcul_ETA-0.125
                    heures, reste = divmod(calcul_ETA, 3600)
                    minutes, secondes = divmod(reste, 60)
                    heures=int(heures)
                    minutes=int(minutes)
                    secondes=int(secondes)
                    p1['value'] = float(Decimal(((counter/(1024-white_block))*100)).quantize(Decimal('1.00')))
                    l6.config(text=str(float(Decimal(((counter/(1024-white_block))*100)).quantize(Decimal('1.00'))))+' % | ETA : '+f"{heures:02}:{minutes:02}:{secondes:02}")
                    app.update()
                    counter+=1
                    if keyboard.is_pressed("f"):
                        disable_event()
                    if keyboard.is_pressed("p"):
                        l5.config(text = 'Paused')
                        app.update()
                        keyboard.wait('v')
                        l5.config(text = 'We draw your pixel art')
                        app.update()
                    time.sleep(delay)
    p1['value'] = 0
    l6.config(text='0 %')
    l5.config(text=': Drawing info :')
    image = ''
    draw=0
    os.remove(file_path[0:len(file_path)-4]+'_temp.jpg')
def load():
    global image, colors, calcul_ETA, white_block, platform 
    white_block=0
    calcul_ETA=0
    quality = int(spinbox1.get())
    if int(selected_platform.get()) != 0:
        if file_path != '' and draw == 0 and quality != '':
            platform=int(selected_platform.get())
            l5.config(text = 'Loading image...')
            app.update()
            image= Image.open(file_path)
            image = image.convert("RGB")
            image.save(file_path[0:len(file_path)-4]+'_temp.jpg', quality=quality)
            image = Image.open(file_path[0:len(file_path)-4]+'_temp.jpg')
            largeur, hauteur = image.size
            if largeur != 32 or hauteur != 32:
                image = image.resize((32,32))
            image.show()
            colors=[]
            get_colors()
            if platform == 1:
                calcul_ETA=calcul_ETA+int((0.25*(1024-white_block)))
            elif platform ==2:
                calcul_ETA=calcul_ETA+int((0.125*(1024-white_block)))
            heures, reste = divmod(calcul_ETA, 3600)
            minutes, secondes = divmod(reste, 60)
            heures=int(heures)
            minutes=int(minutes)
            secondes=int(secondes)
            l5.config(text = 'ETA : '+f"{heures:02}:{minutes:02}:{secondes:02}")
            app.update()
    else:
        l5.config(text='Choose your game version')
        app.update()
def browse_file():
    global file_path
    if draw == 0:
        file_path = filedialog.askopenfilename()
        if file_path != '':
            l4.config(text = file_path)
            app.update()
def threading3():
    global platform, hwnd, window_rect, client_rect, border_width, title_bar_height, window_width, window_height, screen_width, screen_height
    if image != '' and draw == 0 and int(selected_platform.get()) != 0 :
        try:
            hwnd=win32gui.FindWindow(None, "Roblox")
            window_rect = win32gui.GetWindowRect(hwnd)
            client_rect = win32gui.GetClientRect(hwnd)
            border_width = (window_rect[2] - window_rect[0] - client_rect[2]) // 2
            title_bar_height = window_rect[3] - window_rect[1] - client_rect[3] - border_width
            window_width = client_rect[2] - window_rect[0]
            window_height = client_rect[3] - window_rect[1]
            win32gui.SetForegroundWindow(hwnd)
            screen_width= win32api.GetSystemMetrics(0)
            screen_height= win32api.GetSystemMetrics(1)
            platform=int(selected_platform.get())
            t3=Thread(target=drawn)
            t3.start()
        except:
            l5.config(text='Your roblox tab aren\'t open')
            app.update()
    elif int(selected_platform.get()) == 0:
        l5.config(text='Choose your game version')
        app.update()
    else:
        l5.config(text='Load image first')
        app.update()
def disable_event():
    try:
        os.remove(file_path[0:len(file_path)-4]+'_temp.jpg')
    except:
        pass
    app.destroy()
hwnd=win32gui.FindWindow(None, "Roblox")
draw = 0
app = Tk()
app.title("Starving Artist BOT (press \"F\" to exit)")
app.geometry("580x350")
app.wm_attributes("-topmost", True)
app.resizable(False, False)
app.protocol("WM_DELETE_WINDOW", disable_event)
l1= ttk.Label(app, anchor='center', text = '" Starving Artist BOT (Press \"F\" to exit) " ')
l1.pack(pady=10)
l9 = ttk.Label(app, anchor='center', text = ' Select your roblox games version : ')
l9.pack()
selected_platform= StringVar()
selected_platform.set(0)
radio_frame = ttk.Frame(app)
radio_frame.pack(side="top", anchor="n")
r1 = ttk.Radiobutton(radio_frame, text="Legacy (web browser)", variable=selected_platform, value=2)
r1.pack(side='left',anchor="w")
r2 = ttk.Radiobutton(radio_frame, text="Microsoft Store", variable=selected_platform, value=1)
r2.pack(side='left',anchor="w")
l2= ttk.Label(app, anchor='center', text = "(Try to use an image with the same height/width to avoid stretching/flattening)")
l2.pack()
l2_2 = ttk.Label(app, anchor='center', text = "(Since the program reduces the image to 32 pixels, the image may not be exactly the same as the original)")
l2_2.pack()
b1 = ttk.Button(app, text="Browse", command=browse_file)
b1.pack()
l2= ttk.Label(app, anchor='center', text = "Votre \"image\" (only JPG) :  ")
l2.pack()
l4= ttk.Label(app, anchor='center', text=': Not selected :')
l4.pack()
l7= ttk.Label(app, anchor='center', text = 'Quality ( % ) :')
l7.pack()
quality_var= StringVar(app)
quality_var.set("100")
spinbox1 = ttk.Spinbox(app, from_=0, to=100, textvariable=quality_var)
spinbox1.pack()
l8= ttk.Label(app, anchor='center', text='( May can alterate the drawing time )')
l8.pack()
b2 = ttk.Button(app, text="Load image", command=load)
b2.pack()
b3 = ttk.Button(app, text="Draw", command=threading3)
b3.pack()
p1 = ttk.Progressbar(app, orient='horizontal', length=500, mode='determinate')
p1.pack()
l5= ttk.Label(app, anchor='center', text=': Drawing info :')
l5.pack()
l6= ttk.Label(app, anchor='center', text = '0 %')
l6.pack()
app.mainloop()