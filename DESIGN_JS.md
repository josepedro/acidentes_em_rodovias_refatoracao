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
if (time < 20)
    {
    x = "Good day";
    }
else
    {
    x = "Good evening";
    }
</code></pre>

####Line Length
Avoid lines longer than 80 characters. When a statement won't fill in a single line, it may be necessary to break it.
Place the breaks after an operator, specially a comma.
The next line should be indented with 8 spaces.
<pre><code>
if (time < 20)
    {
    x = "This is a long sentence. It should have maximum 80 characters long.
        Because of that, we had to break the line."
    }
</code></pre>
