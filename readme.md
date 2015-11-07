# tabbed2md

![](http://d.pr/i/1goO2+ "screenshot")

to:

![](http://d.pr/i/16pOv+ "screenshot")

You want to paste data from an Excel spreadsheet into a markdown document.
    Excel provides its data delimited by tabs.
    Markdown tables are not delimited by tabs.
    Unpleasant text wrangling follows.
    tabbed2md wrangles text so you don't have to.

Pipe data through tabbed2md.
    tabbed2md takes tab-delimited lines of text as input.
    tabbed2md gives a [pandoc][pandoc] markdown formatted table as output.

There is no agreed table format for markdown documents.
    tabbed2md outputs [pandoc-flavoured][pandoc-table] markdown.
    If you want your markdown table in another markdown flavour (e.g. GitHub markdown), use pandoc to transform tabbed2md's output (`pandoc -t markdown_github`).


 [pandoc]: http://johnmacfarlane.net/pandoc/index.html
 [pandoc-table]: http://pandoc.org/README.html#tables
