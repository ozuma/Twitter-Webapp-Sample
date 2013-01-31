#!/usr/bin/perl
use strict;
use warnings;
use CGI;
use CGI::Session;
use Net::Twitter;

my $NOT_LOGIN_MES = "You are not logged in. Access: \n\n" .
  "http://ozuma.sakura.ne.jp/Twitter-Webapp-Sample/login.cgi\n";

my $cgi = new CGI;
print $cgi->header(-type=>'text/plain', -charset=>'utf-8');

unless ($cgi->cookie("CGISESSID")) {
  print $NOT_LOGIN_MES;
  exit;
}

my $session = new CGI::Session(undef, $cgi->cookie("CGISESSID"), {Directory=>'/tmp'});
unless ($session->param(-name=>'access_token')) {
  $session->close;
  $session->delete;
  print $NOT_LOGIN_MES;
  exit;
}

my $nt = Net::Twitter->new(
  traits   => [qw/OAuth API::REST/],
  consumer_key        => "xxxxxxxxxxxx",
  consumer_secret     => "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",
  access_token        => $session->param(-name=>'access_token'),
  access_token_secret => $session->param(-name=>'access_token_secret'),
);

my $res = $nt->mentions({count => 1});
my $mention_status = $res->[0]->{text};
my $mention_from = $res->[0]->{user}->{screen_name};

print "Now You are logged in as: \@" . $session->param(-name=>'screen_name') . "\n";
print "Latest mention from \@$mention_from: $mention_status\n";

