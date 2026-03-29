import logging

logging.basicConfig(level=logging.INFO)


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        logging.error("Invalid input: template is not a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid input: attendees is not a list of dictionaries.")
        return
    if not template:
        logging.error("Template is empty, no output files generated.")
        return
    if not attendees:
        logging.info("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            content = content.replace(
                "{" + key + "}", str(value) if value is not None else "N/A"
            )
        with open(f"output_{index}.txt", "w") as f:
            f.write(content)
