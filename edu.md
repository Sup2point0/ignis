# Ignis

> [!TIP]
> This is a little collection of ‘learnings’, something I include in every non-minor project. Find out more in [*Assort*<sup>↗</sup>](https://sup2point0.github.io/Assort/edu.html).

This was a really fun project(s?) to work on, both down to the variety of aspects involved, and the fact that all of these were pretty separate so I could work on them asynchronously. That being said, it was quite cool thinking up all of these and then realising how they were all inter-linked[^inter-link] in some way – like, everything fit together really nicely. Oh, we’re visualising stats?  – that might help give insight into how we should approach machine learning. Oh, a Discord bot would be cool – wait, that’s actually a far more convenient way of using the model than providing test images in a folder locally!

[^inter-link]: I... think I just invented a word? Yeah, I’ve been using ‘link’ a lot throughout this project as a reference to *Yu-Gi-Oh*.

Returning to [Nextcord<sup>↗</sup>]([https://github.com/nextcord/nextcord](https://docs.nextcord.dev/en/stable/)) after a couple years hiatus felt pretty good, and armed with my many more years of experience, appreciation for actually comprehensible code, and an actual IDE,[^ide] I made sure to code the bot right this time.[^bot] I gotta say, that thing where you learn a thing, stop doing it, and then come back way later in life but pick it up again really quick – SO real. Using Nextcord again was so smooth. And cogs really weren’t that hard to learn, and are a fantastic idea.

[^ide]: For context, [Penguin<sup>↗</sup>](https://github.com/Sup2point0/PENGUIN) was coded in replit, until I started using GitHub more heavily, at which point I integrated it into replit, and started coding on [github.dev<sup>↗</sup>](https://github.dev). But of course, none of those compare to my current (as of writing) setup of VSCode with Intellisense, custom snippets, Copilot, the whole arsenal.
[^bot]: Only shame, really, was that Ai didn’t need all that much functionality.

With that said, here’s what we discovered this time round.


<br>


## Difficulties

*Yu-Gi-Oh* has 13,000+ cards, which is a pretty hefty amount. Handling all that data proved a little problematic. I was pretty impressed VSCode could load and even syntax highlight the 666,000+ line formatted JSON file on my poor laptop. The main challenge came in obtaining the images of the art for all those cards, since it would involve fetching data from a URL, y’know, 13,000 times.

We solved that with `aiohttp` and asynchronous functions, which as promised was blazingly fast. Seeing the wall of debugging info fly past as the program rapidly obtained the art for all 13,000 cards... it was a sight to behold.

Well, size would return for its revenge arc once we got round to working on the neural network. Supplying that data to the model turned out to be a little tricky and fiddly, and eventually I settled on just saving the images to disk and loading from there. Surprisingly, the whole collection of 13,000 images exported to under a gibibyte, with each image taking up only kibibytes, despite their seemingly stellar quality.


<br>


## Learnings

- GIT SUBMODULES ARE AWESOME
  - Having your own standardised utils library is pretty damn awesome.
  - Knowing Git, there’s probably some unobvious danger with them too – but I have yet to discover those, so we’ll just vibe until something explodes ~0.o~
- Setting up infrastructure early can be pretty helpful. It saves you a lotta time later on, abstracting some fiddly technicalities so that you don’t need to worry so much about them.
  - Of course, hyper-focusing on low-level infrastructure can also drag a project and make it way too over-engineered. And while over-engineering can be fun, sometimes it’s really not that necessary. The high-level stuff is the interesting stuff, after all.
  - In this case, the abstraction was going to be letting `ygo.api` and `ygo.sql` handle all JSON and SQL interactions with `data["attribute"]` lookup, and use `Card` instances with `Card.attribute` access everywhere else. This turned out to be a little non-trivial, so I settled with extracting data from the database as dictionaries until I could find time to properly implement the object-oriented approach with SQLAlchemy. In this case that wouldn’t invoke a refactoring nightmare, since it would be as simple as changing all instances of `card["property"]` to `card.property`.
- Asynchronous requests are SO quick.
- Once again, debugging (ofc I only have experience with VSCode’s debugger) is *quite* insane at helping you find the issues in your program.
- Do NOT commit databases to Git.
  - Especially when they’re 500 MB, which is way over GitHub’s 100 MB limit.
- Messing with Git history is pretty dangerous.
  - Thankfully GitHub exists, so that if we mess up locally we can still clone the old intact repo from online before we’ve pushed our broken local copy.
- When following instructions, you should really follow every instruction. Do not skip ones you think are unnecessary or don’t apply to you (unless you’re absolutely certain) ...they’re probably there for a reason, after all.
- Conversely, when writing instructions yourself, remember that the (conscientious) people reading those instructions will probably re-read them – and then most likely re-read them again, several times, however quick that may be. They’ll pick apart the words you’ve used, think over exactly what you mean, make sure they’ve got it exactly right – and so any ambiguitiez, skipped details, or slight inaccuracies will be exposed. So if you yourself haven’t re-read what you’ve written yourself, then...


<br>
