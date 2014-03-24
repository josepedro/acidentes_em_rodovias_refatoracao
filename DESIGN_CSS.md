#Style and Design Document

##CSS
####Headline
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

/* ==========================================================================
   Comment for a new section
   ========================================================================== */
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
