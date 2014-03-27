#Document of style and design

This document defines the patterns of style and design adopted and is divided into three parts: Python, CSS and JavaScript.

##Python
####Header
<pre><code># -*- coding: utf-8 -*-
# Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
</code></pre>

####Comments
The comments will be described into language of programming language.
<pre><code># This is a simple comment.

# This comment occupies
# more than one line.
</code></pre>

####Indentation
Always use 4 spaces to indent.
<pre><code>if __name__ == '__main__':
    print 'Hello, world'
</code></pre>

Always indent.
<pre><code>if x > 5:
    if x == 7:
        print x
    else:
        print x + 1
</code></pre>

####Line Length
Avoid lines longer than 80 characters. When a statement won't fill in a single line, it may be necessary to break it.

####Nomenclatures and Declarations
#####Méthods and Functions
Name of method/function into language of programming language, with initial into lowercase and, if it have more than one word, break with '_'. Arguments separated with one space after comma, following example.
<pre><code>def function_sum(num1, num2):
    # ...
</code></pre>

#####Classes
Class name will be into language of programming language, initial uppercase and, if it have more than one word, break with letter into uppercase in the beginning of the other word. Each class have to have the comment with a short description.

<pre><code>class ClassOne():

    """This class is only a example."""

    def method_x():
        # ...
</code></pre>

#####Variables
Variables will be with meaning name, into language of programming language, with initial into uppercase and, if it have more than one word, break with '_'. One space will be among the variable and the attribution/comparison signal, as well as among attribution/comparison and value to be attributed/compared.

<pre><code>cars_list = []
car.model = '208'</code></pre>

#####Tuples, Lists e Dictionaries
Tuples, lists and dictionaries will be described into following pattern:

<pre><code>tuple = (
    var_x,
    var_y,
    var_z,
)
</code></pre>

####Imports
The imports will be follow pattern:

1. Imports of the especific classes from the package (`from os import path`), ordered and separated each package.
2. Import from entire package (`import os`).

<pre><code>from django.template import RequestContext
from django.http import HttpResponse

from exception.validation_exceptions import *
from exception.internal_exceptions import *

import MySQLdb
</code></pre>


##CSS
####Header
<pre><code>
/**
 * Universidade de Brasilia - FGA
 * Técnicas de Programação, 1/2014
 *
 * Acidentes em Rodovias, 2013-2014
 * GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
 *
 */
</code></pre>


####Comments
The comments should be written in English.
<pre><code>/* This is a simple comment. */

/** 
 * This comment occupies
 * more than one line.
 */

/* =========================================================================
   Comment for a new section
   ========================================================================= */
</code></pre>

####Indent
Use 2 spaces to indent.
<pre><code>
meta.foundation-mq-small {
  font-family: "only screen and (min-width: 768px)";
  width: 768px; }
</code></pre>

