import random
import smtplib
from email.mime.text import MIMEText
from tkinter import Tk, Label, Entry, Button, messagebox, PhotoImage

code_entry = None
otp_code = None
def get_user_email():
    def verify_code():
        global code_entry, otp_code

        entered_code = code_entry.get()
        if entered_code == otp_code:
            messagebox.showinfo("successful verification", "Verified successfully!")
        else:
            messagebox.showerror("Check failed", "Invalid verification code!")

    def send_email(receiver_email, message, subject):
        sender_email = "task2v@gmail.com"
        sender_password = "tumxqzynqjplsxxp"

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            messagebox.showinfo('Mail sent successfully!', 'Verification code has been sent to your email.')
        except Exception as e:
            messagebox.showinfo('An error occurred while sending mail:', str(e))
        finally:
            server.quit()

    def verify_email():
        global code_entry, otp_code
        receiver_email = email_entry.get()
        otp = random.randrange(100000, 999999)
        otp_code = str(otp)
        message = "Your verification code is: {}".format(otp_code)
        send_email(receiver_email, message, "verification code")

        email_window.destroy()

        verify_window = Tk()
        verify_window.title("Email verification")
        verify_window.picture = PhotoImage(file="re.png")

        code_label = Label(verify_window, text="Please enter the code sent to you:",fg="#cce0ff")
        code_label.pack()

        code_entry = Entry(verify_window)
        code_entry.pack()

        verify_button = Button(verify_window, text="verification", command=verify_code)
        verify_button.pack()

        verify_window.mainloop()


    email_window = Tk()
    email_window.title("Enter  email")

    email_window.iconbitmap(default="em.ico")


    label = Label(email_window, text="Please enter your e-mail address:",bg="#cce0ff")
    label.pack()

    email_entry = Entry(email_window)
    email_entry.pack()
    email_entry.focus()
    email_entry.event_generate("<<Paste>>")

    button = Button(email_window, text="confirmation", command=verify_email, fg="#0066ff")
    button.pack()

    email_window.mainloop()

get_user_email()
