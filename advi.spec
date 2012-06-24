Summary:	DVI previewer
Summary(pl):	Przegl�darka DVI
Name:		advi
Version:	1.0.0
Release:	1
License:	LGPL
Group:		Applications/Publishing/TeX
URL:		http://pauillac.inria.fr/advi/
Source0:	ftp://ftp.inria.fr/INRIA/Projects/cristal/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-datadir.patch
BuildRequires:	ocaml-camlp4
BuildRequires:	ocaml >= 3.04
BuildRequires:	tetex
BuildRequires:	tetex-latex
BuildRequires:	tetex-dvips
BuildRequires:	XFree86-devel
BuildRequires:	ghostscript >= 6.52
BuildRequires:	ocaml-x11graphics-devel
BuildRequires:	ocaml-camlimages-devel
Requires:	tetex
Requires:	ghostscript >= 6.52
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

+ Do��cznie plik�w EPS (z u�yciem pakietu graphics)
+ Efekty do prezentacji (pauza, op�nienie, zmiana koloru tekstu)
+ Uruchamianie wbudowanych aplikacji w czasie prezentacji interaktywnych
+ Wy�wietlanie obrazk�w poprzez gpic
+ Wy�wietlanie PostScriptu z u�yciem gs
+ Antialiasing czcionek, kt�ry bierze pod uwag� kolor t�a
+ Hiper��cza
+ Aktywne obszary (wykonuj� akcj� gdy mysz jest nad nimi)
+ Zmiana koloru t�a i wy�wietlanie obrazk�w jako t�a
+ Rozmycie kana�u alfa dla obrazk�w

%prep
%setup -q
%patch0 -p1

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
	
gzip -9nf COPYING README TODO doc/*.ps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.gz *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
