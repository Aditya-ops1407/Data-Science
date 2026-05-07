# Create DF using series

import pandas as pd


dict = {"Name":pd.Series(["Aditya","Vishnu","Adarsh","Poppins","Snitch"]),
        "Age":pd.Series([20,20,22,18,18]),
        "Course":pd.Series(["BCA","BCA","FST","IT","BCA"])}

df = pd.DataFrame(dict)

print(df)