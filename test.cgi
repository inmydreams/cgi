#!/usr/bin/perl

use strict;
use warnings;
use CGI;

my $version = "1.0";

my $current_year = `date +"%Y"`;


print foreach (
    "Content-Type: text/plain\n\n",
    "CGI Test version $version\n",
    "Copyright 2017-$current_year", 
    "Inmydreams\n\n",
    "Versions:\n=================\n",
    "perl: $]\n",
    "CGI: $CGI::VERSION\n"
);

my $vars = CGI::Vars();

my @message;

my $fill="true";

print "\nCGI Values:\n=================\n";

foreach my $key ( sort keys %$vars ){
    if(length($vars->{$key})==0){
        $fill="false";
    }
    else{
        push @message, "$key [$vars->{$key}]\n";
    }
}

unless($fill eq "false"){
    my $to = 'karolinak93@gmail.com';
    my $from = $vars->{"Email"};
    my $subject = 'Feedback form';

 
    open(MAIL, "|/usr/sbin/sendmail -t");
 
    print MAIL "To: $to\n";
    print MAIL "From: $from\n";
    print MAIL "Subject: $subject\n\n";
    print MAIL @message;

    close(MAIL);
    print "Email Sent Successfully\n";
}

