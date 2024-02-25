# from flask import Flask, render_template, request, jsonify


# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch


# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")


# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('chat.html')


# @app.route("/get", methods=["GET", "POST"])
# def chat():
#     msg = request.form["msg"]
#     input = msg
#     return get_Chat_response(input)


# def get_Chat_response(text):

#     # Let's chat for 5 lines
#     for step in range(5):
#         # encode the new user input, add the eos_token and return a tensor in Pytorch
#         new_user_input_ids = tokenizer.encode(str(text) + tokenizer.eos_token, return_tensors='pt')

#         # append the new user input tokens to the chat history
#         bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

#         # generated a response while limiting the total chat history to 1000 tokens, 
#         chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

#         # pretty print last ouput tokens from bot
#         return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)


# if __name__ == '__main__':
#     app.run()




# from flask import Flask, render_template, request, jsonify


# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch


# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")


# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('chat.html')


# @app.route("/get", methods=["GET", "POST"])
# def chat():
#     msg = request.form["msg"]
#     input = msg
#     return get_Chat_response(input)


# import random

# # Define some random questions and corresponding answers
# random_questions = [
#     "What's your favorite color?",
#     "What do you like to do in your free time?",
#     "Do you have any pets?",
#     "What's your favorite food?",
#     "where is inzint located?"
# ]

# random_answers = [
#     "My favorite color is blue.",
#     "I enjoy reading books in my free time.",
#     "Yes, I have a dog named Max.",
#     "Pizza is my favorite food!",
#     "inzint is located in Noida"
# ]

# def get_Chat_response(text):
#     # Check if the input matches any of the predefined questions
#     if text in random_questions:
#         # Find the index of the question
#         index = random_questions.index(text)
#         # Return the corresponding answer
#         return random_answers[index]
    
#     # If the input is not a predefined question, proceed with the dialogue generation
#     for step in range(5):
#         new_user_input_ids = tokenizer.encode(str(text) + tokenizer.eos_token, return_tensors='pt')
#         bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids
#         chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
#         return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)


# if __name__ == '__main__':
#     app.run()





# from flask import Flask, render_template, request, jsonify


# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch


# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")


# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('chat.html')


# @app.route("/get", methods=["GET", "POST"])
# def chat():
#     msg = request.form["msg"]
#     input = msg
#     return get_Chat_response(input)


# def get_Chat_response(text):

#     # Let's chat for 5 lines
#     for step in range(5):
#         # encode the new user input, add the eos_token and return a tensor in Pytorch
#         new_user_input_ids = tokenizer.encode(str(text) + tokenizer.eos_token, return_tensors='pt')

#         # append the new user input tokens to the chat history
#         bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

#         # generated a response while limiting the total chat history to 1000 tokens, 
#         chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

#         # pretty print last ouput tokens from bot
#         return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)


# if __name__ == '__main__':
#     app.run()


# -----------------------------------------------------------------------------------------

# from flask import Flask, render_template, request, jsonify


# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch


# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")


# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('chat.html')


# @app.route("/get", methods=["GET", "POST"])
# def chat():
#     msg = request.form["msg"]
#     input = msg
#     return get_Chat_response(input)


# import random

