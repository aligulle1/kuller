(add-to-list 'load-path "/usr/share/singular/emacs")
(autoload 'singular "singular"
  "Start Singular using default values." t)
(autoload 'singular-other "singular"
  "Ask for arguments and start Singular." t)

(add-to-list 'auto-mode-alist '("\\.sing\\'" . c++-mode))
