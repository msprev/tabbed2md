---
title: "tabbed2md"
author:
    - name: Mark Sprevak
date: 7 November 2015
style: Notes
...

# tabbed2md

You want to paste data from an Excel spreadsheet and into a markdown document.
    Excel provides its data delimited by tabs.
    Markdown tables are not delimited by tabs.
    Unpleasant text wrangling follows.
    tabbed2md does the wrangling so you don't have to.

You pipe data through tabbed2md.
    tabbed2md takes tab-delimited lines of text as input.
    tabbed2md gives a [pandoc][pandoc] markdown formatted table as output.

Note there is no agreed table format for markdown documents.
    tabbed2md output is [pandoc-flavoured markdown][pandoc-table].
    If you prefer your markdown table in another markdown flavour (e.g. GitHub markdown), use pandoc on the output to transform it (`pandoc -t markdown_github`).


 [pandoc]: http://johnmacfarlane.net/pandoc/index.html
 [pandoc-table]: http://pandoc.org/README.html#tables
