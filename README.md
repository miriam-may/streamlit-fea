# Python Streamlit App

This codebase is giving me issues. Streamlit uses "file-like objects" when you upload files, it being a web app so interacting with someone's file system is a no-no. <br/><br/>
The problem I am finding is that when I upload a file, interact with the "file like object" decoded to string, then write the string back to a .txt file, it is writing it back with <b>huge</b> line spacings. These render as extra newlines in VS Code, but if you look in the txt file, they are just large line spacings.<br/><br/>
As well, when I use splitlines() on the string I created from the file like object, the array it returns is completely empty. This makes no sense because the string is not empty, but it might have something to do with these large line spacings.