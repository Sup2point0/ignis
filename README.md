<h1 align="center"> <code> ignis </code> </h1>

A series of related projects involving the [*Yu-Gi-Oh!*<sup>↗</sup>](https://yugipedia.com) card game, including asynchronous API requests, database querying, machine learning, and a Discord bot!


<br>


## Index

| folder | libraries | notes |
| :----- | :-------- | :---- |
| `ygo` | [`aiohttp`](https://docs.aiohttp.org/en/stable/) `sqlite3` | Interfaces for asynchronously accessing the [YGOPRODECK API<sup>↗</sup>](~), saving data to a database, and querying it with SQL. Bear in mind *Yu-Gi-Oh* has 13,000+ cards, so this was quite the effort. |
| `stats` | [`matplotlib`](https://matplotlib.org) | Visualising the statistics of card properties. |
| `ignis` | [`tensorflow`](https://www.tensorflow.org) [`keras`](https://keras.io) | Machine learning models in the form of convolutional neural networks, for predicting a card’s properties from its art. This was the original intention of this project, which everything else was built around. |
| `disc` | [`nextcord`](https://docs.nextcord.dev/en/stable/) | A Discord bot to provide convenient access to the other projects. |
| `tests` | [`pytest`](https://docs.pytest.org/en/8.0.x/) | A couple of unit tests cuz I felt like it. (Nowhere near even 20% code coverage) |
| `scripts` | | Code files that are manually executed for specific purposes. |
| `assets` | | Data and image files, mostly untracked.[^assets-untrack] |
| `suptools` | | A submodule containing my [suptools<sup>↗</sup>](https://github.com/Sup2point0/suptools) repo, with all the utility functions I need. |

[^assets-untrack]: Good reason for this, ofc. Those files are huge. Trying to commit and push them gets rejected by GitHub. Not a good idea. I speak from experience. o.0


<br>


## Notes

* Relative imports, yeah. Somehow I managed to get them working in VSCode, so I went with it. I do like them, cuz you don’t need to worry about disrupting imports if changing your working directory (especially relevant when submodules are involved).


<br>


## License

MIT cuz why not. Take the code if you need it, just might need to extricate it from `suptools` ;)


<br>


## Difficulties & Learnings

See [edu.md](edu.md) :D


<br>
