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
The above profram will save a '.html' file in the given location.
It will open a '.html' document as shown below:

![Image](/images/1.png)
