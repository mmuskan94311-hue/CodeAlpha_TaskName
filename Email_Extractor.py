import re

input_file = "emails.txt ."
output_file = "extracted_emails.txt"

try:
    with open(input_file, "r") as file:
        text = file.read()

    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    emails = re.findall(email_pattern, text)

    unique_emails = list(set(emails))

    with open(output_file, "w") as file:
        for email in unique_emails:
            file.write(email + "\n")

    print("================================")
    print("     EMAIL EXTRACTOR")
    print("================================")

    print("\nEmails found:")

    for email in unique_emails:
        print(email)

    print("\nTotal emails found:", len(unique_emails))
    print("Emails saved to:", output_file)

except FileNotFoundError:
    print("Error: emails.txt file was not found.")