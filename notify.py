from plyer import notification  #pip install plyer

notification.notify(
        title = 'Hello there!',
        message = 'yes',
        app_name= 'Mnemosyne',
        app_icon= None,
        timeout = 10,
        toast= False
    )
