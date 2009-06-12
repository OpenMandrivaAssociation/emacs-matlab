%define tarname	matlab-emacs
%define name	emacs-matlab
%define version 3.2.0
%define release %mkrel 1

Summary:	Matlab mode for emacs
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}.tar.lzma
License:	GPLv2+
Group:		Editors
Url: 		http://matlab-emacs.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	emacs, emacs-cedet >= 1.0-0.pre6.3
BuildRequires:	emacs, emacs-cedet >= 1.0-0.pre6.3

%description
Matlab mode for emacs.

%prep
%setup -q -n %{tarname}

%build
%__sed -i 's,--no-site-file,,' Makefile
%make all

%install
%__rm -rf %{buildroot}

%__rm -f matlab-load.el*
%__mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/matlab/
%__install -m 644 *.el* %{buildroot}%{_datadir}/emacs/site-lisp/matlab/

%__cat > matlab-mode.el << EOF
;; Make Matlab mode available
(add-to-list 'load-path "/usr/share/emacs/site-lisp/matlab")
(autoload 'matlab-mode "matlab" "Enter MATLAB mode." t)
(autoload 'matlab-shell "matlab" "Interactive MATLAB mode." t)
EOF

%__mkdir -p %{buildroot}%{_sysconfdir}/emacs/site-start.d/
%__install -m 644 matlab-mode.el %{buildroot}%{_sysconfdir}/emacs/site-start.d/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog* README
%{_datadir}/emacs/site-lisp/matlab
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/matlab-mode.*
