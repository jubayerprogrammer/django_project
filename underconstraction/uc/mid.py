from django.shortcuts import render
from uc.models import UnderConstraction
import os
from dotenv import load_dotenv






class UnderConstractionMid:
    def __init__(self,get_response):
        print("This section is work")
        self.get_response = get_response
        

    def __call__(self,request):
        if request.user.is_staff:
            return self.get_response(request)
        
        load_dotenv()

        uc_key = os.environ.get("BYPASS_KEY", "000")

        if "u" in request.GET and request.GET["u"] == uc_key:
            request.session["bypass"] = True
            request.session.set_expiry(0)

        if request.session.get("bypass",False):
            return self.get_response(request)    
                    



        


        try:
            uc = UnderConstraction.objects.first()
            if uc and uc.is_underconstraction:
                
                context= {
                    "uc_duration": uc.uc_duration,
                    "uc_note" :uc.uc_note,

                }
                return render(request,"uc/under_const.html",context)
        except:
            pass
            # return render(request,"uc/wrong.html")
        
        return self.get_response(request)
    
    



