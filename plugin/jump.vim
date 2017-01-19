if exists("loaded_jump")
  finish
endif
let loaded_jump = 1

function! s:Jump(line)
    let tokens = split(getline('.'), '\t')
    if len(tokens) >= 2
        let filepath = tokens[0]
        let ex = tokens[1]

        "echom "FilePath:".filepath
        "echom "Ex:".l:ex
        keepjumps execute "e ".filepath
        keepjumps norm gg
        execute ex
    else
        echoerr "No tab character in line to delineate filepath from search string."
    endif
endfunction

function! GetMark(register_letter)
    let file_sub_path=substitute(expand('%:p'), getcwd()."/", "", "")
    let search_string=substitute(getline('.'), "^[ \t]*", "", "")
    let search_string=substitute(search_string, "[ \t]*$", "", "")
    let search_string=substitute(search_string, "\\", "\\\\\\\\", "g")
    let search_string=substitute(search_string, "/", "\\\\/", "g")
    execute 'let @'.a:register_letter.' = file_sub_path."	/\\V".search_string."\n"'
endfunction

noremap <SID>Jump  :call <SID>Jump(getline('.'))<CR>
noremap <unique> <script> <Plug>Jump  <SID>Jump
noremenu <script> Plugin.Jump <SID>Jump
