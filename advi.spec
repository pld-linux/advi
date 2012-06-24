Summary:	DVI previewer
Summary(pl):	Przegl�darka DVI
Name:		advi
Version:	1.4.0
Release:	1
License:	LGPL
Group:		Applications/Publishing/TeX
Source0:	ftp://ftp.inria.fr/INRIA/Projects/cristal/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	f605d653ff7785ff48c39851e990380f
URL:		http://pauillac.inria.fr/advi/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	ghostscript >= 6.52
BuildRequires:	ocaml >= 3.04
BuildRequires:	ocaml-camlimages-devel
BuildRequires:	ocaml-camlp4
BuildRequires:	ocaml-x11graphics-devel
BuildRequires:	tetex
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex
BuildRequires:	tetex-tex-pstricks
BuildRequires:	tetex-tex-misc
# probably some more tetex-* stuff is needed
Requires:	ghostscript >= 6.52
Requires:	tetex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CURRENTLY SUPPORTED FEATURES:
=============================

+ Encapsulated Postscript File inclusion (using graphics package)
+ Effects for presentation (pause, delay, text color change)
+ Embedded applications for interactive demonstration
+ Pictures visualization via gpic specials
+ Display of inlined Postscript using gs
+ Font antialiasing that takes background colors into account
+ Hyperlinks
+ Active areas (execute an action when the mouse is over)
+ Background colors and images
+ Alpha blending for images

%description -l pl
AKTUALNIE WSPIERA:
==================

+ Do��czanie plik�w EPS (z u�yciem pakietu graphics)
+ Efekty do prezentacji (pauza, op�nienie, zmiana koloru tekstu)
+ Uruchamianie wbudowanych aplikacji w czasie prezentacji
  interaktywnych
+ Wy�wietlanie obrazk�w poprzez gpic
+ Wy�wietlanie PostScriptu z u�yciem gs
+ Antialiasing czcionek, kt�ry bierze pod uwag� kolor t�a
+ Hiper��cza
+ Aktywne obszary (wykonuj� akcj� gdy mysz jest nad nimi)
+ Zmiana koloru t�a i wy�wietlanie obrazk�w jako t�a
+ Rozmycie kana�u alfa dla obrazk�w

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make} opt
%{__make} -C doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	ADVI_LOC=$RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING specifies authors, doesn't contain LGPL text
%doc COPYING README TODO doc/*.ps
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
