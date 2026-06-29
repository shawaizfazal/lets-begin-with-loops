medical_cause=input ("did you have a medical cause (Y/N):").strip().upper()
if medical_cause =="Y":
      print("you are allowed") 
else:
 attend=int(input("enter the attendence")) 

 if attend >=75:
     print("allowed")
 else:
     print("not allowed")


