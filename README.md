# Wichteln!

This is a german language implementation of secret santa.
The design goal is minimal hassle for the participants, which is achieved by using e-mails for communication.
The features are:

- No signup/app needed for participants
- No mailserver required, mailjet is used for sending (account required by manager)
- Configurable message text

Sadly, due to cross-origin policy issues, the browser is prohibited from sending POST requests to Mailjet directly, so a python server is necessary to act as a proxy.

# How to use

1. Install python requirements (e.g. with `pip install requests`).
2. Start python server with `python wichteln.py`.
3. Open displayed web-page (likely at <localhost:8000/>)
4. Fill in participants as shown
5. Touch up template if required
6. Fill in Mailjet account data
7. Fill in sender name ("Absender", the e-mail must be approved for sending via Mailjet)
8. Press "Versenden!"

# Requirements

- python 3.6+
- requests library for python
- mailjet account for sending emails

# License

Copyright 2022 Alexander Matz

MIT License, text see `html/index.html`