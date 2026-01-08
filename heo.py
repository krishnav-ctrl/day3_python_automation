def check_pass_fail(name,mark):
  if mark >= 35:
    print(name + "pass agita")
  else:
   print(name + "fail")
students = {"naveen":80,"arun":30,"vijay":95}
for s_name,s_mark in students.items():
    check_pass_fail(s_name,s_mark)