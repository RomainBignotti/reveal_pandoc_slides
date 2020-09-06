# Lecture slides with pandoc + reveal.js + markdown

## Installation

You need a recent version of pandoc. For sure, this will work with pandoc 2.10.1. If necessary, [install a more recent version](https://pandoc.org/installing.html).

You need to clone the repository 

	git clone --recursive git@github.com:jeremyfix/reveal_pandoc_slides.git
	cd reveal_pandoc_slides; git submodule update --init --recursive

Then you are advised to symlink to `slidemaker`, e.g.

	cd ~/.local/bin
	ln -s /path/where/the/git/is/slidemaker/slidemake

## Compilation

Now, suppose you have a worktree somewhere with your markdown files, image directories, d3js scripts, and so (see the `example` directory for an example). The first time, we need to setup some stuff

	slidemake config

and then you just compile the slides with

	slidemake make

If you need to cleanup, 

	slidemake clean

All the things that are compiled are place in the `build` directory. You can serve this somewhere and open locally with firefox the generated page.

## Exporting in PDF

Using the built-in pdf export does not work very well. Instead :

	npm install -g puppeteer --unsafe-perm=true
	npm install -g decktape

And then use `decktape`. See the [project page](https://github.com/astefanutti/decktape)

## References

This project was intially motivated by [this post](http://bloch.ece.gatech.edu/2020/02/15/workflow.html) of M. Bloch.


