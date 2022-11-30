import streamlit as st



def delim(file): 
       
    
        #read the selected file and apply it to variable elms
    elms = file.decode('utf-8')
        #replace the applicable parts of variable elms with the delimiters
    elms = elms.replace('e+002', 'e+002, ')
    elms = elms.replace('e+003', 'e+003, ')
    elms = elms.replace('e+004', 'e+004, ')
    elms = elms.replace('e+005', 'e+005, ')
    elms = elms.replace('e+006', 'e+006, ')
    elms = elms.replace('e+007', 'e+007, ')
    elms = elms.replace('e+008', 'e+008, ')
    elms = elms.replace('e+009', 'e+009, ')
   

    with open('final_file.txt', 'w') as magma_file:
        #write a file with the stored, altered text in variable elms
        magma_file.write(elms)
    #close the writeable file
    magma_file.close()
    st.success('Delimeters succesfully added')


#function to add the prefix elem n where n is the node number
def addElem(file):

    #create counting variables
    counter = 0
    linecount = 1

    #put file as string in variable checks
    checks = file.decode('utf-8')
    checks.splitlines()
    
    
    #check to see if the start of the file is formatted correctly   
    if checks[0].rstrip().endswith('5'):
        with open('final_file.txt', 'w') as ff:            
        #iterate through the lines in the file
            for line in checks:
                counter+=1
                    
                #skip every second (non-node) line
                if counter % 2 == 0:
                    #write the correct prepend with an incrementing number
                    ff.write('Elem ' + str(linecount) + ' ' + checks[line] + '\n')
                    #incrememt the number
                    linecount += 1
                        
                else:
                    #write the (non-node) line without prepend
                    ff.write(line + '\n')
        ff.close()
        st.success('Element labels successfully added.')
    else:
        st.warning("Don\'t forget to format the original file correctly. The first line should read '    1    5'")    
 
    
          
           