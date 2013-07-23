;;; emacs-jabber site-lisp configuration

(add-to-list 'load-path "/usr/share/emacs/site-lisp/")
(autoload 'jabber-customize "jabber" "customize jabber options" t)
(autoload 'jabber-connect "jabber"
  "connect to the jabber server and start a jabber xml stream" t)
