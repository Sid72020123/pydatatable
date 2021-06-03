# pydatatable v1.0
## Python Library to create graphical table from the data and is with auto update feature!
```pydatatable``` is a Python library made to display graphical tables from the given data.
### Introduction
```pydatatable``` is a Python library made to display graphical tables from given data. It can create a graphical table in the form of a '.html' file. This library is made by Siddhesh Chavan(me). The table can even self update itself if you enable it.
### Installation
To install the library type: ```pip insall pydatatable``` in the command prompt.
### Import Statement
Type ```import pydatatable``` to import it after installation.
### Creating a Simple Table
To create a simple table, type:
```python
import pydatatable as table

table1 = table.Table(location = 'table_test', title='Simple Table') #Create a Table object.
all_data = [[1,1,1],[2,2,2]] #Define the 'all_data' list.
title = ['Title1','Title2','Title3'] #Define the 'title' list.
table1.add_data(data=all_data, columns=title) #Add data to the table.
table1.open() #Automatically open tha table.
``` 
The above program will save a '.html' file in the given location.
It will open a '.html' document as shown below:

![Image](/images/1.png)
## The Table Class
The Table class contains many features:
### Parameters:
The Table class's parameters:
* ```location``` --> The path to save the table.
* ```title``` --> The title of the table.
* ```table_border``` --> The boder of the table in integer format.
* ```border_color``` --> The boder colour of the table in string format like 'red', 'black', 'green', etc. and you can also use hexadecimal values as '#ff0000'
* ```cell_padding``` --> The space between the individual cell contents and the cell border. Use the value in integer format.
* ```cell_spacing``` -> The space between the cell border and the table border. Use the value in integer format.
* ```cell_horizontal_text_align``` --> The horizontal text align of the text in each cell. Use values like 'center', 'left', 'right'.
* ```cell_vertical_text_align``` --> The vertical text align of the text in each cell. Use values like 'middle', 'top', 'bottom'.
* ```column_bg_color``` --> The background colour of the columns in the table. Use any color or the hexadecimal value in string format.
* ```data_bg_color``` --> The background colour of the data in the table. Use any color or the hexadecimal value in string format.
* ```column_text_color``` --> The text colour of the text in columns.
* ```data_text_color``` --> The text colour of the text in the data rows.
* ```print_log``` --> Set it to ```True``` if you want the table making log to be printed out on the console.4
#### Use above parameters like:
```python
import pydatatable as table

table1 = table.Table(location='test_table', title='Table', table_border=5, border_color='Black', cell_padding=3, cell_spacing=0,
                 cell_horizontal_text_align='center', cell_vertical_text_align='middle', column_bg_color='Yellow',
                 data_bg_color='White', column_text_color='Black', data_text_color='Black', print_log=False) #Create a Table object.
all_data = [[1,1,1],[2,2,2]] #Define the 'all_data' list.
title = ['Title1','Title2','Title3'] #Define the 'title' list.
table1.add_data(data=all_data, columns=title) #Add data to the table.
table1.open() #Automatically open tha table.
```

### Functions:
#### 1. add_data(data, columns)
  Function to add the data to the table. 
  * The ```data``` should have a nested list with all the data. For example, ```data=[[1,1,1],[2,2,2]]```
  * The ```columns``` should have a list of all columns to be showwed in the table. For example, ```columns=['Title1','Title2','Title3']```
  
  **The length of the nested list, data, should be equal to the data in the columns as shown in the above example.**

#### 2. enable_auto_update(time=5000)
  Function to enable auto update teh table.
  * The ```time``` should be in milliseconds and integer format. It is the time after which teh table is updated.
