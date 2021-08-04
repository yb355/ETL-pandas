
# ETL-pandas

This is an application that takes the required data from Excel and performs necessary transformations to create a CSV file that corresponds to a correct format determined by the inventory optimization software. 
  
The backbone of this application is a Python data analysis and automation library called Pandas. More information:https://pandas.pydata.org/

This application utilizes a command-line interface to prompt the user questions regarding the location of the Excel's target columns, starting row, sheet name, etc. It then extracts the required information from the Excel file located in the input directory and transforms it. The transformed CSV file is created in the output folder and the original is moved to the history folder.
 
It was made with flexibility in mind, meaning other interactive input mechanisms (ex: web client instead of command-line) can be developed and the application can be further extended. 

The output file would look like that:

![example](https://user-images.githubusercontent.com/88110913/127644355-55d16841-b588-470e-ae20-21af95c7c0a7.jpg)
