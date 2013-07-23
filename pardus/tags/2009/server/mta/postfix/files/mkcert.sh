#!/bin/sh

# Generates a self-signed certificate.
# Edit /etc/postfix/ssl/smtpd-ssl.cnf before running this.

OPENSSL=${OPENSSL-openssl}
SSLDIR="/etc/postfix/ssl"
OPENSSLCONFIG=${OPENSSLCONFIG-/etc/postfix/ssl/smtpd-ssl.cnf}

CERTDIR=$SSLDIR
KEYDIR=$SSLDIR

CERTFILE=$CERTDIR/smtpd-cert.pem
KEYFILE=$KEYDIR/smtpd-key.pem

if [ ! -d $CERTDIR ]; then
  echo "$SSLDIR/certs directory doesn't exist"
  exit 1
fi

if [ ! -d $KEYDIR ]; then
  echo "$SSLDIR/private directory doesn't exist"
  exit 1
fi

if [ -f $CERTFILE ]; then
  echo "$CERTFILE already exists, won't overwrite"
  exit 1
fi

if [ -f $KEYFILE ]; then
  echo "$KEYFILE already exists, won't overwrite"
  exit 1
fi

$OPENSSL req -new -x509 -nodes -config $OPENSSLCONFIG -out $CERTFILE -keyout $KEYFILE -days 3650 || exit 2
chmod 0600 $KEYFILE
echo 
$OPENSSL x509 -subject -fingerprint -noout -in $CERTFILE || exit 2
