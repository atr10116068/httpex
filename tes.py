import webbrowser

url = 'https://pythonexamples.org'


try:
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"))
    webbrowser.get('chrome').open_new(url)
except Exception as e:
    print(f"Error : {e}")