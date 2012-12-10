%define tarname	matlab-emacs
%define name	emacs-matlab
%define version 3.3.1
%define rel	1.30
%define release %mkrel 1.cvs%{rel}

Summary:	Matlab mode for emacs
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}.tar.bz2
License:	GPLv2+
Group:		Editors
Url: 		http://matlab-emacs.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	emacs, emacs-cedet >= 0:1.0-1
BuildRequires:	emacs, emacs-cedet >= 0:1.0-1

%description
Matlab mode for emacs.

%prep
%setup -q -n %{tarname}

%build
%__sed -i 's,--no-site-file,,' Makefile
%make all

%install
%__rm -rf %{buildroot}

%__rm -f *~
%__mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp/matlab/
%__install -m 644 *.el* %{buildroot}%{_datadir}/emacs/site-lisp/matlab/

%__cat > tmp <<EOF
;; Set path to matlab mode files on Mandriva
(add-to-list 'load-path "/usr/share/emacs/site-lisp/matlab")

EOF
%__cat tmp matlab-load.el > tmp2
%__mv -f tmp2 matlab-load.el

%__mkdir -p %{buildroot}%{_sysconfdir}/emacs/site-start.d/
%__install -m 644 matlab-load.el* %{buildroot}%{_sysconfdir}/emacs/site-start.d/
%__rm -f %{buildroot}%{_datadir}/emacs/site-lisp/matlab/matlab-load*

%__chmod 644 ChangeLog* README

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog* README
%{_datadir}/emacs/site-lisp/matlab
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/matlab-load.*


%changelog
* Sun May 15 2011 Lev Givon <lev@mandriva.org> 3.3.1-1.cvs1.30mdv2011.0
+ Revision: 674858
- Require cedet 1.0 (integrated cedet in emacs 23.2+ insufficient).
- Update to 1.30.
- Update to release 1.28 from CVS.
- Update to revision 1.25.

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Tue Feb 02 2010 Lev Givon <lev@mandriva.org> 3.3.1-0.cvs1.23mdv2010.1
+ Revision: 499781
- Update to latest version.

* Fri Jun 12 2009 Lev Givon <lev@mandriva.org> 3.2.0-1mdv2010.0
+ Revision: 385588
- imported package emacs-matlab


