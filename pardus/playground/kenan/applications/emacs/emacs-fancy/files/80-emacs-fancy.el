;;; python-mode site-lisp configuration
(add-to-list 'load-path "/usr/share/emacs/site-lisp/fancy/")
;;;;;;;;;;;;;;;;
(require 'active-menu)
;;(active-menu 1)
;;;;;;;;;;;;;;;;
;;(require 'amarok)
;;;;;;;;;;;;;;;;
(require 'bindings+)
;;;;;;;;;;;;;;;;
;;Boxes
(require 'boxes)
(autoload 'boxes-command-on-region "boxes" nil t)
(autoload 'boxes-remove "boxes" nil t)
(autoload 'boxes-create "boxes" nil t)
(global-set-key "\C-cq" 'boxes-create)
(global-set-key "\C-cr" 'boxes-remove)
;;;;;;;;;;;;;;;;
;; buff-menu+.el
(eval-after-load "buff-menu" '(require 'buff-menu+))
;;;;;;;;;;;;;;;;
(require 'boxquote)
;;;;;;;;;;;;;;;;
(require 'color-grep)
;;;;;;;;;;;;;;;;
(require 'color-moccur)
(require 'moccur-edit)
;;;;;;;;;;;;;;;;
;; ChangingCursorDynamically
(require 'cursor-chg)
(toggle-cursor-type-when-idle 1) ; Turn on cursor change when Emacs is idle
(change-cursor-mode 1) ; Turn on change for overwrite, read-only, and input mode
;; Change cursor color according to mode
(defvar hcz-set-cursor-color-color "")
(defvar hcz-set-cursor-color-buffer "")
(defun hcz-set-cursor-color-according-to-mode ()
  "change cursor color according to some minor modes."
  ;; set-cursor-color is somewhat costly, so we only call it when needed:
  (let ((color
         (if buffer-read-only "white"
           (if overwrite-mode "blue"
             "yellow"))))
    (unless (and
             (string= color hcz-set-cursor-color-color)
             (string= (buffer-name) hcz-set-cursor-color-buffer))
      (set-cursor-color (setq hcz-set-cursor-color-color color))
      (setq hcz-set-cursor-color-buffer (buffer-name)))))
(add-hook 'post-command-hook 'hcz-set-cursor-color-according-to-mode)
;;;;;;;;;;;;;;;;
;;DfMode
(require 'df-mode)
(autoload 'df-mode "df-mode" nil t)
(df-mode 1)
(defcustom directory-free-space-program "df"
     "*Name of your df(1) program."
  :type 'string
  :group 'df)
;;;;;;;;;;;;;;;;
(require 'dircolors)
;;;;;;;;;;;;;;;;
(require 'dired+)
;;;;;;;;;;;;;;;;
(require 'dired-details+)
;;;;;;;;;;;;;;;;
(add-hook 'dired-load-hook
           (lambda () (require 'dired-sort-menu)))
;;;;;;;;;;;;;;;;
;;(require 'erc-bbdb)
;;;;;;;;;;;;;;;;
(require 'erc-highlight-nicknames)
;;;;;;;;;;;;;;;;
(require 'erc-nick-colors)
;;;;;;;;;;;;;;;;
(require 'erc-nicklist)
;;;;;;;;;;;;;;;;
(require 'find-dired++)
;;;;;;;;;;;;;;;;
(require 'findr)
(autoload 'findr "findr" "Find file name." t)
;;;;;;;;;;;;;;;;
(require 'fit-frame)
(add-hook 'after-make-frame-functions 'fit-frame)
;;;;;;;;;;;;;;;;
(require 'folding)
(autoload 'folding-mode          "folding" "Folding mode" t)
(autoload 'turn-off-folding-mode "folding" "Folding mode" t)
(autoload 'turn-on-folding-mode  "folding" "Folding mode" t)
;;;;;;;;;;;;;;;;
(require 'gnus-notify)
;;;;;;;;;;;;;;;;
(require 'google)
(require 'google-define)
;;;;;;;;;;;;;;;;
(require 'highlight)
;;;;;;;;;;;;;;;;
(require 'highlight-regexp)
;;;;;;;;;;;;;;;;
(require 'highline)
;;;;;;;;;;;;;;;;
(require 'imenu+)
;;;;;;;;;;;;;;;;
(require 'lbdb)
(autoload 'lbdb "lbdb" "Query the Little Brother's Database" t)
(autoload 'lbdb-region "lbdb" "Query the Little Brother's Database" t)
(autoload 'lbdb-maybe-region "lbdb" "Query the Little Brother's Database" t)
;;;;;;;;;;;;;;;;
(require 'light)
;;;;;;;;;;;;;;;;
(require 'linkd)
;;;;;;;;;;;;;;;;
(require 'mail-cmple-addr)
;;;;;;;;;;;;;;;;
(eval-after-load "menu-bar" '(require 'menu-bar+))
;;;;;;;;;;;;;;;;
(require 'message-multiple-frames)
;;;;;;;;;;;;;;;;
(require 'mgrep)
;; (setq mgrep-list
;;       '(
;;          name   directory        mask   option
;;         ("dir" default-directory "*.el" dir)
;;         ("config" "~/mylisp/"  ("\\.js" "\\.el$") nil)
;;         ("1.99" "d:/unix/Meadow2/1.99a6/" (".*") sub)
;;         ))

;; name : Input your favorite name
;; directory : Directory you'd like to search
;; mask : file-mask for grep command.
;; option : usually option is nil. If option is t, mgrep uses find
;; command. If option is "dir", you can select directory like
;; find-file. If option is "sub", you can select sub directory to
;; search. "dirfind" , "subfind" are the options to use find command
;; of "dir" , "sub"
;;;;;;;;;;;;;;;;
;; mic-paren
(require 'mic-paren)
(paren-activate)
;;;;;;;;;;;;;;;;
(require 'minibuffer-complete-cycle)
;;;;;;;;;;;;;;;;
(require 'moccur-edit)
;;;;;;;;;;;;;;;;
;; Abbrev mode
(setq-default abbrev-mode t)
(read-abbrev-file "~/.abbrev_defs")
(setq save-abbrevs t)

;; load up abbrevs for these modes
(require 'msf-abbrev)
(setq msf-abbrev-verbose t) ;; optional
(setq msf-abbrev-root "~/.elisp/abbrevs")
(global-set-key (kbd "C-c l") 'msf-abbrev-goto-root)
(global-set-key (kbd "C-c a") 'msf-abbrev-define-new-abbrev-this-mode)
(msf-abbrev-load)
;;;;;;;;;;;;;;;;
(require 'mutt-alias)
(require 'muttrc)
;;;;;;;;;;;;;;;;
;; PSVN
(setq svn-status-prefix-key '[(meta 8)])
(require 'psvn)
(define-key svn-log-edit-mode-map [f6] 'svn-log-edit-svn-diff)
;;;;;;;;;;;;;;;;
(require 'savehist-20+)
(savehist-mode 1)
;;;;;;;;;;;;;;;;
(require 'shell-completion)
;;;;;;;;;;;;;;;;
(require 'shell-current-directory)
;;;;;;;;;;;;;;;;
(require 'show-wspace)
;;;;;;;;;;;;;;;;
;; examine
(require 'soap)
;;;;;;;;;;;;;;;;
;; Speedbar
(require 'sr-speedbar)
;;(setq sr-speedbar t)
(global-set-key [(super s)] 'sr-speedbar-toggle)
(setq speedbar-mode-hook '(lambda ()
   (interactive)
   (other-frame 0)))

(defun speedbar-expand-all-lines ()
  "Expand all items in the speedbar buffer.
But be careful: this opens all the filesto parse them."
  (interactive)
  (goto-char (point-min))
  (while (not (eobp))
         (forward-line)
         (speedbar-expand-line)))
;;;;;;;;;;;;;;;;
;;Tabbar-mode
(require 'tabbar)
(setq tabbar-background-color nil)
(tabbar-mode 1)
;;;;;;;;;;;;;;;;
(eval-after-load "timer" '(require 'timer+))
;;;;;;;;;;;;;;;;
(require 'todoo)
(autoload 'todoo "todoo" "TODO Mode" t)
(add-to-list 'auto-mode-alist '("TODO$" . todoo-mode))
;;;;;;;;;;;;;;;;
(require 'tool-bar+)
;;(tool-bar-mode -1)
;;;;;;;;;;;;;;;;
(require 'top-mode)
;;;;;;;;;;;;;;;;
(require 'tree-mode)
;;;;;;;;;;;;;;;;
(require 'xml-event)
;;;;;;;;;;;;;;;;
(require 'xml-stream)
;;;;;;;;;;;;;;;;
;; Theme
(require 'zenburn)
(color-theme-initialize)
(color-theme-zenburn)
(unless (zenburn-format-spec-works-p)
  (zenburn-define-format-spec))
;;;;;;;;;;;;;;;;
(require 'crontab-mode)
(add-to-list 'auto-mode-alist '("\\.cron\\(tab\\)?\\'" . crontab-mode))
(add-to-list 'auto-mode-alist '("cron\\(tab\\)?\\."    . crontab-mode))
;;;;;;;;;;;;;;;;
(require 'w3m-meteo)
;;;;;;;;;;;;;;;;
