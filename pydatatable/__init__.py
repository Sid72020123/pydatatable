"""
Library to create graphical Tables from the given data. This library is made by Siddhesh Chavan! The module's version is 1.0.
Import Statement:
    import pydatatable

Documentation(Tutorial):
    For documentation go to -------

Credits:
    All code credits to Siddhesh Chavan

Information:
    Module made by:- Siddhesh Chavan
    Age:- 15 (as of 2021)
    Email:- siddheshchavan2020@gmail.com
    YouTube Channel:- Siddhesh Chavan (Link: https://www.youtube.com/channel/UCWcSxfT-SbqAktvGAsrtadQ)
    Scratch Account:- @Sid72020123 (Link: https://scratch.mit.edu/users/Sid72020123/)
    My self-made Website: https://Sid72020123.github.io
"""
import os
import time


class Table:
    def __init__(self, location, title='Table', table_border=5, border_color='Black', cell_padding=3, cell_spacing=0,
                 cell_horizontal_text_align='center', cell_vertical_text_align='middle', column_bg_color='Yellow',
                 data_bg_color='White', column_text_color='Black', data_text_color='Black', print_log=False):
        """
        Class to Create a Table from given data.
        :param location: The location of the table to be stored as a '.html' file.
        :param title: The Title of the Table.
        :param table_border: The Border of the table.
        :param border_color: The Border color of the table.
        :param cell_padding: The cell padding. The space between the cell contents and cell border.
        :param cell_spacing: The cell spacing. The space between the cell and table border.
        :param cell_horizontal_text_align: The horizontal align of the text in the table. The values are: 'left','center','right'.
        :param cell_vertical_text_align: The vertical align of the text in the table. The values are: 'top','bottom','center'.
        :param column_bg_color: The Background color of the column.
        :param data_bg_color: The Background color of the data.
        :param column_text_color: The text color of the column.
        :param data_text_color: The text color of the data.
        :param print_log: Set it to 'True' to see the log of making of the table.
        """
        self.location = location
        self.title = title
        self.data = []
        self.columns = []
        self.table_border = table_border
        self.border_color = border_color
        self.cell_padding = cell_padding
        self.cell_spacing = cell_spacing
        self.cell_horizontal_text_align = cell_horizontal_text_align
        self.cell_vertical_text_align = cell_vertical_text_align
        self.column_bg_color = column_bg_color
        self.data_bg_color = data_bg_color
        self.column_text_color = column_text_color
        self.data_text_color = data_text_color
        self.auto_update = False
        self.update_time = 5000
        self.wait = True
        self.print_log = print_log

    def add_data(self, data, columns):
        """
        Function to add the data to the table.
        :param data: The 2-d list of all data to be added.
        :param columns:  The 2-d list of all column data to be added. Make sure that the length of the data is equal to the length of the column list.
        """
        self.data = data
        self.columns = columns
        if self.print_log:
            print(f"'{self.title}': Creating Table.....")
        file = open(f'{self.location}.html', 'w')
        file.write(f"<html>\n<head>\n<title>\n{self.title}\n</title>\n</head>\n<body>\n<center><h1>{self.title}</h1>\n")
        file.write(
            f"<table border = '{self.table_border}' BorderColor='{self.border_color}' cellpadding='{self.cell_padding}' cellspacing='{self.cell_spacing}'>\n")
        file.write(
            f"<tr Valign='{self.cell_vertical_text_align}' bgcolor='{self.column_bg_color}' style='color: {self.column_text_color};'>\n")
        if self.print_log:
            print(f"'{self.title}': Adding Data.....")
        for i in range(0, len(columns)):
            file.write(
                f"<td align='{self.cell_horizontal_text_align}'>{columns[i]}</td>\n")
        file.write(f"</tr>\n")

        for i in range(0, len(data)):
            file.write(
                f"<tr Valign='{self.cell_vertical_text_align}' bgcolor='{self.data_bg_color}' style='color: {self.data_text_color};'>\n")
            for j in range(0, len(data[i])):
                file.write(
                    f"<td align='{self.cell_horizontal_text_align}'>{data[i][j]}</td>\n")
            file.write(f"</tr>\n")
        file.write(f"</table>\n</center>\n</body>\n</html>")
        file.close()
        if self.print_log:
            print(f"'{self.title}': Created Table!")

    def enable_auto_update(self, time=5000):
        """
        Function to enable auto update for a Table.
        :param time: The time  interval to update the data (in millisecond).
        """
        self.auto_update = True
        self.update_time = time
        if self.print_log:
            print(f"'{self.title}': Enabling Auto Update.....")
        file = open(f'{self.location}.html', 'w')
        file.write(
            f"<html>\n<head>\n<title>\n{self.title}\n</title>\n</head>\n<body onload='AutoRefresh({self.update_time})'>\n<center><h1>{self.title}</h1>\n")
        file.write(
            f"<table border = '{self.table_border}' BorderColor='{self.border_color}' cellpadding='{self.cell_padding}' cellspacing='{self.cell_spacing}'>\n")
        file.write(
            f"<tr Valign='{self.cell_vertical_text_align}' bgcolor='{self.column_bg_color}' style='color: {self.column_text_color};'>\n")
        for i in range(0, len(self.columns)):
            file.write(
                f"<td align='{self.cell_horizontal_text_align}'>{self.columns[i]}</td>\n")
        file.write(f"</tr>\n")

        for i in range(0, len(self.data)):
            file.write(
                f"<tr Valign='{self.cell_vertical_text_align}' bgcolor='{self.data_bg_color}' style='color: {self.data_text_color};'>\n")
            for j in range(0, len(self.data[i])):
                file.write(
                    f"<td align='{self.cell_horizontal_text_align}'>{self.data[i][j]}</td>\n")
            file.write(f"</tr>\n")
        file.write(f"</table>\n</center>\n</body>\n")
        file.write('<script>\nfunction AutoRefresh(t){\nsetInterval("location.reload(true);",' +
                   str(self.update_time) + ')\n}\n</script>')
        file.write("\n</html>")
        file.close()
        if self.print_log:
            print(f"'{self.title}': Auto Update Enabled!")

    def disable_auto_update(self):
        """
        Function to disable auto update to the Table.
        """
        self.auto_update = False
        if self.print_log:
            print(f"'{self.title}': Disabling Auto Update.....")
        file = open(f'{self.location}.html', 'w')
        file.write(f"<html>\n<head>\n<title>\n{self.title}\n</title>\n</head>\n<body>\n<center><h1>{self.title}</h1>\n")
        file.write(
            f"<table border = '{self.table_border}' BorderColor='{self.border_color}' cellpadding='{self.cell_padding}' cellspacing='{self.cell_spacing}'>\n")
        file.write(
            f"<tr Valign='{self.cell_vertical_text_align}' bgcolor='{self.column_bg_color}' style='color: {self.column_text_color};'>\n")
        for i in range(0, len(self.columns)):
            file.write(
                f"<td align='{self.cell_horizontal_text_align}'>{self.columns[i]}</td>\n")
        file.write(f"</tr>\n")

        for i in range(0, len(self.data)):
            file.write(
                f"<tr Valign='{self.cell_vertical_text_align}' bgcolor='{self.data_bg_color}' style='color: {self.data_text_color};'>\n")
            for j in range(0, len(self.data[i])):
                file.write(
                    f"<td align='{self.cell_horizontal_text_align}'>{self.data[i][j]}</td>\n")
            file.write(f"</tr>\n")
        file.write(f"</table>\n</center>\n</body>\n</html>")
        file.close()
        if self.print_log:
            print(f"'{self.title}': Auto Update Disabled!")

    def update_data(self, data, append=False, wait=True):
        """
        Function to update the data of a Table.
        :param data: The list of data to be updated.
        :param append:  If 'True' then it appends the new data with the previous data and shows the Table.
        :param wait: Wait for the data to update. Set it to 'True' to wait for the given time and then update the data or else set it to 'False' to update the data continuously.
        """
        self.wait = wait
        self.auto_update = True
        if self.print_log:
            print(f"'{self.title}': Updating Data.....")
        if append:
            self.data += data
        else:
            self.data = data
        if self.wait:
            time.sleep(self.update_time / 1000)
        file = open(f'{self.location}.html', 'w')
        file.write(
            f"<html>\n<head>\n<title>\n{self.title}\n</title>\n</head>\n<body onload='AutoRefresh({self.update_time})'>\n<center><h1>{self.title}</h1>\n")
        file.write(
            f"<table border = '{self.table_border}' BorderColor='{self.border_color}' cellpadding='{self.cell_padding}' cellspacing='{self.cell_spacing}'>\n")
        file.write(
            f"<tr Valign='{self.cell_vertical_text_align}' bgcolor='{self.column_bg_color}' style='color: {self.column_text_color};'>\n")
        for i in range(0, len(self.columns)):
            file.write(
                f"<td align='{self.cell_horizontal_text_align}'>{self.columns[i]}</td>\n")
        file.write(f"</tr>\n")

        for i in range(0, len(self.data)):
            file.write(
                f"<tr Valign='{self.cell_vertical_text_align}' bgcolor='{self.data_bg_color}' style='color: {self.data_text_color};'>\n")
            for j in range(0, len(self.data[i])):
                file.write(
                    f"<td align='{self.cell_horizontal_text_align}'>{self.data[i][j]}</td>\n")
            file.write(f"</tr>\n")
        file.write(f"</table>\n</center>\n</body>\n")
        file.write('<script>\nfunction AutoRefresh(t){\nsetInterval("location.reload(true);",' +
                   str(self.update_time) + ')\n}\n</script>')
        file.write("\n</html>")
        file.close()
        if self.print_log:
            print(f"'{self.title}': Data Updated!")

    def open(self):
        """
        Function to open the table automatically.
        """
        if self.print_log:
            print(f"'{self.title}': Opening Table.....")
        os.system(f'start {self.location}.html')
        if self.print_log:
            print(f"'{self.title}': Table Opened!")

    def print_settings(self):
        print(f"Table '{self.title}' settings:-")
        print(
            f"\tTable Name:- {self.title}\n\tTable Location:- {self.location}.html\n\tTable Border:- {self.table_border}\n\tBorder Color:- {self.border_color}\n\tCell padding:- {self.cell_padding}\n\tCell Spacing:- {self.cell_spacing}\n\tHorizontal Text Align:- {self.cell_horizontal_text_align}\n\tVertical Text Align:- {self.cell_vertical_text_align}\n\tColumn Background Color:- {self.column_bg_color}\n\tData Background Color:- {self.data_bg_color}\n\tColumn Font Color:- {self.column_text_color}\n\tData Font Color:- {self.data_text_color}\n\tPrint Log:- {self.print_log}")