# # Define some random questions and corresponding answers
# random_questions = [
#     "What's your favorite color?",
#     "What do you like to do in your free time?",
#     "Do you have any pets?",
#     "What's your favorite food?",
#     "where is inzint located?",
#     "How do I reset my password?",
#     "What are your support hours?",
#     "How can I contact customer support?",
#     "I'm having trouble logging into my account. What should I do?",
#     "How long does it take to receive a response from customer support?",
#     "Can I track the status of my support ticket?",
#     "What information should I provide when submitting a support ticket?",
#     "How do I update my billing information?",
#     "Do you offer refunds?",
#     "Can I cancel my subscription?",
#     "How do I download the latest version of the software?",
#     "Are there any known issues or outages with your service?",
#     "Can I upgrade my account to a higher tier?",
#     "How do I access my account from a different device?",
#     "Do you offer technical support for your products?",
#     "How secure is my data with your service?",
#     "Can I change my account settings?",
#     "Is there a user manual or documentation available for your products?",
#     "How do I report a bug or issue with your software?",
#     "Do you offer training or tutorials for your products?",
#     "Can I customize the settings or features of your software?",
#     "How do I unsubscribe from marketing emails?",
#     "Can I access my account offline?",
#     "How do I provide feedback or suggestions for improvement?",
#     "Are there any known compatibility issues with your software and other applications?",
#     "How do I set up automatic backups for my data?",
#     "Can I access historical support tickets?",
#      "How do I change the language or region settings in my account?",
#     "Is there a mobile app available for your service?",
#     "Can I access support documentation offline?",
#     "How do I set up two-factor authentication for my account?",
#     "Can I change my username?",
#     "How do I delete my account?",
#     "How do I recover a deleted file or document?",
#     "How do I set up email notifications for new messages or updates?",
#     "Can I access support through social media channels?",
#     "How do I change my subscription plan?",
#     "Can I request a feature or enhancement for your software?",
#     "How do I access previous invoices or billing statements?",
#     "How do I set up auto-reply messages for customer inquiries?",
#     "How do I transfer ownership of an account or subscription?",
#     "Can I integrate your service with other tools or applications?",
#     "How do I change the currency for my billing?",
#     "Is there a limit to the number of support tickets I can submit?",
#     "How do I set up email forwarding for support inquiries?",
#     "Can I access support documentation in multiple languages?",
#     "How do I escalate a support ticket?",
#     "How do I check the status of a service outage or maintenance?",
#     "Can I schedule a call with a support representative?",
#     "How do I enable/disable notifications for new messages?",
#     "Is there a limit to the number of devices I can use with my account?",
#     "How do I change the primary contact for my account?",
#     "Can I access support through live chat?",
#     "How do I create a support ticket?",
#     "Can I export my data from your service?",
#      "How do I change my notification preferences?",
#     "How do I access training materials or resources?",
#     "How do I set up email alerts for support tickets?",
#     "Can I access support documentation without logging in?",
#     "How do I add users to my account?",
#     "How do I set up automatic replies for incoming emails?",
#     "Do you know shilpi",
#     "where is inzint located?",
#     "where is the address of Inzint?",
#     "who is Ravi Gf?"
    



# ]

