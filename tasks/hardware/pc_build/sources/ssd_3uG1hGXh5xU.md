# Please Stop Buying the Wrong SSD

Linus Tech Tips | 20260408 | 8:57 | 1172515 views
https://www.youtube.com/watch?v=3uG1hGXh5xU

## Chapters

- 0:00 Intro
- 1:45 What's the difference?
- 2:44 Why does it matter?
- 4:16 It wasn't always this way
- 5:30 HMB isn't useless
- 6:13 Your OS storage should use DRAM
- 6:44 What can we do about it?

## Description

Buy Sihoo Doro C300 Pro V2 here:
 
US:https://sihoooffice.com/YTBLINUSTECHTIP
EU:https://de.sihoooffice.com/YTBLINUSTECHTIP
Discount Code: YTBLINUSTECHTIP
Buy Via Amazon: https://bit.ly/48SEneb
Discount Code: SIHOODEAL

What makes an SSD good or bad? Did you know there's an important hardware difference between top-performing and low-cost storage devices? You might not, because many SSD makers don't talk about DRAM.

Check out a few recommended NVMe SSDs with DRAM Cache: 

Samsung 990 PRO SSD 1TB PCIe 4.0 M.2 SSD: https://geni.us/MLyvyik
Sandisk Optimus GX PRO 8100 PCIe 5.0 NVMe SSD: https://geni.us/kMHopF
Kingston KC3000 PCIe 4.0 NVMe M.2 SSD: https://geni.us/6bbr4
Acer Predator GM7000 NVMe M.2 SSD: https://geni.us/AQ6LMr8

Discuss on the forum: https://linustechtips.com/topic/1635313-please-stop-buying-the-wrong-ssd/

Check out our Channel Partners:
Secretlab - Grab a TITAN Evo ergonomic gaming chair:  https://lmg.gg/secretlabltt
PIA - Get the VPN of our choice: https://www.piavpn.com/ltt
dbrand - Buy a "Circuit" series skin for your device: https://dbrand.com/pcb

► SHOP LTT PRODUCTS: https://lttstore.com
► GET EXCLUSIVE CONTENT ON FLOATPLANE: https://lmg.gg/lttfloatplane
► DIVE DEEPER ON THE LTT LABS WEBSITE: https://lmg.gg/labs
► SPONSORS, AFFILIATES, AND PARTNERS: https://lmg.gg/partners

Purchases made through some store links may provide some compensation to Linus Media Group. Affiliate links powered in part by https://affilimate.com/

Linus Sebastian is an investor in Framework Computer, Inc and HexOS by Eshtek.

CHAPTERS
---------------------------------------------------
0:00 Intro
1:45 What's the difference?
2:44 Why does it matter?
4:16 It wasn't always this way
5:30 HMB isn't useless
6:13 Your OS storage should use DRAM
6:44 What can we do about it?

## Transcript

[0:00] As far as exciting PC components go, storage is pretty close to the bottom. So, I can understand why many gamers simply add up their Steam backlog, key their target capacity into the filter menu, sort by price, and click buy. I mean, it's not like your SSD impacts gaming performance anyway. Or does it? Actually, it can. And even for day-to-day use, the difference between a bottom-of-the-barrel SSD and a good one can be a lot more than you would think from quickly glancing at a spec sheet. And I'm not just talking about

[0:32] performance. Some of the most popular SSDs on the market are missing an important feature that also impacts reliability. I'm talking about cold, hard cash, baby. That little DRAM cash chip right there can [music] make a big difference, and many SSD makers just don't want to talk about it. To the point where until you peel up the sticker, it can be hard to know whether their product has one or doesn't. Why? Of course, the answer is the other kind of cash. So, let's talk about how to

[1:05] tell the difference, how much it matters or doesn't matter, and which manufacturers are transparent about their products, and which ones seem to be going out of their way to make this information harder to find. Just like I'm going out of my way to tell you about our sponsor. See who? Their new SeeWho Doro C300 Pro V2 is a full-body adaptive ergonomic chair with some features you may not be used to seeing or SeeWhoing. See who what I did? Learn more by using our link in the video description. &gt;&gt; [music]

[1:45] &gt;&gt; What's the difference between this SSD and this one? Well, if you knew that this one came later, and if you were already familiar with this one, you would probably think that the SE was short for second edition or special edition and that wow, that's a pretty good deal, right? Wrong. See, unlike the original, the sequel omits a DRAM chip making it about as good of a follow-up on the original as the return of Jafar. But, if you look at the product pages or the technical specifications, you will

[2:17] find no mention of that important [music] difference. Now, the SE does have things about it that are better. It moves to PCIE Gen 4, but the thing is that even in a best-case scenario, this drive hardly takes advantage of that increased bandwidth. So, what is supposed to be a product information sheet turns instead into a product marketing sheet and WD [music] is far from the only one engaging in this behavior. So, why does it matter? Well, your SSD is actually a tiny little computer inside your computer with its

