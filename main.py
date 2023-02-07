import Config as Conf
import Lib.Functions as Func
import json
import pandas as pd 


# BASE = Conf.base
# GATEWAY = BASE.replace("qualysapi","gateway")
# cleanPassword = Conf.PASSWORD.replace("%","%25")
# safePassword = cleanPassword.replace("&","%26")
# safePassword = safePassword.replace("#","%23")
# payload = 'username='+Conf.USERNAME+"&password="+safePassword+"&token=true&permissions=true"
# header = Func.getTokenHeader() 
# REQUEST_URL = GATEWAY+"/auth"
# response = Func.postRequest(REQUEST_URL,payload,header)
# if (response.ok != True):
#   print("Failed to get response from API")
#   exit()

# token = response.text


# URL = "/pm/v1/"

# PAGE_SIZE = Conf.PAGESIZE
# ACTION = "patchcatalog/patches?pageSize=10000&pageNumber=0"

# REQUEST_URL = GATEWAY + URL + ACTION
# header = Func.getHeaderBearer(token)
# payload = {}
# #getting a list of all Pataches
# response = Func.getRequest(REQUEST_URL,payload,header)

# if (response.ok != True):
#   print("Failed to get response from API")
#   exit()


# records = int(response.headers['count'])
# with open(Conf.RESPONSEJSON, "w") as f:
#     f.write(response.text.encode("utf8").decode("ascii", "ignore"))
#     f.close()

f = open(Conf.RESPONSEJSON)
data = json.load(f)

print("repsonse file contain the maximum number of records (10000)")



rows = []
Asset_Patch_Header = ['isSecurity','rebootRequired','vendorSeverity','title','type',\
    'appFamily','qid','enabled','platform','supersedes','patchId',\
    'isRollback','cve','vendor','kb','downloadMethod','id','supportedOs',\
    'architecture','packageDetails','product','advisory','vendorlink','osIdentifier','advisoryLink',\
    'deleted','isSuperseded','patchFeedProviderId','syncDateTime','vendorPatchId','modifiedDate','publishedDate',\
    'category','supersededBy','bulletin']
#     'installDate','lastUpdated']
for asset in data:
  row = {
    'isSecurity' : Func.tryToGetAttribute(asset,"isSecurity"),
    'rebootRequired' : Func.tryToGetAttribute(asset,"rebootRequired"),
    'vendorSeverity' : Func.tryToGetAttribute(asset,"vendorSeverity"),
    #'description' : Func.tryToGetAttribute(asset,"description"),
    'title' : Func.tryToGetAttribute(asset,"title"),
    'type' : Func.tryToGetAttribute(asset,"type"),
    'appFamily' : Func.tryToGetAttribute(asset,"appFamily"),
    'qid' : Func.tryToGetAttribute(asset,"isSecurity"),
    'enabled' : Func.tryToGetAttribute(asset,"enabled"),
    'platform' : Func.tryToGetAttribute(asset,"platform"),
    'supersedes' : Func.tryToGetAttribute(asset,"supersedes"),
    'patchId' : Func.tryToGetAttribute(asset,"patchId"),
    'isRollback' : Func.tryToGetAttribute(asset,"isRollback"),
    'cve' : Func.tryToGetAttribute(asset,"cve"),
    'vendor' : Func.tryToGetAttribute(asset,"vendor"),
    'kb' : Func.tryToGetAttribute(asset,"kb"),
    'downloadMethod' : Func.tryToGetAttribute(asset,"downloadMethod"),
    'id' : Func.tryToGetAttribute(asset,"id"),
    'supportedOs' : Func.tryToGetAttribute(asset,"supportedOs"),
    'architecture' : Func.tryToGetAttribute(asset,"architecture"),
    'packageDetails' : Func.tryToGetAttribute(asset,"packageDetails"),
    'product' : Func.tryToGetAttribute(asset,"product"),
    'advisory' : Func.tryToGetAttribute(asset,"isSecurity"),
    'vendorlink' : Func.tryToGetAttribute(asset,"vendorlink"),
    'osIdentifier' : Func.tryToGetAttribute(asset,"osIdentifier"),
    'advisoryLink' : Func.tryToGetAttribute(asset,"advisoryLink"),
    'deleted' : Func.tryToGetAttribute(asset,"deleted"),
    'isSuperseded' : Func.tryToGetAttribute(asset,"isSuperseded"),
    'patchFeedProviderId' : Func.tryToGetAttribute(asset,"patchFeedProviderId"),
    'syncDateTime' : Func.tryToGetAttribute(asset,"syncDateTime"),
    'vendorPatchId' : Func.tryToGetAttribute(asset,"vendorPatchId"),
    'modifiedDate' : Func.tryToGetAttribute(asset,"modifiedDate"),
    'publishedDate' : Func.tryToGetAttribute(asset,"publishedDate"),
    'category' : Func.tryToGetAttribute(asset,"category"),
    'supersededBy' : Func.tryToGetAttribute(asset,"supersededBy"),
    'bulletin' : Func.tryToGetAttribute(asset,"bulletin")
  }
  rows.append(row)




MyAssetData = pd.DataFrame(rows,columns=Asset_Patch_Header)
MyAssetData.to_csv(Conf.CSV_SW,index=False)