# random_answers = [
#     "My favorite color is blue.",
#     "I enjoy reading books in my free time.",
#     "Yes, I have a dog named Max.",
#     "Pizza is my favorite food!",
#     "inzint is located in Noida",
#     "To reset your password, please visit our website and click on the 'Forgot Password' link. Follow the instructions to reset your password.",
#     "Our support team is available from Monday to Friday, 9 AM to 5 PM Eastern Time.",
#     "You can contact our customer support team by phone at 1-800-123-4567 or by email at support@example.com.",
#     "If you're having trouble logging in, please double-check your username and password. If the issue persists, contact our support team for further assistance.",
#     "We strive to respond to all inquiries within 24 hours. However, during busy periods, it may take longer to receive a response.",
#     "Yes, you can track the status of your support ticket by logging into your account on our website and navigating to the 'Support Tickets' section.",
#     "When submitting a support ticket, please provide your name, email address, a detailed description of the issue, and any relevant screenshots or error messages.",
#     "To update your billing information, log into your account on our website and navigate to the 'Billing' or 'Account Settings' section.",
#     "Refund policies vary depending on the product or service. Please refer to our terms and conditions or contact our support team for more information.",
#     "Yes, you can cancel your subscription at any time by contacting our support team or visiting the subscription management section of your account.",
#     "You can download the latest version of the software from our website's download section. Make sure to select the appropriate version for your operating system.",
#     "We strive to minimize service disruptions, but occasionally, issues may arise. You can check our status page or contact support for updates on any known issues or outages.",
#     "Yes, you can upgrade your account to a higher tier by contacting our sales team or visiting the account upgrade section of your account.",
#     "You can access your account from a different device by logging in with your username and password on our website or mobile app.",
#     "Yes, we offer technical support for our products. If you encounter any technical issues, please contact our support team for assistance.",
#     "We take the security of your data seriously and use industry-standard encryption and security protocols to protect it. Your data is safe with us.",
#     "Yes, you can change your account settings, such as your email address or notification preferences, by logging into your account on our website.",
#     "Yes, we provide user manuals and documentation for our products. You can find them on our website's support page or in the product's help section.",
#     "If you encounter a bug or issue with our software, please report it to our support team with as much detail as possible, including steps to reproduce the issue.",
#     "Yes, we offer training sessions and tutorials for our products. You can schedule a training session with our support team or access tutorials on our website.",
#     "Yes, many of our software products allow for customization of settings and features to suit your specific needs. Contact our support team for assistance with customization.",
#     "You can unsubscribe from marketing emails by clicking the 'Unsubscribe' link at the bottom of any marketing email you receive from us.",
#     "Most of our services require an internet connection to access. However, some features may be available offline. Contact our support team for more information.",
#     "We welcome feedback and suggestions for improvement. You can submit feedback through our website's contact form or by emailing our support team directly.",
#     "We strive to ensure compatibility with popular software and applications, but occasionally, compatibility issues may arise. Contact our support team for assistance.",
#     "You can set up automatic backups for your data through the settings or preferences section of our software. Consult the user manual or contact support for assistance.",
#     "Yes, you can access historical support tickets by logging into your account on our website and navigating to the 'Support Tickets' or 'Ticket History' section.",
#      "You can change the language or region settings in your account by accessing the settings or preferences section of our website or software.",
#     "Yes, we offer a mobile app for some of our services. You can download the app from the App Store or Google Play Store.",
#     "Yes, you can download support documentation for offline access from our website's support page or product help section.",
#     "You can set up two-factor authentication for your account through the security settings section of our website or software.",
#     "In most cases, you cannot change your username once it has been created. Contact our support team for assistance if you need to change your username.",
#     "You can delete your account by contacting our support team and requesting an account deletion. Please note that account deletion is irreversible and will result in the loss of all data associated with your account.",
#     "If you accidentally delete a file or document, contact our support team as soon as possible for assistance with recovery. We may be able to restore the file from backup.",
#     "You can set up email notifications for new messages or updates through the notification settings section of our website or software.",
#     "Yes, you can contact our support team through social media channels such as Twitter or Facebook. However, we recommend contacting support through official channels for faster assistance.",
#     "You can change your subscription plan by logging into your account on our website and navigating to the subscription or billing section.",
#     "Yes, you can request a feature or enhancement for our software by submitting a feature request through our website's contact form or by emailing our support team directly.",
#     "You can access previous invoices or billing statements by logging into your account on our website and navigating to the billing or account settings section.",
#     "You can set up auto-reply messages for customer inquiries through the settings or preferences section of our customer support platform.",
#     "To transfer ownership of an account or subscription, contact our support team and provide the necessary details for the transfer.",
#     "Yes, many of our services offer integrations with other tools or applications. Contact our support team for assistance with integration.",
#     "You can change the currency for your billing by contacting our support team and requesting a currency change.",
#     "There may be a limit to the number of support tickets you can submit depending on your subscription plan. Contact our support team for more information.",
#     "You can set up email forwarding for support inquiries through your email settings or by contacting our support team for assistance.",
#     "Yes, we offer support documentation in multiple languages. You can select your preferred language from the language settings section of our website or software.",
#     "If you need to escalate a support ticket, contact our support team and request escalation. Please provide the ticket number and any relevant details for the escalation.",
#     "You can check the status of a service outage or maintenance on our status page or by contacting our support team for updates.",
#     "Yes, you can schedule a call with a support representative by contacting our support team and requesting a callback.",
#     "You can enable/disable notifications for new messages through the notification settings section of our website or software.",
#     "There may be a limit to the number of devices you can use with your account depending on your subscription plan. Contact our support team for more information.",
#     "You can change the primary contact for your account by logging into your account on our website and navigating to the account settings or contact information section.",
#     "Yes, you can access support through live chat on our website during our support hours. Look for the chat icon in the bottom corner of the page.",
#     "You can create a support ticket by logging into your account on our website and navigating to the support or help section. Click on the 'Create Ticket' button and fill out the required information.",
#     "Yes, you can export your data from our service by accessing the export or backup settings section of our website or software.",
#     "You can change your notification preferences by logging into your account on our website and navigating to the notification settings or preferences section.",
#     "You can access training materials or resources through the training or resources section of our website or software.",
#     "You can set up email alerts for support tickets through the notification settings section of our website or software.",
#     "Yes, you can access support documentation without logging in by visiting our website's support page or product help section.",
#     "You can add users to your account by logging into your account on our website and navigating to the users or team section. Click on the 'Add User' button and fill out the required information.",
#     "You can set up automatic replies for incoming emails through your email settings or by contacting our support team for assistance.",
#     "yes, you mean beauty!",
#     "B-111 Sector-65 Noida, UP",
#     "B-111 sector-65 Noida, UP",
#     "One and only Priyanka Pandey!"
# ]

