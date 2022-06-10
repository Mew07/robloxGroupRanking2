from flask import Flask
from flask_restful import Api,Resource
import requests
import json
from flask import Response as r
app = Flask(__name__)
cookie = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_4EEE853C6ADC8D1E8FC913543D38E1C074CCD7D8E9B624E3822861CA7B72AFBFF151C9E75271EB7F8066D9E38063D1B72020BFB086663470174E361387C148573EF13325C67F0C195A68D35585CF72DBD65CE41E4E5FC255CCE70367AD6F83CF0CC3C8D65D91E19618E602762D7DE43EDD3A588DBCC526096C34D454FB63A728837041F9972C9F9B8AB2935C083BC2A094091D82BF9D86970A290C826DD698DE843267B499AA2BD9D44C0A7C5BA10164876D92DC2262E6C5A596583F88802A3BD1C8E9A2A9BCD3349E28F04F867FFA76A297899D8C6F1BF88F20A6A0C3C1CB9EB572B0635CFCB0FB50E8B9B4657291328681880D4F2F0B1CB019C3B748D4792F335F6BDD280D4095D7DD272E95324702298E97275AF3290972C543B857776B564A2D22DD4333EA08AE471EA48568B85AB27ADE52F0A0164177FDEB1AA8470B71E7280732F2AE02D8EA39B6CB9E27795A4398D22AA6766CD3B4C88E144A343CD1418BD21C4C994D85E759EBB04300CE02D745A857308A6923C514DA4F29C4A6736659536F0220FB93905310209E0DDB52533AC00A"


password = ""
groupid = ""
url = f"https://groups.roblox.com/v1/groups/{groupid}/users/"
authurl = "https://auth.roblox.com/v2/login"
api = Api(app)
def getXsrf():
  xsrfRequest = requests.post(authurl, cookies={'.ROBLOSECURITY': cookie})
  return xsrfRequest.headers["x-csrf-token"]
    



class rank(Resource):
  def get(self,userId,rank,key):
  
   
    if key == password:
      requestBody = json.dumps({"roleId" : rank})
      xsrf = getXsrf()
      Response = requests.request("PATCH",
        url+userId,

        headers= {
              "Cookie": ".ROBLOSECURITY=" + cookie,
              "Content-Type": "application/json",
              "Accept": "application/json",
              "X-CSRF-TOKEN": xsrf},
        data = requestBody
        )
      
      if Response.status_code == 200:
        return{
                "userId":userId,
                "rank":rank,
                "Status":Response.status_code}
      else:
        return r(status = Response.status_code)

    else:
      return r('''{acsess":"denied,
              status: incorrect key please double check what you entered or stop trying to hac D:}
                ''', status=403)
  
api.add_resource(rank,"/user/<string:userId>/rank/<string:rank>/key/<string:key>")

if __name__ == "__main__":
  app.run(debug=True)

