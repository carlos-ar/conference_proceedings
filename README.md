# Conference Proceedings Template

Template for generating a conference proceedings document from an online submission.

## Tools

This template uses various tools to generate the latex source files from a spreadsheet that collects the abstracts for a general conference.

- Templating with Jinja2 in python
- Custom latex style file (TO DO) for package import
- `standalone` latex package for multiple file compilation
- Pandas in python for managing excel submission files

## Usage

1. Generate submissions from some submission website (I use Google Forms)
2. Modify template source files in `./templates` directory
3. Output template subfiles to `./texsrc` directory
4. Run `pdflatex` to compile
   1. Working on getting subprocess to do this all within python file

## References

This is no the first time I attempt this! I had done this before, a long time ago, where this was not as easy as this time around. Either I learned a lot, or it became easier. Maybe the version of Jinja i was using was older, or I was using Python 2.7, but in the end, I have followed some other's examples.

Some of the Jinja doc

- https://jinja.palletsprojects.com/en/2.11.x/api/
- https://jinja.palletsprojects.com/en/2.11.x/templates/#for

Some examples and tutorials that have proven useful

- http://eosrei.net/articles/2015/11/latex-templates-python-and-jinja2-generate-pdfs
- http://akuederle.com/Automatization-with-Latex-and-Python-2
- https://www.tug.org/tug2019/slides/slides-ziegenhagen-python.pdf

