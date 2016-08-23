"""GUI number pad"""
import gtk

#window
win = gtk.Window()
win.connect("destroy",lambda w:gtk.main_quit())

box = gtk.VBox()
win.add(box)

entry = gtk.Entry()
box.pack_start(entry)

table = gtk.Table(2,2,gtk.TRUE)

#initialize the number values
a=[1,2,3,4,5,6,7,8,9,"#",0,"*"]
x=0
y=0

for i in a:
    button = gtk.Button(str(i))
    table.attach(button,x,x+1,y,y+1)
    x+=1
    if x>2:
        x=0
        y+=1

box.pack_start(table)

#view output
win.show_all()

#call function
gtk.main()
