import getapi,json

tkn="Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXBpLnlvaGEucHJvL2FwaS9hdXRoL2xvZ2luIiwiaWF0IjoxNjYwOTgxOTQ2LCJleHAiOjE2NjE1ODY3NDYsIm5iZiI6MTY2MDk4MTk0NiwianRpIjoiOWRzcXZJMjVOM1hxSVpVbyIsInN1YiI6NDAyNTcyLCJwcnYiOiIyM2JkNWM4OTQ5ZjYwMGFkYjM5ZTcwMWM0MDA4NzJkYjdhNTk3NmY3In0.wCDGZo8-IPG48inIvL1-MjUoWuRflTXF9fEimTQ3SSY"
# xxx=getapi.profileuser(tkn,input("id user : "))["data"]

# print(json.dumps(xxx,indent=2))

ttt=getapi.updateuser(tkn)
print(ttt)