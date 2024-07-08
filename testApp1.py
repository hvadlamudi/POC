# repose to df
import ast
import pandas as pd
from io import StringIO

with open('out.txt', 'r') as file:
    response = file.read().rstrip()
# Convert to dictionary
# print(response)
dict_obj = ast.literal_eval(str(response))
TESTDATA = (dict_obj["text"])
TESTDATA = StringIO(TESTDATA)
print (TESTDATA)

# df = pd.DataFrame.from_dict(dict_obj,  orient='index', columns=["Testcase ID", "Test case description", "Expected result ", " Actual result ", " Test data ", " Prerequisite ", "Screenshot"])
df = pd.read_csv(TESTDATA, sep="|")
# df.columns = df.iloc[0]
# df = df[1:]
df.drop(columns=[1,8])
df.drop([0,1])
print(df.shape)
print(df)
# print(df) # displaying the DataFrame
# st.dataframe(df)  # Same as st.write(df)

# string_data = ""
# Create a DataFrame from the string data
# df = pd.read_csv(StringIO(string_data), sep=\";\")
# print(df)