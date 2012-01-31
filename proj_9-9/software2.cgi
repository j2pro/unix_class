#!/usr/bin/perl
# Program name: software.cgi

require "subparseform.lib";
&Parse_Form;

$frontdk = $formdata {'frontdk'};
$reserve = $formdata {'reserve'};
$convmgt = $formdata {'convmgt'};

$qtotal = $frontdk+$reserve+$convmgt;
$tfrontdk = $frontdk*200;
$treserve = $reserve*150;
$tconvmgt = $convmgt*180;
$total = $tfrontdk+$treserve+$tconvmgt;

print "Content-Type: text/html\n\n";
print "<BODY BGCOLOR=WHITE>";
print "<FONT COLOR=RED><H1><CENTER>Software Special</CENTER></H1></FONT><BR>";
print "<center><h2><u><p>Thank You For Your Order</p></u></h2></center>";
print "<br>";
print "<table border=1 bgcolor=cyan alighn=center width=300 cellspacing=5>";
print "<tr><th align=center>Qty</th>";
print "<th align=center>Software</th>";
print "<th align=center>Total</th>";
print "";
print "";
print "";
print "";
print "";
print "";
print "";
print "";
print "";
print "";
print "";
print "";
print "</BODY>";