from inky_draw import PixelType, new_inky_image, set_pixel, new_inky_draw, draw_text, draw_rect
from calendar_client import get_calendar_client
import datetime


def checker_demo():
    values = [PixelType.BLACK, PixelType.WHITE, PixelType.COLOR]
    image = new_inky_image()
    drawer = new_inky_draw()
    index = 0
    for y in range(0, image.height):
        for x in range(0, image.width):
            index = index + 1
            if index >= len(values):
                index = 0
            set_pixel(image, (x, y), values[index])

    drawer(image)


def text_demo(text):
    image = new_inky_image()

    draw_rect(image, (0, 0), (image.width, 40), PixelType.COLOR)
    draw_text(image, text, 22, (5, 8), PixelType.WHITE)

    draw_text(image, text, 22, (5, 48), PixelType.BLACK)

    draw_rect(image, (0, 80), (image.width, 120), PixelType.BLACK)
    draw_text(image, text, 22, (5, 88), PixelType.WHITE)

    new_inky_draw()(image)


def calendar_demo():
    image = new_inky_image()
    try:
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        client = get_calendar_client()
        events = client.events().list(
            calendarId='primary',
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy='startTime',
        ).execute()
        print(events)

    except Exception as e:
        print(f"unexpected exception {e}")
        draw_text(f"x.X something bad happened")
