# YoutubeDownloader

#to create exe file using pyinstaller 
#preview function not yet working with pyinstaller


c:\users\nacar\appdata\local\programs\python\python310\lib\site-packages

pyinstaller --noconfirm --onedir --windowed --add-data "<CustomTkinter Location>/customtkinter;customtkinter/"  "<Path to Python Script>"


pyinstaller --noconfirm --onedir --windowed --add-data "c:\users\nacar\appdata\local\programs\python\python310\lib\site-packages\customtkinter;customtkinter\" "C:\Users\nacar\reposPython\YoutubeDownloader\projectGUI.py"