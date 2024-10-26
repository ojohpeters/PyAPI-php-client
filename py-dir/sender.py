import requests

baseurl = "http://127.0.0.1:5000/"
# posted = requests.post(baseurl+"/test", json=({"name":"dfsfadd","email":"rrjdsfadjxdh@jsnjffer","phone":"343433","password":"sbhscxc"}))

dell =  requests.delete(baseurl+"/test/jaksdjbh@jsnjda.sd")

# print(posted.json())
# input()
print(dell.json())
input()
gotten = requests.get(baseurl + "/test/")
print(gotten.json())

response = requests.delete(baseurl + "/test")
print(response)

response = requests.patch(baseurl + "/test/0")
print(response)