%% This file is generated on-the-fly by curlconfig.P
%% Do not edit--any changes will be written over.
%% config:    x86_64-unknown-linux-gnu
%% CC:        gcc
%% CC Opts:    -I/usr/java/jdk/include  -O3 -fno-strict-aliasing   -fPIC -Wall -pipe    -I /home/kifer/XSB/XSB/config/x86_64-unknown-linux-gnu /home/kifer/XSB/XSB/packages/curl/cc/load_page.c
:- export pl_load_page/1, curl_allocate_error_term/2, curl_finalize_warn/1, pl_encode_url/2.
:- ldoption('  -lm -ldl -Wl,-export-dynamic -lpthread -lcurl').
