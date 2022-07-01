from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk
import numpy as np


class PyPhotoEditor:
	def __init__(self):
		self.root = Tk()
		self.init()

	def init(self):
		self.root.title('Photo Editor')
		self.root.iconphoto(True, ImageTk.PhotoImage(Image.open('resources/icon.jpg')))

		self.root.bind('<Escape>', self._close)

	def run(self):
		self.draw_menu()
		self.draw_widgets()

		self.root.mainloop()

	def draw_menu(self):
		menu_bar = Menu(self.root)

		file_menu = Menu(menu_bar, tearoff=0)
		file_menu.add_command(label='Open', command=self.open_new_image)
		file_menu.add_command(label='Open in gray', command=self.open_in_gray_image)
		menu_bar.add_cascade(label='File', menu=file_menu)

		effect_menu = Menu(menu_bar, tearoff=1)
		effect_menu.add_command(label='gray', command=self.do_gray_img)
		menu_bar.add_cascade(label='Effects', menu=effect_menu)

		self.root.configure(menu=menu_bar)

	def draw_widgets(self):
		pass

	def open_new_image(self):
		image_path = fd.askopenfilename(filetypes=(("images", ".jpeg .jpg .png"), ))
		img = Image.open(image_path)
		if self.root.winfo_screenwidth() <= 1920 and self.root.winfo_screenwidth() > 1400:
			img.thumbnail(size=(1500, 1000))
		elif self.root.winfo_screenwidth() <= 1400 and self.root.winfo_screenwidth() > 1100:
			img.thumbnail(size=(800, 600))
		print(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), sep='\n')
		print(Image.open(image_path))
		image = ImageTk.PhotoImage(img)
		image_pannel = Label(self.root, image=image)
		image_pannel.image = image
		image_pannel.pack()

	def do_gray_img(self):
		print(self.root.children)

	def open_in_gray_image(self):
		image_path = fd.askopenfilename(filetypes=(("images", ".jpeg .jpg .png"), ))
		img = Image.open(image_path).convert('L')
		if self.root.winfo_screenwidth() <= 1920 and self.root.winfo_screenwidth() > 1400:
			img.thumbnail(size=(1500, 1000))
		elif self.root.winfo_screenwidth() <= 1400 and self.root.winfo_screenwidth() > 1100:
			img.thumbnail(size=(800, 600))
		print(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), sep='\n')
		print(Image.open(image_path))
		image = ImageTk.PhotoImage(img)
		image_pannel = Label(self.root, image=image)
		image_pannel.image = image
		image_pannel.pack()

	def _close(self, event):
		self.root.quit()


if __name__ == '__main__':
	PyPhotoEditor().run()