class MultipleTables:
    def __init__(self, location, title="Multiple Chart", height=600, width=1000, frame_border=0, border=0,
                 border_color='Black'):
        """
        Class to create multiple tables on one page.
        :param location: The location of the '.html' page to be saved.
        :param title: The title of group of tables.
        :param height: The height of all frames.
        :param width: The width of all frames.
        :param frame_border: The frame border of all frames.
        :param border: The border width of all frames.
        :param border_color: The border color of all frames.
        """
        self.location = location
        self.title = title
        self.height = height
        self.width = width
        self.frame_border = frame_border
        self.border = border
        self.border_color = border_color
        self.frame_value = []
        self.frame_size = []
        self.table_locations = ''

    def add_chart(self, table_locations, frame_value=[], frame_size=[]):
        """
        Function to add the saved charts on one page.
        :param table_locations: The list of all the chart's saved locations to be added on one page. The elements should be separated by commas and should be in 'string' format. Please give the correct location along with the extension. The order of charts in the page is same as the order of files given in the list. You can change the values in the list to add the charts accordingly.
        :param frame_value: If you want to change the size of one chart in a page then give the chart's list index according to the 'table_locations' list and use the frame_size parameter to set a different size for that specified chart.
        :param frame_size: If you pass the 'frame_size' parameter, then give the size of that chart in a 2-d list. First is height and then width.
        """
        self.table_locations = table_locations
        self.frame_value = frame_value
        self.frame_size = frame_size
        frame_height = []
        frame_width = []
        for i in range(0, len(table_locations)):
            frame_height.append(self.height)
            frame_width.append(self.width)

        for i in range(0, len(table_locations)):
            for j in range(0, len(self.frame_value)):
                if i == self.frame_value[j]:
                    frame_height[i] = self.frame_size[j][0]
                    frame_width[i] = self.frame_size[j][1]

        file = open(f"{self.location}.html", "w")
        file.write(
            f"<html>\n<head>\n<title>\n{self.title}\n</title>\n</head>\n<body>\n<center>\n<h1>\n{self.title}\n</h1>\n</center>\n")
        for i in range(0, len(table_locations)):
            file.write(
                f"<iframe src = '{table_locations[i]}', width='{frame_width[i]}px', height = '{frame_height[i]}px', frameBorder='{self.frame_border}', style = 'border: {self.border}px solid {self.border_color}'>\n</iframe>\n")
        file.write("</body>\n</html>")
        file.close()

    def open(self):
        """
        Function to open the saved multiple charts.
        """
        os.system(f'start {self.location}.html')

    def print_settings(self):
        """
        Function to print the chart settings.
        """
        print(f"Multiple Tables - '{self.title}' settings:-\n\tTable Name:- {self.title}\n\tTable Type:- Multiple Table\n\tTable Location:- {self.location}.html\n\tTable Height:- {self.height}\n\tTable Width:- {self.width}\n\tTable Border:- {self.border}\n\tFrame Border:- {self.frame_border}\n\tBorder Color:- {self.border_color}")
        print(f"\tSub tables:-")
        for i in range(0, len(self.table_locations)):
            print(f"\t\t{i} -> {self.table_locations[i]}")
        print(f"\tDifferent Size:- ")
        for i in range(0, len(self.frame_value)):
            print(f"\t\t{self.frame_value[i]} -> {self.frame_size[i]}")
