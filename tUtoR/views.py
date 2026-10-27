from django.shortcuts import render


def landing(request):
    """Public landing page. No accounts or bookings are read here."""
    return render(request, "landing.html", {
        "site_name": "tUtoR",
        "campus": "University of Regina",
        "problems": [
            {
                "title": "A posting gets covered",
                "text": "The next flyer hides the one that mattered. The student who passed the course never sees the request.",
            },
            {
                "title": "Anyone can pin a note",
                "text": "A noticeboard cannot show who actually passed the course, or which hours they can teach.",
            },
            {
                "title": "Contact is a scrap of paper",
                "text": "A name and a number sit in public. There is no booking, no shared time, and no record of the session.",
            },
        ],
        "steps": [
            {
                "number": "01",
                "title": "Say which side you are on",
                "text": "A student names the course they need. A tutor offers a course they have already passed.",
            },
            {
                "number": "02",
                "title": "Match on course and time",
                "text": "Faculty, course, and free hours narrow the list, so both people see the same opening.",
            },
            {
                "number": "03",
                "title": "Book the session",
                "text": "The slot is confirmed first. Contact details are shared after that, not pinned in a hallway.",
            },
        ],
    })
