from .viewsGame import *
from .viewsMarketplace import *
from .viewsProfil import *
from .viewsStronisi import *
from .viewsTexnisesci import *

def pageNotFound_(request, exception):
    return HttpResponseNotFound(Eroor404_E(request,exception))
