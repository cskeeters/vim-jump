if exists("b:current_syntax")
   finish
endif

syn keyword jumpTask TODO DONE
syn match jumpSearch contained "/\\V.*" contains=@NoSpell skipwhite
syn match jumpFile contained "[^	]\+" contains=@NoSpell nextgroup=jumpSearch skipwhite
syn region jumpLine start=/[^	]\+	/ end=/$/ contains=jumpFile,jumpSearch oneline skipwhite
syn match jumpH1 /^.\+\n=\+$/
syn match jumpH2 /^.\+\n-\+$/

hi link jumpTask Keyword
hi link jumpTodo Keyword
hi link jumpFile Function
hi link jumpSearch String
hi link jumpH1 Label
hi link jumpH2 Constant
hi link jumpText Normal

let b:current_syntax="jump"
let b:spell_options="contained"
