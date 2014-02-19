%define git 20130402

Summary:	Matlab mode for emacs
Name:		emacs-matlab
Version:	3.3.1
Release:	2.%{git}.1
License:	GPLv2+
Group:		Editors
Url: 		http://matlab-emacs.sourceforge.net/
Source0:	matlab-emacs-%{git}.tar.bz2
BuildRequires:	emacs
BuildRequires:	emacs-cedet
Requires:	emacs
Requires:	emacs-cedet
BuildArch:	noarch

%description
Matlab mode for emacs.

%files
%doc ChangeLog* README
%{_datadir}/emacs/site-lisp/matlab
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/matlab-load.*

#----------------------------------------------------------------------------

%prep
%setup -q -n matlab-emacs

%build
sed -i 's,--no-site-file,,' Makefile
%make all

%install
rm -f *~
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/matlab/
install -m 644 *.el* %{buildroot}%{_datadir}/emacs/site-lisp/matlab/

cat > tmp <<EOF
;; Set path to matlab mode files on Mandriva
(add-to-list 'load-path "/usr/share/emacs/site-lisp/matlab")

EOF
cat tmp matlab-load.el > tmp2
mv -f tmp2 matlab-load.el

mkdir -p %{buildroot}%{_sysconfdir}/emacs/site-start.d/
install -m 644 matlab-load.el* %{buildroot}%{_sysconfdir}/emacs/site-start.d/
rm -f %{buildroot}%{_datadir}/emacs/site-lisp/matlab/matlab-load*

chmod 644 ChangeLog* README

