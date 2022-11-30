import copy
import decimal
import streamlit as st
import os

#create Coordinate class

class Coordinate():
    def __init__(self, coordinate_name: str, values: list): 
        self.coordinate_name = coordinate_name
        self.values = values

    def __repr__(self):
        if self.coordinate_name is None:
            self.coordinate_name = "Unnamed_coordinate"
        else:
            self.coordinate_name =f"{self.coordinate_name}"
        return(f"Coordinate name={self.coordinate_name}, ",f"values = {self.values}, ")

    def formatNumbers(self):
        temp_list = []
        for node in self.values:
            temp_node = decimal.Decimal(node)
            temp_list.append(temp_node)
        self.values.clear()
        for node in temp_list:
            self.values.append(node)
        

#create list variables for known coordinates, and placeholder variables for unknown coordinate
#instances of the Coordinate class

colxx = []
colyy = []
colzz = []
colxy = []
colyz = []
colxz = []

list_filler = []

#create instances of coordinate class
coordxx = Coordinate('xx', colxx)
coordyy = Coordinate('yy', colyy)
coordzz = Coordinate('zz', colzz)
coordxy = Coordinate('xy', colxy)
coordyz = Coordinate('yz', colyz)
coordxz = Coordinate('xz', colxz)

#create more empty instances, to be used as needed
seven_coord = Coordinate('xxx', copy.deepcopy(list_filler))
eight_coord = Coordinate('yyy', copy.deepcopy(list_filler))
nine_coord = Coordinate('zzz', copy.deepcopy(list_filler))
ten_coord = Coordinate('xxy', copy.deepcopy(list_filler))
eleven_coord = Coordinate('yyz', copy.deepcopy(list_filler))

counter = 0

def addCol(col_name, originalFile, newcolfile):

    RESIDUAL_STRESS_TXT = originalFile.decode('utf-8')
    NEW_COLUMN_TXT = newcolfile.decode('utf-8')

    current_col = Coordinate('', [])
    global counter
    counter += 1
    if counter == 1:
        current_col = seven_coord
    elif counter == 2:
        current_col = eight_coord
    elif counter == 3:
        cuurent_col = nine_coord
    elif counter == 4:
        current_col = ten_coord
    elif counter == 5:
        current_col = eleven_coord
    else:
        #return False

        st.warning('Error - no columns available. Please exit program and inform support')
        return
       

    #name the column with the user input from main module
    current_col.coordinate_name=col_name   

    #split the txt file into individual lines (as arraylists)
    #with open(RESIDUAL_STRESS_TXT, 'r') as orig:
     #       fin = orig.read().splitlines()
    #orig.close()

    #reopen the txt file, and open the txt file with the new columns
    #turn the new column into the text file into an array
    #then write the data of the new column onto the end of every node 
    #line until there are no lines in the new column left
    #with open(os.path.join('txtdir', RESIDUAL_STRESS_TXT), 'w') as newOrig:
       # with open(os.path.join('txtdir',NEW_COLUMN_TXT), 'r') as newCol:
    with open('final_file.txt', 'w') as newOrig:
        i=0
        newCol_arr = NEW_COLUMN_TXT.split('\n')
        fin = RESIDUAL_STRESS_TXT.split('\n')
        for line in fin:
            if i < len(newCol_arr):
                if line.__contains__('e+00'):
                    newOrig.write(line + str(newCol_arr[i]).rstrip('\n') + ',' '\n')
                    i+=1
                else:
                    newOrig.write(line + '\n')
            else:
                newOrig.write(line + '\n')
        current_col.values=newCol_arr
       # newCol.close()
    newOrig.close()
    st.success('Column succesfully added to {}'.format(RESIDUAL_STRESS_TXT))