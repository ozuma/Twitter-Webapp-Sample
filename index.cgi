#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use CGI::Session;
use Net::Twitter;

my $cgi = new CGI;
print $cgi->header(-type=>'text/html', -charset=>'utf-8');

unless ($cgi->cookie("CGISESSID")) {
  printNotLogin();
  exit;
}

my $session = new CGI::Session(undef, $cgi->cookie("CGISESSID"), {Directory=>'/tmp'});
unless ($cgi->cookie("CGISESSID") eq $session->id) {
  $session->close;
  $session->delete;
  printNotLogin();
  exit;
}

my $nt = Net::Twitter->new(
  traits   => [qw/API::RESTv1_1/],
  consumer_key        => "xxxxxxxxxxxxxxxxxx",
  consumer_secret     => "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",
  access_token        => $session->param(-name=>'access_token'),
  access_token_secret => $session->param(-name=>'access_token_secret'),
);

my $res = $nt->mentions({count => 1});
my $mention_status = $res->[0]->{text};
my $mention_from = $res->[0]->{user}->{screen_name};

print "<html><head><title>Twitter Webapp Sample</title></head><body>\n";
print "<p>Now You are logged in as: \@" . $session->param(-name=>'screen_name') . "</p>\n";
print "<p>Latest mention from \@$mention_from: $mention_status\n</p>";
print "</body></html>\n";


sub printNotLogin {
  print "<html><head><title>Twitter Webapp Sample</title></head><body>\n";
  print "<p>You are not logged in. Access:</p> \n";
  print "<p><a href=\"http://ozuma.sakura.ne.jp/Twitter-Webapp-Sample/login.cgi\">login.cgi</a></p>\n";
  print "</body></html>\n";
}

