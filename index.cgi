#!/usr/bin/perl

use strict;
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser); 

my $q = CGI->new; #creates CGI object

print $q->header; #prints the HTTP header

my $content = $q->param('page'); #identifies the page from the parameter in the URL

$content = "home" if !$content;	 #if no page is specified (e.g. if people are accessing the home page), get the home page content
#print $content;
#the reason the page is printed as so many separate files is to make it very easy for people who don't know what they're doing to edit the menu/events box
open TOP, "txt/top.html" or die $!; #fetch and print the top of the document
print <TOP>;
close TOP;

open EVENTS, "txt/events.html" or die $!; #fetch and print the forthcoming events box
print <EVENTS>;
close EVENTS;

open MIDDLE, "txt/middle.html" or die $!; #fetch and print the middle of the document
print <MIDDLE>;
close MIDDLE;

$content = "404" unless -e "txt/$content.html"; #return 404 if the file doesn't exist

open CONTENT, "txt/$content.html" or die $!; #fetch and print the content of the requested page
print <CONTENT>;
close CONTENT;

open BOTTOM, "txt/bottom.html" or die $!; #fetch and print the bottom of the document
print <BOTTOM>;
close BOTTOM;