[2:51] own little energy-efficient SOC called a controller. The SOC [music] contains a CPU, firmware, its own memory by the way, and everything it needs both to interface with your PC and with the NAND flash chips that actually store your data. The ones that have a DRAM cache are using that to store the flash translation layer, which is sort of like a map or a lookup table that tells your operating system exactly where all of the data is stored on the physical NAND that makes up your storage. Aside from improving performance by just knowing

[3:24] where your data lives, especially as the drive becomes more full, that map helps your SSD to organize and decide which blocks are best to erase and where to write new data in order to minimize wear. But, since some drives don't have a DRAM cache, obviously that's not the only solution. Modern drives do have some good enough workarounds so they don't need to use expensive DRAM, which is especially relevant today. For NVMe drives, the ones that look like this, host memory buffer is a feature that uses a little bit of your system memory

[3:57] to store this map. It's not as fast as having it directly on board the SSD or as large, but given that this strategy is usually employed in lower cost drives, the PCIe interface has enough bandwidth for it to offer decent performance. Finally, the map can just be stored on the good old regular NAND. None of these strategies are as good as a dedicated DRAM chip on board though, which is exactly why years ago the industry identified DRAM caches as an important factor for potential buyers and plopped it front and center. But

[4:29] [music] then, fast forward to today and do you know whether your WD Black SSD has a DRAM chip? I do. Let me explain. The top end SN850X does, but the SN7100 and SN770 do not, which is weird because if you go back a little further to the SN750, that drive does have a DRAM chip. Not the SN750 SE though. [music] And things are even worse in WD Blue. Did you know that if you buy a SATA WD Blue SA510 in 2 TB, it has a DRAM chip, but the smaller sizes of the same model don't? Are you confused yet? You should be. No, really.

[5:02] You should be. As far as we can tell, WD Black, Blue, Green, etc. are just colors that exist [music] more to trick you into thinking something is better than it is than they are about clear and consistent product labeling for consumers. And WD is not the only one guilty of this. SanDisk, Seagate, MSI, Corsair, Crucial, and Netac have all been guilty at times of not sharing whether their drives use DRAM or not. Now, to be fair to our corporate overlords, please don't punish me. Being DRAM-less doesn't make an SSD

[5:35] useless. Doesn't even make it bad. Modern drives with host memory buffer can be perfectly performant, especially as a secondary storage drive or for for And I will always say that real world performance trumps whatever you can put on a spec sheet. But I also always say that consumers have a right to be informed about what they're buying. And too often, we were not able to confirm whether a device had a DRAM chip or didn't without resorting to a third-party resource like TechPowerUp or just having the physical drive in our hands so that we could peel off the heat

[6:09] spreader {slash} sticker, likely voiding our warranty. And this is important because there is one situation where I would strongly recommend a DRAM cache, and that's as an operating system drive. This is especially true as your drive starts to get older and more full, but you will notice a difference in system responsiveness during background operations like system updates or virus scans. And furthermore, if you wanted to play a game that benefits from DirectStorage, that is, streaming game assets directly from your SSD, it might not be a terrible idea to have a DRAM

[6:42] cache drive for that as well. I think the most frustrating thing about this for me, though, is how easy it would be for manufacturers to fix it. Samsung, for all of their participation in this problem of some drives being DRAM-less and others not, at least actually says whether their drives have DRAM right on the product pages. I shouldn't have to praise them for that, but here we are. So, what do we do? Well, we vote with our wallets. WD is dead as an SSD brand now, but SanDisk still exists as a separate entity and has had a similarly spotty history. Though, to their credit, they've begun

[7:14] specifying the cache in their new Optimus lines data sheet, so [music] that's progress. As for the companies who do disclose things properly, well, Samsung we already mentioned, but also Kingston and Acer Predator all list whether their drives have a DRAM chip. So, as new Gen 5 SSDs continue to come onto the market, pick the ones that let consumers know what the heck is inside them. And I mean, just generally, make your voice heard. If you were researching an SSD and you had to dig deep to figure out whether it had D-Ram or not, let the manufacturer know that that major shopping experience

[7:45] frustrating. While you're at it, let them know about our sponsor. Sihoo, their new Doro C300 Pro V2 office chair was built with your comfort in mind. Their signature Dinacore system offers full body dynamic support, not just for your back, but in the headrest, lumbar, and armrests as well. The chair moves with you as you adjust and get more comfortable with something they call Synchro-Flex, which means you won't be constantly readjusting how you fit in the chair. This extends to the lumbar support as well, which allows for the chair to cover the majority of your back

[8:19] without it jutting into you with some uncomfortable pressure. Their 8D bionic armrests pivot in, you guessed it, eight different directions. That's up, down, all around, so no matter how you're sitting, your arms can rest easy. And the fabric is made with a breathable mesh to cut down on the sweat build-up. If you're gaming on an ultra-wide monitor, you may even appreciate their ultra-wide headrest as you pivot from side to side. Click our link down below to order your Sihoo Doro C300 Pro V2 today. Or you can even sign up to their mailing list to save an additional $50. You guys enjoyed this video, maybe

[8:51] you'll enjoy the time we water-cooled an SSD. Totally unnecessary, but definitely fun.
