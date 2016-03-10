set nocompatible
set nowrap
syntax on
set ruler
set number
set numberwidth=4
set tabstop=4
set softtabstop=2
set showcmd
set showmatch

set hlsearch
nnoremap <leader><space> :nohlsearch<CR> " leader is a backslash!

" Neobundle shit
set runtimepath^=~/.vim/bundle/neobundle.vim/

call neobundle#begin(expand('~/.vim/bundle/'))

" Let NeoBundle manage NeoBundle
NeoBundleFetch 'Shougo/neobundle.vim'

" My Bundles here:
" Refer to |:NeoBundle-examples|.

call neobundle#end()

  " Required:
  filetype plugin indent on

  " If there are uninstalled bundles found on startup,
  " this will conveniently prompt you to install them.
  NeoBundleCheck