# def get_Chat_response(text):
#     # Check if the input matches any of the predefined questions
#     if text in random_questions:
#         # Find the index of the question
#         index = random_questions.index(text)
#         # Return the corresponding answer
#         return random_answers[index]
    
#     # If the input is not a predefined question, proceed with the dialogue generation
#     for step in range(5):
#         new_user_input_ids = tokenizer.encode(str(text) + tokenizer.eos_token, return_tensors='pt')
#         bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids
#         chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
#         return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)


# if __name__ == '__main__':
#     app.run()



# ******************************************************************************>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#model with functionality that it caan return whole ans if i ask question in one word
from flask import Flask, render_template, request
# Lists of predefined questions and answers
qa_pairs = [

    ("How do I reset my password?", "To reset your password, please visit our website and click on the 'Forgot Password' link. Follow the instructions to reset your password."),
    ("What are your support hours?", "Our support team is available from Monday to Friday, 9 AM to 5 PM Eastern Time."),
    ("How can I contact customer support?", "You can contact our customer support team by phone at 1-800-123-4567 or by email at support@example.com."),
    ("I'm having trouble logging into my account. What should I do?", "If you're having trouble logging in, please double-check your username and password. If the issue persists, contact our support team for further assistance."),
    ("How long does it take to receive a response from customer support?", "We strive to respond to all inquiries within 24 hours. However, during busy periods, it may take longer to receive a response."),
    ("Can I track the status of my support ticket?", "Yes, you can track the status of your support ticket by logging into your account on our website and navigating to the 'Support Tickets' section."),
    ("What information should I provide when submitting a support ticket?", "When submitting a support ticket, please provide your name, email address, a detailed description of the issue, and any relevant screenshots or error messages."),
    ("How do I update my billing information?", "To update your billing information, log into your account on our website and navigate to the 'Billing' or 'Account Settings' section."),
    ("Do you offer refunds?", "Refund policies vary depending on the product or service. Please refer to our terms and conditions or contact our support team for more information."),
    ("Can I cancel my subscription?", "Yes, you can cancel your subscription at any time by contacting our support team or visiting the subscription management section of your account."),
    ("How do I download the latest version of the software?", "You can download the latest version of the software from our website's download section. Make sure to select the appropriate version for your operating system."),
    ("Are there any known issues or outages with your service?", "We strive to minimize service disruptions, but occasionally, issues may arise. You can check our status page or contact support for updates on any known issues or outages."),
    ("Can I upgrade my account to a higher tier?", "Yes, you can upgrade your account to a higher tier by contacting our sales team or visiting the account upgrade section of your account."),
    ( "How do I access my account from a different device?", "You can access your account from a different device by logging in with your username and password on our website or mobile app."),
    ("Do you offer technical support for your products?", "Yes, we offer technical support for our products. If you encounter any technical issues, please contact our support team for assistance."),
    ("How secure is my data with your service?", "We take the security of your data seriously and use industry-standard encryption and security protocols to protect it. Your data is safe with us."),
    ("Can I change my account settings?", "Yes, you can change your account settings, such as your email address or notification preferences, by logging into your account on our website."),
    ("Is there a user manual or documentation available for your products?", "Yes, we provide user manuals and documentation for our products. You can find them on our website's support page or in the product's help section."),
    ("How do I report a bug or issue with your software?", "If you encounter a bug or issue with our software, please report it to our support team with as much detail as possible, including steps to reproduce the issue."),
    ("Do you offer training or tutorials for your products?", "Yes, we offer training sessions and tutorials for our products. You can schedule a training session with our support team or access tutorials on our website."),
    ("Can I customize the settings or features of your software?", "Yes, many of our software products allow for customization of settings and features to suit your specific needs. Contact our support team for assistance with customization."),
    ("How do I unsubscribe from marketing emails?", "You can unsubscribe from marketing emails by clicking the 'Unsubscribe' link at the bottom of any marketing email you receive from us."),
    ("Can I access my account offline?", "Most of our services require an internet connection to access. However, some features may be available offline. Contact our support team for more information."),
    ("How do I provide feedback or suggestions for improvement?", "We welcome feedback and suggestions for improvement. You can submit feedback through our website's contact form or by emailing our support team directly."),
    ("Are there any known compatibility issues with your software and other applications?", "We strive to ensure compatibility with popular software and applications, but occasionally, compatibility issues may arise. Contact our support team for assistance."),
    ("How do I set up automatic backups for my data?", "You can set up automatic backups for your data through the settings or preferences section of our software. Consult the user manual or contact support for assistance."),
    ("Can I access historical support tickets?", "Yes, you can access historical support tickets by logging into your account on our website and navigating to the 'Support Tickets' or 'Ticket History' section."),
    ("How do I change the language or region settings in my account?", "You can change the language or region settings in your account by accessing the settings or preferences section of our website or software."),
    ("Is there a mobile app available for your service?", "Yes, we offer a mobile app for some of our services. You can download the app from the App Store or Google Play Store."),
    ("Can I access support documentation offline?", "Yes, you can download support documentation for offline access from our website's support page or product help section."),
    ("How do I set up two-factor authentication for my account?", "You can set up two-factor authentication for your account through the security settings section of our website or software."),
    ( "Can I change my username?", "In most cases, you cannot change your username once it has been created. Contact our support team for assistance if you need to change your username."),
    ("How do I delete my account?", "You can delete your account by contacting our support team and requesting an account deletion. Please note that account deletion is irreversible and will result in the loss of all data associated with your account."),
    ( "How do I recover a deleted file or document?", "If you accidentally delete a file or document, contact our support team as soon as possible for assistance with recovery. We may be able to restore the file from backup."),
    ("How do I set up email notifications for new messages or updates?", "You can set up email notifications for new messages or updates through the notification settings section of our website or software."),
    ( "Can I access support through social media channels?", "Yes, you can contact our support team through social media channels such as Twitter or Facebook. However, we recommend contacting support through official channels for faster assistance."),
    ( "How do I change my subscription plan?", "You can change your subscription plan by logging into your account on our website and navigating to the subscription or billing section."),
    ( "Can I request a feature or enhancement for your software?", "Yes, you can request a feature or enhancement for our software by submitting a feature request through our website's contact form or by emailing our support team directly."),
    ("How do I access previous invoices or billing statements?", "You can access previous invoices or billing statements by logging into your account on our website and navigating to the billing or account settings section."),
    ("How do I set up auto-reply messages for customer inquiries?", "You can set up auto-reply messages for customer inquiries through the settings or preferences section of our customer support platform."),
    ( "How do I transfer ownership of an account or subscription?", "To transfer ownership of an account or subscription, contact our support team and provide the necessary details for the transfer."),
    (  "Can I integrate your service with other tools or applications?", "Yes, many of our services offer integrations with other tools or applications. Contact our support team for assistance with integration."),
    ("How do I change the currency for my billing?", "You can change the currency for your billing by contacting our support team and requesting a currency change."),
    ( "Is there a limit to the number of support tickets I can submit?", "There may be a limit to the number of support tickets you can submit depending on your subscription plan. Contact our support team for more information."),
    ( "How do I set up email forwarding for support inquiries?", "You can set up email forwarding for support inquiries through your email settings or by contacting our support team for assistance."),
    ("Can I access support documentation in multiple languages?", "Yes, we offer support documentation in multiple languages. You can select your preferred language from the language settings section of our website or software."),
    ( "How do I escalate a support ticket?", "If you need to escalate a support ticket, contact our support team and request escalation. Please provide the ticket number and any relevant details for the escalation."),
    ( "How do I check the status of a service outage or maintenance?", "You can check the status of a service outage or maintenance on our status page or by contacting our support team for updates."),
    ( "Can I schedule a call with a support representative?", "Yes, you can schedule a call with a support representative by contacting our support team and requesting a callback."),
    ( "How do I enable/disable notifications for new messages?", "You can enable/disable notifications for new messages through the notification settings section of our website or software."),
    ( "Is there a limit to the number of devices I can use with my account?", "There may be a limit to the number of devices you can use with your account depending on your subscription plan. Contact our support team for more information."),
    ("How do I change the primary contact for my account?", "You can change the primary contact for your account by logging into your account on our website and navigating to the account settings or contact information section."),
    ("Can I access support through live chat?", "Yes, you can access support through live chat on our website during our support hours. Look for the chat icon in the bottom corner of the page."),
    ( "How do I create a support ticket?", "You can create a support ticket by logging into your account on our website and navigating to the support or help section. Click on the 'Create Ticket' button and fill out the required information."),
    ("Can I export my data from your service?", "Yes, you can export your data from our service by accessing the export or backup settings section of our website or software."),
    ( "How do I change my notification preferences?", "You can change your notification preferences by logging into your account on our website and navigating to the notification settings or preferences section."),
    ("How do I access training materials or resources?", "You can access training materials or resources through the training or resources section of our website or software."),
    ("How do I set up email alerts for support tickets?", "You can set up email alerts for support tickets through the notification settings section of our website or software."),
    ("Can I access support documentation without logging in?", "Yes, you can access support documentation without logging in by visiting our website's support page or product help section."),
    ("How do I add users to my account?", "You can add users to your account by logging into your account on our website and navigating to the users or team section. Click on the 'Add User' button and fill out the required information."),
    ( "How do I set up automatic replies for incoming emails?", "You can set up automatic replies for incoming emails through your email settings or by contacting our support team for assistance."),
    ("Do you know shilpi","yes, you mean beauty!"),
    ("where is inzint located?","B-111 Sector-65 Noida, UP"),
    ("where is the address of Inzint?","B-111 sector-65 Noida, UP")
    
    
]

# Initialize Microsoft DialoGPT-Medium model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

def get_chat_response(text):
    global qa_pairs
    
    # Check if the input contains any word from the questions
    matched_answers = []
    for question, answer in qa_pairs:
        if text.lower() in question.lower():
            matched_answers.append(answer)
    
    if matched_answers:
        return '\n'.join(matched_answers)
    
    # If no match found in predefined qa_pairs, generate response using DialoGPT
    bot_input = tokenizer.encode(text + tokenizer.eos_token, return_tensors='pt')
    chat_history = model.generate(bot_input, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(chat_history[:, bot_input.shape[-1]:][0], skip_special_tokens=True)
    return response

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    return get_chat_response(msg)

if __name__ == '__main__':
    app.run()











