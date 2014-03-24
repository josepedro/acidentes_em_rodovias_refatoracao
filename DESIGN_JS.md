#Documento de Estilo e Design JS

##JavaScript

###Headline
<pre><code># Universidade de Brasilia - FGA
# Técnicas de Programação, 1/2014
#
# Acidentes em Rodovias, 2013-2014
# GitHub: https://github.com/josepedro/acidentes_em_rodovias_refatoracao
#
</code></pre>

####Comments
The comments must be written in english.
<pre><code>//This is a simple comment

/*This comment occupies
more than one line.*/
</code></pre>

####Identation
The unit of indentation is four spaces. Use of tabs should be avoided because there still is not a standard for the placement of tabstops.

<pre><code>
if (time < 20) {
    x = "Good day";
    }
else {
    x = "Good evening";
    }
</code></pre>

####Line Length
Avoid lines longer than 80 characters. When a statement won't fill in a single line, it may be necessary to break it.
Place the breaks after an operator, specially a comma.
The next line should be indented with 8 spaces.

<pre><code>
if(time < 20) {
    x = "This is a long sentence. It should have maximum 80 characters long.
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
