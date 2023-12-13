#!/usr/bin/perl

use strict;
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser); 
use HTML::Template;
use XML::Parser;

my $q = CGI->new; #creates CGI object

print $q->header; #prints the HTTP header

my $content = $q->param('page'); #identifies the page from the parameter in the URL

my @discussion_summary = (    
	{'txt' => "When: 19:00, Mondays"},
    {'txt' => "Where: St John's College Teaching Room 1"},
    {'txt' => "A casual discussion about sci-fi and fantasy, loosely themed around a weekly topic. If you\'re new, meet us outside the St John\'s Old Divinity School at 18:55 and we\'ll show you to the room."}
);

my @film_summary = (    
	{'txt' => "When: 19:00, Saturdays"},
    {'txt' => "Where: Normally St John's College Old Divinity Theatre"},
    {'txt' => "We show a film, and usually hang around for a chat about it afterwards."}
);

my @pub_summary = (    
	{'txt' => "When: 19:30, Every Other Friday (13/10, 27/10, 10/11, 24/11)."},
    {'txt' => "Where: The Bath House Pub."},
    {'txt' => "We talk sci-fi (and other rubbish) in a pub. Food and drink optional."}
);


$content = "home" if !$content;	 #if no page is specified (e.g. if people are accessing the home page), get the home page content
#print $content;
#the reason the page is printed as so many separate files is to make it very easy for people who don't know what they're doing to edit the menu/events box
open TOP, "txt/top.html" or die $!; #fetch and print the top of the document
print <TOP>;
close TOP;

my $tmpl = new HTML::Template( filename => "txt/events.html" ); #fetch and print the forthcoming events box 
$tmpl->param( discussion_summary => \@discussion_summary );
$tmpl->param( film_summary => \@film_summary );
$tmpl->param( pub_summary => \@pub_summary );
print $tmpl->output;

open BODY_START, "txt/body_start.html" or die $!; #fetch and print the start of the body
print <BODY_START>;
close BODY_START;

open MIDDLE, "txt/middle.html" or die $!; #fetch and print the middle of the document
print <MIDDLE>;
close MIDDLE;

$content = "404" unless -e "txt/$content.html"; #return 404 if the file doesn't exist

my $tmpl = new HTML::Template( filename => "txt/$content.html", die_on_bad_params => 0); #fetch and print the forthcoming events box 
$tmpl->param(discussion_summary => \@discussion_summary );
$tmpl->param(film_summary => \@film_summary );
$tmpl->param(pub_summary => \@pub_summary );
print $tmpl->output;

open BODY_END, "txt/body_end.html" or die $!; #fetch and print the end of the body
print <BODY_END>;
close BODY_END;

open BOTTOM, "txt/bottom.html" or die $!; #fetch and print the bottom of the document
print <BOTTOM>;
close BOTTOM;
