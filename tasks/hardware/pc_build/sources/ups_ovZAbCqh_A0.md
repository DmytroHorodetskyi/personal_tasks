# Choosing a UPS (Uninterruptible Power Supply)

Geerling Engineering | 20220225 | 10:25 | 168965 views
https://www.youtube.com/watch?v=ovZAbCqh_A0

## Chapters

- 0:00 Introduction
- 0:37 Single workstation UPS
- 1:27 Rackmount UPS
- 3:00 Sizing a UPS
- 3:23 Network integration and monitoring
- 4:21 Getting clean power
- 4:54 Battery hot-swap
- 6:36 Battery chemistry and choice
- 8:55 Stories from the trenches
- 9:47 Why you need a UPS

## Description

Radio engineer Joe Geerling explains UPSes, why you need one, and how to choose one, based on decades of experience building and maintaining critical radio infrastructure.

Support me on Patreon: https://www.patreon.com/geerlingguy
Sponsor me on GitHub: https://github.com/sponsors/geerlingguy
Merch: https://redshirtjeff.com
Main Channel: https://www.youtube.com/c/JeffGeerling

#UPS #Backup #IT

Contents:

00:00 - Introduction
00:37 - Single workstation UPS
01:27 - Rackmount UPS
03:00 - Sizing a UPS
03:23 - Network integration and monitoring
04:21 - Getting clean power
04:54 - Battery hot-swap
06:36 - Battery chemistry and choice
08:55 - Stories from the trenches
09:47 - Why you need a UPS

## Transcript

[0:00] ups's or uninterruptable power supplies that's what we're going to talk about today and i have somebody special here it's my dad hello everybody he is the one who's taught me everything i know about ups's and i have a couple here that we can talk about but uh what is your experience with ups well i've had ups's or battery backups uh from you know 300 watts to 60 000 watt units and 60 000 watts units are expensive but they're awesome and they can do a whole facility probably a little bigger than my little uh little floor one over there

[0:32] yes and seven thousand dollar battery changes probably by now that'd be ten thousand this one does not have a seven thousand dollar battery but um so you know i've used a lot of these in my time and i have one over here i have another one on my other computer down here um what like i know you use some of these too even though you have those giant ones sometimes yes yeah these uh these are great for a single purpose single location uh they're they're not great as a facility or a large installation you know you wouldn't want to have 30 or 40 of these or one in

[1:05] every single rack that you have so that's where the bigger ups is come in but these are great they do what they're supposed to do they switch power they have a single battery usually in them you pop they usually slide out put new battery in but they do have a great purpose they're very reliable i personally like the apc units there's others that are i'm sure equally good so now a couple months ago uh a radio station in st louis closed down and when that happened they actually had a bunch of these apc ups the big rackmount ones so that was the time that

[1:38] i decided i actually need a network rack for all my stuff this has my nas's so i have a primary and backup nas has my raspberry pi's running everything and this ups actually has a load indicator and mine has no leds on it so even with all this equipment it's not doing much but what would be the point at which you'd switch from using those little desk ups to using some massive one in the rack like this the reason you would go to the bigger unit is the bigger load would be the number one reason the reliability the way it makes ups power so battery

[2:12] sources can be used as the source is always making power and it's plugged in the wall or it can be plugged in the wall passing the wall power and then flicking power really quick to a battery supplied power so those are all options you have but the number one reason is uh is size and quality so that one is a nice quality unit it's a little older but it's a it's free and it's a great unit uh the the things that are the gotchas about these units are as the older ones you got to watch out at what they do when you overload them

[2:45] so we could have a time when the battery pack goes to turn back on on a power fail and the load is too much the battery shuts it down and then it says okay let's look at this again it turns on for a second and then it loads again it'll just keep doing that and doing that so i always sizing a battery pack or battery and a ups you want to get it like 50 to 75 loaded at the most and 50 is a great space to load it gives you a little longer run time and so forth and i see yours is like barely loaded you can see the uh the load yeah very low level i mean the nasa has probably used

[3:18] the most power in this whole rack maybe that 10 gigabit switch but yeah there's there's not a whole lot here but i did test it and it goes about 90 minutes um another cool thing i just did a couple weeks ago which i don't know if we can see back here there's that led blinking that is the network card for this ups and it's hot plugged so i just bought one on ebay and slapped it in there and now on my network i can observe the ups from any other device and tie it into my management software and and yeah so jeff mentioned that network accessibility is great it can send you warnings test

[3:52] results when it goes on and off power as you can see i had this one just from tuesday going on and off uh power response to distorted input as opposed to no input so i love that stuff that's what we need more email okay so if you were gonna buy one of these now what are some of the considerations you'd have coming into it and what are some things that you need to look for in the specs especially if you're you know dealing with audio and or video or something that needs that more clean power signal uh well the first thing is your size like i mentioned before and you're going

