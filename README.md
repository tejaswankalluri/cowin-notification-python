# cowin-notification-python

## Installations

-   First clone this repo
-   Install python in your PC [python download](https://www.python.org/downloads/)
-   Created an account in usebasin [usebasin](https://usebasin.com/)
-   Create a form in usebasin and add link to line 25 into the code
-   thats it you can add this python file on to your server and run it
-   free python server [link](https://www.pythonanywhere.com/)

## Commons errors

-   If you get an error like this
    ```
    Traceback (most recent call last):
    File "cowin.py", line 77, in <module>
    if temp == {} and getdata["sessions"] != [] and checkAgeandDose(getdata["sessions"], age, dose):
    KeyError: 'sessions'
    ```
    -   Then you have to use a indian proxy server
    -   you can get a free proxy [link](https://www.proxyhub.me/en/in-https-proxy-list.html)
    -   add it to line 35
    ```
    proxies ={
      "https": "proxylink:port",
      "http": "proxylink:port"
    }
    try:
        res = requests.get(url=url,headers=headers,proxies=proxies)
    ```
