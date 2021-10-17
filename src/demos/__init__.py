from inky_draw import PixelType, new_inky_image, set_pixel, new_inky_draw, draw_text, draw_rect, get_truncated_text
from calendar_client import get_calendar_client
from datetime import datetime
from dateutil.parser import parse
from dateutil.tz import gettz
from dateutil.utils import default_tzinfo


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


def multiline(text):
    index = -1
    multi_line = ""
    for char in text:
        index = index + 1
        if index % 50 == 0 and not index == 0:
            multi_line = f'{multi_line}\n'
        multi_line = f'{multi_line}{char}'
    return multi_line


def calendar_demo():

    try:
        image = new_inky_image()
        now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        client = get_calendar_client()
        events = client.events().list(
            calendarId='primary',
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy='startTime',
        ).execute()

        day_map = {}
        eastern = gettz('America/New York')
        for event in events['items']:
            start = parse(event['start']['dateTime'])
            start_eastern = default_tzinfo(start, eastern)
            start_day = start_eastern.strftime('%a. %B %m, %Y')
            if start_day not in day_map:
                day_map[start_day] = []
            day_map[start_day].append({
                'description': event['summary'],
                'start': start_eastern,
            })
        height = 0
        width = image.width
        for day in day_map.items():
            if height > image.height - 20:
                break
            bar_bottom_right = (width, height + 40)
            bar_top_left = (0, height)
            draw_rect(image, bar_top_left, bar_bottom_right, PixelType.COLOR)
            draw_text(image, day[0], 18, (5, height + 8), PixelType.WHITE)
            height = height + 40
            max_width = image.width - 30
            for event in day[1]:
                if height > image.height - 20:
                    break
                description = event['description']
                start_time = event['start'].strftime('%H:%M')
                text = get_truncated_text(
                    image,
                    f"{start_time} | {description}",
                    18,
                    max_width,
                )
                draw_text(image, text, 18, (15, height + 6), PixelType.BLACK)
                height = height + 35
        now = datetime.now().strftime('%Y-%m-%dT%H:%M')
        print(f"now is {now}")
        draw_text(
            image=image,
            text=f"as of {now}",
            size=16,
            point=(image.width - 100, image.height - 30),
            color_type=PixelType.BLACK,

        )
        new_inky_draw()(image)

    except Exception as e:
        print(f"unexpected exception {e}")
        image = new_inky_image()
        draw_text(
            text=f"^(x.x)^ something bad happened",
            image=image,
            point=(5, 5),
            size=22,
            color_type=PixelType.COLOR
        )
        draw_text(
            text=multiline(f"{e}"),
            image=image,
            point=(5, 40),
            size=16,
            color_type=PixelType.BLACK
        )
        new_inky_draw()(image)
        raise e
