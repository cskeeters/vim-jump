vim-jump is a vim plugin that enables a documenter/developer to write a text
file describing an aspect of a program and include "links" to the spots in the
source code in a robust way.  The method of creating robust links was inspired
by ctags.  It uses an ex command that search through a file for a point in the
code rather than relying on line numbers (that change often).

This plugin automates creating a "link" or a "jump line" and jumping when the
cursor is on a jump line.

For more details see the [vim doc](doc/jump.txt).
