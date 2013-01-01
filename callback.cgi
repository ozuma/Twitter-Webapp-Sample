#!/usr/bin/perl
use strict;
use warnings;
use Net::Twitter;
use CGI;
use CGI::Session;

my $cgi = new CGI;
my $session = new CGI::Session(undef, undef, {Directory=>'/tmp'});
$session->expire('+1M');

my $oauth_verifier = $cgi->param('oauth_verifier');

my $nt = Net::Twitter->new(
    traits => [qw/API::REST OAuth/],
    consumer_key => "xxxxxxxxxxxxxxxxxx",
    consumer_secret => "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",
);

$nt->request_token($cgi->cookie('token'));
$nt->request_token_secret($cgi->cookie('token_secret'));
my($access_token, $access_token_secret, $user_id, $screen_name)
   = $nt->request_access_token(verifier => $oauth_verifier);

$session->param(-name=>'access_token', -value=>$access_token);
$session->param(-name=>'access_token_secret', -value=>$access_token_secret);
$session->param(-name=>'user_id', -value=>$user_id);
$session->param(-name=>'screen_name', -value=>$screen_name);

my $cookie = CGI::Cookie->new(-name    =>  'CGISESSID',
                             -value   =>  $session->id(),
                             -expires =>  '+1M',
                             -path    =>  '/Twitter-Webapp-Sample'
                            );

print $cgi->header(-cookie=>$cookie, -location => 'http://ozuma.sakura.ne.jp/Twitter-Webapp-Sample/');

