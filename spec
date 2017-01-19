%define name	vim-jump
%define version	1.2
%define release	1

Name: %{name}
Summary: Vim plugin for creating jump lines and jumping to source code from those jump lines.
Version: %{version}
Release: %{release}%{?dist}
License: Propietary
Group: Development/Other
URL: http://www.nciinc.com
Source: %{name}-%{version}.tgz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot
Packager: Chad Skeeters <cskeeters@nciinc.com>

%description
Vim plugin for creating jump lines and jumping to source code from those jump lines.

%prep

%setup

%build

%install
mkdir -p %{buildroot}/usr/share/vim/bundle/jump.vim/plugin
mkdir -p %{buildroot}/usr/share/vim/bundle/jump.vim/ftdetect
mkdir -p %{buildroot}/usr/share/vim/bundle/jump.vim/syntax
mkdir -p %{buildroot}/usr/share/vim/bundle/jump.vim/doc
/usr/bin/install -t %{buildroot}/usr/share/vim/bundle/jump.vim/plugin plugin/jump.vim
/usr/bin/install -t %{buildroot}/usr/share/vim/bundle/jump.vim/ftdetect ftdetect/jump.vim
/usr/bin/install -t %{buildroot}/usr/share/vim/bundle/jump.vim/syntax syntax/jump.vim
/usr/bin/install -t %{buildroot}/usr/share/vim/bundle/jump.vim/doc doc/jump.txt

%clean
if [ ! %{buildroot} = "/" ]; then 
    %{__rm} -rf %{buildroot}
fi

%files
%dir  %attr(0755,     root,  wheel) /usr/share/vim/bundle/jump.vim
%dir  %attr(0775,     root,  users) /usr/share/vim/bundle/jump.vim/doc
      %attr(0664,     root,  users) /usr/share/vim/bundle/jump.vim/doc/jump.txt
%dir  %attr(0775,     root,  users) /usr/share/vim/bundle/jump.vim/syntax
      %attr(0664,     root,  users) /usr/share/vim/bundle/jump.vim/syntax/jump.vim
%dir  %attr(0775,     root,  users) /usr/share/vim/bundle/jump.vim/ftdetect
      %attr(0664,     root,  users) /usr/share/vim/bundle/jump.vim/ftdetect/jump.vim
%dir  %attr(0775,     root,  users) /usr/share/vim/bundle/jump.vim/plugin
      %attr(0664,     root,  users) /usr/share/vim/bundle/jump.vim/plugin/jump.vim

%post
/usr/bin/ex -u /dev/null +"helptags /usr/share/vim/bundle/jump.vim/doc" +qa

%preun
if [ $1 = 0 ]; then #removing, not upgrading
    rm -f /usr/share/vim/bundle/jump.vim/doc/tags
fi
