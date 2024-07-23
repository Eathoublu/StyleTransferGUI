# coding:utf8

from tkinter import *
import tkinter.filedialog
from tkMessageBox import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from PIL import Image
from img_handler import *

root = Tk()
root.title('毕业设计项目')

did_select = 0

img_url = ''
image = PhotoImage(file="./default/default_ori.png")
img = Label(image=image, width=600, height=300)
# img.pack(side=LEFT)
img.grid(row=0, column=0, columnspan=6)

image_out = PhotoImage(file="./default/default_ori.png")
img_out = Label(image=image_out, width=600, height=300)
# img_out.pack(side=LEFT)
img_out.grid(row=0, column=7, columnspan=6)


def xz():

    global img, image, did_select

    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
        did_select = 1
        img.image = None
        img_url = filename
        print(img_url)
        lb.config(text="您选择了："+filename)
        im = Image.open(filename)
        im = im.resize((600, 300))
        im.save("./temp/img/tmp.png")
        image = PhotoImage(file="./temp/img/tmp.png")
        img.configure(image=image)
        # img.pack()
    else:
        did_select = 0
        lb.config(text="您没有选择任何文件")


def change():
    global did_select, image_out, img_out, chengdu, weitiao
    # print(var2.get())
    # print(chengdu.get())
    # print(weitiao.get())
    # print(li.get(li.curselection()))
    if did_select == 0:
        showinfo('请选择一张图片', '您还没有选择任何图片哦')
        return
    elif did_select == 1:
        # _chengdu = float(str(chengdu)) + float(str(weitiao))

        if li.get(li.curselection()) == '莫奈':
            color_handler.color_setter(color=var2.get())
            # img_handler_youhua1.change_youhua1(ero=int(chengdu.get()), dil=int(weitiao.get()))
            # print(int(chengdu.get()))
            cheng_du = int(chengdu.get())
            if cheng_du < 2:
                cheng_du = 2
            # print(int(weitiao.get()))
            img_handler_youhua1.change_youhua1(ero=cheng_du)
            image_out = PhotoImage(file='./temp/out/tmp_out.png')
            img_out.configure(image=image_out)

        if li.get(li.curselection()) == '原图':
            color_handler.color_setter(color=var2.get())
            image_out = PhotoImage(file='./temp/out/tmp_out.png')
            img_out.configure(image=image_out)

        # if li.get(li.curselection()) == '梵高':
        #     color_handler.color_setter(color=var2.get())
        #     img_handler_youhua2.change_youhua2()
        #
        #     image_out = PhotoImage(file='./temp/out/tmp_out.png')
        #     img_out.configure(image=image_out)

        # if li.get(li.curselection()) == '黑客帝国':
        #     color_handler.color_setter(color=var2.get())
        #

            # img_handler_matrix1.change_matrix1()
            #
            # image_out = PhotoImage(file='./temp/out/tmp_out.png')
            # img_out.configure(image=image_out)

        # if li.get(li.curselection()) == '水墨画':
        #     color_handler.color_setter(color=var2.get())
        #

            #
            # image_out = PhotoImage(file='./temp/out/tmp_out.png')
            # img_out.configure(image=image_out)

        if li.get(li.curselection()) == '葛饰北斋':
            color_handler.color_setter(color=var2.get())
            #
            img_handler_fsh.change_fsh()
            image_out = PhotoImage(file='./temp/out/tmp_out.png')
            img_out.configure(image=image_out)


        if li.get(li.curselection()) == '毕加索':
            color_handler.color_setter(color=var2.get())
            #
            img_handler_cubist.change_cubist()
            image_out = PhotoImage(file='./temp/out/tmp_out.png')
            img_out.configure(image=image_out)


        if li.get(li.curselection()) == '窗花':
            color_handler.color_setter(color=var2.get())
            #
            img_handler_mosaic.change_mosaic()
            image_out = PhotoImage(file='./temp/out/tmp_out.png')
            img_out.configure(image=image_out)


        if li.get(li.curselection()) == '李有行':
            color_handler.color_setter(color=var2.get())
            #
            img_handler_udnie.change_udnie()
            image_out = PhotoImage(file='./temp/out/tmp_out.png')
            img_out.configure(image=image_out)


        return


    return


lb = Label(root, text='')
# lb.pack(side=LEFT)
lb.grid(row=1, column=2, columnspan=10)
btn = Button(root, text="选择图片", command=xz, width=10, height=2, padx=15)
btn2 = Button(root, text='转换风格', command=change, width=10, height=2)

# btn2.pack(side=LEFT)
btn.grid(row=2, column=0)
# btn.pack(side=LEFT)
btn2.grid(row=2, column=1)

lb4 = Label(text='颜色风格：').grid(row=2, column=2)

var = StringVar()
var.set(('原图', '莫奈', '葛饰北斋', '毕加索', '李有行', '窗花'))
lb2 = Label(text='风格效果选择').grid(row=3, column=0, padx=15)
lb3 = Label(text='效果程度调节').grid(row=3, column=1, padx=15)
li = Listbox(root, listvariable=var)
li.grid(row=4, column=0, rowspan=3, padx=15, pady=15)
li.select_set(0, 0)

var2 = StringVar()
var2.set('REAL')

chengdu = StringVar()
weitiao = StringVar()

r1 = Radiobutton(root, text='黑白', variable=var2, value='BW').grid(row=2, column=3)
r2 = Radiobutton(root, text='灰度', variable=var2, value='GRAY').grid(row=2, column=4)
# r3 = Radiobutton(root, text='怀旧', variable=var2, value='OLD').grid(row=2, column=5)
r4 = Radiobutton(root, text='原色', variable=var2, value='REAL').grid(row=2, column=5)

s1 = Scale(root, label='程度', from_=0, to=10, orient=HORIZONTAL, length=200, variable=chengdu).grid(row=4, column=1, columnspan=2)
s2 = Scale(root, label='微调', from_=0, to=0.99, orient=HORIZONTAL, length=200, resolution=0.01, variable=weitiao).grid(row=5, column=1, columnspan=2)

root.mainloop()