Indent always.
<pre><code>
/* Medium Displays: 768px - 1279px */
@media only screen and (min-width: 768px) {
  .show-for-medium,
  .show-for-medium-up {
    display: inherit !important; 
}
</code></pre>

####Line Length
Avoid lines longer than 120 characters. When a statement won't fill in a single line, it may be necessary to break it.

####Nomenclature and Declarations
#####Class, Methods and Functions
Should use this model.
<pre><code>
.some-class {
  color: red;
}

.another-class {
  color: blue;
}
</code></pre>

#####Shorthands
They should be similar from class.
<pre><code>
.text {
  font: 1em/1.1em bold italic small-caps Verdana, Arial, Helvetica, sans-serif;}
</code></pre>

 Or like this to multi-lines:

 <pre><code>
.text {
  font-size: 10em;
  line-height: 1.1em;
  font-weight: bold;
  font-style: italic;
  font-variant: small-caps;
  font-family: Verdana, Arial, Helvetica, sans-serif;}
</code></pre>

#####Variables
If it has, they should be like this:
<pre><code>
hr {
    -moz-box-sizing: content-box;
    box-sizing: content-box;
    height: 0;
}
</code></pre>


##JavaScript

###Header
<pre><code>
/*
 * Universidade de Brasilia - FGA
 * Técnicas de Programação, 1/2014
 * Acidentes em Rodovias, 2013-2014
 * GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
*/
</code></pre>

####Comments
The comments must be written in english.
<pre><code>//This is a simple comment

/*This comment occupies
more than one line.*/
</code></pre>

####Identation
The unit of indentation is one tab of four spaces.

<pre><code>
if (time == 20) {
    x ;
    }
else {
    x = "Good evening";
    }
</code></pre>

####Line Length
Avoid lines longer than 120 characters. When a statement won't fill in a single line, it may be necessary to break it.
Place the breaks after an operator, specially a comma.
The next line should be indented with 1 tab.

<pre><code>
if(time == 20) {
    x = "This is a long sentence. It should have maximum 120 characters long.
        Because of that, we had to break the line."
    }
</code></pre>

####Nomenclature and Declarations
#####Variables
All variables should be declared before use.
It is preferred that each variable be given its own line and comment.
They should be listed in alphabetical order.
Use of global variables should be minimized.

<pre><code>
    var currentEntry; // currently selected table entry
    var level;        // indentation level
    var size;         // size of table
</code></pre>

#####Methods and Functions

All functions should be declared before they are used. 
Inner functions should follow the var statement. 
This helps make it clear what variables are included in its scope.

There should be no space between the function name and the '(' of its parameters list. There should be one space between the ')' and the '{'
that begins the statement body.
The '}' is aligned with the line containing the beginning of the declaration of the function.

<pre><code>
function outer(c, d) {
    var e = c * d;

    function inner(a, b) {
    	return (e * a) + b;
    }

    return inner(0, 1);
}
</code></pre>

If a function literal is anonymous, there should be one space between the word function and the ( (left parenthesis). If the space is
omited, then it can appear that the function's name is function, which is an incorrect reading.

<pre><code>
div.onclick = function (e) {
    return false;
};

that = {
    method: function () {
        return this.datum;
    },
    datum: 0
};
</code></pre>

#####Whitespace
Blank lines improve readability by setting off sections of code that are logically related.
Blank spaces should be used in the following circumstances:

-A keyword followed by ( (left parenthesis) should be separated by a space.

<pre><code>
while (true) {
    document.write('Hello World!');
}
</code></pre>

-A blank space should not be used between a function value and its ( (left parenthesis). This helps to distinguish between keywords and
function invocations.

-Whitespace should follow every , (comma).

<pre><code>
function inner(a, b) {
    return (e * a) + b;
    }
</code></pre>

##HTML
####Header
<pre><code>
<!--
<meta charset="utf-8">
Universidade de Brasilia - FGA
Técnicas de Programação, 1/2014
Acidentes em Rodovias, 2013-2014
GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
-->
</code></pre>

####Identation
For identation, use 2 spaces at a time.

Don't mix tabs and spaces for identation.

<pre><code>
<ul>
  <li>Fantastic
  <li>Great
</ul>
.example {
  color: blue;
}
</code></pre>

####Comments
The comments are to be written in English, according to the programming language.

<pre><code>
<!--This is a sinlge line comment-->
<!--This is a comment
That occupies more
than one line.-->
</code></pre>

####HTML Validity
Use valid HTML code unless that is not possible due to otherwise unattainable performance goals regarding file size.
Using valid HTML is a measurable baseline quality attribute that contributes to learning about technical requirements and constraints, and 
that ensures proper HTML usage.

<pre><code>
<!-- Not recommended -->
<title>Test</title>
<article>This is only a test.

<!-- Recommended -->
<!DOCTYPE html>
<meta charset="utf-8">
<title>Test</title>
<article>This is only a test.</article>
</code></pre>

####Formatting
Use a new line for every block, list, or table element, and indent every such child element.
Indent them if they are child elements of a block, list, or table element.
If you run into issues around whitespace between list items it’s acceptable to put all li elements in one line. A linter is encouraged to 
throw a warning instead of an error.

<pre><code>
<blockquote>
  <p><em>Space</em>, the final frontier.</p>
</blockquote>
<ul>
  <li>Moe
  <li>Larry
  <li>Curly
</ul>
<table>
  <thead>
    <tr>
      <th scope="col">Income
      <th scope="col">Taxes
  <tbody>
    <tr>
      <td>$ 5.00
      <td>$ 4.50
</table>
</code></pre>

####Quotation
When quoting attributes values, use double quotation marks.
Use double ("") rather than single quotation marks ('') around attribute values.

<pre><code>
<!-- Not recommended -->
<a class='maia-button maia-button-secondary'>Sign in</a>
<!-- Recommended -->
<a class="maia-button maia-button-secondary">Sign in</a>
</code></pre>

####Semantics
Use HTML according to its purpose.
Use elements (sometimes incorrectly called “tags”) for what they have been created for. For example, use heading elements for headings, p 
elements for paragraphs, a elements for anchors, etc.

Using HTML according to its purpose is important for accessibility, reuse, and code efficiency reasons.

<pre><code>
<!-- Not recommended -->
<div onclick="goToRecommendations();">All recommendations</div>
<!-- Recommended -->
<a href="recommendations/">All recommendations</a>
</code></pre>

####'type' Attributes.

Omit type attributes for style sheets and scripts.
Do not use type attributes for style sheets (unless not using CSS) and scripts (unless not using JavaScript).

Specifying type attributes in these contexts is not necessary as HTML5 implies text/css and text/javascript as defaults. This can be 
safely done even for older browsers.

<pre><code>
<!-- Not recommended -->
<link rel="stylesheet" href="//www.google.com/css/maia.css"
  type="text/css">
<!-- Recommended -->
<link rel="stylesheet" href="//www.google.com/css/maia.css">
<!-- Not recommended -->
<script src="//www.google.com/js/gweb/analytics/autotrack.js"
  type="text/javascript"></script>
<!-- Recommended -->
<script src="//www.google.com/js/gweb/analytics/autotrack.js"></script>
</code></pre>

