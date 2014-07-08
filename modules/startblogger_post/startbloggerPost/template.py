#!/usr/bin/python

tempstr = """
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html>
<html b:version='2' class='v2' expr:dir='data:blog.languageDirection' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
  <head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
<title>test1</title>
<script src='http://cdn.mathjax.org/mathjax/latest/MathJax.js' type='text/javascript'>
    MathJax.Hub.Config({
        HTML: ["input/TeX","output/HTML-CSS"],
        TeX: { extensions: ["AMSmath.js","AMSsymbols.js"],
               equationNumbers: { autoNumber: "AMS" } },
        extensions: ["tex2jax.js"],
        jax: ["input/TeX","output/HTML-CSS"],
        tex2jax: { inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                   displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
                   processEscapes: true },
        "HTML-CSS": { availableFonts: ["TeX"],
                      linebreaks: { automatic: true } }
    });
</script>
<script type="text/javascript">
function hidepre() {
    var pre = this.getElementsByTagName("pre")[0]
    if (pre.style.display === "none") {
        pre.style.display = "block";
    } else {
        pre.style.display = "none";
    }
}
// initial state of pre tags depends on whether there is a fig
function checkimg() {
    var imgs = document.getElementsByClassName("fig");
    var pres = document.getElementsByTagName("pre");
    if(imgs.length) {
        Array.prototype.slice.call(pres, 0).forEach(function(pre) {
            pre.style.display = "none";
        });
    } else {
        Array.prototype.slice.call(pres, 0).forEach(function(pre) {
            pre.style.display = "block";
        });
    }
}
function hidepreall() {
    checkimg();
    var prewraps = document.getElementsByClassName("prewrap");
    if(prewraps.length) {
        // for (var i = 0; i &lt; prewraps.length; i++) {
        //     var prewrap = prewraps[i];
        //     prewrap.onclick = hidepre;
        // }
        Array.prototype.slice.call(prewraps, 0).forEach(function(prewrap) {
            prewrap.ondblclick = hidepre;
        });
    }
}
window.onload = hidepreall;
</script>


<style type='text/css'>
.smallnote {
    display: inline;
    font-size: 80%;
    color: #2b9600;
}
.hidden {
    color: white;
}
.description {
    font-family: serif;
    font-size: 10;
}
.codeclick {
    font-weight: bold;
}
.prewrap {
    opacity: 0.7;
    font-size: 90%;
	padding: 16px;
    max-height: 300px;
	overflow: auto;
    display: block;
    margin-right: auto !important;
    margin-left: auto !important;
    margin-above: 20px !important;
    margin-below: 20px !important;
}
.pretitle {
	text-align: center;
}
code {
    padding: 2px 2px;
}
pre {
    padding: 6px 10px;
}
.pretitle, code, pre {
    background-color: #F8F8F8;
    border: 1px solid #DDD;
    font-size: 13px;
    line-height: 19px;
    overflow: auto;
    border-radius: 3px;
}
.placeholder {
    height: 200px;
    margin: 100px;
}
object
{
    display: block !important;
    margin-left: auto !important;
    margin-right: auto !important;
}
img
{
    height: auto !important;
    max-width:500px !important;
    display: block !important;
    margin-left: auto !important;
    margin-right: auto !important;
    padding: 20px;
}
a,
a:hover
{
    color: black !important;
    text-decoration: none !important;
    font-weight: bold;
}
</style>

</head>
<body>
<!-- ........... bmark here...........  -->
{

htmlstarthere

}
<!-- ........... bmark here...........  -->
<div id="end" class="placeholder"></div>
</body>
</html>
"""
