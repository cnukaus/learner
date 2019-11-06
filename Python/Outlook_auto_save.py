# modified from https://www.codementor.io/aliacetrefli/how-to-read-outlook-emails-by-python-jkp2ksk95

import win32com.client
import win32com
import os
import sys

f = open("testfile.txt","w+")

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
accounts= win32com.client.Dispatch("Outlook.Application").Session.Accounts;

def emailleri_al(folder,title,savepath):
    messages = folder.Items
    a=len(messages)
    if a>0:
        for message2 in messages:
             if title in message2.subject:
	             try:
	                sender = message2.SenderEmailAddress
	                if sender != "":
	                    print(sender, file=f)
	             except Exception as e:
	                print("exception"+str(e))
	                print(account.DeliveryStore.DisplayName, "deliveryStore")
	                pass

	             try:
	                print("saving")
	                for attachment in  message2.Attachments:
	                	print(attachment.DisplayName)
	                	attachment.SaveAsFile(savepath+attachment.DisplayName) 
 #SaveAsFile is a method only to be used on attachments


	                #message2.Close(0)
	             except:
	                 pass


savepath="c:\\temp"
email_subject_contains="keywords"
for account in accounts:
    global inbox
    inbox = outlook.Folders(account.DeliveryStore.DisplayName)
    print("****Account Name**********************************",file=f)
    print(account.DisplayName,file=f)
    print(account.DisplayName)
    print("***************************************************",file=f)
    folders = inbox.Folders

    for folder in folders:
        print(folder.name," folder")
        
        print("****Folder Name**********************************", file=f)
        print(folder, file=f)
        print("*************************************************", file=f)
        emailleri_al(folder,email_subject_contains,savepath)
        a = len(folder.folders)

        if a>0 :
            global z
            z = outlook.Folders(account.DeliveryStore.DisplayName).Folders(folder.name)
            x = z.Folders
            for y in x:
            	if y.name == "Inbox folder":
	                emailleri_al(y,email_subject_contains,savepath)
	                print("****Folder Name**********************************", file=f)
	                print("..."+y.name,file=f)
	                print("*************************************************", file=f)



print("Finished Succesfully")
'''is interacting with Outlook COM object. Since Outlook is a singleton, you are actually spawning a "hidden" instance of Outlook. '''