[4:25] to see them all they're rated in volt amps so you're going to convert that to watts because most of us talk in watts but the other thing is you want clean sine wave power it's just sine wave is nice and smooth it's going to be more expensive they have a triangular wave and they have a stepped wave and for a lot of equipment you're going to be fine with any of them but you do want to think about that and think about whether you want the power delivered from the batteries all the time or let that little switch happen so those are the main things and then being able to hot swap a battery that's huge who wants to

[4:58] shut the whole rack down right and then change the batteries then turn it back on so you always want to make sure it's safe hot swappable battery that is something i noticed on this unit when i installed it it is ridiculously heavy and this rack is not sized for a unit like this it didn't work with the actual rails designed to improvise a mounting solution yes i remember that it fits but it's not i wouldn't recommend it but i did think to myself like man changing the battery on this thing would be a beast so yeah you know i noticed that it has a battery that's pretty new yeah um what what is involved in changing out

[5:30] one of these batteries and always put a sticker on because you want to you you go four five six at some point you're asking for trouble so put the sticker on the front so you don't have to do a dig search for it but uh that's a good good move there anyway the battery packs everything's behind us you pop this off so you can see here here i'll just pull this off jeff and then we'll see if you got a hot swappable maybe i won't pull that off my nasa is doing something right now so i don't know if i'd risk it yeah but that but you literally there if it's a hot swap which this one is i'm sure uh you would you you can pull this and unplug and then you got a screw here

[6:05] i see a screw there missing missing anyway then it slides out and you'll have a tray of batteries and then you you have to be careful to change out those plugs you don't want to damage or do anything weird with the connectors put them back in slide it in or you can buy the you can buy the pack from uh apc or your favorite supplier yeah so and then the satisfaction after the job always of putting the cover back on is uh it's great because you know you're not gonna have to touch that thing probably for another four years so if i did need a battery in a hurry like let's

[6:39] say that this this ups was doing something crazy and i noticed like oh the battery's bad or smoking or something fun like that um i have a few questions one is let's say i didn't need it in a hurry i've heard some people are switching their batteries like these lead acid batteries are super heavy like when i installed it i almost i almost feel messed up my finger um is there any other type of battery i could just buy and swap in i know some people talking about lipo or lithium and also where can you get batteries in a hurry or would you recommend buying third-party batteries or the first party

[7:10] any experiences there yeah so battery replacement substitution substitution i don't recommend anything outside of what the unit was built for because it's charging circuits cooling all of that is built for that style of battery there are ups's that you can actually in software change the battery type if you don't have that feature don't change your batteries to a different type for sure and then in town we we have batteries pluses like a lot of towns would have and they do stock a lot of these batteries that go in the ups's they're not a sponsor

[7:43] yeah but uh but they do a great job that they are helpful so uh and and their pricing if you're you go in as a company or as uh um what would you call it uh you have an account there you get a good discount uh and they help you with all your other stuff in your house and your life so there you go now there are sponsored right no no there's still no responsibility for that easy what a year when i need the batteries so so anyway so don't replace i mean batteries um even as they age normally you want to keep them like you got a nice cool basement here batteries can swell and then you try to

[8:15] take that pack out with swollen batteries that can be a problem so there's just a lot of funny things about batteries the other thing is that the same stock size battery with the same terminals on it you can find them in a lower for less cost you can buy the lower capacity battery in amp hours or you could buy the higher the same thing of course you're going to pay more for the higher but you got to figure out of your load how long do you want to last if you have a generator you don't need much time if you don't have a generator you want to last long enough for someone to physically get to the equipment right and do

[8:48] something to shut it down cleanly or something so which is another feature on ups is they can send a shutdown command to a lot of your equipment and you said you had an experience one time with the ups that was acting a little funny what what happened and it was probably uh very early on in the big ups in my life but we had uh incorporated a new station into our rack room and so we plugged a bunch of stuff in but still we wouldn't we would not have uh surpassed our rule 50 to 75 percent but we probably were at 75 percent and one time we had a power outage a momentary

[9:21] power outage when the generator kicked on and the rack of equipment was going on and off and it was probably 25 minutes drive you know driving and walking in the room to get there the equipment would turn on and turn off so fast uh the ups was literally being overloaded by the stuff turning on and then it would shut down and then it would go okay things are cool and it would start up again so horrible experience uh for sure that's why you don't overload your ups so if you can give like a a one paragraph summary of of the things that you need to think about with ups is why they're important

[9:55] and uh you know why why it's not something you should just put off and hope for the best there's no question that we all have dealt with power issues and the more investment you have in equipment the more you should spend time thinking about your ups it's going to protect you from outages so you have time to react and settle things before your power might go out and it always protects your equipment from spikes lightning and so forth so that's the reason that i tell you get your ups
