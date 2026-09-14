# Using the laptop as a second display

**Written 2026-09-13 by the source audit.** Dmytro asked this on 2026-09-12 (`91be6983:3`):
*"i would like to connect my laptop to the pc as the second display / what cable do i need"*, and
sent five videos to check. The answer was given in chat and **never written down** — this file
closes that gap. Every claim below is quoted from those five in
[../source_audit.md](../source_audit.md).

## The short answer

**No cable will do it.** Laptop screens are outputs only: *"laptops do not have a video input
port, so you cannot directly connect it to your desktop via VGA or HDMI cable and use it as a
monitor"* (Techy Druid). An HDMI cable between the two makes the **laptop drive the PC's monitor**,
which is the reverse of what is wanted.

There are three routes, and the third is the one this build should probably take.

## Route 1 — Windows Wireless Display (Miracast). Built in, free, laggy

Both machines on the same Wi-Fi network. *"You don't even need to install anything"* (Kevin
Stratvert) — though on Windows 11 the feature is an optional component that has to be added first.

**On the laptop** (the machine that will act as the screen):

1. Settings → **System** → **Projecting to this PC**.
2. If it offers optional features: **View features** → **See available features** → scroll to
   **Wireless Display** → check it → install.
3. Launch the **Wireless Display** app and leave its window open. That is what makes the laptop
   discoverable.

**On the desktop:**

4. **Win+K** → pick the laptop from the Connect pane.
5. It duplicates by default. **Win+P** → **Extend** to make it a real second screen.
6. Settings → System → Display → drag the numbered rectangles so the mouse crosses between
   screens in the direction the machines actually sit. **Identify** labels which is which.
7. **Win+P → PC screen only** disconnects.

**Two things worth knowing**, both read off
[`../frames/pm6IylldpMg_01m58s.png`](../frames/pm6IylldpMg_01m58s.png) rather than from the
captions, which garble the shortcut: the Connect pane has a **Change projection mode** link that
does the same job as Win+P, and a checkbox **"Allow mouse, keyboard, touch, and pen input from
this device"** — tick it and the laptop's own keyboard and trackpad drive the desktop session.

**The limitation, in the source's own words:** *"the connection is wireless so it's not quite the
same experience as having a dedicated second monitor connected via cable"* (Techy Druid). Good for
a reference window, a terminal, a document. Not for anything that moves.

## Route 2 — spacedesk. The fallback when Miracast will not

*"If you notice lag or maybe it doesn't work on your device, here's a second method"* (Kevin
Stratvert). Driver on the PC, viewer app on the laptop, from **spacedesk.net**. Viewers also exist
for Android, iOS and a browser, so a tablet or a phone can be a third panel.

**And this is the closest thing to an answer to "what cable":** *"if you use a wired ethernet
connection, it'll be even smoother."* Not a video cable — an **Ethernet** cable, or both machines
on the same wired LAN. That is the only cable in this file that improves anything.

Unverified here: spacedesk is third-party software installing a display driver on the desktop.
Nobody in this repo has run it. Treat Route 1 as the default and this as the fallback.

## Route 3 — share the monitor instead of using the laptop's screen

The best setup in the five videos answers a question that was not asked, and **the monitor already
chosen supports it**.

Clueless Expert runs both machines into one monitor: *"since my monitor supports multiple HDMI
inputs, both the PC and the laptop are connected to it"*, with a **USB/KVM switch** carrying
*"the mouse, keyboard, mic, headset or anything else"* between them, so *"I don't have to
reconnect anything"*. One button changes which machine owns the desk.

**The AOC Q27G4ZR in [components/monitor.md](../components/monitor.md) has two HDMI 2.0 inputs**
alongside the DisplayPort the desktop should be using for 240 Hz. So the laptop can take an HDMI
input the desktop is not using, for the price of an HDMI cable. Sharing the keyboard and mouse as
well needs a USB switch on top; that has **not** been priced, and no shop check has been done for
one — see the open item below.

The trade is plain: Route 3 gives the laptop a **real 27" 1440p screen** with no lag, but only one
machine is on the monitor at a time. Routes 1 and 2 give both screens at once, wirelessly, with
lag. If the laptop is used *instead of* the desktop at times, Route 3 is better. If it is used
*alongside* the desktop, Route 1 is the only one that does that.

**This changes nothing about the monitor decision, which is closed.** It is a capability that
decision already bought and nobody had noticed.

## What the five videos actually covered

Two of them answer the opposite question — how to drive an external monitor **from** a laptop
(Filip Tech, TechSimplify). They are not wrong, they are the other direction, and a cable is
exactly what that needs. Their one transferable part is the Windows display-settings mechanics:
**Identify**, **Extend these displays**, **Make this my main display**, and dragging the rectangles
so the mouse crosses the right way. Those steps are identical however the second screen arrives,
and both on-topic videos skip past them.

| Video | Channel, date | Answers the question? |
|---|---|---|
| [`pm6IylldpMg`](https://www.youtube.com/watch?v=pm6IylldpMg) | Techy Druid, 2023-03 | **Yes** — the "no video input" answer and the Miracast route |
| [`fuuYIZoqZFE`](https://www.youtube.com/watch?v=fuuYIZoqZFE) | Kevin Stratvert, 2026-04 | **Yes** — Miracast again, clearer, plus spacedesk and the Ethernet note |
| [`9RDBvS-yGbk`](https://www.youtube.com/watch?v=9RDBvS-yGbk) | Clueless Expert, 2023-08 | **A different question** — KVM and monitor sharing. The best setup of the five |
| [`1bIWybLzOhg`](https://www.youtube.com/watch?v=1bIWybLzOhg) | Filip Tech, 2020-09 | **The opposite question** — laptop → monitor. Useful for the display-settings steps |
| [`2-PgZVAvTpE`](https://www.youtube.com/watch?v=2-PgZVAvTpE) | TechSimplify, 2024-02 | **The opposite question**, in 53 seconds, adding nothing |

None of the five carries a sponsor. Transcripts are in [`../sources/`](../sources).

## Open, and cheap to close

1. **Which ports does the laptop actually have?** Route 3 needs an HDMI or USB-C output on it;
   Route 1 needs nothing. Not recorded anywhere in this repo.
2. **A USB/KVM switch has never been priced** at Telemart, Brain, ITbox or Foxtrot. Only needed if
   the keyboard and mouse are to be shared as well as the screen — an HDMI cable alone already
   gets the laptop onto the monitor.
