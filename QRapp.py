from pyqrcode import create
import tkinter
import socket


host = socket.gethostbyname(socket.gethostname())
print(host)

root = tkinter.Tk()
root.title('Qr Code Generator')


def gen_qr():
    global dta
    dta = host
    dta = create(dta)
    test = dta.xbm(scale=5)
    global xbm_image
    xbm_image = tkinter.BitmapImage(data=test, foreground="black", background='white')
    image_view.config(image=xbm_image)
    statement.config(text="this is a qr code for : " + str(host))


heading = tkinter.Label(root, text="QR code Generator", font="times 40")
make_button = tkinter.Button(root, text=" Make QR", font="times 20", command=gen_qr)
image_view = tkinter.Label(root)
statement = tkinter.Label(root)

# gui grid

heading.grid(row=0, column=0, columnspan=2)
make_button.grid(row=2, column=0, columnspan=2)
image_view.grid(row=3, column=0, columnspan=2)
statement.grid(row=4, column=0, columnspan=2)

root.mainloop()