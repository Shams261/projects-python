import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_windows = tk.Tk()
main_windows.geometry('1200x800')
main_windows.title('White Board')


main_menu = tk.Menu()

# file icons

file = tk.Menu(main_menu, tearoff=False)

new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')


# edit icons

edit = tk.Menu(main_menu, tearoff=False)

copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')


# view icons

view = tk.Menu(main_menu, tearoff=False)

tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')


# back_ground colors

back_ground_color = tk.Menu(main_menu, tearoff=False)

light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')


back_ground_choice = tk.StringVar()

color_icons = (light_default_icon, light_plus_icon, dark_icon,
               red_icon, monokai_icon, night_blue_icon)
color_dict = {
    'Light Default': ('#000000', '#ffffff'),
    'Light Plus': ('#474747', '#e0e0e0'),
    'Dark ': ('#c4c4c4', '#2d2d2d'),
    'Red ': ('#2d2d2d', '#ffe8e8'),
    'Monokai': ('#d3b774', '#474747'),
    'Night Blue': ('#ededed', '#6b9dc2')
}


# cascading
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Back_ground _color', menu=back_ground_color)


tool_bar = ttk.Label(main_windows)
tool_bar.pack(side=tk.TOP, fill=tk.X)

# font box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(
    tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Nakula'))
font_box.grid(row=0, column=0, padx=5)

# size box
size_var = tk.IntVar()
font_size = ttk.Combobox(
    tool_bar, width=14, textvariable=size_var, state='readonly')
font_size['values'] = tuple(range(6, 81))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)


# bold
bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_button = ttk.Button(tool_bar, image=bold_icon)
bold_button.grid(row=0, column=2, padx=5)

# italic
italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_button = ttk.Button(tool_bar, image=italic_icon)
italic_button.grid(row=0, column=3, padx=5)

# underline
underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_button = ttk.Button(tool_bar, image=underline_icon)
underline_button.grid(row=0, column=4, padx=5)

# font color button
font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_button = ttk.Button(tool_bar, image=font_color_icon)
font_color_button.grid(row=0, column=5, padx=5)


# align left
align_left_icon = tk.PhotoImage(file='icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

# align center
align_center_icon = tk.PhotoImage(file='icons2/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

# align right
align_right_icon = tk.PhotoImage(file='icons2/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)


text_editor = tk.Text(main_windows)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_windows)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)


current_font_family = 'Nakula'
current_font_size = 10


def change_font(main_windows):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))


def change_fontsize(main_windows):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)


# bold_button_functionality
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(
            font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(
            font=(current_font_family, current_font_size, 'normal'))


bold_button.configure(command=change_bold)


# italic_button_functionlaity
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(
            font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(
            font=(current_font_family, current_font_size, 'normal'))


italic_button.configure(command=change_italic)

# underline_button_functionality


def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(
            font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(
            font=(current_font_family, current_font_size, 'normal'))


underline_button.configure(command=change_underline)


# foreground_color_functionality

def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


# align_functionality

# left align
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')


align_left_btn.configure(command=align_left)

# center


def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')


align_center_btn.configure(command=align_center)

# right


def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')


align_right_btn.configure(command=align_right)


font_color_button.configure(command=change_font_color)


text_editor.configure(font=('Meera', 20))

status_bar = ttk.Label(main_windows, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False


def changed(main_windows):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        # if we don't want to count the spaces then we can use the replace function at the end of this line (.replace ('',''))
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Words : {words} Characters : {characters}')
    text_editor.edit_modified(False)


text_editor.bind('<<Modified>>', changed)


# variable
url = ''


# new_functionality


def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)


# new commands
file.add_command(label='New', image=new_icon, compound=tk.LEFT,
                 accelerator='Ctrl+N', command=new_file)

# open_functionality


def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(
    ), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_windows.title(os.path.basename(url))


# open commands
file.add_command(label='Open', image=open_icon, compound=tk.LEFT,
                 accelerator='Ctrl+O', command=open_file)

# save_file_function


def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(
                ('Text File', '*.txt'), ('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return


# save commands
file.add_command(label='Save', image=save_icon, compound=tk.LEFT,
                 accelerator='Ctrl+S', command=save_file)

# save_as_functionality


def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(
            ('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return


# save command
file.add_command(label='Save_as', image=save_as_icon,
                 compound=tk.LEFT, accelerator='Ctrl+Alt+S', command=save_file)

# Exit_functionality


def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel(
                'Save Document?', 'Your Changes will be lost if you do not save them. ')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(
                        ('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_windows.destroy()
            elif mbox is False:
                main_windows.destroy()
        else:
            main_windows.destroy()
    except:
        return


# exit command

file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT,
                 accelerator='Ctrl+Q', command=exit_func)


# find_functionality

def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(
                    word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config(
                    'match', foreground='red', background='blue')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0, 0)

    # frame
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    # labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text='Replace')

    # entry
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    # button
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text='Replace', command=replace)

    # label grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    # entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    # button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()


# edit_commands

edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT,
                 accelerator='Ctrl+C', command=lambda: text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT,
                 accelerator='Ctrl+V', command=lambda: text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X',
                 command=lambda: text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear_all_icon ', image=clear_all_icon, compound=tk.LEFT,
                 accelerator='Ctrl+Alt+X', command=lambda: text_editor.delete(1.0, tk.END))

# Find_command

edit.add_command(label='Find_icon', image=find_icon,
                 compound=tk.LEFT, accelerator='Ctrl+F', command=find_func)


# View_check_button

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)


def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True


view.add_checkbutton(label='Tool Bar', onvalue=True, offvalue=0, variable=show_toolbar,
                     image=tool_bar_icon, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar', onvalue=1, offvalue=False, variable=show_statusbar,
                     image=status_bar_icon, compound=tk.LEFT, command=hide_statusbar)


# Color_theme
def change_theme():
    chosen_theme = back_ground_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)


count = 0
for i in color_dict:
    back_ground_color.add_radiobutton(
        label=i, image=color_icons[count], variable=back_ground_choice, compound=tk.LEFT, command=change_theme)
    count += 1


main_windows.config(menu=main_menu)

# Bind_shortcut_keys

main_windows.bind("<Control-n>", new_file)
main_windows.bind("<Control-o>", open_file)
main_windows.bind("<Control-s>", save_file)
main_windows.bind("<Control-Alt-s>", save_as)
main_windows.bind("<Control-q>", exit_func)
main_windows.bind("<Control-f>", find_func)


main_windows.mainloop()
