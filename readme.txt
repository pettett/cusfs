How to edit the CUSFS website: a guide for classicists*
v1.0
*and others who have no idea what they're doing

0. If you know what CGI is, ignore this document and go work it out for yourself. Otherwise, read on.

1. How it works

The way I've built the site is actually very primitive and easy to understand. I've used a bit of Perl purely to simplify updates. Here's how it works. The majority of each page is identical - the menu, the events box, and so on are on every page. So, rather than sticking them in every single page (and having to change every single page to change them), index.cgi - which you should never need to edit - does all the work. Basically it pieces together each page from text files located in the txt directory. In short: it takes the top bit of the page - everything until the actual content which we want to change from page to page - and shows that. This content is spread across three files (top, events, middle) so that the events box is isolated, making it easy to edit. Then, index.cgi looks at the url and takes everything after the base (i.e. cusfs.soc.srcf.net/), looks for the corresponding text file, and displays that. If that text file doesn't exist, it returns a 404, and if there is nothing specified (i.e. you're on the home page) it returns the home page. Finally, it adds the bottom of the page.

If you can't see the advantage in this system, it makes creating new pages very easy. All you have to do is make a new text file and put it in txt/. Furthermore, you don't need to edit each page individually to make sitewide changes - simply edit top.txt or bottom.txt as necessary.

If that still doesn't make sense, don't worry. It's not really crucial.

2. How to maintain the site

2a. Editing the front page

The content of the front page is in txt/home.txt. The idea is to copy mailing list posts here, with the newest first. I suggest you delete everything at the start of a new term. In case you can't work it out, here's the format I've been using:

<h1>Heading</h1>
<h2>Subheadings, if you need them.</h2>
<p>Paragraphs.</p>

2b. Editing the events box

The events box is in txt/events.txt. The weekly events should be easy to edit; just change the existing information. If you want to add an extraordinary event or a new weekly event, just copy/paste the HTML for an existing event and change that.

3. How to change the site

3a. Adding new pages

This is easy. You need to do two things: make the page, and add it to the menu. The content of the page should go in a text file located in the txt directory. Name the text file whatever you want the URL to be. Then, add it to the menu by copy/pasting an existing menu link and changing the details. The link should be to /foobar where foobar is the name of your text file (without the .txt extension, of course).

3b. If you're still confused...

You're Cambridge students. I trust in your ability to look at existing pages and work out how they're doing what they're doing. :)

4. And finally...

If you do know way more about all this than I do, feel free to make it better - but please do make sure that it is better rather than simply shinier, and that it remains accessible to people who don't know anything about websites.