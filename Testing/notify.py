from plyer import notification  #pip install plyer

notification.notify(
        title = 'Hello there!',
        message = 'yes',
        app_name= 'Mnemosyne',
        app_icon= './App/images/Icon.ico',
        timeout = 10,
        toast= False
    )
