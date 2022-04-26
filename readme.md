import ezhost,os
    aaa=input("Enter filename:")
    ezhost.upload(aaa,os.getenv("data"))
