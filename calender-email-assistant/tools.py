from datetime import datetime
import os
from langchain.tools import Tool

def schedule_event(event: str, time: str) -> str:
    return f"Scheduled event '{event}' at {time}."

def reschedule_event(event: str, old_time: str,new_time: str):
    return f"Rescheduled event '{event}' from {old_time} to {new_time}."


def cancel_event(event: str, time: str):
    return f"Canceled event '{event}' at {time}."

def read_email():
    return "3 unread emails:\n1.From HR - Offer letter\n2.From Tanvir - Meeting request\n3.Promo - Amazon Deals"

def draft_email(recipient: str, subject: str, body: str):
    os.makedirs("drafts", exist_ok=True)
    filename = f"drafts/{recipient.replace('@', '_')}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"subject: {subject}\n\n{body}")
    return f"Drafted email to {recipient} with subject '{subject}' and body:\n{body}\nSaved as {filename}"

tools = [
    Tool(name="schedule_event",
         func=schedule_event,
         description="Schedule a calendar event."),
    Tool(name="reschedule_event",
         func=reschedule_event,
         description="Reschedule a calendar event."),
    Tool(name="cancel_event",
         func=cancel_event,
         description="Cancel a calendar event."),
    Tool(name="read_email",
         func=read_email,
         description="Read and summarize unread emails."),
    Tool(name="draft_email",
         func=draft_email,
         description="Create and save an email draft with recipient, subject, and body.")     
]