import os
import win32com.client

def save_attachments_from_latest_email(folder_name, save_path, sender_email):
    # Create Outlook application object
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    
    # Access the account
    account = outlook.Folders.Item("ratan.jha@edfin-india.com")
    
    # Select the folder within the account
    inbox = account.Folders.Item("Data connectivity")
    
    # Sort the messages by received time in descending order
    messages = inbox.Items
    messages.Sort("[ReceivedTime]", True)  # True indicates descending order
   
    # Loop through messages
    for message in messages:
        print(message)
        if message.Class == 43:  # 43 indicates a Mail Item
            try:
                sender_email_address = message.SenderEmailAddress
            except AttributeError:
                try:
                    sender_email_address = message.Sender.Address
                except AttributeError:
                    print("Sender email address not found.")
                    continue
            print(f"Sender email: {sender_email_address}")
            
            if sender_email_address.lower() == sender_email.lower():
                attachments = message.Attachments
                
                for attachment in attachments:
                    # Check attachment file extension
                    print(attachment.FileName)
                    if attachment.FileName.lower().endswith(('.xlsx', '.csv')):
                        # Save attachment
                        attachment.SaveAsFile(os.path.join(save_path, attachment.FileName))
                        print(f"DOWNLOAD:  Attachment {attachment.FileName} from {message.Subject} saved.")
                        
                # Process only the latest email
                break

# Define the folder name, save path, and sender email address
folder_name = "MAIL_AUTO_DATA_DOWNLOAD"
save_path = r"C:\Users\Ratan Kumar Jha\Desktop\MAIL_AUTO_DATA_DOWNLOAD"
sender_email = "/O=EXCHANGELABS/OU=EXCHANGE ADMINISTRATIVE GROUP (FYDIBOHF23SPDLT)/CN=RECIPIENTS/CN=9D1930D485AF4D0DBF56C07B289000FC-2739C1E2-77"

# Call the function
save_attachments_from_latest_email(folder_name, save_path, sender_email)
