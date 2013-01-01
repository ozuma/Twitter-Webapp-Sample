#!/usr/bin/perl
use strict;
use warnings;
use Net::Twitter;
use CGI;

my $cgi = new CGI;

my $nt = Net::Twitter->new(
  traits          => ['API::REST', 'OAuth'],
  consumer_key    => "xxxxxxxxxxxxxxxxxx",
  consumer_secret => "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",
);
my $url = $nt->get_authorization_url(callback => 'http://ozuma.sakura.ne.jp/twitter_sample/callback.cgi');

print 'Set-Cookie: '.$cgi->cookie(-name => 'token', -value => $nt->request_token, -path => '/twitter_sample')."\n";
print 'Set-Cookie: '.$cgi->cookie(-name => 'token_secret', -value => $nt->request_token_secret, -path => '/twitter_sample')."\n";
print $cgi->redirect(-uri => $url);

