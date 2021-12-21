# Inky Zero Day

> Your Google Calendar for the next **day**. Running on a Raspberry **Zero**. Displayed with **Inky**What.

## What's this thing?

**Inky Zero Day** is a Raspberry Pi / 3D Printing maker project.
Your desktop will act as an "authorization server", running a small Flask app to handle authorization requests from the Pi.
In response to auth requests, the server will pop an OAuth consent browser window on your desktop, prompting you to authorize the Pi for access to your Google Calendar.
Once authorized, the Pi will then use those credentials to grab your upcoming events and paint them to the e-ink InkyWhat display.
The Pi repeats this process indefinitely every hour on startup with cached credentials where possible. 

## Why did you do this?
Inspired after seeing [MagicInkCal](https://github.com/speedyg0nz/MagInkCal), I put together this project as a chance to tinker and learn a couple of new skills (Fusion360, Python, Google's Calendar API). 

## How can I make one too?

Follow these steps to bake your very own **Inky Zero Day** from scratch. 

> 💬 All scripts under [scripts](./scripts) from the repo root assume they are being run from the repo root.

> 💬 While following these steps, replace `[RepoRoot]` with the directory this repository has been cloned into.

> 🔥 In case it's not obvious, **DO NOT** expose the desktop running the Auth Server below (or your Pi for that matter) to the internet.

### Parts

In addition to a 3D printer, a spool of your favorite color of PLA and some soldering tools you'll need:

* [Raspberry Pi Zero W](https://www.raspberrypi.com/products/raspberry-pi-zero-w/)
* [InkyWhat E-Ink Display](https://shop.pimoroni.com/products/inky-what)
* Micro USB Power Supply
* GPIO Header
* SD Card
* Jumper Wires

### Running the Auth Server

*First, we need our desktop to act as an authentication server so that it can pop an OAuth consent screen for your Google Calendar events on behalf of the Pi*

 * Clone this repo onto your computer and install Python3 if you haven't already.

 * Then, from the repo root, run `sh ./scripts install_server.sh`. If your running windows (like I am), `.bat` file equivalents are provided.

 * We'll give the server a run in the next step after we have the credentials for our Calendar enabled app.

### Google Cloud App Setup

*Next, we need to create an application with Google Cloud so that our Pi can request events from our Google Calendar*

* Create a new app on Google's [Cloud Developer Console](https://console.cloud.google.com). Enable the [Calendar API](https://console.cloud.google.com/apis/library/calendar-json.googleapis.com) before enabling OAuth for the application with the following scopes:
  * `.../auth/calendar.readonly`
  * `.../auth/calendar.calendarlist.readonly`

* Generate and Save OAuth2.0 credentials as json to your desktop at `[RepoRoot]/.temp/credentails.json`.
  * The `./temp` folder should always be ignored via `.gitignore`.

* You should now be able to run the auth server on your desktop via `sh ./scripts/run_auth_server.sh`. Note the hostname or reserved IP address of your desktop for the next step.
  * You'll need to keep this server running later on if your credentials expire. For now, it's probably just enough that you leave it running while we complete these steps. 

### Assembling the Pi
*Last, lets put the actual calendar together so that we can finally call this thing done.*

* Sadly, Pi Zeros omit a GPIO header out of the box. To wire up the InkyWhat to your Pi you'll need to solder on a GPIO header or find a GPIO solderless alternative

* Wire the InkyWhat's GPIO to the Pi following their [published pinout](https://pinout.xyz/pinout/inky_what).
  * See the provided [reference image](./images/gpio-reference.jpg) for another example.

* 3D print the case using the [STL model](./models/) files provided.

* Slide the InkyWhat into the case front and snap the PiZero into the base before popping the lid shut

### Setting Up The Pi

* Using your preferred method, flash the latest [Raspberry Pi OS Lite image](https://www.raspberrypi.com/software/operating-systems/) onto the Pi and configure it for secure SSH access over Wi-Fi. SSH into the pi, run the usual updates before cloning this repo onto it.

* Install the pi calendar client by running `sh ./scripts install.sh` from the cloned repo root.

* Modify the `.env` in the repo root (ignored from git by default) as needed. `CREDS_HOST` should be set to the hostname or IP address of the desktop your setup as the **Auth Server** in the first few steps. Other settings can be modified here as well including Timezone offsets.

* Run the client automatically on reboot by adding the following entry to crontab `sudo crontab -e`

  ```bash
  @reboot [RepoRoot] && sh ./scripts/cron_task.sh
  ```

### Run it!

Plug the pi in and the calendar client should start on boot. If everything went well, your desktop should prompt you for Google Calendar login and, once completed, your Pi should now be displaying your next few calendar events 🚀 

 