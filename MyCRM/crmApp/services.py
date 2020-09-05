from .unitAPIs import AliApi

# ключи Али
appAliKey='31102380'
Alisecret='ea36c75363323184e6779cff827368d4'
AlisSessionKey='50000000b46gvlSAoYNrD9bGtGosBVRl9gEyhqRvenhMpaltVZEzoLTORH13ec5298w'

class serviceAli():
    def __init__(self):
        self.session = AliApi(app_key=appAliKey, secret=Alisecret, sessionkey=AlisSessionKey)


    def importProductsList(self):
        pass
