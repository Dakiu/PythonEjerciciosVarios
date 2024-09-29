//HTML
var nota1Html = prompt("Ingrese nota 1 Html");
var nota2Html = prompt("Ingrese nota 2 Html");
var nota3Html = prompt("Ingrese nota 3 Html");

document.getElementById("HTML1").innerHTML = nota1Html;
document.getElementById("HTML2").innerHTML = nota2Html;
document.getElementById("HTML3").innerHTML = nota3Html;

var promedioHtml = (Number(nota1Html)+Number(nota2Html)+Number(nota3Html))/3;

document.getElementById("HTMLPromedio").innerHTML = (Math.round(promedioHtml * 100) / 100).toFixed(2);
//CSS

var nota1Css = prompt("Ingrese nota 1 Css");
var nota2Css = prompt("Ingrese nota 2 Css");
var nota3Css = prompt("Ingrese nota 3 Css");

document.getElementById("CSS1").innerHTML = nota1Css
document.getElementById("CSS2").innerHTML = nota2Css
document.getElementById("CSS3").innerHTML = nota3Css

var promedioCss = (Number(nota1Css)+Number(nota2Css)+Number(nota3Css))/3;

document.getElementById("CSSPromedio").innerHTML = (Math.round(promedioCss * 100) / 100).toFixed(2);

//JS
var nota1Js = prompt("Ingrese nota 1 Js");
var nota2Js = prompt("Ingrese nota 2 Js");
var nota3Js = prompt("Ingrese nota 3 Js");

document.getElementById("JS1").innerHTML = nota1Js
document.getElementById("JS2").innerHTML = nota2Js
document.getElementById("JS3").innerHTML = nota3Js

var promedioJs = (Number(nota1Js)+Number(nota2Js)+Number(nota3Js))/3;

document.getElementById("JSPromedio").innerHTML = (Math.round(promedioJs * 100) / 100).toFixed(2);
